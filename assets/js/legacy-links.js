(() => {
  'use strict';
  // Preserve links shared before the homepage was split into separate pages.
  const pages = {
    research: 'research/', publications: 'research/#publications',
    teaching: 'teaching/', community: 'community/', background: 'journey/',
    fail: 'research/#fail', 'ad-mpcc': 'research/#ad-mpcc',
    'stl-svpio': 'research/#stl-svpio', nonplanar: 'research/#nonplanar',
    'sit-lmpc': 'research/#sit-lmpc', 'ensemble-gp': 'research/#ensemble-gp',
    vahr: 'research/#vahr', 'friction-estimation': 'research/#friction-estimation',
    poseinn: 'research/#poseinn'
  };
  function redirectOldLink() {
    const target = pages[window.location.hash.slice(1)];
    if (target) window.location.replace(new URL(target, window.location.href));
  }
  redirectOldLink();
  window.addEventListener('hashchange', redirectOldLink);
})();
