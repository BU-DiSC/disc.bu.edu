// Mobile side menu, header dropdowns, the home-page carousel and the team slideshow.
(function () {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      document.body.classList.toggle('nav-open', open);
      toggle.setAttribute('aria-expanded', open);
    });
  }
  const folders = [...document.querySelectorAll('.folder')];
  const closeFolders = (except) => folders.forEach((f) => {
    if (f === except) return;
    f.classList.remove('open');
    f.querySelector('.folder-toggle')?.setAttribute('aria-expanded', 'false');
  });
  const desktop = () => window.matchMedia('(min-width: 901px)').matches;
  folders.forEach((f) => {
    const btn = f.querySelector('.folder-toggle');
    btn.addEventListener('click', () => {
      closeFolders(f);
      const open = f.classList.toggle('open');
      btn.setAttribute('aria-expanded', open);
    });
    // On desktop the dropdown follows the mouse, like Squarespace's: leaving it closes it.
    f.addEventListener('mouseleave', () => { if (desktop()) closeFolders(); });
    // Picking a link closes the menu, so it isn't left open when the link opens a new tab.
    f.querySelectorAll('.subnav a').forEach((a) => a.addEventListener('click', () => {
      a.blur();
      if (desktop()) closeFolders();
    }));
  });
  document.addEventListener('click', (e) => { if (!e.target.closest('.folder')) closeFolders(); });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && document.activeElement?.closest('.folder')) document.activeElement.blur();
    if (e.key === 'Escape') closeFolders();
  });
  // Coming back with the Back button restores the old page state; start with menus closed.
  window.addEventListener('pageshow', () => closeFolders());

  document.querySelectorAll('[data-carousel]').forEach((root) => {
    const track = root.querySelector('.carousel-track');
    const prev = root.querySelector('.prev');
    const next = root.querySelector('.next');
    const step = () => track.clientWidth;
    const update = () => {
      prev.disabled = track.scrollLeft <= 1;
      next.disabled = track.scrollLeft + track.clientWidth >= track.scrollWidth - 1;
    };
    prev.addEventListener('click', () => { track.scrollLeft -= step(); setTimeout(update, 400); });
    next.addEventListener('click', () => { track.scrollLeft += step(); setTimeout(update, 400); });
    update();
  });

  // Team lab photos, like the Squarespace slideshow: photos crossfade, and the thumbnail
  // strip glides to keep the current photo's thumbnail centered (stopping at either end).
  document.querySelectorAll('[data-slideshow]').forEach((root) => {
    const slides = [...root.querySelectorAll('.slide')];
    const thumbs = [...root.querySelectorAll('.thumb')];
    const strip = root.querySelector('.thumbs');
    const track = root.querySelector('.thumbs-track');
    const FADE = 700;
    let i = 0;
    let busy = false;
    // Fit the caption to the photo's displayed box (object-fit: contain letterboxes it).
    const fitCaption = (k = i) => {
      const img = slides[k].querySelector('img');
      const cap = slides[k].querySelector('figcaption');
      if (!cap || !img.naturalWidth) return;
      const W = slides[k].clientWidth, H = slides[k].clientHeight;
      const s = Math.min(W / img.naturalWidth, H / img.naturalHeight);
      const w = img.naturalWidth * s, h = img.naturalHeight * s;
      cap.style.left = `${(W - w) / 2}px`;
      cap.style.right = `${(W - w) / 2}px`;
      cap.style.bottom = `${(H - h) / 2}px`;
    };
    const centerThumb = () => {
      if (!track || !thumbs[i]) return;
      const t = thumbs[i];
      const max = Math.max(0, track.scrollWidth - strip.clientWidth);
      const x = Math.min(max, Math.max(0, t.offsetLeft + t.offsetWidth / 2 - strip.clientWidth / 2));
      track.style.transform = `translateX(${-x}px)`;
    };
    slides.forEach((sl, k) => sl.querySelector('img').addEventListener('load', () => fitCaption(k)));
    thumbs.forEach((t) => t.querySelector('img').addEventListener('load', centerThumb));
    window.addEventListener('resize', () => { fitCaption(); centerThumb(); });
    const show = (n) => {
      n = (n + slides.length) % slides.length;
      if (busy || n === i) return;
      busy = true;
      const old = slides[i];
      old.classList.remove('active');
      old.classList.add('leaving');
      thumbs[i]?.classList.remove('active');
      i = n;
      const img = slides[i].querySelector('img');
      img.loading = 'eager';
      slides[i].classList.add('active');
      thumbs[i]?.classList.add('active');
      fitCaption();
      centerThumb();
      setTimeout(() => { old.classList.remove('leaving'); busy = false; }, FADE);
    };
    root.classList.add('animated');
    fitCaption();
    centerThumb();
    root.querySelector('.prev').addEventListener('click', () => show(i - 1));
    root.querySelector('.next').addEventListener('click', () => show(i + 1));
    thumbs.forEach((t, n) => t.addEventListener('click', () => show(n)));
  });

  // Banners: like Squarespace, center the image on its focal point (CSS percentages
  // align the focal point with the same point of the box instead, which crops differently).
  document.querySelectorAll('.banner[data-focal]').forEach((banner) => {
    const el = banner.querySelector('.banner-image') || banner;
    const [fx, fy] = banner.dataset.focal.split(' ').map((v) => parseFloat(v) / 100);
    const url = getComputedStyle(el).backgroundImage.slice(5, -2);
    const img = new Image();
    const place = () => {
      const W = el.clientWidth, H = el.clientHeight;
      const s = Math.max(W / img.naturalWidth, H / img.naturalHeight);
      const w = img.naturalWidth * s, h = img.naturalHeight * s;
      const x = Math.min(0, Math.max(W - w, W / 2 - fx * w));
      const y = Math.min(0, Math.max(H - h, H / 2 - fy * h));
      el.style.backgroundPosition = `${x}px ${y}px`;
    };
    img.onload = () => { place(); window.addEventListener('resize', place); };
    img.src = url;
  });

  // Pre-footer: reveal its content when it scrolls into view (as the Squarespace template does).
  const preFooter = document.querySelector('.pre-footer');
  if (preFooter && 'IntersectionObserver' in window) {
    const rect = preFooter.getBoundingClientRect();
    if (rect.top > window.innerHeight) {
      preFooter.classList.add('unscrolled');
      const io = new IntersectionObserver((entries) => {
        if (entries.some((e) => e.isIntersecting)) { preFooter.classList.remove('unscrolled'); io.disconnect(); }
      });
      io.observe(preFooter);
    }
  }

  // News: place each item in the currently shortest column, left to right.
  document.querySelectorAll('.news-grid').forEach((grid) => {
    const items = [...grid.children];
    const layout = () => {
      const n = getComputedStyle(grid).gridTemplateColumns.split(' ').length;
      grid.querySelectorAll('.masonry-col').forEach((c) => c.remove());
      const cols = Array.from({ length: n }, () => {
        const c = document.createElement('div');
        c.className = 'masonry-col';
        grid.appendChild(c);
        return c;
      });
      // Like Squarespace, size every thumbnail from the narrow (first) column's width, so
      // the slightly wider last column crops its images instead of making them taller.
      const base = cols[0].clientWidth;
      items.forEach((it) => {
        const img = it.querySelector('.summary-thumbnail img');
        if (img && img.naturalWidth) img.style.height = `${(base * img.naturalHeight) / img.naturalWidth}px`;
      });
      items.forEach((it) => {
        const shortest = cols.reduce((a, b) => (b.offsetHeight < a.offsetHeight ? b : a));
        shortest.appendChild(it);
      });
    };
    let lastN = 0, lastW = 0;
    const maybeLayout = () => {
      const n = getComputedStyle(grid).gridTemplateColumns.split(' ').length;
      const w = grid.clientWidth;
      if (n !== lastN || w !== lastW) { lastN = n; lastW = w; layout(); }
    };
    // Re-run once images have their real heights.
    const imgs = items.map((i) => i.querySelector('img')).filter(Boolean);
    Promise.all(imgs.map((im) => (im.complete ? 0 : new Promise((r) => { im.onload = im.onerror = r; }))))
      .then(() => { lastN = 0; maybeLayout(); });
    imgs.forEach((im) => { im.loading = 'eager'; });
    maybeLayout();
    window.addEventListener('resize', maybeLayout);
  });
})();
