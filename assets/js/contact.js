(() => {
  'use strict';
  const button = document.getElementById('reveal-email');
  const details = document.getElementById('email-details');
  const link = document.getElementById('email-link');
  if (!button || !details || !link) return;
  button.hidden = false;
  button.addEventListener('click', () => {
    // Basic harvesting deterrence, not a secret or an access-control mechanism.
    // Keep the complete address out of the initial HTML and metadata.
    const address = String.fromCharCode(
      97, 109, 105, 110, 101, 97, 64, 115, 101, 97, 115, 46,
      117, 112, 101, 110, 110, 46, 101, 100, 117
    );
    link.textContent = address;
    link.href = 'mailto:' + address;
    details.hidden = false;
    button.setAttribute('aria-expanded', 'true');
    button.textContent = 'Email revealed';
    link.focus();
  }, { once: true });
})();
