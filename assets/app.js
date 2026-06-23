// Theme toggle + collapsible sidebar sections
(function () {
  var root = document.documentElement;

  // Restore saved theme
  try {
    var saved = localStorage.getItem('xi-theme');
    if (saved) root.setAttribute('data-theme', saved);
  } catch (e) {}

  document.addEventListener('click', function (e) {
    // Theme toggle
    var toggle = e.target.closest('.navbar__theme');
    if (toggle) {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('xi-theme', next); } catch (e) {}
      return;
    }

    // Collapsible category
    var label = e.target.closest('.menu__category-label');
    if (label) {
      var cat = label.closest('.menu__category');
      var collapsed = cat.getAttribute('data-collapsed') === 'true';
      cat.setAttribute('data-collapsed', collapsed ? 'false' : 'true');
    }
  });

  // ---- Mobile sidebar drawer (hamburger toggle) ----
  (function () {
    var inner = document.querySelector('.navbar__inner');
    var brand = inner && inner.querySelector('.navbar__brand');
    var sidebar = document.querySelector('.sidebar-container');
    if (!inner || !brand || !sidebar) return;

    // Group hamburger + brand on the left
    var left = document.createElement('div');
    left.className = 'navbar__left';
    var burger = document.createElement('button');
    burger.type = 'button';
    burger.className = 'navbar__hamburger';
    burger.setAttribute('aria-label', 'Toggle navigation');
    burger.setAttribute('aria-expanded', 'false');
    burger.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>';
    inner.insertBefore(left, brand);
    left.appendChild(burger);
    left.appendChild(brand);

    var overlay = document.createElement('div');
    overlay.className = 'sidebar-overlay';
    document.body.appendChild(overlay);

    function setOpen(open) {
      document.body.classList.toggle('sidebar-open', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    }
    burger.addEventListener('click', function () {
      setOpen(!document.body.classList.contains('sidebar-open'));
    });
    overlay.addEventListener('click', function () { setOpen(false); });
    // Close after navigating via a sidebar link
    sidebar.addEventListener('click', function (e) {
      if (e.target.closest('.menu__link')) setOpen(false);
    });
    // Reset when leaving mobile width
    window.addEventListener('resize', function () {
      if (window.innerWidth > 860) setOpen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') setOpen(false);
    });
  })();

  // Search placeholder (no backend) — focus a hint
  var search = document.querySelector('.navbar__search');
  if (search) {
    search.addEventListener('click', function () {
      // Hook for future search modal; harmless no-op for now.
    });
  }

  var copyIcon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg>';

  // Reusable copy button. getText() is called at click time.
  function makeCopyButton(getText) {
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'code-copy';
    btn.setAttribute('aria-label', 'Copy');
    btn.innerHTML = copyIcon + '<span>Copy</span>';
    btn.addEventListener('click', function () {
      var raw = getText();
      var done = function () {
        btn.classList.add('is-copied');
        btn.querySelector('span').textContent = 'Copied';
        setTimeout(function () {
          btn.classList.remove('is-copied');
          btn.querySelector('span').textContent = 'Copy';
        }, 1800);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(raw).then(done).catch(function () {});
      } else {
        var ta = document.createElement('textarea');
        ta.value = raw; document.body.appendChild(ta); ta.select();
        try { document.execCommand('copy'); done(); } catch (e) {}
        document.body.removeChild(ta);
      }
    });
    return btn;
  }

  // Next element sibling, skipping whitespace-only text nodes.
  function nextEl(node) {
    node = node && node.nextSibling;
    while (node && node.nodeType === 3 && !node.textContent.trim()) node = node.nextSibling;
    return node && node.nodeType === 1 ? node : null;
  }

  var article = document.querySelector('.doc-content.markdown') || document;

  // ---- 1) HTTP method endpoint bars ----
  var METHODS = { GET: 'get', POST: 'post', PUT: 'put', PATCH: 'patch', DELETE: 'delete' };
  function makeEndpointRow(method, rest) {
    var row = document.createElement('div');
    row.className = 'endpoint';
    var m = document.createElement('span');
    m.className = 'http-method http-' + METHODS[method];
    m.textContent = method;
    row.appendChild(m);
    var path = document.createElement('code');
    path.className = 'endpoint-path';
    var hashIdx = rest.indexOf('#');
    var pathText = hashIdx > -1 ? rest.slice(0, hashIdx).trim() : rest.trim();
    path.textContent = pathText;
    row.appendChild(path);
    if (hashIdx > -1) {
      var c = document.createElement('span');
      c.className = 'endpoint-comment';
      c.textContent = rest.slice(hashIdx).trim();
      row.appendChild(c);
    }
    row.appendChild(makeCopyButton(function () { return method + ' ' + pathText; }));
    return row;
  }

  Array.prototype.forEach.call(article.querySelectorAll('.highlight'), function (block) {
    var codeEl = block.querySelector('code') || block.querySelector('pre');
    if (!codeEl) return;
    var lines = codeEl.innerText.replace(/\s+$/, '').split('\n').filter(function (l) { return l.trim() !== ''; });
    if (!lines.length) return;
    var ok = lines.every(function (l) { return /^(GET|POST|PUT|PATCH|DELETE)\s+\/\S.*$/.test(l.trim()); });
    if (!ok) return;
    var list = document.createElement('div');
    list.className = 'endpoint-list';
    lines.forEach(function (l) {
      var m = l.trim().match(/^(GET|POST|PUT|PATCH|DELETE)\s+(.*)$/);
      list.appendChild(makeEndpointRow(m[1], m[2]));
    });
    block.parentNode.replaceChild(list, block);
  });

  // ---- 2) Labeled code panels + request/response tabs ----
  // A "label" is a <p> whose sole content is a <strong> ending in ":",
  // immediately followed by a code block.
  function labelOf(p) {
    if (!p || p.tagName !== 'P' || p.children.length !== 1) return null;
    if (!p.querySelector('strong')) return null;
    var txt = p.textContent.trim();
    if (txt.length > 40 || !/:$/.test(txt)) return null;
    return txt.replace(/:$/, '').trim();
  }
  function isHighlight(el) { return el && el.classList && el.classList.contains('highlight'); }

  var used = [];
  Array.prototype.forEach.call(article.querySelectorAll('p'), function (p) {
    if (used.indexOf(p) > -1) return;
    var run = [];
    var cur = p;
    while (true) {
      var lbl = labelOf(cur);
      if (lbl === null) break;
      var code = nextEl(cur);
      if (!isHighlight(code)) break;
      run.push({ label: lbl, labelP: cur, code: code });
      used.push(cur);
      var after = nextEl(code);
      if (after && after.tagName === 'P' && used.indexOf(after) === -1) cur = after; else break;
    }
    if (run.length === 1) {
      var u = run[0];
      var panel = document.createElement('div');
      panel.className = 'code-panel';
      var head = document.createElement('div');
      head.className = 'code-panel__header';
      head.textContent = u.label;
      u.code.parentNode.insertBefore(panel, u.code);
      panel.appendChild(head);
      panel.appendChild(u.code);
      u.labelP.parentNode.removeChild(u.labelP);
    } else if (run.length > 1) {
      var tabs = document.createElement('div');
      tabs.className = 'code-tabs';
      var nav = document.createElement('div');
      nav.className = 'code-tabs__nav';
      tabs.appendChild(nav);
      run[0].code.parentNode.insertBefore(tabs, run[0].code);
      run.forEach(function (u2, i) {
        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'code-tabs__tab' + (i === 0 ? ' is-active' : '');
        btn.textContent = u2.label;
        nav.appendChild(btn);
        var pnl = document.createElement('div');
        pnl.className = 'code-tabs__panel' + (i === 0 ? ' is-active' : '');
        pnl.appendChild(u2.code);
        tabs.appendChild(pnl);
        u2.labelP.parentNode.removeChild(u2.labelP);
        btn.addEventListener('click', function () {
          Array.prototype.forEach.call(nav.children, function (b) { b.classList.remove('is-active'); });
          Array.prototype.forEach.call(tabs.querySelectorAll('.code-tabs__panel'), function (x) { x.classList.remove('is-active'); });
          btn.classList.add('is-active');
          pnl.classList.add('is-active');
        });
      });
    }
  });

  // ---- 3) Parameter tables (type pills + required badges) ----
  Array.prototype.forEach.call(article.querySelectorAll('table'), function (table) {
    var ths = table.querySelectorAll('thead th');
    if (!ths.length) return;
    var headers = Array.prototype.map.call(ths, function (th) { return th.textContent.trim().toLowerCase(); });
    var typeIdx = headers.indexOf('type');
    var nameIdx = -1, reqIdx = headers.indexOf('required');
    headers.forEach(function (h, i) { if (nameIdx === -1 && (h === 'parameter' || h === 'field' || h === 'name')) nameIdx = i; });
    if (typeIdx === -1 || nameIdx === -1) return; // only true param tables
    table.classList.add('param-table');
    Array.prototype.forEach.call(table.querySelectorAll('tbody tr'), function (tr) {
      var cells = tr.children;
      if (cells[typeIdx]) {
        var t = cells[typeIdx].textContent.trim();
        if (t && t !== '—') cells[typeIdx].innerHTML = '<span class="type-pill">' + t + '</span>';
      }
      if (reqIdx > -1 && cells[reqIdx]) {
        var r = cells[reqIdx].textContent.trim().toLowerCase();
        if (r === 'yes') cells[reqIdx].innerHTML = '<span class="req-badge req-yes">Required</span>';
        else if (r === 'no') cells[reqIdx].innerHTML = '<span class="req-badge req-no">Optional</span>';
      }
    });
  });

  // ---- 4) Code blocks: language badge + copy button ----
  function detectLang(text) {
    var t = text.trim();
    if (/^\s*[\{\[]/.test(t) && /[:,]/.test(t)) return 'json';
    if (/^(\$ |sudo |curl |pip |docker |export |cd |ls |git |aws |npm |yarn |brew )/m.test(t)) return 'bash';
    if (/\b(import |from .+ import|def |print\(|requests\.|openai\.)/.test(t)) return 'python';
    if (/^[A-Z_]+=.+/m.test(t) && !/[{};]/.test(t)) return 'env';
    if (/<\/?[a-z][\s\S]*>/i.test(t)) return 'html';
    return '';
  }

  Array.prototype.forEach.call(document.querySelectorAll('.highlight'), function (block) {
    if (block.querySelector('.code-toolbar')) return; // idempotent
    var codeEl = block.querySelector('code') || block.querySelector('pre');
    if (!codeEl) return;
    var raw = codeEl.innerText;

    var toolbar = document.createElement('div');
    toolbar.className = 'code-toolbar';

    var lang = detectLang(raw);
    if (lang) {
      var badge = document.createElement('span');
      badge.className = 'code-lang';
      badge.textContent = lang;
      toolbar.appendChild(badge);
    }

    toolbar.appendChild(makeCopyButton(function () { return raw; }));
    block.appendChild(toolbar);
  });

  // ---- 5) Arrow-link lists -> card grid ----
  if (article && article !== document) {
    Array.prototype.forEach.call(article.querySelectorAll('ul'), function (ul) {
      var items = Array.prototype.filter.call(ul.children, function (li) { return li.tagName === 'LI'; });
      if (!items.length) return;
      var allArrow = items.every(function (li) {
        var a = li.querySelector('a');
        return li.children.length === 1 && a && /→\s*$/.test(a.textContent);
      });
      if (!allArrow) return;
      var grid = document.createElement('div');
      grid.className = 'card-grid';
      items.forEach(function (li) {
        var a = li.querySelector('a');
        var card = document.createElement('a');
        card.className = 'card card--compact';
        card.href = a.getAttribute('href');
        var title = a.textContent.replace(/→\s*$/, '').trim();
        card.innerHTML = '<span class="card__title">' + title + ' <span class="card__arrow">→</span></span>';
        grid.appendChild(card);
      });
      ul.parentNode.replaceChild(grid, ul);
    });
  }

  // ---- 6) Admonition icons ----
  var admIcons = {
    tip: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-4 10c.7.7 1 1.3 1 2h6c0-.7.3-1.3 1-2a6 6 0 0 0-4-10Z"/></svg>',
    warning: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0Z"/><path d="M12 9v4M12 17h.01"/></svg>',
    danger: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M15 9l-6 6M9 9l6 6"/></svg>',
    info: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>'
  };
  Array.prototype.forEach.call(document.querySelectorAll('.admonition'), function (ad) {
    var head = ad.querySelector('.admonition-heading');
    if (!head || head.querySelector('.admonition-icon')) return;
    var type = 'info';
    if (ad.classList.contains('admonition-tip')) type = 'tip';
    else if (ad.classList.contains('admonition-warning') || ad.classList.contains('admonition-caution')) type = 'warning';
    else if (ad.classList.contains('admonition-danger')) type = 'danger';
    var ic = document.createElement('span');
    ic.className = 'admonition-icon';
    ic.innerHTML = admIcons[type];
    head.insertBefore(ic, head.firstChild);
  });

  // ---- 7) Breadcrumbs + prev/next page nav (derived from sidebar) ----
  var activeLink = document.querySelector('.menu__link--active');
  var navLinks = Array.prototype.slice.call(document.querySelectorAll('.sidebar .menu__link'));

  if (activeLink && article && article !== document) {
    var brand = document.querySelector('.navbar__brand');
    var bc = document.createElement('nav');
    bc.className = 'breadcrumbs';
    bc.setAttribute('aria-label', 'Breadcrumb');
    var html = '';
    if (brand) html += '<a href="' + brand.getAttribute('href') + '">Docs</a><span class="breadcrumbs__sep">/</span>';
    var cat = activeLink.closest('.menu__category');
    if (cat) {
      var catLabel = cat.querySelector('.menu__category-label');
      if (catLabel && catLabel.firstChild) html += '<span>' + catLabel.firstChild.textContent.trim() + '</span><span class="breadcrumbs__sep">/</span>';
    }
    html += '<span class="breadcrumbs__current">' + activeLink.textContent.trim() + '</span>';
    bc.innerHTML = html;
    article.insertBefore(bc, article.firstChild);
  }

  if (activeLink && article && article !== document) {
    var idx = navLinks.indexOf(activeLink);
    if (idx > -1) {
      function makeNavCard(dir, link) {
        var a = document.createElement('a');
        a.className = 'page-nav__card page-nav__card--' + dir.toLowerCase();
        a.href = link.getAttribute('href');
        a.innerHTML = '<span class="page-nav__dir">' + dir + '</span>' +
          '<span class="page-nav__title">' + link.textContent.trim() + '</span>';
        return a;
      }
      var pageNav = document.createElement('nav');
      pageNav.className = 'page-nav';
      pageNav.setAttribute('aria-label', 'Pagination');
      if (idx > 0) pageNav.appendChild(makeNavCard('Previous', navLinks[idx - 1]));
      if (idx < navLinks.length - 1) pageNav.appendChild(makeNavCard('Next', navLinks[idx + 1]));
      if (pageNav.children.length) article.appendChild(pageNav);
    }
  }

  // ---- 8) TOC scroll-spy ----
  var tocLinks = document.querySelectorAll('.toc__item a');
  if (tocLinks.length && 'IntersectionObserver' in window) {
    var tocMap = {};
    Array.prototype.forEach.call(tocLinks, function (a) {
      var id = (a.getAttribute('href') || '').replace(/^#/, '');
      var el = id && document.getElementById(id);
      if (el) tocMap[id] = a;
    });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting && tocMap[en.target.id]) {
          Array.prototype.forEach.call(tocLinks, function (a) { a.classList.remove('toc__link--active'); });
          tocMap[en.target.id].classList.add('toc__link--active');
        }
      });
    }, { rootMargin: '0px 0px -75% 0px', threshold: 0 });
    Object.keys(tocMap).forEach(function (id) { spy.observe(document.getElementById(id)); });
  }

  // ---- 9) ⌘K search modal (client-side, indexes nav + page headings) ----
  (function () {
    var trigger = document.querySelector('.navbar__search');
    if (!trigger) return;

    var index = [];
    navLinks.forEach(function (a) {
      index.push({ title: a.textContent.trim(), href: a.getAttribute('href'), tag: 'Page' });
    });
    if (article && article !== document) {
      Array.prototype.forEach.call(article.querySelectorAll('h2[id], h3[id]'), function (h) {
        index.push({ title: h.textContent.trim(), href: '#' + h.id, tag: 'On this page' });
      });
    }

    var overlay = document.createElement('div');
    overlay.className = 'search-modal';
    overlay.innerHTML =
      '<div class="search-modal__box" role="dialog" aria-modal="true" aria-label="Search">' +
        '<div class="search-modal__field">' +
          '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m21 21-4-4"/></svg>' +
          '<input class="search-modal__input" type="text" placeholder="Search documentation..." aria-label="Search documentation" />' +
          '<kbd class="search-modal__esc">esc</kbd>' +
        '</div>' +
        '<ul class="search-modal__results"></ul>' +
      '</div>';
    document.body.appendChild(overlay);

    var input = overlay.querySelector('.search-modal__input');
    var results = overlay.querySelector('.search-modal__results');
    var isOpen = false, active = -1, current = [];

    function render(q) {
      q = (q || '').trim().toLowerCase();
      current = q
        ? index.filter(function (it) { return it.title.toLowerCase().indexOf(q) > -1; }).slice(0, 14)
        : index.slice(0, 8);
      active = current.length ? 0 : -1;
      results.innerHTML = current.length
        ? current.map(function (it, i) {
            return '<li class="search-modal__item' + (i === 0 ? ' is-active' : '') + '" data-href="' + it.href + '">' +
              '<span class="search-modal__title">' + it.title + '</span>' +
              '<span class="search-modal__tag">' + it.tag + '</span></li>';
          }).join('')
        : '<li class="search-modal__empty">No results</li>';
    }
    function highlight() {
      var items = results.querySelectorAll('.search-modal__item');
      Array.prototype.forEach.call(items, function (el, i) { el.classList.toggle('is-active', i === active); });
      if (items[active]) items[active].scrollIntoView({ block: 'nearest' });
    }
    function go(i) { if (i >= 0 && i < current.length) window.location.href = current[i].href; }
    function open() { isOpen = true; overlay.classList.add('is-open'); input.value = ''; render(''); setTimeout(function () { input.focus(); }, 30); }
    function close() { isOpen = false; overlay.classList.remove('is-open'); }

    trigger.addEventListener('click', open);
    input.addEventListener('input', function () { render(input.value); });
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) return close();
      var li = e.target.closest('.search-modal__item');
      if (li) window.location.href = li.getAttribute('data-href');
    });
    document.addEventListener('keydown', function (e) {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); isOpen ? close() : open(); return; }
      if (!isOpen) return;
      if (e.key === 'Escape') { close(); }
      else if (e.key === 'ArrowDown') { e.preventDefault(); active = Math.min(active + 1, current.length - 1); highlight(); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); active = Math.max(active - 1, 0); highlight(); }
      else if (e.key === 'Enter') { e.preventDefault(); go(active); }
    });
  })();
})();
