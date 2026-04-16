
const menuToggle = document.querySelector('[data-menu-toggle]');
const mobileNav = document.querySelector('[data-mobile-nav]');
if (menuToggle && mobileNav) {
  menuToggle.addEventListener('click', () => {
    const open = mobileNav.classList.toggle('open');
    menuToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
}

function buildWhatsAppMessage(form) {
  const data = new FormData(form);
  const rows = {
    nombre: data.get('nombre') || '',
    comuna: data.get('comuna') || '',
    direccion: data.get('direccion') || '',
    rol: data.get('rol') || '',
    objetivo: data.get('objetivo') || '',
    detalles: data.get('detalles') || '',
    telefono: data.get('telefono') || ''
  };
  const message = [
    'Hola, quiero evaluar un terreno.',
    rows.nombre ? `Nombre: ${rows.nombre}` : '',
    rows.comuna ? `Comuna: ${rows.comuna}` : '',
    rows.direccion ? `Dirección: ${rows.direccion}` : '',
    rows.rol ? `Rol: ${rows.rol}` : '',
    rows.objetivo ? `Objetivo: ${rows.objetivo}` : '',
    rows.telefono ? `WhatsApp/Teléfono: ${rows.telefono}` : '',
    rows.detalles ? `Detalles: ${rows.detalles}` : ''
  ].filter(Boolean).join('
');
  return `https://wa.me/56976052356?text=${encodeURIComponent(message)}`;
}
const form = document.querySelector('[data-whatsapp-form]');
if (form) {
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    window.open(buildWhatsAppMessage(form), '_blank', 'noopener');
  });
}
