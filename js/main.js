
document.addEventListener('DOMContentLoaded', () => {
  const WHATSAPP_NUMBER = '56976052356';
  const DEFAULT_MESSAGE = 'Hola, estaba revisando estudiodecabida.cl y quiero evaluar un terreno.';
  const buildWhatsAppUrl = (message) => `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;
  const toggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-mobile-menu]');
  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      menu.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', menu.classList.contains('is-open') ? 'true' : 'false');
    });
  }
  document.querySelectorAll('a[href*="wa.me/56976052356"]').forEach((link) => {
    if (!link.matches('[data-wa-form-submit]')) {
      const current = link.getAttribute('href') || '';
      if (!current.includes('?text=')) link.setAttribute('href', buildWhatsAppUrl(DEFAULT_MESSAGE));
    }
  });
  const form = document.querySelector('[data-whatsapp-form]');
  const submit = document.querySelector('[data-wa-form-submit]');
  if (form && submit) {
    submit.addEventListener('click', (event) => {
      event.preventDefault();
      const fields = [...form.querySelectorAll('input, select, textarea')];
      const lines = fields.map((field) => {
        const rawValue = (field.value || '').trim();
        if (!rawValue || rawValue === 'Seleccionar') return null;
        const fieldWrap = field.closest('.field');
        const label = fieldWrap ? fieldWrap.querySelector('label') : null;
        return label ? `${label.textContent.trim()}: ${rawValue}` : rawValue;
      }).filter(Boolean);
      const message = lines.length ? `${DEFAULT_MESSAGE}\n\n${lines.join('\n')}` : DEFAULT_MESSAGE;
      window.open(buildWhatsAppUrl(message), '_blank', 'noopener');
    });
  }
});
