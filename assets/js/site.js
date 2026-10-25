(function () {
  var hd = document.querySelector('.hd.over');
  function onScroll() { if (hd) hd.classList.toggle('solid', window.scrollY > 40); }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  var els = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }

  // hero background clip: respect reduced-motion preferences
  var hv = document.querySelector('.hbg');
  if (hv && window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) { hv.pause(); hv.removeAttribute('autoplay'); }

  // equipment filters ("video" shows only machines with footage)
  var btns = document.querySelectorAll('.filters button');
  function filter(f) {
    btns.forEach(function (x) { x.classList.toggle('on', x.getAttribute('data-f') === f); });
    document.querySelectorAll('.eq').forEach(function (c) {
      var show = f === '*' || (f === 'video' ? c.classList.contains('hasv') : c.getAttribute('data-c') === f);
      c.classList.toggle('hide', !show);
    });
  }
  btns.forEach(function (b) { b.addEventListener('click', function () { filter(b.getAttribute('data-f')); }); });
  if (btns.length && location.hash === '#video') filter('video');

  // shared lightbox for video clips and certificate / photo enlargements
  var lb = document.getElementById('lb');
  function open(media, title, portrait) {
    if (!lb || !lb.showModal) return false;
    var box = lb.querySelector('.lbm');
    box.innerHTML = '';
    box.appendChild(media);
    lb.querySelector('.lbt b').textContent = title || '';
    lb.classList.toggle('p', !!portrait);
    lb.showModal();
    return true;
  }
  document.addEventListener('click', function (e) {
    var v = e.target.closest('.vc');
    if (v) {
      e.preventDefault();
      var el = document.createElement('video');
      el.src = v.getAttribute('data-src');
      el.controls = true; el.autoplay = true; el.muted = true; el.playsInline = true; el.loop = true;
      el.poster = (v.querySelector('img') || {}).src || '';
      if (!open(el, v.getAttribute('data-title'), v.getAttribute('data-o') === 'p')) window.open(el.src, '_blank');
      return;
    }
    var a = e.target.closest('[data-img]');
    if (a) {
      e.preventDefault();
      var im = document.createElement('img');
      im.src = a.getAttribute('data-img'); im.alt = a.getAttribute('data-title') || '';
      if (!open(im, im.alt, false)) window.open(im.src, '_blank');
    }
  });
  if (lb) {
    lb.querySelector('.lbx').addEventListener('click', function () { lb.close(); });
    lb.addEventListener('click', function (e) { if (e.target === lb) lb.close(); });
    lb.addEventListener('close', function () { lb.querySelector('.lbm').innerHTML = ''; });
  }

  document.querySelectorAll('#nav a').forEach(function (a) {
    a.addEventListener('click', function () { document.body.classList.remove('navopen'); });
  });
})();
