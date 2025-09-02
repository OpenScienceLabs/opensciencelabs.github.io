/* /js/theme.js */
(function () {
  const STORAGE_KEY = 'osl-color-mode';
  const docEl = document.documentElement;

  function applyMode(mode) {
    const bs = (mode === 'dim') ? 'dark' : 'light';
    docEl.setAttribute('data-mode', mode);
    docEl.setAttribute('data-bs-theme', bs);
    try { localStorage.setItem(STORAGE_KEY, mode); } catch (e) {}

    const toggle = document.getElementById('mode');
    if (toggle) {
      toggle.checked = (mode === 'dim');
      toggle.setAttribute('aria-checked', String(toggle.checked));
    }
  }

  function getInitialMode() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved === 'dim' || saved === 'lit') return saved;
    } catch (e) {}
    return (window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches) ? 'dim' : 'lit';
  }

  window.addEventListener('DOMContentLoaded', function () {
    /* 1) Color mode */
    const currentAttr = docEl.getAttribute('data-mode');
    const mode = (currentAttr === 'dim' || currentAttr === 'lit') ? currentAttr : getInitialMode();
    applyMode(mode);

    const toggle = document.getElementById('mode');
    if (toggle) {
      toggle.checked = (mode === 'dim');
      toggle.setAttribute('aria-checked', String(toggle.checked));
      toggle.addEventListener('change', function () {
        applyMode(this.checked ? 'dim' : 'lit');
      }, false);
    }

    /* 2) Copyright year */
    document.querySelectorAll('.year').forEach(n => n.textContent = String(new Date().getFullYear()));

    /* 3) MkDocs search (desktop + mobile) if available */
    if (typeof window.initSearch === 'function') {
      const desktopSearch = document.getElementById('mkdocs-search');
      const mobileSearch  = document.getElementById('mkdocs-search-mobile');
      if (desktopSearch) window.initSearch(desktopSearch);
      if (mobileSearch)  window.initSearch(mobileSearch);
    }

    /* 4) Close offcanvas after selecting a link (not when toggling accordions) */
    const offcanvasEl = document.getElementById('offcanvasNav');
    if (offcanvasEl) {
      offcanvasEl.addEventListener('click', function (e) {
        const a = e.target.closest('a');
        if (!a) return; // ignore clicks on accordion buttons etc.
        const offcanvas = bootstrap.Offcanvas.getInstance(offcanvasEl) ||
                          new bootstrap.Offcanvas(offcanvasEl);
        // Close for internal links (no target="_blank")
        if (a.getAttribute('href') && !a.getAttribute('target')) {
          offcanvas.hide();
        }
      });
    }

    /* 5) Mega dropdown accordions: ensure one-open-at-a-time via data-bs-parent */
    document.querySelectorAll('.dropdown-menu.mega .accordion').forEach((acc, i) => {
      // Make sure the accordion has an id
      if (!acc.id) acc.id = `mega-acc-${i}`;
      const parentSel = `#${acc.id}`;

      // For each collapse pane, set data-bs-parent if missing
      acc.querySelectorAll('.accordion-collapse').forEach(col => {
        if (!col.getAttribute('data-bs-parent')) {
          col.setAttribute('data-bs-parent', parentSel);
        }
      });
    });

    /* 6) Keep clicks inside mega from bubbling to the dropdown toggle (belt & suspenders).
          With data-bs-auto-close="outside" this isn’t strictly needed, but it’s harmless. */
    document.querySelectorAll('.dropdown-menu.mega').forEach(menu => {
      menu.addEventListener('click', (e) => e.stopPropagation());
    });
  });

  // Optional public API
  window.OSLTheme = {
    getMode: () => docEl.getAttribute('data-mode'),
    setMode: (m) => applyMode(m === 'dim' ? 'dim' : 'lit'),
    clearPreference: () => { try { localStorage.removeItem(STORAGE_KEY); } catch (e) {} }
  };

  // --- Minimal extras formerly in bundle.js ---

  // A) external links => target=_blank, rel=noopener
  document.querySelectorAll('a[href^="http"]').forEach(a => {
    try {
      const url = new URL(a.href);
      // skip same-origin
      if (url.origin === window.location.origin) return;
      if (!a.hasAttribute('target')) a.setAttribute('target', '_blank');
      if (!a.hasAttribute('rel')) a.setAttribute('rel', 'noopener');
    } catch (_) {}
  });

  // B) small “copy code” buttons for pygments blocks (MkDocs default markup)
  document.querySelectorAll('div.highlight > pre').forEach((pre, i) => {
    // container for the button
    const wrap = pre.parentElement; // .highlight
    wrap.style.position = 'relative';

    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'btn btn-sm btn-secondary position-absolute top-0 end-0 m-2 copy-code';
    btn.setAttribute('aria-label', 'Copy code');
    btn.textContent = 'Copy';

    btn.addEventListener('click', async () => {
      const code = pre.innerText;
      try {
        await navigator.clipboard.writeText(code);
        const old = btn.textContent;
        btn.textContent = 'Copied!';
        setTimeout(() => (btn.textContent = old), 1200);
      } catch (e) {
        // fallback
        const ta = document.createElement('textarea');
        ta.value = code;
        ta.style.position = 'fixed';
        ta.style.left = '-9999px';
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        const old = btn.textContent;
        btn.textContent = 'Copied!';
        setTimeout(() => (btn.textContent = old), 1200);
      }
    });

    wrap.appendChild(btn);
  });

  // C) heading anchors (h2–h4) inside main content
  const contentRoot = document.querySelector('main .content-inner') || document.querySelector('main');
  if (contentRoot) {
    contentRoot.querySelectorAll('h2[id], h3[id], h4[id]').forEach(h => {
      if (h.querySelector('a.anchor-link')) return; // idempotent
      const a = document.createElement('a');
      a.href = `#${h.id}`;
      a.className = 'anchor-link ms-2';
      a.setAttribute('aria-label', 'Copy link to this section');
      a.innerHTML = '¶'; // simple mark; you can swap for an SVG if you prefer
      a.addEventListener('click', (e) => {
        // let it navigate, then copy
        setTimeout(() => navigator.clipboard.writeText(window.location.href), 0);
      });
      h.appendChild(a);
    });
  }

})();


// --- Search results link absolutizer ---
(function () {
  // Which containers might hold search result links?
  const candidates = [
    '.mk-search-results',
    '.search-results',
    '#mkdocs-search-results'
  ];

  function absolutize(href) {
    if (!href) return href;
    if (/^([a-z]+:)?\/\//i.test(href)) return href;      // already absolute URL
    if (href.startsWith('/')) return href;                // already site-absolute
    return '/' + href.replace(/^\/+/, '');                // make it site-absolute
  }

  function fixLinks(root = document) {
    candidates.forEach(sel => {
      root.querySelectorAll(`${sel} a[href]`).forEach(a => {
        const fixed = absolutize(a.getAttribute('href'));
        if (fixed && fixed !== a.getAttribute('href')) a.setAttribute('href', fixed);
      });
    });
  }

  // 1) Run once after DOM ready (in case results render immediately)
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => fixLinks());
  } else {
    fixLinks();
  }

  // 2) Watch for results being (re)rendered
  const obs = new MutationObserver(muts => {
    for (const m of muts) {
      if (m.type === 'childList' && (m.addedNodes && m.addedNodes.length)) {
        fixLinks(document);
      }
    }
  });
  obs.observe(document.body, { childList: true, subtree: true });
})();
