#!/usr/bin/env python3
"""One-time exporter: Squarespace (disc.bu.edu) -> Jekyll sources.

Uses Squarespace's public `?format=json` view of every page/collection,
converts block HTML to Markdown, downloads images, and writes:

  _papers/<slug>.md        papers collection   (/papers/<slug>)
  _posts/<date>-<slug>.md  news-blog           (/news-blog/<slug>)
  _minipages/<slug>.md     minipages           (/minipages/<slug>)
  _blog/<slug>.md          disc-blog           (/disc-blog/<slug>)
  _pages/<slug>.md         standalone pages
  _data/team.yml           team page, structured
  _data/sponsors.yml       homepage sponsor logos
  assets/img/...           all images
  tools/export-report.md   things that need a human look

Usage:
  pip install -r tools/requirements.txt
  python tools/export_squarespace.py [--site https://disc.bu.edu] [--out .] [--cache DIR]
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
import urllib.parse
from pathlib import Path

import requests
import yaml
from bs4 import BeautifulSoup, NavigableString, Tag
from markdownify import MarkdownConverter

UA = {"User-Agent": "Mozilla/5.0 (static-site-migration)"}

COLLECTIONS = {
    # squarespace url slug -> (jekyll dir, kind)
    "papers": ("_papers", "paper"),
    "news-blog": ("_posts", "post"),
    "minipages": ("_minipages", "minipage"),
    "disc-blog": ("_blog", "blog"),
}
PAGES = ["home", "team", "classes", "research", "research-artifacts",
         "publications", "news", "lethe", "pio", "lsm-compaction",
         "persistent-deletes", "relational-memory", "wiki", "coming-soon"]
# Pages that are only a summary listing; rebuilt by Jekyll layouts instead.
GENERATED_PAGES = {"home", "publications", "news", "team"}


class Report:
    def __init__(self):
        self.lines: dict[str, list[str]] = {}

    def add(self, section: str, line: str):
        self.lines.setdefault(section, []).append(line)

    def write(self, path: Path):
        out = ["# Squarespace export report", "",
               f"Generated {dt.date.today().isoformat()} by `tools/export_squarespace.py`.", ""]
        for sec, items in self.lines.items():
            out += [f"## {sec}", ""] + [f"- {i}" for i in items] + [""]
        path.write_text("\n".join(out))


class Exporter:
    def __init__(self, site: str, out: Path, cache: Path | None):
        self.site = site.rstrip("/")
        self.host = urllib.parse.urlparse(self.site).netloc
        self.out = out
        self.cache = cache
        self.sess = requests.Session()
        self.sess.headers.update(UA)
        self.images: dict[str, str] = {}  # remote url -> local web path
        self.used: set[str] = set()
        self.banners: dict[str, dict] = {}
        self.report = Report()

    # ------------------------------------------------------------------ fetch
    def refresh_target(self, path: str) -> str | None:
        r = self.sess.get(f"{self.site}{path}", timeout=30)
        m = re.search(r'http-equiv\s*=\s*"refresh"\s+content\s*=\s*"\d+;\s*url\s*=\s*([^"]+)"', r.text, re.I)
        return m.group(1).strip() if m else None

    def get_json(self, path: str) -> dict:
        url = f"{self.site}{path}{'&' if '?' in path else '?'}format=json"
        key = hashlib.sha1(url.encode()).hexdigest()
        if self.cache:
            f = self.cache / f"{key}.json"
            if f.exists():
                return json.loads(f.read_text())
        for attempt in range(4):
            r = self.sess.get(url, timeout=30)
            if r.status_code == 200:
                break
            time.sleep(2 ** attempt)
        r.raise_for_status()
        data = r.json()
        if self.cache:
            self.cache.mkdir(parents=True, exist_ok=True)
            (self.cache / f"{key}.json").write_text(json.dumps(data))
        return data

    def collection_items(self, slug: str) -> list[dict]:
        items, path = [], f"/{slug}"
        while path:
            d = self.get_json(path)
            items += d.get("items", [])
            pg = d.get("pagination") or {}
            path = pg.get("nextPageUrl") if pg.get("nextPage") else None
        return items

    # ----------------------------------------------------------------- assets
    def image(self, url: str, folder: str) -> str:
        if not url:
            return ""
        if url.startswith("//"):
            url = "https:" + url
        url = url.split("?")[0]
        if url in self.images:
            return self.images[url]
        name = urllib.parse.unquote_plus(url.rstrip("/").rsplit("/", 1)[-1])
        name = re.sub(r"[^A-Za-z0-9._-]+", "-", name).strip("-").lower() or "image"
        if "." not in name:
            name += ".jpg"
        dest = self.out / "assets" / "img" / folder / name
        stem, ext = os.path.splitext(name)
        n = 1
        while "/" + dest.relative_to(self.out).as_posix() in self.used:
            n += 1
            dest = dest.with_name(f"{stem}-{n}{ext}")
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            try:
                # Ask for the original format (the CDN serves WebP to browser-like
                # clients) and cap width at 1500px, which is plenty for the web.
                fetch = url + "?format=1500w" if "squarespace-cdn.com" in url else url
                r = self.sess.get(fetch, timeout=60,
                                  headers={"Accept": "image/png,image/jpeg,image/gif;q=0.9,*/*;q=0.1"})
                r.raise_for_status()
                dest.write_bytes(r.content)
            except Exception as e:  # noqa: BLE001
                self.report.add("Failed image downloads", f"{url} ({e})")
                return url
        web = "/" + dest.relative_to(self.out).as_posix()
        self.images[url] = web
        self.used.add(web)
        return web

    def fix_href(self, href: str | None) -> str | None:
        if not href:
            return href
        p = urllib.parse.urlparse(href)
        if p.netloc in (self.host, "www." + self.host):
            href = p.path or "/"
            if p.query:
                href += "?" + p.query
            if p.fragment:
                href += "#" + p.fragment
        if "squarespace.com" in href and "/s/" in href:
            self.report.add("Links to Squarespace-hosted files (download manually)", href)
        return href

    # ------------------------------------------------------------- html -> md
    def md(self, node) -> str:
        if node is None:
            return ""
        frag = BeautifulSoup(str(node), "html.parser")
        for a in frag.find_all("a"):
            a["href"] = self.fix_href(a.get("href")) or ""
        for el in frag.find_all(["style", "script"]):
            el.decompose()
        text = _Converter(heading_style="ATX", bullets="-", escape_underscores=False,
                          escape_asterisks=False).convert_soup(frag)
        text = re.sub(r"[ \t]+\n", lambda m: "  \n" if m.group(0).startswith("  ") else "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()

    def img_from(self, el: Tag) -> tuple[str, str]:
        img = el.find("img")
        if not img:
            return "", ""
        url = img.get("data-image") or img.get("data-src") or img.get("src") or ""
        return url, (img.get("alt") or "").strip()

    def blocks_to_md(self, html: str, folder: str, context: str,
                     skip_text: str | None = None) -> str:
        soup = BeautifulSoup(html or "", "html.parser")
        self._ctx = (folder, context, skip_text)
        root = soup.select_one(".sqs-layout") or soup
        parts = self.render_layout(root)
        while parts and parts[-1] == "<hr>":
            parts.pop()
        return "\n\n".join(p for p in parts if p).strip() + "\n"

    def render_layout(self, node: Tag) -> list[str]:
        """Walk Squarespace's row/column grid. Rows with several non-empty columns are kept
        as <div class="sqs-row"> / <div class="sqs-col span-N" markdown="1"> so the
        side-by-side layout survives; everything else becomes plain Markdown."""
        parts: list[str] = []
        children = [c for c in node.children if isinstance(c, Tag)]
        k = 0
        while k < len(children):
            child = children[k]
            k += 1
            cls = child.get("class", [])
            if "sqs-block" in cls and "float" in cls:
                # A block floated left/right with a span-N width: the blocks after it in the
                # same column wrap beside it, so render the pair as a two-column row.
                span = int(next((x.split("-")[1] for x in cls if x.startswith("span-")), "12"))
                end = next((j for j in range(k, len(children))
                            if children[j].get("data-definition-name") == "website.components.horizontalrule"),
                           len(children))
                rest = children[k:end]
                k = end
                side = [md for md in (self.block_md(b) for b in rest if "sqs-block" in b.get("class", [])) if md]
                main = self.block_md(child)
                cols = [(span, [main] if main else []), (12 - span, side)]
                if "float-right" in cls:
                    cols.reverse()
                html = ['<div class="sqs-row">']
                for n, inner in cols:
                    html.append(f'<div class="sqs-col span-{n}" markdown="1">\n\n' + "\n\n".join(inner) + "\n\n</div>")
                html.append("</div>")
                parts.append("\n".join(html))
            elif "sqs-block" in cls:
                md = self.block_md(child)
                if md:
                    parts.append(md)
            elif "sqs-row" in cls:
                cols = [c for c in child.children if isinstance(c, Tag) and "sqs-col" in " ".join(c.get("class", []))]
                rendered = [(c, self.render_layout(c)) for c in cols]
                filled = [r for r in rendered if r[1]]
                if len(filled) > 1:
                    html = ['<div class="sqs-row">']
                    for c, inner in rendered:
                        span = next((x.split("-")[1] for x in c.get("class", []) if x.startswith("span-")), "12")
                        html.append(f'<div class="sqs-col span-{span}" markdown="1">\n\n' + "\n\n".join(inner) + "\n\n</div>")
                    html.append("</div>")
                    parts.append("\n".join(html))
                else:
                    for _, inner in rendered:
                        parts += inner
            else:
                parts += self.render_layout(child)
        return parts

    def block_md(self, b: Tag) -> str:
        folder, context, skip_text = self._ctx
        out: list[str] = []
        kind = b.get("data-definition-name") or next(
            (c for c in b.get("class", []) if c.endswith("-block") and c != "sqs-block"), "?")
        content = b.select_one(".sqs-block-content")
        if kind in ("website.components.spacer", "website.components.socialLinks"):
            return ""
        if kind == "website.components.horizontalrule":
            out.append("<hr>")
        elif kind in ("website.components.markdown", "html-block"):
            inner = content.select_one(".sqs-html-content") or content
            if skip_text and _norm(inner.get_text(" ")) == skip_text:
                return ""
            txt = self.md(inner)
            if txt and txt != "Double-click to edit...":
                out.append(txt)
        elif kind in ("website.components.imageLayout", "image-block"):
            url, alt = self.img_from(b)
            local = self.image(url, folder)
            link = b.select_one("a.sqs-block-image-link, figure a[href]")
            cap = b.select_one(".image-caption, figcaption")
            caption = self.md(cap) if cap else ""
            img_md = f"![{alt}]({local})"
            if link and link.get("href"):
                img_md = f"[{img_md}]({self.fix_href(link['href'])})"
            out.append(img_md + (f"\n\n{caption}" if caption else ""))
        elif kind == "gallery-block":
            figs = []
            for slide in b.select(".slide, .gallery-grid-item, .gallery-masonry-item"):
                url, alt = self.img_from(slide)
                if not url:
                    return ""
                title = slide.select_one(".meta-title")
                cap = title.get_text(" ", strip=True) if title else alt
                figs.append(f'  <figure><img src="{self.image(url, folder)}" alt="{_attr(alt)}" '
                            f'loading="lazy"><figcaption>{cap}</figcaption></figure>')
            out.append('<div class="gallery">\n' + "\n".join(figs) + "\n</div>")
        elif kind == "website.components.button":
            a = b.find("a")
            if a:
                out.append(f'<p class="button-row"><a class="button" href="{self.fix_href(a.get("href"))}">'
                             f'{a.get_text(strip=True)}</a></p>')
        elif kind == "website.components.code":
            box = b.select_one(".sqs-code-container")
            raw = box.decode_contents().strip() if box else ""
            if raw:
                out.append(raw)
        elif kind == "website.components.summary":
            self.report.add("Summary (auto-listing) blocks replaced by Jekyll loops", context)
        elif kind in ("video-block", "embed-block", "website.components.video"):
            out.append(content.decode_contents().strip() if content else "")
            self.report.add("Embeds copied as raw HTML (check they render)", context)
        else:
            out.append(content.decode_contents().strip() if content else "")
            self.report.add("Unknown block types copied as raw HTML", f"{context}: `{kind}`")
        return "\n\n".join(o for o in out if o)

    # --------------------------------------------------------------- writers
    def write(self, rel: str, front: dict, body: str):
        path = self.out / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        fm = yaml.safe_dump(front, sort_keys=False, allow_unicode=True, width=1000).strip()
        path.write_text(f"---\n{fm}\n---\n\n{body}")

    def parse_paper_excerpt(self, excerpt: str) -> dict:
        s = BeautifulSoup(excerpt or "", "html.parser")
        out: dict = {}
        em = s.find("em")
        if em:
            out["venue"] = _norm(em.get_text(" "))
            nxt = []
            for sib in em.next_siblings:
                if isinstance(sib, Tag) and sib.name == "br":
                    continue
                nxt.append(sib.get_text(" ") if isinstance(sib, Tag) else str(sib))
            authors = _norm(" ".join(nxt))
            if authors:
                out["authors"] = authors
        links = []
        for a in s.find_all("a"):
            label = _norm(a.get_text(" "))
            if label and a.get("href"):
                links.append({"label": label, "url": self.fix_href(a["href"])})
        if links:
            out["links"] = links
        if "venue" not in out:
            out["excerpt_md"] = self.md(s)
        return out

    def export_collection(self, slug: str):
        folder, kind = COLLECTIONS[slug]
        items = self.collection_items(slug)
        seen_titles: dict[str, str] = {}
        for idx, it in enumerate(items):
            url_id = it["urlId"].split("/")[-1]
            date = dt.datetime.fromtimestamp((it.get("publishOn") or it["addedOn"]) / 1000, dt.timezone.utc)
            title = _norm(it.get("title") or url_id)
            front: dict = {"title": title, "date": date.strftime("%Y-%m-%d %H:%M:%S %z")}
            if it.get("tags"):
                front["tags"] = it["tags"]
            if it.get("categories"):
                front["categories"] = it["categories"]
            if it.get("starred"):
                front["featured"] = True
            skip = None
            if kind == "paper":
                meta = self.parse_paper_excerpt(it.get("excerpt", ""))
                front.update({k: v for k, v in meta.items() if k != "excerpt_md"})
                front["order"] = len(items) - idx  # preserve manual Squarespace ordering
                skip = _norm(BeautifulSoup(it.get("excerpt", ""), "html.parser").get_text(" "))
                if "venue" not in meta:
                    self.report.add("Papers whose excerpt didn't parse as venue/authors", f"`{url_id}`")
            elif it.get("excerpt"):
                ex = self.md(BeautifulSoup(it["excerpt"], "html.parser"))
                if ex:
                    front["excerpt"] = ex
            asset = it.get("assetUrl") or ""
            if asset and not asset.endswith("/"):
                front["image"] = self.image(asset, slug)
            body = self.blocks_to_md(it.get("body", ""), slug, f"/{slug}/{url_id}", skip_text=skip)
            if it.get("passthrough") and it.get("sourceUrl"):
                front["external_url"] = self.fix_href(it["sourceUrl"])
            elif not body.strip() and "venue" not in front:
                self.report.add("Empty collection items", f"/{slug}/{url_id}")
            if kind == "post" and "image" not in front:
                m = re.search(r"!\[[^\]]*\]\((/assets/img/[^)]+)\)", body)
                if m:
                    front["image"] = m.group(1)
            front["permalink"] = f"/{slug}/{url_id}"
            if kind == "post":
                rel = f"{folder}/{date.strftime('%Y-%m-%d')}-{url_id}.md"
            else:
                rel = f"{folder}/{url_id}.md"
            if title in seen_titles:
                self.report.add("Probable duplicates (same title)",
                                f"/{slug}/{url_id} duplicates /{slug}/{seen_titles[title]}")
            else:
                seen_titles[title] = url_id
            self.write(rel, front, body)
        print(f"{slug}: {len(items)} items")

    def banner(self, slug: str, coll: dict) -> None:
        """Page banner = Squarespace page thumbnail + description overlay."""
        img = (coll.get("mainImage") or {}).get("assetUrl")
        if not img:
            return
        desc = BeautifulSoup(coll.get("description") or "", "html.parser")
        lines = [_norm(p.get_text(" ")) for p in desc.find_all("p") if _norm(p.get_text(" "))]
        fp = (coll.get("mainImage") or {}).get("mediaFocalPoint") or {}
        self.banners[slug] = {"image": self.image(img, "banners"),
                              "position": f"{round(fp.get('x', .5) * 100)}% {round(fp.get('y', .5) * 100)}%",
                              "title": lines[0] if lines else "",
                              "subtitle": lines[1] if len(lines) > 1 else ""}

    def export_pages(self):
        for slug in PAGES:
            d = self.get_json(f"/{slug}")
            self.banner(slug, d.get("collection") or {})
            html = d.get("mainContent") or ""
            title = _norm((d.get("collection") or {}).get("title") or slug)
            if slug == "team":
                self.export_team(html)
                continue
            if slug == "home":
                self.export_home(html)
                continue
            body = self.blocks_to_md(html, slug, f"/{slug}")
            if slug in GENERATED_PAGES:
                continue
            if not body.strip():
                # Some "empty" pages are short links: a meta refresh in the page's header
                # code injection, which the JSON view doesn't expose. Check the HTML.
                target = self.refresh_target(f"/{slug}")
                if target:
                    self.report.add("Redirect pages (keep in _data/redirects.yml)", f"/{slug} -> {target}")
                else:
                    self.report.add("Empty pages (not exported; delete or redirect)", f"/{slug}")
                continue
            front = {"title": title, "permalink": f"/{slug}"}
            if slug in self.banners:
                front["banner"] = slug
            self.write(f"_pages/{slug}.md", front, body)
        (self.out / "_data" / "banners.yml").write_text(
            yaml.safe_dump(self.banners, sort_keys=False, allow_unicode=True, width=1000))
        print(f"pages: {len(PAGES)}")

    def export_home(self, html: str):
        soup = BeautifulSoup(html, "html.parser")
        intro = None
        for b in soup.select(".sqs-block-html"):
            if "Welcome to" in b.get_text():
                intro = self.md(b.select_one(".sqs-html-content") or b)
        sponsors = []
        for g in soup.select(".sqs-block-gallery"):
            for img in g.select("img[data-src]"):
                name = os.path.splitext(img.get("alt") or "")[0]
                name = SPONSOR_NAMES.get(name, name)
                sponsors.append({"name": name, "logo": self.image(img["data-src"], "sponsors")})
        (self.out / "_data").mkdir(exist_ok=True)
        (self.out / "_data" / "sponsors.yml").write_text(yaml.safe_dump(sponsors, sort_keys=False))
        (self.out / "_includes").mkdir(exist_ok=True)
        (self.out / "_includes" / "home-intro.md").write_text((intro or "") + "\n")

    def export_team(self, html: str):
        soup = BeautifulSoup(html, "html.parser")
        sections: list[dict] = [{"title": "Current Members", "people": []}]
        photos: list[dict] = []
        join_md = ""
        for b in soup.select(".sqs-block"):
            kind = b.get("data-definition-name") or " ".join(b.get("class", []))
            if "html-block" in kind:
                text = _norm(b.get_text(" "))
                if text.startswith("Join Us"):
                    join_md = re.sub(r"^#.*\n+", "", self.md(b.select_one(".sqs-html-content") or b))
                elif text and text.lower() not in ("lab photos", "alumni"):
                    title = " ".join(w.capitalize() if w.isupper() and len(w) > 2 else w for w in text.split())
                    sections.append({"title": title, "people": []})
            elif kind == "website.components.imageLayout":
                url, _ = self.img_from(b)
                cap = b.select_one(".image-caption")
                link = b.select_one("a.sqs-block-image-link")
                person = self.parse_person(cap)
                person["photo"] = self.image(url, "team")
                if link and link.get("href"):
                    person.setdefault("website", self.fix_href(link["href"]))
                sections[-1]["people"].append(person)
            elif "gallery-block" in kind:
                for slide in b.select(".slide"):
                    url, alt = self.img_from(slide)
                    t = slide.select_one(".meta-title")
                    photos.append({"caption": t.get_text(" ", strip=True) if t else alt,
                                   "image": self.image(url, "lab-photos")})
        # `year`, `pin` and `rank` exist only in the repo (Squarespace has no such fields): carry them
        # over from the current team.yml so a re-export doesn't erase them.
        path = self.out / "_data" / "team.yml"
        keep: dict = {}
        if path.exists():
            for s in (yaml.safe_load(path.read_text()) or {}).get("sections", []):
                for p in s.get("people", []):
                    keep[(s.get("title"), p.get("name"))] = {k: p[k] for k in ("pin", "year", "rank") if k in p}
        for s in sections:
            for i, p in enumerate(s["people"]):
                extra = keep.get((s["title"], p.get("name")))
                if extra is None:
                    extra = {"year": None}
                items = list(p.items())
                at = next((n + 1 for n, (k, _) in enumerate(items) if k == "roles"), len(items))
                s["people"][i] = dict(items[:at] + list(extra.items()) + items[at:])
        data = {"sections": [s for s in sections if s["people"]], "lab_photos": photos, "join_us": join_md}
        (self.out / "_data").mkdir(exist_ok=True)
        header = (
            "# Team page data. The first section is \"Current Members\"; every later section is shown\n"
            "# under \"Alumni\". Each section is ordered by `year` (format: 2024 or 2024-09):\n"
            "#   current members: year joined, earliest first;  alumni: year left, most recent first.\n"
            "# People without a year are listed last, in the order they appear here. Optional `rank`\n"
            "# (lower first) groups people within a section, e.g. visiting faculty / PhD / undergrads.\n")
        body = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=1000)
        body = body.replace("    year: null\n", "    year:\n").replace("    pin: true\n", "    pin: true   # always first\n")
        path.write_text(header + body)

    def parse_person(self, cap: Tag | None) -> dict:
        if cap is None:
            return {}
        lines: list[str] = []
        website = None
        for p in cap.find_all("p"):
            for a in p.find_all("a"):
                if a.get_text(strip=True).lower() == "website":
                    website = a.get("href")
                    a.decompose()
            for br in p.find_all("br"):
                br.replace_with("\n")
            lines += [_norm(x) for x in p.get_text().split("\n") if _norm(x)]
        person: dict = {}
        if lines:
            person["name"] = lines.pop(0)
        for ln in lines:
            low = ln.lower()
            if low.startswith("office"):
                person["office"] = ln.split(" ", 1)[1].strip()
            elif "@" in ln and " " not in ln:
                person["email"] = ln
            elif low.startswith("next:"):
                person["next"] = ln.split(":", 1)[1].strip()
            else:
                person.setdefault("roles", []).append(ln)
        if website:
            person["website"] = self.fix_href(website)
        return person

    def run(self):
        for slug in COLLECTIONS:
            self.export_collection(slug)
        self.export_pages()
        self.report.add("Stats", f"{len(self.images)} images downloaded to assets/img/")
        self.report.write(self.out / "tools" / "export-report.md")
        print(f"images: {len(self.images)}; report: tools/export-report.md")


SPONSOR_NAMES = {"facebook_research": "Facebook Research", "redhat": "Red Hat",
                 "Cisco_logo_PNG2": "Cisco", "Meta_logo-small": "Meta"}


class _Converter(MarkdownConverter):
    """Keep inline HTML that Markdown can't express (iframes, tables w/ spans, etc.)."""

    def convert_iframe(self, el, text, *args, **kwargs):
        return "\n\n" + str(el) + "\n\n"

    def convert_figure(self, el, text, *args, **kwargs):
        return "\n\n" + text.strip() + "\n\n"


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").replace("\xa0", " ")).strip()


def _attr(s: str) -> str:
    return s.replace('"', "&quot;")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--site", default="https://disc.bu.edu")
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--cache", default=None, help="directory to cache raw JSON responses")
    a = ap.parse_args()
    Exporter(a.site, Path(a.out), Path(a.cache) if a.cache else None).run()


if __name__ == "__main__":
    sys.exit(main())
