/* OSL Search – minimal Lunr typeahead for MkDocs
   - Requires lunr.min.js (and optional lunr-languages) loaded BEFORE this file.
   - Exposes window.initSearch(inputEl) so theme.js can initialize both desktop & mobile fields.
*/

(function () {
  'use strict';

  const INDEX_URL = '/search/search_index.json';
  const MAX_RESULTS = 8;
  const MIN_QUERY_LEN = 2;

  // Internal state (built once)
  let _docs = null;           // array of { title, text, location }
  let _byRef = null;          // Map(location -> doc)
  let _idx = null;            // lunr.Index
  let _building = null;       // build promise (avoid duplicate builds)

  // --- Utilities -----------------------------------------------------------

  function toAbsolute(href) {
    if (!href) return href;
    // keep full URLs as-is
    if (/^([a-z]+:)?\/\//i.test(href)) return href;
    // force site-rooted path
    return '/' + href.replace(/^\/+/, '');
  }

  function injectBaseStylesOnce() {
    if (document.getElementById('osl-search-styles')) return;
    const css = `
      .osl-search-panel {
        position: absolute;
        z-index: 1055; /* above navbar/offcanvas */
        min-width: 280px;
        max-width: 560px;
        max-height: 60vh;
        overflow-y: auto;
        background: var(--dd-bg, rgba(20,20,28,.98));
        border: 1px solid var(--dd-border, rgba(255,255,255,.12));
        border-radius: .5rem;
        box-shadow: 0 6px 28px rgba(0,0,0,.25);
        padding: .35rem;
      }
      .osl-search-item {
        display: block;
        text-decoration: none;
        padding: .5rem .6rem;
        border-radius: .375rem;
        color: var(--fg, #e8e8ea);
      }
      .osl-search-item:hover,
      .osl-search-item.is-active {
        background: var(--dd-hover-bg, rgba(255,255,255,.08));
        color: var(--dd-hover, #fff);
      }
      .osl-search-title {
        font-weight: 600;
        line-height: 1.25;
        margin: 0 0 .15rem 0;
      }
      .osl-search-snippet {
        font-size: .875rem;
        line-height: 1.25rem;
        opacity: .82;
        margin: 0;
      }
      .osl-search-empty {
        padding: .6rem .7rem;
        color: var(--fg, #e8e8ea);
        opacity: .8;
      }
      .osl-search-mark { background: rgba(255, 208, 0, .35); border-radius: .2rem; }
    `;
    const style = document.createElement('style');
    style.id = 'osl-search-styles';
    style.textContent = css;
    document.head.appendChild(style);
  }

  async function ensureLunrReady() {
    if (window.lunr) return;
    await new Promise((resolve) => {
      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', resolve, { once: true });
      } else {
        setTimeout(resolve, 0);
      }
    });
    if (!window.lunr) throw new Error('Lunr failed to load');
  }

  async function fetchIndexJSON() {
    const res = await fetch(INDEX_URL, { credentials: 'same-origin' });
    if (!res.ok) throw new Error(`Failed to fetch ${INDEX_URL}: ${res.status}`);
    const json = await res.json();
    // MkDocs "search" plugin typically returns { docs: [...] }
    return Array.isArray(json) ? json : (json.docs || []);
  }

  function normalizeDocs(arr) {
    return arr.map(d => ({
      title: d.title || '',
      text: d.text || '',
      location: d.location || ''
    }));
  }

  function buildSnippet(text, rawQuery) {
    if (!text) return '';
    const q = (rawQuery || '').trim();
    const MAX = 160;
    if (!q) return text.slice(0, MAX) + (text.length > MAX ? '…' : '');

    // find first occurrence of any term (basic, case-insensitive)
    const terms = q.split(/\s+/).filter(Boolean);
    let hit = -1, termUsed = '';
    for (const t of terms) {
      const idx = text.toLowerCase().indexOf(t.toLowerCase());
      if (idx !== -1 && (hit === -1 || idx < hit)) { hit = idx; termUsed = t; }
    }
    if (hit === -1) {
      return text.slice(0, MAX) + (text.length > MAX ? '…' : '');
    }
    const start = Math.max(0, hit - 40);
    const end = Math.min(text.length, hit + 120);
    let snip = (start > 0 ? '…' : '') + text.slice(start, end) + (end < text.length ? '…' : '');

    // simple highlight for all terms
    terms.forEach(t => {
      if (!t) return;
      const re = new RegExp(`(${escapeRegExp(t)})`, 'ig');
      snip = snip.replace(re, '<span class="osl-search-mark">$1</span>');
    });
    return snip;
  }

  function escapeRegExp(s) {
    return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  async function ensureIndex() {
    if (_idx) return _idx;
    if (_building) return _building;

    _building = (async () => {
      await ensureLunrReady();

      const raw = await fetchIndexJSON();
      _docs = normalizeDocs(raw);
      _byRef = new Map(_docs.map(d => [d.location, d]));

      // Build index
      const hasMulti = typeof lunr.multiLanguage === 'function';
      _idx = lunr(function () {
        if (hasMulti) {
          // Adjust languages if you only need some of them
          this.use(lunr.multiLanguage('en', 'es', 'pt'));
        }
        this.ref('location');
        this.field('title', { boost: 10 });
        this.field('text');

        _docs.forEach(doc => this.add(doc));
      });

      return _idx;
    })();

    try {
      return await _building;
    } finally {
      _building = null;
    }
  }

  function search(query) {
    if (!_idx) return [];
    if (!query || query.trim().length < MIN_QUERY_LEN) return [];
    // Keep it simple; allow prefix matches
    let q = query.trim();
    // Improve small queries a bit: foo -> foo*
    if (!/[~^*]/.test(q)) q = q.split(/\s+/).map(t => t + '*').join(' ');
    let hits = [];
    try {
      hits = _idx.search(q);
    } catch (e) {
      // fallback: plain search without wildcard if syntax error
      try { hits = _idx.search(query); } catch (_e) { hits = []; }
    }
    return hits.slice(0, MAX_RESULTS).map(h => {
      const doc = _byRef.get(h.ref);
      return doc ? { doc, score: h.score } : null;
    }).filter(Boolean);
  }

  // --- UI (panel) ---------------------------------------------------------

  function mkPanel() {
    const div = document.createElement('div');
    div.className = 'osl-search-panel';
    div.setAttribute('role', 'listbox');
    div.style.display = 'none';
    document.body.appendChild(div);
    return div;
  }

  function positionPanel(panel, inputEl) {
    const r = inputEl.getBoundingClientRect();
    const scrollY = window.scrollY || document.documentElement.scrollTop;
    const scrollX = window.scrollX || document.documentElement.scrollLeft;
    const width = Math.min(Math.max(r.width, 320), 560);
    panel.style.left = `${r.left + scrollX}px`;
    panel.style.top = `${r.bottom + scrollY + 6}px`;
    panel.style.width = `${width}px`;
  }

  function renderResults(panel, items, rawQuery) {
    panel.innerHTML = '';
    if (!items.length) {
      const empty = document.createElement('div');
      empty.className = 'osl-search-empty';
      empty.textContent = (rawQuery && rawQuery.length >= MIN_QUERY_LEN) ? 'No results' : 'Type to search…';
      panel.appendChild(empty);
      return;
    }
    items.forEach(({ doc }, idx) => {
      const a = document.createElement('a');
      a.className = 'osl-search-item';
      a.href = toAbsolute(doc.location);

      const title = document.createElement('div');
      title.className = 'osl-search-title';
      title.innerHTML = doc.title || '(untitled)';

      const snip = document.createElement('p');
      snip.className = 'osl-search-snippet';
      snip.innerHTML = buildSnippet(doc.text || '', rawQuery);

      a.appendChild(title);
      a.appendChild(snip);
      a.dataset.index = String(idx);
      panel.appendChild(a);
    });
  }

  function activateItem(panel, nextIndex) {
    const items = Array.from(panel.querySelectorAll('.osl-search-item'));
    if (!items.length) return -1;
    items.forEach(el => el.classList.remove('is-active'));
    const idx = Math.max(0, Math.min(nextIndex, items.length - 1));
    items[idx].classList.add('is-active');
    items[idx].scrollIntoView({ block: 'nearest' });
    return idx;
  }

  function currentActiveIndex(panel) {
    const active = panel.querySelector('.osl-search-item.is-active');
    return active ? parseInt(active.dataset.index, 10) : -1;
  }

  function navigateActive(panel) {
    const active = panel.querySelector('.osl-search-item.is-active') ||
                   panel.querySelector('.osl-search-item');
    if (active) window.location.assign(active.href);
  }

  function closePanel(panel) {
    panel.style.display = 'none';
    panel.innerHTML = '';
  }

  // --- Per-input wiring ----------------------------------------------------

  function wireInput(inputEl) {
    if (!inputEl || inputEl.__oslWired__) return;
    inputEl.__oslWired__ = true;

    injectBaseStylesOnce();
    const panel = mkPanel();
    let lastQuery = '';
    let lastActive = -1;

    function openPanel() {
      positionPanel(panel, inputEl);
      panel.style.display = 'block';
    }

    function updatePosition() {
      if (panel.style.display !== 'none') positionPanel(panel, inputEl);
    }

    // Debounce to keep it snappy
    let t = null;
    function onInput() {
      clearTimeout(t);
      t = setTimeout(async () => {
        const q = inputEl.value || '';
        lastQuery = q;
        if (q.trim().length < MIN_QUERY_LEN) {
          renderResults(panel, [], q);
          openPanel();
          lastActive = activateItem(panel, -1);
          return;
        }
        try {
          await ensureIndex();
          const items = search(q);
          renderResults(panel, items, q);
          openPanel();
          lastActive = activateItem(panel, 0);
        } catch (e) {
          console.warn('[OSL Search] failed:', e);
          renderResults(panel, [], q);
          openPanel();
        }
      }, 120);
    }

    function onKey(e) {
      if (panel.style.display === 'none' && (e.key === 'ArrowDown' || e.key === 'ArrowUp')) {
        openPanel();
      }
      switch (e.key) {
        case 'ArrowDown':
          e.preventDefault();
          lastActive = activateItem(panel, currentActiveIndex(panel) + 1);
          break;
        case 'ArrowUp':
          e.preventDefault();
          lastActive = activateItem(panel, currentActiveIndex(panel) - 1);
          break;
        case 'Enter':
          // If the panel is open and we have results, navigate the active item
          if (panel.style.display !== 'none') {
            const anyItem = panel.querySelector('.osl-search-item');
            if (anyItem) {
              e.preventDefault();
              navigateActive(panel);
              closePanel(panel);
            }
          }
          break;
        case 'Escape':
          closePanel(panel);
          break;
      }
    }

    function onFocus() {
      if ((inputEl.value || '').trim().length >= 0) {
        updatePosition();
        panel.style.display = 'block';
      }
    }

    function onBlur(e) {
      // delay to allow clicks
      setTimeout(() => {
        if (!panel.contains(document.activeElement)) closePanel(panel);
      }, 120);
    }

    // Clicks inside panel: follow links, also set active on hover
    panel.addEventListener('mousemove', (e) => {
      const a = e.target.closest('.osl-search-item');
      if (a && panel.contains(a)) {
        const idx = parseInt(a.dataset.index, 10);
        if (!Number.isNaN(idx)) {
          activateItem(panel, idx);
        }
      }
    });
    panel.addEventListener('click', (e) => {
      const a = e.target.closest('a.osl-search-item');
      if (!a) return;
      e.preventDefault();
      window.location.assign(a.href);
      closePanel(panel);
    });

    // Outside click closes panel
    document.addEventListener('click', (e) => {
      if (e.target === inputEl) return;
      if (panel.contains(e.target)) return;
      if (!panel.contains(e.target)) closePanel(panel);
    });

    // Reposition on scroll/resize
    window.addEventListener('scroll', updatePosition, { passive: true });
    window.addEventListener('resize', updatePosition);

    inputEl.setAttribute('autocomplete', 'off');
    inputEl.addEventListener('input', onInput);
    inputEl.addEventListener('keydown', onKey);
    inputEl.addEventListener('focus', onFocus);
    inputEl.addEventListener('blur', onBlur);
  }

  // Public initializer (used by theme.js)
  window.initSearch = function (inputEl) {
    if (!inputEl) return;
    wireInput(inputEl);
  };

  // Optional: auto-wire known fields if present
  document.addEventListener('DOMContentLoaded', () => {
    const desktop = document.getElementById('mkdocs-search');
    const mobile = document.getElementById('mkdocs-search-mobile');
    if (desktop) wireInput(desktop);
    if (mobile) wireInput(mobile);
  });

})();
