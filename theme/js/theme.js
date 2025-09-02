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
})();
