/* /js/theme.js */
(function () {
  const STORAGE_KEY = 'osl-color-mode';
  const docEl = document.documentElement;

  function applyMode(mode) {
    const bs = (mode === 'dim') ? 'dark' : 'light';
    docEl.setAttribute('data-mode', mode);
    docEl.setAttribute('data-bs-theme', bs);
    try { localStorage.setItem(STORAGE_KEY, mode); } catch (e) {}
    // sync the checkbox UI if present
    const toggle = document.getElementById('mode');
    if (toggle) toggle.checked = (mode === 'dim');
    // ARIA (if you later add role="switch")
    if (toggle) toggle.setAttribute('aria-checked', String(toggle.checked));
  }

  function getInitialMode() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved === 'dim' || saved === 'lit') return saved;
    } catch (e) {}
    return (window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches) ? 'dim' : 'lit';
  }

  /* === On DOM ready === */
  window.addEventListener('DOMContentLoaded', function () {
    // 1) Ensure mode attributes & checkbox state are in sync
    const currentAttr = docEl.getAttribute('data-mode');
    const mode = currentAttr === 'dim' || currentAttr === 'lit' ? currentAttr : getInitialMode();
    applyMode(mode);

    const toggle = document.getElementById('mode');
    if (toggle) {
      // initialize checked state
      toggle.checked = (mode === 'dim');
      toggle.setAttribute('aria-checked', String(toggle.checked));
      toggle.addEventListener('change', function () {
        applyMode(this.checked ? 'dim' : 'lit');
      }, false);
    }

    // 2) Copyright year
    document.querySelectorAll('.year').forEach(n => n.textContent = String(new Date().getFullYear()));

    // 3) MkDocs search (desktop + mobile) if available
    if (typeof window.initSearch === 'function') {
      const desktopSearch = document.getElementById('mkdocs-search');
      const mobileSearch  = document.getElementById('mkdocs-search-mobile');
      if (desktopSearch) window.initSearch(desktopSearch);
      if (mobileSearch)  window.initSearch(mobileSearch);
    }

    // 4) Close offcanvas after selecting a link
    const offcanvasEl = document.getElementById('offcanvasNav');
    if (offcanvasEl) {
      offcanvasEl.addEventListener('click', function (e) {
        const a = e.target.closest('a');
        if (!a) return;
        const offcanvas = bootstrap.Offcanvas.getInstance(offcanvasEl) ||
                          new bootstrap.Offcanvas(offcanvasEl);
        // internal links: close immediately
        if (a.getAttribute('href') && !a.getAttribute('target')) {
          offcanvas.hide();
        }
      });
    }
  });

  // optional public API
  window.OSLTheme = {
    getMode: () => docEl.getAttribute('data-mode'),
    setMode: (m) => applyMode(m === 'dim' ? 'dim' : 'lit'),
    clearPreference: () => { try { localStorage.removeItem(STORAGE_KEY); } catch (e) {} }
  };
})();
