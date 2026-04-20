document.addEventListener('DOMContentLoaded', () => {
  const WHATSAPP_NUMBER = '56976052356';
  const PAGE_TYPE = document.body?.dataset?.pageType || 'general';
  const dataLayer = (window.dataLayer = window.dataLayer || []);
  const pushedScrollMilestones = new Set();

  const PAGE_MESSAGES = {
    general: 'Hola, estaba revisando estudiodecabida.cl y quiero evaluar un terreno.',
    home: 'Hola, estaba revisando estudiodecabida.cl y quiero evaluar un terreno.',
    service: 'Hola, estaba revisando estudiodecabida.cl y quiero evaluar un terreno y entender si conviene avanzar o no.',
    prices: 'Hola, estaba revisando estudiodecabida.cl y quiero orientación sobre qué estudio me conviene para evaluar un terreno.',
    commercial: 'Hola, estaba revisando estudiodecabida.cl y quiero evaluar un terreno con un estudio comercial para decidir, visualizar y mostrar su potencial.',
    technical: 'Hola, estaba revisando estudiodecabida.cl y quiero evaluar un terreno con un estudio técnico para decidir con base normativa.',
    ads_general: 'Hola, estaba revisando estudiodecabida.cl y quiero evaluar un terreno antes de comprar, ofertar o invertir.',
    ads_prebuy: 'Hola, estaba revisando estudiodecabida.cl y quiero evaluar un terreno antes de comprar para saber si conviene avanzar o no.',
    ads_premium: 'Hola, estaba revisando estudiodecabida.cl y quiero evaluar un terreno con un estudio comercial para decidir, visualizar y mostrar su potencial.',
    contact: 'Hola, estaba revisando estudiodecabida.cl y quiero enviar un terreno para evaluación.',
    local: 'Hola, estaba revisando estudiodecabida.cl y quiero evaluar un terreno en esta comuna.',
  };

  const normalize = (text) =>
    (text || '')
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .replace(/\s+/g, ' ')
      .trim();

  const buildWhatsAppUrl = (message) => `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;
  const pageDefaultMessage = PAGE_MESSAGES[PAGE_TYPE] || PAGE_MESSAGES.general;

  const pushEvent = (eventName, params = {}) => {
    const payload = {
      event: eventName,
      page_type: PAGE_TYPE,
      page_path: window.location.pathname,
      ...params,
    };
    dataLayer.push(payload);
    if (typeof window.gtag === 'function') {
      window.gtag('event', eventName, payload);
    }
  };

  const inferMessageFromLink = (link) => {
    const explicit = link.dataset.waMessage || link.getAttribute('data-wa-message');
    if (explicit) return explicit;

    const text = normalize(link.textContent);
    const href = normalize(link.getAttribute('href'));
    const cardText = normalize(link.closest('.priceCard, .card, .ctaBand, .homeHero, .caseCard, .faqItem')?.textContent || '');
    const pageText = normalize(document.querySelector('h1')?.textContent || '');
    const combined = `${text} ${href} ${cardText} ${pageText}`;

    if (combined.includes('comercial') || combined.includes('visualizar y mostrar') || combined.includes('cabida comercial')) {
      return 'Hola, estaba revisando estudiodecabida.cl y quiero evaluar un terreno con un estudio comercial para decidir, visualizar y mostrar su potencial.';
    }

    if (combined.includes('tecnica') || combined.includes('técnica') || combined.includes('estudio tecnico')) {
      return 'Hola, estaba revisando estudiodecabida.cl y quiero evaluar un terreno con un estudio técnico para decidir con base normativa.';
    }

    if (combined.includes('antes de comprar')) {
      return 'Hola, estaba revisando estudiodecabida.cl y quiero evaluar un terreno antes de comprar para saber si conviene avanzar o no.';
    }

    if (combined.includes('las condes') || combined.includes('providencia') || combined.includes('vitacura') || combined.includes('lo barnechea')) {
      const commune = ['Las Condes', 'Providencia', 'Vitacura', 'Lo Barnechea'].find((name) => combined.includes(normalize(name)));
      return commune
        ? `Hola, estaba revisando estudiodecabida.cl y quiero evaluar un terreno en ${commune}.`
        : PAGE_MESSAGES.local;
    }

    if (combined.includes('precio') || combined.includes('alcance') || combined.includes('orientacion')) {
      return PAGE_MESSAGES.prices;
    }

    return pageDefaultMessage;
  };

  const toggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-mobile-menu]');
  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      const isOpen = menu.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      pushEvent('mobile_menu_toggle', { is_open: isOpen });
    });
  }

  document.querySelectorAll('a[href*="wa.me/56976052356"]').forEach((link) => {
    if (!link.matches('[data-wa-form-submit]')) {
      link.setAttribute('href', buildWhatsAppUrl(inferMessageFromLink(link)));
    }
    link.addEventListener('click', () => {
      pushEvent('whatsapp_click', {
        label: link.dataset.trackLabel || link.textContent.trim() || 'whatsapp_link',
        wa_message: inferMessageFromLink(link),
      });
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
      field.addEventListener(
        'focus',
        () => pushEvent('form_start', { field: field.previousElementSibling?.textContent?.trim() || field.name || 'unknown' }),
        { once: true }
      );
    });

    submit.addEventListener('click', (event) => {
      event.preventDefault();
      const fields = [...form.querySelectorAll('input, select, textarea')];
      const lines = fields
        .map((field) => {
          const rawValue = (field.value || '').trim();
          if (!rawValue || rawValue === 'Seleccionar') return null;
          const fieldWrap = field.closest('.field');
          const label = fieldWrap ? fieldWrap.querySelector('label') : null;
          return label ? `${label.textContent.trim()}: ${rawValue}` : rawValue;
        })
        .filter(Boolean);

      const baseMessage = submit.dataset.waMessage || pageDefaultMessage;
      const message = lines.length ? `${baseMessage}\n\n${lines.join('\n')}` : baseMessage;
      pushEvent('form_submit', { fields_completed: lines.length, destination: 'whatsapp' });
      window.open(buildWhatsAppUrl(message), '_blank', 'noopener');
    });
  }

  pushEvent('page_view_custom');

  window.addEventListener(
    'scroll',
    () => {
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      if (docHeight <= 0) return;
      const scrolled = Math.round((window.scrollY / docHeight) * 100);
      [25, 50, 75, 90].forEach((mark) => {
        if (scrolled >= mark && !pushedScrollMilestones.has(mark)) {
          pushedScrollMilestones.add(mark);
          pushEvent('scroll_depth', { percent: mark });
        }
      });
    },
    { passive: true }
  );
});
