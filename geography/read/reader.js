(function () {
  var KEY = 'atlas-lang';
  var body = document.body;
  var article = document.getElementById('article');
  var toc = document.getElementById('toc');
  var btn = document.getElementById('langBtn');
  var blocks = Array.prototype.slice.call(article.children);

  function getLang() {
    try { return localStorage.getItem(KEY) === 'en' ? 'en' : 'ru'; } catch (e) { return 'ru'; }
  }
  function level(el) { var m = /^H([1-6])$/.exec(el.tagName); return m ? +m[1] : 0; }
  function shown(el, lang) {
    var other = lang === 'ru' ? 'en' : 'ru';
    return !el.classList.contains(other);
  }

  // Hide headings that have nothing under them in the current language.
  function hideEmpty(lang) {
    blocks.forEach(function (b) { b.classList.remove('empty'); });
    for (var i = blocks.length - 1; i >= 0; i--) {
      var h = blocks[i], lv = level(h);
      if (!lv || lv === 1 || !shown(h, lang)) continue;
      var has = false;
      for (var j = i + 1; j < blocks.length; j++) {
        var b = blocks[j], bl = level(b);
        if (bl && bl <= lv) { if (shown(b, lang) && !b.classList.contains('empty')) break; continue; }
        if (!shown(b, lang) || b.classList.contains('empty')) continue;
        has = true; break;
      }
      if (!has) h.classList.add('empty');
    }
  }

  function buildToc(lang) {
    toc.innerHTML = '';
    var t = document.createElement('b');
    t.textContent = lang === 'ru' ? 'Содержание главы' : 'In this chapter';
    toc.appendChild(t);
    blocks.forEach(function (b) {
      if (b.tagName !== 'H2' || !shown(b, lang) || b.classList.contains('empty')) return;
      var span = b.querySelector('.' + lang) || b;
      var a = document.createElement('a');
      a.href = '#' + b.id;
      a.textContent = span.textContent;
      a.addEventListener('click', function () { body.classList.remove('tocOpen'); });
      toc.appendChild(a);
    });
  }

  function setAlts(lang) {
    article.querySelectorAll('img').forEach(function (img) {
      if (!img.dataset.altRu) img.dataset.altRu = img.alt;
      if (img.dataset.altEn) img.alt = lang === 'en' ? img.dataset.altEn : img.dataset.altRu;
    });
  }

  // Collapsible sections: the page opens as a short list of headings.
  var openSet = {0: true}, secHeads = [];
  function buildFold(lang) {
    secHeads = [];
    var cur = -1;
    blocks.forEach(function (b) {
      b.classList.remove('foldable', 'open', 'folded'); delete b.dataset.sec;
    });
    blocks.forEach(function (b) {
      if (b.tagName === 'H2' && shown(b, lang) && !b.classList.contains('empty')) {
        cur = secHeads.length; secHeads.push(b); b.classList.add('foldable'); b.dataset.n = cur;
      } else if (cur >= 0 && b.tagName !== 'H1') { b.dataset.sec = cur; }
    });
    paintFold();
  }
  function paintFold() {
    secHeads.forEach(function (h, i) { h.classList.toggle('open', !!openSet[i]); });
    blocks.forEach(function (b) {
      if (b.dataset.sec !== undefined) b.classList.toggle('folded', !openSet[+b.dataset.sec]);
    });
    var all = secHeads.length > 0 && secHeads.every(function (h, i) { return openSet[i]; });
    document.querySelectorAll('.foldAll').forEach(function (bt) {
      var en = bt.parentNode.classList.contains('en');
      bt.textContent = all ? (en ? 'Collapse all sections' : 'Свернуть все разделы') : (en ? 'Expand all sections' : 'Развернуть все разделы');
    });
  }
  function secOf(el) {
    var b = el; while (b && b.parentNode !== article) b = b.parentNode;
    if (!b) return -1;
    if (b.classList.contains('foldable')) return +b.dataset.n;
    return b.dataset.sec !== undefined ? +b.dataset.sec : -1;
  }
  function reveal(id) {
    var el = id && document.getElementById(id); if (!el) return;
    var i = secOf(el);
    if (i >= 0 && !openSet[i]) { openSet[i] = true; paintFold(); }
    setTimeout(function () { el.scrollIntoView(); }, 30);
  }
  article.addEventListener('click', function (e) {
    var h = e.target.closest('h2.foldable');
    if (h && !e.target.closest('a')) { openSet[+h.dataset.n] = !openSet[+h.dataset.n]; paintFold(); }
    var fa = e.target.closest('.foldAll');
    if (fa) {
      var all = secHeads.every(function (x, i) { return openSet[i]; });
      secHeads.forEach(function (x, i) { openSet[i] = !all; }); paintFold();
    }
  });
  window.addEventListener('hashchange', function () { reveal(location.hash.slice(1)); });
  window.addEventListener('beforeprint', function () { secHeads.forEach(function (x, i) { openSet[i] = true; }); paintFold(); });

  function apply(lang) {
    body.dataset.lang = lang;
    document.documentElement.lang = lang;
    btn.textContent = lang === 'ru' ? 'EN' : 'RU';
    var t = window.CHAPTER_TITLES || {};
    document.title = (t[lang] || t.ru || '') + (lang === 'ru' ? ' — Атлас географии' : ' — Atlas of Geography');
    hideEmpty(lang);
    buildFold(lang);
    buildToc(lang);
    setAlts(lang);
    spy();
  }

  btn.addEventListener('click', function () {
    var lang = body.dataset.lang === 'ru' ? 'en' : 'ru';
    try { localStorage.setItem(KEY, lang); } catch (e) {}
    apply(lang);
  });

  // Mobile: contents button
  var tb = document.createElement('button');
  tb.className = 'tocBtn'; tb.type = 'button';
  tb.innerHTML = '<span class="ru">Содержание</span><span class="en">Contents</span>';
  tb.addEventListener('click', function () { body.classList.toggle('tocOpen'); });
  btn.parentNode.insertBefore(tb, btn);

  // Highlight current section in the contents
  function spy() {
    var links = toc.querySelectorAll('a'), cur = null;
    for (var i = 0; i < links.length; i++) {
      var h = document.getElementById(links[i].hash.slice(1));
      if (h && h.getBoundingClientRect().top < 120) cur = links[i];
    }
    links.forEach(function (a) { a.classList.toggle('on', a === cur); });
  }
  window.addEventListener('scroll', spy, { passive: true });

  // Tap a figure to enlarge it
  article.addEventListener('click', function (e) {
    var img = e.target.closest('p.fig img');
    if (!img) return;
    var z = document.createElement('div');
    z.className = 'zoom';
    var c = img.cloneNode();
    c.removeAttribute('loading');
    z.appendChild(c);
    z.addEventListener('click', function () { z.remove(); });
    document.body.appendChild(z);
  });

  apply(getLang());
  if (location.hash) reveal(location.hash.slice(1));
})();
