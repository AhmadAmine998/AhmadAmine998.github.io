(() => {
  'use strict';
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  const videos = document.querySelectorAll('.motion-figure video');
  function apply() {
    videos.forEach(video => {
      video.muted = true;
      if (preference.matches) {
        video.autoplay = false;
        video.pause();
      } else {
        video.autoplay = true;
        const playback = video.play();
        if (playback && playback.catch) playback.catch(() => {});
      }
    });
  }
  apply();
  if (preference.addEventListener) preference.addEventListener('change', apply);
  else preference.addListener(apply);
})();
