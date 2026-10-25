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

  document.querySelectorAll('.filters button').forEach(function (b) {
    b.addEventListener('click', function () {
      var f = b.getAttribute('data-f');
      document.querySelectorAll('.filters button').forEach(function (x) { x.classList.toggle('on', x === b); });
      document.querySelectorAll('.eq').forEach(function (c) { c.classList.toggle('hide', f !== '*' && c.getAttribute('data-c') !== f); });
    });
  });

  document.querySelectorAll('#nav a').forEach(function (a) {
    a.addEventListener('click', function () { document.body.classList.remove('navopen'); });
  });
})();
