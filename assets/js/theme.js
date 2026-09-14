(function () {
  'use strict';
  const root = document.documentElement;
  const key = 'aa-color-theme';
  const system = window.matchMedia('(prefers-color-scheme: dark)');
  const valid = value => ['system', 'light', 'dark'].includes(value);
  let preference = 'system';
  try {
    const saved = window.localStorage.getItem(key);
    if (valid(saved)) preference = saved;
  } catch (_) { /* System appearance remains available without storage. */ }

  function apply() {
    const theme = preference === 'system' ? (system.matches ? 'dark' : 'light') : preference;
    root.setAttribute('data-theme', theme);
    root.setAttribute('data-theme-preference', preference);
    root.querySelectorAll('meta[name="theme-color"]').forEach(meta => {
      meta.setAttribute('content', theme === 'dark' ? '#16212b' : '#faf9f6');
    });
  }

  function bindControl() {
    const select = root.querySelector('#theme-select');
    if (!select) return;
    select.value = preference;
    select.closest('.theme-control').hidden = false;
    select.addEventListener('change', function () {
      preference = valid(select.value) ? select.value : 'system';
      try { window.localStorage.setItem(key, preference); } catch (_) { /* Apply for this page. */ }
      apply();
    });
  }

  apply();
  const onSystemChange = () => { if (preference === 'system') apply(); };
  if (system.addEventListener) system.addEventListener('change', onSystemChange);
  else system.addListener(onSystemChange);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', bindControl, { once: true });
  else bindControl();
}());
