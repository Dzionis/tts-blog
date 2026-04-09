(function () {
  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12 }
  );

  document.querySelectorAll(
    '.feature-card, .way-card, .review-card, .post-card'
  ).forEach(function (card, i) {
    card.classList.add('animate-on-scroll');
    card.style.transitionDelay = (i % 4) * 80 + 'ms';
    observer.observe(card);
  });
})();
