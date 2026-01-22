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
        if (!a) return;
        const offcanvas = bootstrap.Offcanvas.getInstance(offcanvasEl) ||
                          new bootstrap.Offcanvas(offcanvasEl);
        if (a.getAttribute('href') && !a.getAttribute('target')) {
          offcanvas.hide();
        }
      });
    }

    /* 5) Mega dropdown accordions */
    document.querySelectorAll('.dropdown-menu.mega .accordion').forEach((acc, i) => {
      if (!acc.id) acc.id = `mega-acc-${i}`;
      const parentSel = `#${acc.id}`;
      acc.querySelectorAll('.accordion-collapse').forEach(col => {
        if (!col.getAttribute('data-bs-parent')) {
          col.setAttribute('data-bs-parent', parentSel);
        }
      });
    });

    /* 6) Stop mega menu click bubbling */
    document.querySelectorAll('.dropdown-menu.mega').forEach(menu => {
      menu.addEventListener('click', (e) => e.stopPropagation());
    });

    /* =========================================================
       7) Client-side Text-to-Speech (Listen to Article)
       ========================================================= */
    if ('speechSynthesis' in window) {
      const ttsBtn = document.getElementById('tts-btn');
      let speaking = false;
      let utterance = null;

      function getArticleText() {
        const main = document.querySelector('main');
        return main ? main.innerText : '';
      }

      if (ttsBtn) {
        ttsBtn.addEventListener('click', function () {
          if (speaking) {
            window.speechSynthesis.cancel();
            speaking = false;
            ttsBtn.textContent = 'Listen to article';
            return;
          }

          const text = getArticleText();
          if (!text) return;

          utterance = new SpeechSynthesisUtterance(text);
          utterance.lang = 'en-US';
          utterance.rate = 1;

          utterance.onend = function () {
            speaking = false;
            ttsBtn.textContent = 'Listen to article';
          };

          window.speechSynthesis.speak(utterance);
          speaking = true;
          ttsBtn.textContent = 'Stop listening';
        });
      }
    }
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
      if (url.origin === window.location.origin) return;
      if (!a.hasAttribute('target')) a.setAttribute('target', '_blank');
      if (!a.hasAttribute('rel')) a.setAttribute('rel', 'noopener');
    } catch (_) {}
  });

  // B) copy code buttons
  document.querySelectorAll('div.highlight > pre').forEach((pre, i) => {
    const wrap = pre.parentElement;
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

  // C) heading anchors
  const contentRoot = document.querySelector('main .content-inner') || document.querySelector('main');
  if (contentRoot) {
    contentRoot.querySelectorAll('h2[id], h3[id], h4[id]').forEach(h => {
      if (h.querySelector('a.anchor-link')) return;
      const a = document.createElement('a');
      a.href = `#${h.id}`;
      a.className = 'anchor-link ms-2';
      a.setAttribute('aria-label', 'Copy link to this section');
      a.innerHTML = '¶';
      a.addEventListener('click', () => {
        setTimeout(() => navigator.clipboard.writeText(window.location.href), 0);
      });
      h.appendChild(a);
    });
  }

})();


// --- Search results link absolutizer ---
(function () {
  const candidates = [
    '.mk-search-results',
    '.search-results',
    '#mkdocs-search-results'
  ];

  function absolutize(href) {
    if (!href) return href;
    if (/^([a-z]+:)?\/\//i.test(href)) return href;
    if (href.startsWith('/')) return href;
    return '/' + href.replace(/^\/+/, '');
  }

  function fixLinks(root = document) {
    candidates.forEach(sel => {
      root.querySelectorAll(`${sel} a[href]`).forEach(a => {
        const fixed = absolutize(a.getAttribute('href'));
        if (fixed && fixed !== a.getAttribute('href')) {
          a.setAttribute('href', fixed);
        }
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => fixLinks());
  } else {
    fixLinks();
  }

  const obs = new MutationObserver(muts => {
    for (const m of muts) {
      if (m.type === 'childList' && m.addedNodes.length) {
        fixLinks(document);
      }
    }
  });
  obs.observe(document.body, { childList: true, subtree: true });
})();
