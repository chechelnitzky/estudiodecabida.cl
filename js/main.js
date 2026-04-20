document.addEventListener('DOMContentLoaded', () => {
  const WHATSAPP_NUMBER = '56976052356';
  const DEFAULT_MESSAGE = 'Hola, estaba revisando estudiodecabida.cl y quiero evaluar un terreno.';
  const buildWhatsAppUrl = (message) => `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;
  const toggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-mobile-menu]');
  const pageType = document.body?.dataset?.pageType || 'general';
  const analyticsQueue = window.dataLayer = window.dataLayer || [];
  const pushedScrollMilestones = new Set();

  const pushEvent = (eventName, params = {}) => {
    const payload = { event: eventName, page_type: pageType, page_path: window.location.pathname, ...params };
    analyticsQueue.push(payload);
    if (typeof window.gtag === 'function') {
      window.gtag('event', eventName, payload);
    }
  };

  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      menu.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', menu.classList.contains('is-open') ? 'true' : 'false');
      pushEvent('mobile_menu_toggle', { is_open: menu.classList.contains('is-open') });
    });
  }

  document.querySelectorAll('a[href*="wa.me/56976052356"]').forEach((link) => {
    if (!link.matches('[data-wa-form-submit]')) {
      const current = link.getAttribute('href') || '';
      if (!current.includes('?text=')) link.setAttribute('href', buildWhatsAppUrl(DEFAULT_MESSAGE));
    }
    link.addEventListener('click', () => {
      pushEvent('whatsapp_click', { label: link.dataset.trackLabel || link.textContent.trim() || 'whatsapp_link' });
    });
  });

  document.querySelectorAll('[data-track="cta_click"]').forEach((el) => {
    el.addEventListener('click', () => {
      pushEvent('cta_click', { label: el.dataset.trackLabel || el.textContent.trim() || 'cta' });
    });
  });

  const form = document.querySelector('[data-whatsapp-form]');
  const submit = document.querySelector('[data-wa-form-submit]');
  if (form && submit) {
    form.querySelectorAll('input, select, textarea').forEach((field) => {
      field.addEventListener('focus', () => pushEvent('form_start', { field: field.previousElementSibling?.textContent?.trim() || field.name || 'unknown' }), { once: true });
    });
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
      const message = lines.length ? `${DEFAULT_MESSAGE}

${lines.join('
')}` : DEFAULT_MESSAGE;
      pushEvent('form_submit', { fields_completed: lines.length, destination: 'whatsapp' });
      window.open(buildWhatsAppUrl(message), '_blank', 'noopener');
    });
  }

  pushEvent('page_view_custom');

  window.addEventListener('scroll', () => {
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    if (docHeight <= 0) return;
    const scrolled = Math.round((window.scrollY / docHeight) * 100);
    [25, 50, 75, 90].forEach((mark) => {
      if (scrolled >= mark && !pushedScrollMilestones.has(mark)) {
        pushedScrollMilestones.add(mark);
        pushEvent('scroll_depth', { percent: mark });
      }
    });
  }, { passive: true });
});
