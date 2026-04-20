document.addEventListener('DOMContentLoaded', () => {
  const WHATSAPP_NUMBER = '56976052356';
  const DEFAULT_MESSAGE = 'Hola, estaba revisando estudiodecabida.cl y quiero evaluar un terreno.';
  const buildWhatsAppUrl = (message) => `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;
  const track = (eventName, detail = {}) => {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ event: eventName, ...detail });
    try { console.debug('[track]', eventName, detail); } catch (e) {}
  };

  const toggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-mobile-menu]');
  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      menu.classList.toggle('is-open');
      const expanded = menu.classList.contains('is-open');
      toggle.setAttribute('aria-expanded', expanded ? 'true' : 'false');
      track('menu_toggle', { open: expanded });
    });
  }

  track('page_view_custom', {
    page_path: window.location.pathname,
    page_title: document.title
  });

  document.querySelectorAll('a[href*="wa.me/56976052356"]').forEach((link) => {
    if (!link.matches('[data-wa-form-submit]')) {
      const current = link.getAttribute('href') || '';
      if (!current.includes('?text=')) link.setAttribute('href', buildWhatsAppUrl(DEFAULT_MESSAGE));
    }
    link.addEventListener('click', () => {
      track('whatsapp_click', {
        page_path: window.location.pathname,
        location: link.dataset.trackLocation || 'unknown',
        link_text: (link.textContent || '').trim() || link.getAttribute('aria-label') || 'whatsapp'
      });
    });
  });

  document.querySelectorAll('a[href*="/contacto/"], a[data-track="form"]').forEach((link) => {
    link.addEventListener('click', () => {
      track('form_click', {
        page_path: window.location.pathname,
        location: link.dataset.trackLocation || 'unknown',
        link_text: (link.textContent || '').trim()
      });
    });
  });

  document.querySelectorAll('a[data-track="cta"]').forEach((link) => {
    link.addEventListener('click', () => {
      track('cta_click', {
        page_path: window.location.pathname,
        location: link.dataset.trackLocation || 'unknown',
        link_text: (link.textContent || '').trim()
      });
    });
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
      const message = lines.length ? `${DEFAULT_MESSAGE}

${lines.join('
')}` : DEFAULT_MESSAGE;
      track('form_submit', { page_path: window.location.pathname, form_type: 'whatsapp_form' });
      window.open(buildWhatsAppUrl(message), '_blank', 'noopener');
    });
  }

  let tracked50 = false;
  let tracked90 = false;
  const onScroll = () => {
    const doc = document.documentElement;
    const scrollable = doc.scrollHeight - window.innerHeight;
    if (scrollable <= 0) return;
    const pct = Math.round((window.scrollY / scrollable) * 100);
    if (!tracked50 && pct >= 50) {
      tracked50 = true;
      track('scroll_depth', { page_path: window.location.pathname, percent: 50 });
    }
    if (!tracked90 && pct >= 90) {
      tracked90 = true;
      track('scroll_depth', { page_path: window.location.pathname, percent: 90 });
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
});
