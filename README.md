# disc.bu.edu

Source for the [DiSC lab](https://disc.bu.edu) website — a [Jekyll](https://jekyllrb.com) site
deployed to GitHub Pages by `.github/workflows/pages.yml` on every push to `main`.
It was ported from Squarespace in November 2026 with `tools/export_squarespace.py`.

## Run locally

```bash
bundle install
bundle exec jekyll serve --livereload   # http://localhost:4000
```

## Where things live

| What | Where | URL |
|---|---|---|
| Papers | `_papers/<slug>.md` | `/papers/<slug>` |
| News posts | `_posts/YYYY-MM-DD-<slug>.md` | `/news-blog/<slug>` |
| Demos / project pages | `_minipages/<slug>.md` (set `external_url` to link out) | `/minipages/<slug>` |
| Team & alumni, lab photos, "Join us" | `_data/team.yml` | `/team` |
| Sponsors (home page) | `_data/sponsors.yml` | `/` |
| Home intro text | `_includes/home-intro.md` | `/` |
| Other pages (Projects, Classes, Artifacts…) | `_pages/*.md` | `/<slug>` |
| Header menu | `_data/navigation.yml` | |
| Redirects for old URLs | `_data/redirects.yml` | |
| Images | `assets/img/<section>/` | |
| Styles / JS | `assets/css/main.css`, `assets/js/site.js` | |

Tag pages (`/papers/tag/PVLDB`, …) are generated automatically from paper `tags`.

**Fonts** are the same as on the Squarespace site. Proxima Nova, Adobe Garamond Pro and Effra
come from the lab's Adobe Fonts web project (`https://use.typekit.net/xtb8lri.css`, linked in
`_layouts/default.html`), which is managed at fonts.adobe.com under the Adobe account that
created it. Montserrat comes from Google Fonts. If the Adobe subscription lapses, the site falls
back to similar system fonts.

### Add a paper

Create `_papers/vldb27-someone.md`:

```yaml
---
title: "Paper title"
date: 2027-01-15
tags: [PVLDB]                 # venue tag(s); drive the filter on /publications
venue: Proceedings of the VLDB Endowment, Vol. 20(5), 2027
authors: First Author, Manos Athanassoulis
links:
  - {label: Official PDF, url: "https://www.vldb.org/pvldb/..."}
  - {label: Local PDF, url: "https://cs-people.bu.edu/mathan/publications/vldb27-someone.pdf"}
order: 81                     # higher = listed first; use the current max + 1
permalink: /papers/vldb27-someone
---

# Abstract

...
```

### Add a news post

Create `_posts/2027-01-15-short-slug.md` with `title`, `date`, `permalink: /news-blog/short-slug`,
and optionally `image:` (thumbnail on the News page; defaults to nothing). Put images in
`assets/img/news-blog/`.

### Add a team member

Add an entry under the first section (Current Members) of `_data/team.yml`, with their photo
in `assets/img/team/` (square works best):

```yaml
  - name: Jane Doe
    roles:
    - PhD Researcher
    year: 2026-09          # year joined: 2026 or 2026-09
    office: CCDS 9xx       # people with an office get a large photo
    email: jdoe@bu.edu
    website: https://cs-people.bu.edu/jdoe/
    photo: /assets/img/team/jane-doe.jpg
```

Current members are ordered by `year` joined, earliest first; alumni sections by `year`
left, most recent first. A bare `2026` sorts after any `2026-MM`; people without a year come
last, in file order. `pin: true` keeps someone on top. An optional `rank` groups people
within a section (lower first): Visiting Researchers use 1 for faculty, 2 for PhD students
and 3 for undergrads, and each group is ordered by year.

### Move a member to alumni

Cut their entry from Current Members and paste it into the right alumni section, then:

- remove `office` and `email`;
- set `year` to when they left (e.g. `2027-05`);
- add `next:` with what they do next (shown as "next: …");
- optionally replace `website` with a link that will outlive their BU page.

## Going live (DNS cutover)

1. In the repo's **Settings → Pages**, *Source* is set to **GitHub Actions** (done). Every push
   to `main` builds and deploys the site.
2. Check the site at https://bu-disc.github.io/disc.bu.edu/. There it lives in a subfolder, so
   the build adds `/disc.bu.edu` to every link and image (`_plugins/baseurl_links.rb`, with the
   folder passed in by the workflow); content files keep plain `/team`-style paths.
3. Set **Custom domain** to `disc.bu.edu` in Settings → Pages (no `CNAME` file is needed with
   GitHub Actions) and ask BU IT to point `disc.bu.edu` at GitHub Pages (a `CNAME` record to
   `bu-disc.github.io`). The next deploy then builds for the root of the domain automatically.
4. Once DNS has switched and HTTPS is issued, cancel the Squarespace plan.

## Re-running the export

Note: the export regenerates `_data/team.yml` from Squarespace (keeping the `year` and `pin`
values already in the file), so after the switch edit the files directly instead.

`tools/export_squarespace.py` regenerates all content from the live Squarespace site (only
useful before the cutover; it overwrites `_papers`, `_posts`, `_minipages`, `_blog`, `_pages`,
`_data/team.yml`, `_data/sponsors.yml`). See `tools/export-report.md` for what it flagged.

```bash
python3 -m venv .venv && .venv/bin/pip install -r tools/requirements.txt
.venv/bin/python tools/export_squarespace.py
```
