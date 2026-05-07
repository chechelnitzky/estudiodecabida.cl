from pathlib import Path
import shutil, json, html

ROOT = Path('/mnt/data/site')
IMG = '/assets/images'
BASE_OG = 'https://estudiodecabida.cl'
WHATSAPP = 'https://wa.me/56976052356'
DEFAULT_WA = 'Hola, estaba revisando estudiodecabida.cl y quiero evaluar un terreno.'

hero_src = ROOT / 'assets/images/hero-estudio-cabida-santiago.webp'
asset_names = [
    'hero-home.webp',
    'hero-estudio-de-cabida.webp',
    'hero-estudio-de-cabida-comercial.webp',
    'hero-estudio-de-cabida-tecnica.webp',
    'hero-evaluar-terreno.webp',
    'hero-antes-de-comprar-terreno.webp',
    'hero-cabida-comercial.webp',
]
for name in asset_names:
    dst = ROOT / 'assets/images' / name
    if not dst.exists():
        shutil.copy(hero_src, dst)

SEO_LINKS = [
    ('Qué revisar antes de comprar un terreno', '/antes-de-comprar-terreno/'),
    ('Cómo leer un CIP', '/como-leer-un-cip/'),
    ('Qué puedo construir en mi terreno', '/que-puedo-construir/'),
    ('Técnico vs comercial', '/estudio-tecnico-vs-comercial/'),
]

GUIDE_LINKS = [
    ('Qué incluye un estudio de cabida', '/que-incluye-un-estudio-de-cabida/'),
    ('Cómo se hace un estudio de cabida', '/como-se-hace-un-estudio-de-cabida/'),
    ('Ejemplo de estudio de cabida', '/ejemplo-de-estudio-de-cabida/'),
    ('Cómo leer un CIP', '/como-leer-un-cip/'),
]

COMMUNES = [
    ('Las Condes', '/comunas/las-condes/'),
    ('Providencia', '/comunas/providencia/'),
    ('Vitacura', '/comunas/vitacura/'),
    ('Lo Barnechea', '/comunas/lo-barnechea/'),
]


def j(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(',', ': '))


def page_head(title, description, canonical, og_image, active=None, extra_schema=None, body_class='internal-page', page_type='general'):
    if extra_schema is None:
        extra_schema = []
    org = {"@context": "https://schema.org", "@type": "Organization", "name": "Equipo de estudiodecabida.cl", "url": "https://estudiodecabida.cl/", "logo": "https://estudiodecabida.cl/assets/favicon.png", "image": og_image, "description": "Estudio de cabida, análisis normativo y evaluación de terrenos antes de comprar, invertir o desarrollar en Chile.", "areaServed": {"@type": "Country", "name": "Chile"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+56-9-7605-2356", "contactType": "sales", "areaServed": "CL", "availableLanguage": ["es", "es-CL"]}]}
    website = {"@context": "https://schema.org", "@type": "WebSite", "name": "estudiodecabida.cl", "url": "https://estudiodecabida.cl/", "inLanguage": "es-CL"}
    scripts = '\n'.join([f'<script type="application/ld+json">{html.escape(j(obj))}</script>' for obj in [org, website] + extra_schema])
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-N6MZJNKL');</script>
<!-- End Google Tag Manager -->
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{html.escape(title)}</title>
<meta content="{html.escape(description)}" name="description"/>
<meta content="index, follow, max-image-preview:large" name="robots"/>
<link href="https://estudiodecabida.cl{canonical}" rel="canonical"/>
<meta content="website" property="og:type"/>
<meta content="estudiodecabida.cl" property="og:site_name"/>
<meta content="{html.escape(title)}" property="og:title"/>
<meta content="{html.escape(description)}" property="og:description"/>
<meta content="https://estudiodecabida.cl{canonical}" property="og:url"/>
<meta content="{og_image}" property="og:image"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="#0f1722" name="theme-color"/>
<link href="/assets/favicon.png" rel="icon" type="image/png"/>
<link href="/assets/favicon.png" rel="apple-touch-icon"/>
<link href="/css/style.css" rel="stylesheet"/>
<link href="/css/home-hero.css" rel="stylesheet"/>
{scripts}
</head>
<body class="{body_class}" data-page-type="{page_type}">
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-N6MZJNKL"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
{header(active)}
<main class="page">'''


def header(active=None):
    def navcls(name):
        return 'active' if active == name else ''
    return f'''<header class="siteHeader">
  <div class="wrap siteHeader__inner">
    <a class="brand" href="/" aria-label="Ir a la portada de estudiodecabida.cl">
      <span class="brand__top">Equipo de</span>
      <span class="brand__name">estudiodecabida.cl</span>
    </a>
    <nav class="nav" aria-label="Principal"><a href="/estudio-de-cabida/" class="{navcls('servicio')}">Servicio</a><a href="/precios/" class="{navcls('precios')}">Precios</a><a href="/casos/" class="{navcls('casos')}">Casos</a><a href="/contacto/" class="{navcls('contacto')}">Contacto</a></nav>
    <a class="btn btn--primary siteHeader__cta" href="{WHATSAPP}" target="_blank" rel="noopener" data-track="whatsapp_click" data-track-label="header_cta">Evaluar terreno</a>
    <button class="siteHeader__toggle" type="button" data-menu-toggle aria-label="Abrir menú" aria-expanded="false">☰</button>
  </div>
  <div class="wrap">
    <div class="mobileMenu" data-mobile-menu>
      <a href="/estudio-de-cabida/">Servicio</a><a href="/precios/">Precios</a><a href="/casos/">Casos</a><a href="/contacto/">Contacto</a>
      <a class="btn btn--primary" href="{WHATSAPP}" target="_blank" rel="noopener" data-track="whatsapp_click" data-track-label="mobile_header_cta">Evaluar terreno</a>
    </div>
  </div>
</header>'''


def footer():
    guide_links = ''.join([f'<li><a href="{u}">{t}</a></li>' for t,u in GUIDE_LINKS])
    commune_links = ''.join([f'<li><a href="{u}">{t}</a></li>' for t,u in COMMUNES])
    return f'''</main>
<footer class="footer">
<div class="wrap footer__inner">
<div class="footer__brand">
<div class="footer__title">Equipo de estudiodecabida.cl</div>
<p class="small">Confirmamos si un terreno conviene antes de invertir. Traducimos CIP, norma urbana y restricciones reales en una conclusión clara para decidir con más seguridad.</p>
<div class="footer__meta">
<span>Santiago, Chile</span>
<span>WhatsApp: <a href="{WHATSAPP}" rel="noopener" target="_blank" data-track="whatsapp_click" data-track-label="footer_whatsapp">+56 9 7605 2356</a></span>
<span><a href="/contacto/">Enviar dirección o rol</a></span>
</div>
</div>
<div class="footer__cols">
<div>
<div class="footer__heading">Servicio</div>
<ul><li><a href="/estudio-de-cabida/">Página madre del servicio</a></li><li><a href="/estudio-de-cabida-comercial/">Cabida comercial</a></li><li><a href="/estudio-de-cabida-tecnica/">Cabida técnica</a></li><li><a href="/precios/">Precios y alcances</a></li></ul>
</div>
<div>
<div class="footer__heading">Guías clave</div>
<ul>{guide_links}</ul>
</div>
<div>
<div class="footer__heading">Cobertura y SEO</div>
<ul><li><a href="/comunas/">Estudios por comuna</a></li>{commune_links}</ul>
</div>
</div>
</div>
</footer>
<a aria-label="Abrir WhatsApp" class="waFloat" href="{WHATSAPP}?text=Hola%2C%20estaba%20revisando%20estudiodecabida.cl%20y%20quiero%20evaluar%20un%20terreno%21" rel="noopener" target="_blank" data-track="whatsapp_click" data-track-label="floating_whatsapp">
<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M20.52 3.48A11.8 11.8 0 0 0 12.1 0C5.58 0 .28 5.3.28 11.82c0 2.08.55 4.11 1.58 5.89L0 24l6.48-1.7a11.8 11.8 0 0 0 5.62 1.43h.01c6.52 0 11.82-5.3 11.82-11.82 0-3.16-1.23-6.13-3.41-8.43Zm-8.42 18.25h-.01a9.83 9.83 0 0 1-5-1.37l-.36-.22-3.85 1.01 1.03-3.75-.24-.38A9.8 9.8 0 0 1 2.28 11.82C2.28 6.4 6.68 2 12.1 2c2.62 0 5.08 1.02 6.93 2.87a9.74 9.74 0 0 1 2.88 6.95c0 5.42-4.4 9.91-9.81 9.91Zm5.38-7.37c-.29-.14-1.71-.84-1.98-.94-.26-.1-.45-.14-.64.15-.19.29-.74.94-.91 1.13-.17.19-.34.22-.63.07-.29-.14-1.2-.44-2.29-1.41-.85-.76-1.42-1.7-1.58-1.99-.17-.29-.02-.45.12-.59.13-.13.29-.34.43-.5.14-.17.19-.29.29-.48.1-.19.05-.36-.02-.5-.07-.14-.64-1.55-.88-2.13-.23-.56-.47-.49-.64-.49-.16-.01-.35-.01-.54-.01s-.5.07-.76.36c-.26.29-1 1-1 2.45s1.03 2.85 1.17 3.05c.14.19 2.02 3.08 4.89 4.32.68.29 1.21.47 1.63.6.69.22 1.31.19 1.8.12.55-.08 1.71-.7 1.95-1.37.24-.67.24-1.25.17-1.37-.07-.12-.26-.19-.55-.34Z"></path></svg>
</a>
<script src="/js/main.js"></script>
</body>
</html>'''


def breadcrumb(items):
    bits = ['<nav aria-label="Breadcrumbs" class="breadcrumbs">']
    for i, (name, url) in enumerate(items):
        if i:
            bits.append('<span>/</span>')
        if url:
            bits.append(f'<a href="{url}">{name}</a>')
        else:
            bits.append(f'<strong>{name}</strong>')
    bits.append('</nav>')
    return ''.join(bits)


def hero(asset, kicker, title, lead, cta1=('Evaluar terreno', WHATSAPP), cta2=('Ver qué incluye el estudio','/que-incluye-un-estudio-de-cabida/'), trust=None, badge='Certeza normativa', panel_label='Base de decisión antes de invertir', panel_title='Menos intuición. Más claridad normativa.', cards=None):
    trust = trust or ['Antes de comprar', 'Antes de ofertar', 'Antes de diseñar', 'Antes de comprometer capital']
    cards = cards or [
        ('Qué se puede hacer','Uso de suelo y compatibilidades reales','Evita asumir programas que la norma no admite o condiciona.'),
        ('Qué no conviene asumir','Altura, constructibilidad y límites críticos','Aterriza el potencial antes de prometer metros o rentabilidad.'),
        ('Riesgos','Restricciones que cambian el negocio','Detecta afectaciones o condiciones que pueden bajar el valor real del terreno.'),
        ('Decisión','Avanzar, renegociar o descartar','La cabida ordena la siguiente jugada con más criterio y menos ruido.'),
    ]
    trust_html=''.join([f'<span>{t}</span>' for t in trust])
    card_html=[]
    for i,(e,s,p) in enumerate(cards):
        cls='homeHeroCard homeHeroCard--accent' if i==3 else 'homeHeroCard'
        card_html.append(f'<article class="{cls}"><span class="homeHeroCard__eyebrow">{e}</span><strong>{s}</strong><p>{p}</p></article>')
    return f'''<div class="wrap wrap--hero">
<section class="homeHeroSection">
  <div class="homeHero" aria-labelledby="page-hero-title">
    <div class="homeHero__bg" aria-hidden="true">
      <img class="homeHero__art" src="{asset}" alt="" />
    </div>
    <div class="homeHero__inner">
      <div class="homeHero__copy">
        <div class="homeHero__kicker"><span class="dot"></span> {kicker}</div>
        <h1 id="page-hero-title">{title}</h1>
        <p class="homeHero__lead">{lead}</p>
        <div class="homeHero__actions">
          <a class="btn btn--primary" href="{cta1[1]}" target="{'_blank' if cta1[1].startswith('http') else '_self'}" rel="noopener" data-track="{'whatsapp_click' if cta1[1].startswith('http') else 'cta_click'}" data-track-label="hero_primary">{cta1[0]}</a>
          <a class="btn btn--ghost" href="{cta2[1]}" data-track="cta_click" data-track-label="hero_secondary">{cta2[0]}</a>
        </div>
        <div class="homeHero__trust">{trust_html}</div>
      </div>
      <div class="homeHero__panelWrap">
        <div class="homeHero__badge">{badge}</div>
        <div class="homeHero__panel">
          <div class="homeHero__panelHead">
            <span class="homeHero__panelLabel">{panel_label}</span>
            <strong>{panel_title}</strong>
          </div>
          <div class="homeHero__panelGrid">{''.join(card_html)}</div>
        </div>
      </div>
    </div>
  </div>
</section>'''


def offer_cards(section_title='Dos alcances principales. Una misma base seria.', section_lead='Mostramos dos formas de trabajo según el nivel de claridad técnica y visual que necesita la decisión.', with_buttons=True):
    btn1 = '<a class="btn btn--primary btn--full" href="/estudio-de-cabida-comercial/" data-track="cta_click" data-track-label="commercial_offer">Ver Estudio Comercial</a>' if with_buttons else ''
    btn2 = '<a class="btn btn--primary btn--full" href="/estudio-de-cabida-tecnica/" data-track="cta_click" data-track-label="technical_offer">Ver Estudio Técnico</a>' if with_buttons else ''
    return f'''<section class="section">
  <div class="section__head">
    <div>
      <p class="eyebrow">Alcances principales</p>
      <h2>{section_title}</h2>
      <p class="lead">{section_lead}</p>
    </div>
    <a class="btn" href="/precios/">Ver precios y comparación</a>
  </div>
  <div class="grid2">
    <article class="priceCard priceCard--featured has-badge">
      <div class="priceCard__topbar"><div class="pill">Desde $890.000</div><div class="priceCard__badge">Más recomendado</div></div>
      <div class="priceCard__name">Estudio de Cabida Comercial</div>
      <p class="muted">La opción recomendada cuando, además de entender el terreno, necesitas comunicar su potencial con mayor claridad frente a socios, inversionistas o clientes.</p>
      <ul class="list list--compact"><li>Todo lo del Estudio de Cabida Técnica</li><li>Visualización conceptual del potencial</li><li>Al menos 1 imagen tipo render conceptual</li><li>Visualizaciones adicionales según caso</li><li>Reunión de revisión</li></ul>
      <div class="note"><strong>La mayoría de los casos:</strong><br/>entre $890.000 y $1.490.000.</div>
      {btn1}
    </article>
    <article class="priceCard">
      <div class="priceCard__topbar"><div class="pill">Desde $490.000</div></div>
      <div class="priceCard__name">Estudio de Cabida Técnica</div>
      <p class="muted">La opción técnica para tomar una decisión sólida con base normativa y gráfica funcional, sin que se sienta recortada ni insuficiente.</p>
      <ul class="list list--compact"><li>Análisis normativo aplicado</li><li>Revisión de CIP, zonificación y restricciones</li><li>Cuadros de superficies</li><li>Esquemas normativos y volumétricos simples</li><li>Conclusión clara y reunión de revisión</li></ul>
      <div class="note"><strong>La mayoría de los casos:</strong><br/>entre $490.000 y $790.000.</div>
      {btn2}
    </article>
  </div>
</section>'''


def comparison_table():
    rows = [
        ('Utilidad principal','Entender y comunicar mejor una oportunidad','Tomar una decisión técnica sólida'),
        ('Mejor para','Inversión, socios, presentación o comparación','Compra, oferta o evaluación con foco técnico'),
        ('Sirve para decidir','Sí, con base normativa y lectura estratégica','Sí, con base normativa y gráfica funcional'),
        ('Sirve para presentar','Sí, con mucha más claridad para terceros','Sí, pero de forma más interna y funcional'),
        ('Profundidad visual','Alta','Media'),
        ('Tipo de gráfica','Esquemas + render conceptual + visualizaciones','Esquemas normativos + volumetría simple'),
        ('Incluye reunión','Sí','Sí'),
        ('Nivel de claridad para terceros','Más alto','Correcto, pero menos comercial'),
    ]
    trs = ''.join([f'<tr><th>{a}</th><td>{b}</td><td>{c}</td></tr>' for a,b,c in rows])
    return f'''<section class="section section--slate">
  <div class="section__head section__head--light">
    <div>
      <p class="eyebrow">Comparación clara</p>
      <h2>Técnico vs comercial sin letra chica rara.</h2>
      <p class="lead">Los dos sirven para decidir. La diferencia está en el nivel de claridad visual y en qué tan bien necesitas comunicar el potencial a terceros.</p>
    </div>
  </div>
  <div class="card card--padded">
    <table class="tableGuide">
      <thead><tr><th>Aspecto</th><th>Comercial</th><th>Técnica</th></tr></thead>
      <tbody>{trs}</tbody>
    </table>
  </div>
</section>'''


def related_guides():
    links=''.join([f'<a class="card card--padded" href="{u}"><h3>{t}</h3><p class="muted">Abrir guía</p></a>' for t,u in SEO_LINKS])
    return f'''<section class="section">
      <div class="section__head"><div><p class="eyebrow">Autoridad temática</p><h2>Guías útiles para decidir mejor.</h2><p class="lead">Complementan el servicio y ayudan a entender por qué una buena cabida cambia una compra.</p></div></div>
      <div class="relatedLinks">{links}</div>
    </section>'''


def faq_section(items, title='Preguntas frecuentes', lead='Lo importante es decidir mejor, no entender toda la normativa por tu cuenta.'):
    details=''.join([f'<details class="faqItem" {"open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i,(q,a) in enumerate(items)])
    return f'''<section class="section">
      <div class="section__head"><div><p class="eyebrow">{title}</p><h2>{lead}</h2></div></div>
      <div class="faqList">{details}</div>
    </section>'''


def cta_band(title='Envíanos dirección, rol o comuna y te indicamos qué tipo de estudio hace sentido para tu caso.', lead='Puedes partir sin tener todo resuelto. Si aún no compras, igual conviene revisar antes de comprometer capital.'):
    return f'''<section class="section ctaBand">
      <div>
        <p class="eyebrow">Siguiente paso</p>
        <h2>{title}</h2>
        <p class="lead">{lead}</p>
      </div>
      <div class="hero__actions">
        <a class="btn btn--primary" href="{WHATSAPP}" target="_blank" rel="noopener" data-track="whatsapp_click" data-track-label="cta_band_whatsapp">Evaluar terreno</a>
        <a class="btn" href="/contacto/" data-track="cta_click" data-track-label="cta_band_form">Ir al formulario</a>
      </div>
    </section></div>'''


def write(rel, content):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding='utf-8')

# HOME
home_schema = [
    {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://estudiodecabida.cl/"}]},
    {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": "¿Qué es un estudio de cabida?", "acceptedAnswer": {"@type": "Answer", "text": "Es un análisis normativo y estratégico que estima qué se puede hacer en un terreno, qué restricciones lo afectan y si conviene avanzar con una compra, inversión o desarrollo."}},
        {"@type": "Question", "name": "¿Sirve antes de comprar un terreno?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Es uno de los momentos donde más valor entrega, porque permite validar potencial, detectar riesgos y evitar decisiones basadas solo en intuición, precio o ubicación."}},
        {"@type": "Question", "name": "¿Cuál alcance conviene más?", "acceptedAnswer": {"@type": "Answer", "text": "El Estudio de Cabida Comercial es la opción recomendada cuando además de entender el terreno necesitas comunicar mejor su potencial. El Técnico sigue siendo una alternativa sólida y profesional para decidir con base normativa."}},
        {"@type": "Question", "name": "¿Se puede partir sin CIP?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. En muchos casos basta con dirección, rol o comuna para iniciar una revisión preliminar y luego complementar la información faltante."}}
    ]},
    {"@context": "https://schema.org", "@type": "Service", "name": "Estudio de cabida y evaluación normativa de terrenos", "serviceType": "Estudio de cabida", "provider": {"@type": "Organization", "name": "Equipo de estudiodecabida.cl", "url": "https://estudiodecabida.cl/"}, "areaServed": {"@type": "Country", "name": "Chile"}, "url": "https://estudiodecabida.cl/", "description": "Servicio para evaluar terrenos antes de comprar, invertir o desarrollar mediante análisis normativo, CIP y lectura estratégica de restricciones y potencial."}
]
home = page_head('Confirma si un terreno conviene antes de invertir | estudiodecabida.cl','Analizamos CIP, normativa, restricciones y potencial real del predio para ayudarte a decidir con claridad si conviene avanzar, renegociar o descartar.','/','https://estudiodecabida.cl/assets/images/hero-home.webp',None,home_schema, '', 'home')
home += hero('/assets/images/hero-home.webp','Estudio de cabida para inversión inmobiliaria','Confirma si un terreno conviene antes de invertir','Analizamos CIP, normativa, restricciones y potencial real del predio para ayudarte a decidir con claridad si conviene avanzar, renegociar o descartar.',('Evaluar terreno',WHATSAPP),('Ver qué incluye el estudio','/que-incluye-un-estudio-de-cabida/'),['Antes de comprar','Antes de ofertar','Antes de diseñar','Antes de comprometer capital'])
home += '''
<section class="section section--tightTop">
  <div class="section__head">
    <div>
      <p class="eyebrow">Qué hacemos exactamente</p>
      <h2>Los argumentos para decidir. El criterio para avanzar.</h2>
      <p class="lead">La gracia no es listar normas. La gracia es traducirlas en una conclusión usable para una compra, una oferta, una comparación o una decisión de diseño.</p>
    </div>
  </div>
  <div class="grid3">
    <article class="card card--padded"><div class="iconBox">01</div><h3>Qué restricciones afectan el terreno</h3><p class="muted">Uso de suelo, altura, constructibilidad, ocupación, expropiaciones, afectaciones o compatibilidades relevantes.</p></article>
    <article class="card card--padded"><div class="iconBox">02</div><h3>Qué potencial real tiene</h3><p class="muted">Aterrizamos expectativas a datos reales para no prometer metros, programas o rentabilidades sobre supuestos débiles.</p></article>
    <article class="card card--padded"><div class="iconBox">03</div><h3>Qué decisión cambia</h3><p class="muted">Concluimos si conviene avanzar, renegociar, descartar o profundizar con una base mucho más sólida.</p></article>
  </div>
</section>
<section class="section">
  <div class="section__head">
    <div>
      <p class="eyebrow">Momentos donde más valor entrega</p>
      <h2>Antes de comprar, ofertar, diseñar o comprometer capital.</h2>
      <p class="lead">Ahí es donde una cabida bien leída deja de ser un lujo y pasa a ser una capa de protección y criterio.</p>
    </div>
  </div>
  <div class="grid2">
    <article class="card card--padded"><h3>Antes de comprar</h3><p class="muted">Evitas pagar por un terreno equivocado o sobreestimar su potencial real.</p></article>
    <article class="card card--padded"><h3>Antes de ofertar</h3><p class="muted">Ajustas tu oferta según límites, riesgos y oportunidades detectadas.</p></article>
    <article class="card card--padded"><h3>Antes de diseñar</h3><p class="muted">Partes desde una base normativa más limpia para no diseñar en falso.</p></article>
    <article class="card card--padded"><h3>Antes de presentar una oportunidad</h3><p class="muted">Aumentas claridad para socios, clientes o inversionistas cuando el caso lo necesita.</p></article>
  </div>
</section>
'''
home += offer_cards('Dos ofertas principales. Una recomendada para la mayoría de decisiones serias.','El Estudio de Cabida Comercial queda primero porque suele ser la mejor opción cuando además de decidir bien necesitas comunicar mejor el potencial.')
home += '''
<section class="section">
  <div class="section__head">
    <div>
      <p class="eyebrow">Qué cambia después de una buena cabida</p>
      <h2>La decisión deja de apoyarse solo en intuición, precio o entusiasmo.</h2>
    </div>
  </div>
  <div class="grid3">
    <article class="card card--padded"><div class="iconBox">A</div><h3>Detectas restricciones ocultas</h3><p class="muted">Expropiaciones, limitantes de forma, uso o eficiencia que no siempre son obvias en una primera lectura.</p></article>
    <article class="card card--padded"><div class="iconBox">B</div><h3>Ajustas expectativas a datos reales</h3><p class="muted">Metros, altura y programa dejan de ser una ilusión y se convierten en una hipótesis más seria.</p></article>
    <article class="card card--padded"><div class="iconBox">C</div><h3>Comparas opciones con criterio</h3><p class="muted">Dos terrenos pueden costar parecido y aun así tener valores reales muy distintos.</p></article>
    <article class="card card--padded"><div class="iconBox">D</div><h3>Evitas pagar por un terreno equivocado</h3><p class="muted">Lo que no conviene comprar a tiempo también es una buena decisión.</p></article>
    <article class="card card--padded"><div class="iconBox">E</div><h3>Ordenas la siguiente etapa</h3><p class="muted">La cabida ayuda a definir si corresponde seguir con anteproyecto, negociación o descarte.</p></article>
    <article class="card card--padded"><div class="iconBox">F</div><h3>Tomas decisiones con más seguridad</h3><p class="muted">Con menos ruido, menos promesa inflada y más lectura aplicada al caso real.</p></article>
  </div>
</section>
<section class="section">
  <div class="section__head">
    <div>
      <p class="eyebrow">Casos resumidos</p>
      <h2>Cuando una buena cabida cambia la operación.</h2>
      <p class="lead">No todos los hallazgos implican descartar. A veces el valor está en ajustar la estrategia correcta.</p>
    </div>
    <a class="btn" href="/casos/">Ver todos los casos</a>
  </div>
  <div class="grid3">
    <article class="card card--padded"><h3>Lo Barnechea / línea de expropiación</h3><p class="muted">Un terreno que parecía apto para varias viviendas perdió atractivo al detectar una afectación que alteraba fuerte su aprovechamiento real.</p></article>
    <article class="card card--padded"><h3>Santiago Centro / bodega + oficinas</h3><p class="muted">La cabida mostró que sí había viabilidad, pero con un ajuste importante en la mezcla útil del programa para que el negocio cerrara mejor.</p></article>
    <article class="card card--padded"><h3>Lo Barnechea / conjunto armónico</h3><p class="muted">El análisis permitió entender cómo una condición urbana heredada cambiaba restricciones y beneficios para una vivienda en el predio.</p></article>
  </div>
</section>
'''
home += related_guides()
home += faq_section([
    ('¿Qué es un estudio de cabida?','Es un análisis normativo y estratégico que estima qué se puede hacer en un terreno, qué restricciones lo afectan y si conviene avanzar con una compra, inversión o desarrollo.'),
    ('¿Sirve antes de comprar un terreno?','Sí. Es uno de los momentos donde más valor entrega, porque permite validar potencial, detectar riesgos y evitar decisiones basadas solo en intuición, precio o ubicación.'),
    ('¿Cuál alcance recomiendan?','En la mayoría de los casos serios de inversión o evaluación recomendamos el Estudio de Cabida Comercial. El Técnico sigue siendo una opción sólida cuando la prioridad es una decisión técnica clara.'),
    ('¿Garantiza aprobación municipal?','No. El estudio no reemplaza un permiso ni garantiza aprobación municipal. Sí ordena una base mucho más seria para decidir el siguiente paso.'),
])
home += cta_band()
home += footer()
write('index.html', home)

# PRECIOS and alias
faq_prices = [{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://estudiodecabida.cl/"}, {"@type": "ListItem", "position": 2, "name": "Precios", "item": "https://estudiodecabida.cl/precios/"}]}]
precios = page_head('Precios y alcances del estudio de cabida | estudiodecabida.cl','Mostramos rangos orientativos para que entiendas el nivel de análisis antes de escribir. El valor final depende del terreno, la complejidad normativa y el nivel de definición requerido.','/precios/','https://estudiodecabida.cl/assets/images/hero-estudio-de-cabida.webp','precios', faq_prices, 'internal-page','pricing')
precios += hero('/assets/images/hero-estudio-de-cabida.webp','Precios y alcances','Precios y alcances del estudio de cabida','Mostramos rangos orientativos para que entiendas el nivel de análisis antes de escribir. El valor final depende del terreno, la complejidad normativa y el nivel de definición requerido.',('Consultar por WhatsApp',WHATSAPP),('Ir al formulario','/contacto/'),['Rangos orientativos','Transparencia de alcance','Comercial recomendado','Técnica sólida'])
precios += '''
<div class="wrap">'''
precios += offer_cards('Dos alcances visibles. Comercial primero y recomendado.','La lógica antigua de tres planes se reemplaza por dos ofertas más claras, más defendibles y mejor alineadas con decisiones reales.', False)
precios += comparison_table()
precios += '''
<section class="section">
  <div class="section__head"><div><p class="eyebrow">Qué define el precio exacto</p><h2>No depende solo del tamaño del terreno.</h2><p class="lead">El valor cambia según complejidad normativa, calidad de antecedentes, urgencia, necesidad de contraste entre escenarios y nivel de claridad gráfica requerido.</p></div></div>
  <div class="grid2">
    <article class="card card--padded"><h3>Variables que pueden mover el precio</h3><ul class="list"><li>Complejidad normativa y cantidad de restricciones relevantes</li><li>Si existe CIP, levantamiento, planos u otros antecedentes</li><li>Nivel de incertidumbre que hay que despejar</li><li>Necesidad de comparar escenarios o hipótesis</li><li>Necesidad de presentación a terceros</li></ul></article>
    <article class="card card--padded"><h3>Qué no incluye por defecto</h3><ul class="list"><li>Permiso de edificación</li><li>Anteproyecto completo</li><li>Gestión integral municipal</li><li>Garantía de aprobación</li><li>Desarrollo arquitectónico de detalle fuera del alcance cotizado</li></ul></article>
  </div>
</section>
'''
precios += faq_section([
    ('¿Por qué muestran rangos y no una tarifa única?','Porque no todos los terrenos requieren la misma profundidad ni tienen la misma complejidad normativa. Un rango orienta sin vender una falsa simpleza.'),
    ('¿Cuál alcance conviene para decisiones importantes?','En la mayoría de los casos de inversión, comparación o presentación conviene el Estudio de Cabida Comercial, porque suma claridad visual además de la base técnica.'),
    ('¿La Técnica se queda corta?','No. La Técnica sigue siendo una opción seria, sólida y profesional para decidir bien. La diferencia principal está en el nivel de claridad visual y comunicacional.'),
    ('¿Puedo escribir aunque todavía no compré?','Sí. De hecho, muchas veces ese es el mejor momento para consultar.'),
], lead='Precios claros sin empobrecer el servicio.')
precios += cta_band('Cuéntanos tu caso y te orientamos al alcance correcto.','Si nos envías dirección, rol, comuna y objetivo, te decimos qué tipo de estudio hace más sentido para tu caso.')
precios += footer()
write('precios/index.html', precios)
# alias /precio/
alias = precios.replace('href="https://estudiodecabida.cl/precios/" rel="canonical"','href="https://estudiodecabida.cl/precios/" rel="canonical"').replace('/precios/','/precios/')
write('precio/index.html', precios.replace('https://estudiodecabida.cl/precios/','https://estudiodecabida.cl/precios/'))

# PAGE MOTHER ESTUDIO
mother_schema = [{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://estudiodecabida.cl/"}, {"@type": "ListItem", "position": 2, "name": "Estudio de cabida", "item": "https://estudiodecabida.cl/estudio-de-cabida/"}]}]
estudio = page_head('Estudio de cabida para evaluar un terreno con más claridad | estudiodecabida.cl','Entiende qué es un estudio de cabida, cuándo conviene pedirlo, qué revisamos y cómo ayuda a decidir si conviene avanzar, renegociar o descartar.','/estudio-de-cabida/','https://estudiodecabida.cl/assets/images/hero-estudio-de-cabida.webp','servicio',mother_schema,'internal-page','service')
estudio += hero('/assets/images/hero-estudio-de-cabida.webp','Página madre del servicio','Estudio de cabida para evaluar un terreno con más claridad','Ayuda a entender qué restricciones afectan un terreno, qué potencial real tiene y si conviene avanzar, renegociar o descartar antes de comprar, ofertar o diseñar.',('Evaluar terreno',WHATSAPP),('Ver comparación','/estudio-tecnico-vs-comercial/'))
estudio += '''<div class="wrap">'''
estudio += '''
<section class="section section--tightTop">
  <div class="section__head"><div><p class="eyebrow">Qué es</p><h2>Una lectura aplicada del terreno, no un PDF lleno de tecnicismos sueltos.</h2><p class="lead">Tomamos CIP, zonificación, restricciones y contexto urbano para convertirlos en una hipótesis seria de potencial y una recomendación clara de siguiente paso.</p></div></div>
  <div class="grid3">
    <article class="card card--padded"><h3>Qué revisamos</h3><p class="muted">Uso de suelo, alturas, constructibilidad, ocupación, afectaciones, expropiación, forma del predio y otras variables que cambian la operación.</p></article>
    <article class="card card--padded"><h3>Cuándo conviene pedirlo</h3><p class="muted">Antes de comprar, antes de ofertar, antes de diseñar o cuando necesitas comparar opciones de manera más seria.</p></article>
    <article class="card card--padded"><h3>Qué decisiones ayuda a tomar</h3><p class="muted">Avanzar, renegociar, descartar, profundizar o reencuadrar el proyecto realista para el terreno.</p></article>
  </div>
</section>
'''
estudio += offer_cards('Técnica y Comercial conviven bajo una misma lógica seria.','La Comercial queda recomendada para la mayoría de los casos donde además de decidir hay que comunicar mejor el potencial.')
estudio += comparison_table()
estudio += '''
<section class="section">
  <div class="section__head"><div><p class="eyebrow">Casos resumidos</p><h2>Tres situaciones donde el estudio cambió la lectura del negocio.</h2></div><a class="btn" href="/casos/">Ver casos</a></div>
  <div class="grid3">
    <article class="card card--padded"><h3>Expropiación en Lo Barnechea</h3><p class="muted">La compra dejó de verse tan atractiva cuando la afectación se volvió evidente dentro del aprovechamiento real del predio.</p></article>
    <article class="card card--padded"><h3>Bodega + oficinas en Santiago Centro</h3><p class="muted">No era un no. Era un sí con ajustes. Esa diferencia cambió la estrategia del cliente.</p></article>
    <article class="card card--padded"><h3>Conjunto armónico en Lo Barnechea</h3><p class="muted">La lectura correcta de una condición urbana previa permitió entender mejor restricciones y beneficios para una vivienda.</p></article>
  </div>
</section>
'''
estudio += faq_section([
    ('¿Qué es exactamente un estudio de cabida?','Es un análisis normativo y estratégico del terreno para entender restricciones, potencial y decisión.'),
    ('¿En qué se diferencia la Técnica de la Comercial?','Las dos sirven para decidir. La Comercial suma una capa de claridad visual y comunicacional más fuerte.'),
    ('¿Necesito tener CIP para contratarlo?','Idealmente sí, pero en muchos casos se puede comenzar con dirección o rol.'),
    ('¿Sirve para Ads y para SEO a la vez esta página?','Sí. Esta página funciona como página madre del servicio y como hub hacia las páginas más específicas.'),
])
estudio += cta_band()
estudio += footer()
write('estudio-de-cabida/index.html', estudio)

# COMMERCIAL / TECHNICAL pages
for rel, title, desc, h1, lead, page_type, active, asset, alt_title in [
    ('estudio-de-cabida-comercial/index.html','Estudio de Cabida Comercial | estudiodecabida.cl','Opción recomendada para entender y comunicar el potencial del terreno con mayor claridad frente a socios, inversionistas o clientes.','Entiende el potencial del terreno y comunícalo con mayor claridad','Base normativa seria más visualización conceptual para presentar una oportunidad con mayor fuerza frente a inversionistas, socios o clientes.','commercial','servicio','/assets/images/hero-estudio-de-cabida-comercial.webp','Comercial'),
    ('estudio-de-cabida-tecnica/index.html','Estudio de Cabida Técnica | estudiodecabida.cl','Opción técnica, sólida y profesional para tomar una decisión con base normativa y gráfica funcional.','Toma una decisión técnica clara con una base normativa sólida','Una opción completa, seria y profesional para evaluar un terreno sin convertir el alcance en algo recortado o pobre.','technical','servicio','/assets/images/hero-estudio-de-cabida-tecnica.webp','Técnica')
]:
    can = '/' + rel.split('/')[0] + '/'
    body = page_head(title, desc, can, f'https://estudiodecabida.cl{asset}', active, [{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://estudiodecabida.cl/"}, {"@type": "ListItem", "position": 2, "name": f"Estudio de Cabida {alt_title}", "item": f"https://estudiodecabida.cl{can}"}]}], 'internal-page', page_type)
    cards = [
        ('Para qué conviene', 'Presentar mejor el potencial', 'Útil cuando hay socios, inversión, comparación o necesidad de explicar mejor la oportunidad.'),
        ('Qué incluye', 'Base técnica + visualización', 'Suma render conceptual y visualizaciones adicionales según caso.'),
        ('Qué cambia', 'Mayor claridad para terceros', 'Ayuda a alinear decisiones cuando no eres el único que debe entender el terreno.'),
        ('Recomendación', 'Es la opción recomendada', 'La recomendamos para la mayoría de las decisiones importantes con dimensión comercial.'),
    ] if 'comercial' in rel else [
        ('Para qué conviene', 'Decidir con base normativa', 'Útil cuando la prioridad es confirmar viabilidad y restricciones con claridad técnica.'),
        ('Qué incluye', 'Lectura normativa aplicada', 'Suma esquemas, cuadros y volumetría simple sin que el servicio se sienta recortado.'),
        ('Qué cambia', 'Más certeza técnica', 'Ordena el caso y evita avanzar a ciegas hacia diseño o negociación.'),
        ('Complemento', 'Comercial si necesitas presentar', 'Si además necesitas comunicar mejor el potencial a terceros, conviene la Comercial.'),
    ]
    body += hero(asset, f'Estudio de Cabida {alt_title}', h1, lead, ('Evaluar terreno', WHATSAPP), ('Ver precios','/precios/'), cards=cards)
    body += '<div class="wrap">'
    if 'comercial' in rel:
        body += '''
        <section class="section section--tightTop"><div class="section__head"><div><p class="eyebrow">Cuándo conviene</p><h2>Cuando hay una decisión importante y también una historia que comunicar bien.</h2><p class="lead">No se vende como anteproyecto ni promete más de lo que entrega. Su fuerza está en combinar una base normativa seria con visualización conceptual suficiente para alinear mejor una oportunidad.</p></div></div><div class="grid2"><article class="card card--padded"><h3>Qué incluye</h3><ul class="list"><li>Todo lo del Estudio de Cabida Técnica</li><li>Visualización conceptual del potencial</li><li>Al menos 1 imagen tipo render conceptual</li><li>Visualizaciones adicionales según caso</li><li>Reunión de revisión</li></ul></article><article class="card card--padded"><h3>Para qué casos conviene más</h3><ul class="list"><li>Comparar terrenos con socios o inversionistas</li><li>Presentar una oportunidad con mayor claridad</li><li>Explicar potencial a clientes no técnicos</li><li>Ordenar mejor una decisión inmobiliaria seria</li></ul></article></div></section>
        <section class="section"><div class="section__head"><div><p class="eyebrow">Qué cambia respecto al Técnico</p><h2>No cambia la seriedad. Cambia la capacidad de comunicar el potencial.</h2></div></div><div class="grid2"><article class="metricCard"><strong>Base técnica completa</strong><span>La lectura normativa sigue siendo rigurosa, aplicada y enfocada en decidir bien.</span></article><article class="metricCard"><strong>Más claridad visual</strong><span>El caso se vuelve más fácil de leer, explicar y comparar con terceros.</span></article></div></section>
        '''
    else:
        body += '''
        <section class="section section--tightTop"><div class="section__head"><div><p class="eyebrow">Qué revisa</p><h2>Completo, claro y profesional.</h2><p class="lead">No es un plan menor. Es una opción técnica robusta para validar restricciones, potencial y decisión con gráficos funcionales y una conclusión seria.</p></div></div><div class="grid2"><article class="card card--padded"><h3>Qué entrega</h3><ul class="list"><li>Análisis normativo aplicado</li><li>Revisión de CIP, zonificación y restricciones</li><li>Cuadros de superficies</li><li>Esquemas normativos</li><li>Diagramas volumétricos simples</li><li>Conclusión clara y reunión de revisión</li></ul></article><article class="card card--padded"><h3>Qué no incluye</h3><ul class="list"><li>Anteproyecto completo</li><li>Render conceptual comercial</li><li>Gestión integral de permisos</li><li>Garantía de aprobación municipal</li></ul></article></div></section>
        <section class="section"><div class="section__head"><div><p class="eyebrow">Cuándo conviene</p><h2>Cuando el foco está en decidir bien desde lo técnico.</h2></div></div><div class="grid2"><article class="metricCard"><strong>Compra u oferta</strong><span>Muy útil cuando necesitas claridad normativa funcional para no avanzar a ciegas.</span></article><article class="metricCard"><strong>Si luego necesitas presentar mejor</strong><span>En ese caso, la Comercial suma la capa visual y comunicacional recomendada.</span></article></div></section>
        '''
    body += faq_section([
        ('¿Esto reemplaza un anteproyecto?','No. Es una cabida con foco de decisión, no un desarrollo arquitectónico completo.'),
        ('¿Incluye reunión?','Sí. Ambos alcances incluyen reunión de revisión.'),
        ('¿Cuál recomiendan si hay socios o inversionistas?','La Comercial.' if 'comercial' in rel else 'La Comercial, porque comunica mejor el potencial a terceros.'),
        ('¿Se puede partir con dirección o rol?','Sí. En muchos casos eso basta para comenzar la conversación.'),
    ])
    body += cta_band('Envíanos el terreno y te confirmamos si este alcance hace sentido para tu caso.','Podemos orientarte rápido si nos mandas dirección, rol, comuna y objetivo.')
    body += footer()
    write(rel, body)

# Ads pages
ads_pages = [
    ('evaluar-terreno/index.html','Evalúa un terreno antes de comprar, ofertar o invertir | estudiodecabida.cl','Te ayudamos a entender qué restricciones lo afectan, qué potencial tiene y si conviene avanzar o no.','Evalúa un terreno antes de comprar, ofertar o invertir','Te ayudamos a entender qué restricciones lo afectan, qué potencial tiene y si conviene avanzar o no.','/assets/images/hero-evaluar-terreno.webp','ads_general'),
    ('antes-de-comprar-terreno/index.html','Antes de comprar un terreno, conviene saber qué manda de verdad sobre él | estudiodecabida.cl','Ubicación y precio no bastan. Revisamos CIP, normativa y restricciones reales para ayudarte a decidir con más criterio y menos riesgo.','Antes de comprar un terreno, conviene saber qué manda de verdad sobre él','Ubicación y precio no bastan. Revisamos CIP, normativa y restricciones reales para ayudarte a decidir con más criterio y menos riesgo.','/assets/images/hero-antes-de-comprar-terreno.webp','ads_prebuy'),
    ('cabida-comercial/index.html','Cabida comercial para inversionistas | estudiodecabida.cl','Base normativa seria más visualización conceptual para presentar una oportunidad con mayor fuerza.','Entiende el potencial del terreno y muéstralo con claridad','Base normativa seria más visualización conceptual para presentar una oportunidad con mayor fuerza frente a inversionistas, socios o clientes.','/assets/images/hero-cabida-comercial.webp','ads_premium'),
]
for rel, title, desc, h1, lead, asset, ptype in ads_pages:
    can='/' + rel.split('/')[0] + '/'
    p=page_head(title, desc, can, f'https://estudiodecabida.cl{asset}', 'servicio', [{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://estudiodecabida.cl/"}, {"@type": "ListItem", "position": 2, "name": h1, "item": f"https://estudiodecabida.cl{can}"}]}], 'internal-page', ptype)
    p += hero(asset, 'Landing de evaluación', h1, lead, ('Enviar dirección o rol', WHATSAPP), ('Ver precios','/precios/'))
    p += '<div class="wrap">'
    p += '''<section class="section section--tightTop"><div class="section__head"><div><p class="eyebrow">Qué revisamos</p><h2>Restricciones, potencial y decisión.</h2></div></div><div class="grid3"><article class="card card--padded"><h3>CIP y zonificación</h3><p class="muted">Para entender qué manda de verdad sobre el predio.</p></article><article class="card card--padded"><h3>Potencial real</h3><p class="muted">Qué podría sostener el terreno y qué no conviene asumir.</p></article><article class="card card--padded"><h3>Impacto en la decisión</h3><p class="muted">Si conviene avanzar, renegociar, descartar o profundizar.</p></article></div></section>'''
    if 'antes-de-comprar' in rel:
        p += '''<section class="section"><div class="section__head"><div><p class="eyebrow">Errores caros que evita</p><h2>Comprar por ubicación o entusiasmo sin leer la norma con criterio.</h2></div></div><div class="grid3"><article class="card card--padded"><h3>Sobrepagar</h3><p class="muted">Pagar por un potencial que no existe.</p></article><article class="card card--padded"><h3>Ofertar mal</h3><p class="muted">Negociar sin saber qué restricciones pesan de verdad.</p></article><article class="card card--padded"><h3>Diseñar en falso</h3><p class="muted">Avanzar a etapas caras sobre una base débil.</p></article></div></section>'''
    p += offer_cards('Comercial recomendado. Técnica sólida.','Ambas sirven para decidir. La Comercial queda empujada cuando la operación es importante o requiere presentar mejor el potencial.')
    p += faq_section([
        ('¿Puedo escribir aunque aún no compre?','Sí. Ese es precisamente uno de los mejores momentos para evaluar.'),
        ('¿Qué basta para empezar?','Dirección o rol, comuna y objetivo del proyecto.'),
        ('¿Cuál alcance recomiendan para decisiones importantes?','El Comercial.'),
        ('¿Cuánto demora?','Depende del caso y del alcance, pero te orientamos apenas revisamos el terreno.'),
    ], lead='Esta página está pensada para convertir sin distraer de la decisión.')
    p += cta_band('Envíanos dirección, rol o comuna y revisamos si conviene avanzar.','La idea es despejar la duda antes de que gastes más tiempo o capital.')
    p += footer()
    write(rel, p)

# Casos
cases = page_head('Casos reales de estudio de cabida | estudiodecabida.cl','Revisa escenarios donde una cabida bien leída cambió una compra, una negociación o una decisión de desarrollo.','/casos/','https://estudiodecabida.cl/assets/images/casos-hero.webp','casos',[{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://estudiodecabida.cl/"}, {"@type": "ListItem", "position": 2, "name": "Casos", "item": "https://estudiodecabida.cl/casos/"}]}],'internal-page','cases')
cases += hero('/assets/images/hero-estudio-de-cabida.webp','Casos reales','Casos donde una buena cabida cambió la decisión','Los casos sirven para mostrar que la cabida no siempre entrega un sí o un no tajante. Muchas veces entrega una mejor estrategia.')
cases += '<div class="wrap">'
for title, situation, believed, found, changed, final, proves in [
    ('Lo Barnechea / línea de expropiación','El cliente evaluaba un terreno con buena ubicación y expectativa de desarrollo.','Creía que el predio podía sostener una operación más eficiente de lo que parecía a primera vista.','El estudio detectó una afectación a utilidad pública que recortaba fuerte el aprovechamiento real del terreno.','La conversación pasó de entusiasmo por la oportunidad a revisar si tenía sentido seguir negociando bajo otro precio o directamente descartar.','La decisión final fue tratar el activo con mucha más cautela y corregir la lectura inicial del negocio.','Demuestra que una restricción no evidente puede destruir valor si se detecta demasiado tarde.'),
    ('Santiago Centro / bodega + oficinas','Había interés en desarrollar un programa mixto con foco en rentabilidad operacional.','La idea inicial asumía una distribución útil más generosa para bodegaje.','La normativa permitía avanzar, pero con una limitación relevante en la proporción útil destinada a bodega dentro del conjunto.','La operación no se descartó; se rediseñó con más criterio para que el negocio siguiera teniendo sentido.','La decisión final fue ajustar el programa, no abandonar la oportunidad.','Demuestra que el valor del estudio también está en afinar una estrategia viable, no solo en decir que no.'),
    ('Lo Barnechea / conjunto armónico','Se buscaba entender cómo afectaba a una vivienda el hecho de estar en un predio acogido a conjunto armónico por una obra anterior.','La duda inicial mezclaba intuiciones sobre posibles beneficios con temor a restricciones poco claras.','La revisión permitió distinguir qué implicancias reales seguían pesando sobre el predio y cómo eso podía alterar criterios de diseño y lectura urbana.','El cliente dejó de moverse por suposiciones y pasó a evaluar con una base normativa más precisa.','La decisión final fue seguir avanzando, pero con un entendimiento más serio del marco urbano aplicable.','Demuestra que incluso condiciones urbanas más técnicas pueden cambiar la estrategia de proyecto cuando se entienden bien.')
]:
    cases += f'''<section class="section section--tightTop"><div class="section__head"><div><p class="eyebrow">Caso</p><h2>{title}</h2></div></div><div class="grid2"><article class="card card--padded"><h3>Situación inicial</h3><p class="muted">{situation}</p><h3>Lo que el cliente creía</h3><p class="muted">{believed}</p><h3>Lo que detectó el estudio</h3><p class="muted">{found}</p></article><article class="card card--padded"><h3>Qué cambió</h3><p class="muted">{changed}</p><h3>Decisión final</h3><p class="muted">{final}</p><div class="note"><strong>Qué demuestra:</strong><br/>{proves}</div></article></div></section>'''
cases += cta_band('Si tienes un terreno en evaluación, podemos leerlo con el mismo criterio aplicado.','Envíanos la dirección, rol o comuna y te indicamos qué estudio hace más sentido.')
cases += footer()
write('casos/index.html', cases)

# Contacto
contact = page_head('Enviar dirección o rol para evaluar un terreno | estudiodecabida.cl','Envíanos dirección, rol, comuna, objetivo y urgencia. No hace falta tener todo resuelto para escribir.','/contacto/','https://estudiodecabida.cl/assets/images/hero-estudio-de-cabida.webp','contacto',[{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://estudiodecabida.cl/"}, {"@type": "ListItem", "position": 2, "name": "Contacto", "item": "https://estudiodecabida.cl/contacto/"}]}],'internal-page','contact')
contact += '<div class="wrap">' + breadcrumb([('Home','/'),('Contacto',None)]) + '''
<section class="section section--tightTop sectionIntroCard">
  <div class="section__head">
    <div>
      <p class="eyebrow">Contacto</p>
      <h1>Envíanos dirección, rol o comuna y te orientamos al alcance correcto.</h1>
      <p class="lead">No hace falta tener todo resuelto para escribir. También sirve si aún no compras el terreno. La idea es entender tu caso y decirte qué tipo de estudio hace más sentido.</p>
    </div>
    <a class="btn btn--primary" href="'''+WHATSAPP+'''?text=Hola,%20estaba%20revisando%20estudiodecabida.cl%20y%20quiero%20evaluar%20un%20terreno." target="_blank" rel="noopener" data-track="whatsapp_click" data-track-label="contact_header_whatsapp">Enviar terreno por WhatsApp</a>
  </div>
  <div class="grid2 contactGrid">
    <form class="formCard" data-whatsapp-form="">
      <div class="formGrid">
        <div class="field"><label>Nombre</label><input type="text" placeholder="Tu nombre"/></div>
        <div class="field"><label>Email</label><input type="email" placeholder="tu@email.com"/></div>
        <div class="field"><label>WhatsApp</label><input type="text" placeholder="+56 9..."/></div>
        <div class="field"><label>Comuna</label><input type="text" placeholder="Ej: Las Condes, Providencia, Colina"/></div>
        <div class="field"><label>Dirección o rol</label><input type="text" placeholder="Lo que tengas disponible"/></div>
        <div class="field"><label>Objetivo</label><select><option>Seleccionar</option><option>Comprar terreno</option><option>Ofertar</option><option>Desarrollar proyecto</option><option>Comparar opciones</option><option>Presentar a socios o inversionistas</option><option>Otro</option></select></div>
        <div class="field"><label>¿Qué tienes hoy?</label><select><option>Seleccionar</option><option>Dirección</option><option>Rol</option><option>CIP</option><option>Plano</option><option>Ninguno todavía</option></select></div>
        <div class="field"><label>Urgencia / plazo</label><select><option>Seleccionar</option><option>Hoy o mañana</option><option>Esta semana</option><option>Durante el mes</option><option>Sin urgencia</option></select></div>
      </div>
      <div class="field" style="margin-top:14px;"><label>Mensaje breve</label><textarea placeholder="Cuéntanos qué quieres hacer con el terreno y cuál es la duda principal."></textarea></div>
      <div class="formHelp">No necesitas entender de normativa para escribir. La idea del servicio es precisamente traducir esa complejidad en una decisión clara y usable.</div>
      <div style="margin-top:14px;"><a class="btn btn--primary btn--full" data-wa-form-submit href="'''+WHATSAPP+'''" target="_blank" rel="noopener" data-track="form_submit" data-track-label="contact_form_submit">Enviar por WhatsApp</a></div>
    </form>
    <div class="stack">
      <article class="card card--padded"><h3>Qué ayuda a partir más rápido</h3><ul class="list"><li>Dirección o rol del predio</li><li>Comuna o sector</li><li>Objetivo: comprar, ofertar, desarrollar o comparar</li><li>Plazo o urgencia de la decisión</li></ul></article>
      <article class="card card--padded"><h3>Qué pasa después</h3><ul class="list"><li>Revisamos el contexto y la pregunta principal</li><li>Te orientamos sobre el alcance que tiene más sentido</li><li>Definimos qué antecedentes conviene agregar si faltan</li></ul></article>
      <article class="card card--padded"><h3>Qué conviene saber</h3><div class="note"><strong>Idealmente trabajamos con CIP, pero no siempre es imprescindible.</strong><br/>En muchos casos podemos partir con dirección o rol y avanzar desde ahí.</div></article>
    </div>
  </div>
</section>
'''
contact += footer()
write('contacto/index.html', contact)

# Support pages
support_specs = [
    ('que-incluye-un-estudio-de-cabida/index.html','Qué incluye un estudio de cabida | estudiodecabida.cl','Qué se revisa, qué se entrega, qué no incluye y cuándo conviene pedirlo.','Qué incluye un estudio de cabida','Entiende qué revisamos, qué entregamos y por qué la diferencia entre información y criterio aplicado importa.'),
    ('como-se-hace-un-estudio-de-cabida/index.html','Cómo se hace un estudio de cabida | estudiodecabida.cl','Desde los insumos hasta la conclusión aplicada: así se construye una cabida seria.','Cómo se hace un estudio de cabida','Desde CIP y antecedentes hasta hipótesis, escenarios y conclusión aplicada al caso real.'),
    ('estudio-tecnico-vs-comercial/index.html','Estudio técnico vs comercial | estudiodecabida.cl','Comparación clara entre los dos alcances principales de estudiodecabida.cl.','Estudio técnico vs comercial','Las dos opciones sirven para decidir. La diferencia está en el nivel de claridad visual y comunicacional requerido.'),
    ('ejemplo-de-estudio-de-cabida/index.html','Ejemplo de estudio de cabida | estudiodecabida.cl','Cómo se lee un ejemplo de estudio de cabida y qué decisiones ayuda a tomar.','Ejemplo de estudio de cabida','Una estructura tipo para entender cómo se organiza, cómo se lee y qué tipo de decisiones habilita.'),
]
for rel,title,desc,h1,lead in support_specs:
    can='/' + rel.split('/')[0] + '/'
    p=page_head(title,desc,can,'https://estudiodecabida.cl/assets/images/hero-estudio-de-cabida.webp','servicio',[{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://estudiodecabida.cl/"}, {"@type": "ListItem", "position": 2, "name": h1, "item": f"https://estudiodecabida.cl{can}"}]}],'internal-page','guide')
    p += hero('/assets/images/hero-estudio-de-cabida.webp','Guía de apoyo',h1,lead,('Evaluar terreno',WHATSAPP),('Ver precios','/precios/'))
    p += '<div class="wrap">'
    if 'incluye' in rel:
        p += '''<section class="section section--tightTop"><div class="grid2"><article class="card card--padded"><h3>Qué se revisa</h3><ul class="list"><li>CIP, zonificación y uso de suelo</li><li>Restricciones críticas</li><li>Potencial volumétrico y de superficie</li><li>Riesgos que cambian la decisión</li></ul></article><article class="card card--padded"><h3>Qué se entrega</h3><ul class="list"><li>Lectura normativa aplicada</li><li>Esquemas, cuadros y conclusión</li><li>Recomendación de siguiente paso</li><li>Según alcance, visualización conceptual</li></ul></article></div></section><section class="section"><div class="grid2"><article class="card card--padded"><h3>Qué no incluye</h3><ul class="list"><li>Permiso de edificación</li><li>Anteproyecto completo</li><li>Garantía de aprobación</li></ul></article><article class="card card--padded"><h3>Por qué importa</h3><p class="muted">Una lista de datos no reemplaza el criterio aplicado. El valor está en traducir la norma en una decisión usable.</p></article></div></section>'''
    elif 'como-se-hace' in rel:
        p += '''<section class="section section--tightTop"><div class="grid3"><article class="card card--padded"><h3>1. Insumos</h3><p class="muted">Dirección, rol, CIP, plano o lo que exista disponible.</p></article><article class="card card--padded"><h3>2. Lectura normativa</h3><p class="muted">Se interpreta la normativa aplicable al caso concreto, no solo la norma aislada.</p></article><article class="card card--padded"><h3>3. Hipótesis y escenarios</h3><p class="muted">Se testean alternativas razonables según el objetivo del cliente.</p></article></div><div class="grid2"><article class="card card--padded"><h3>4. Contraste con el terreno</h3><p class="muted">Forma del predio, afectaciones, condiciones urbanas y eficiencia real.</p></article><article class="card card--padded"><h3>5. Conclusión</h3><p class="muted">Se aterriza la decisión: avanzar, renegociar, descartar o profundizar.</p></article></div></section>'''
    elif 'tecnico-vs-comercial' in rel:
        p += offer_cards('Cada uno resuelve un problema distinto sin romper la misma lógica de seriedad.','La Comercial es la recomendada cuando la decisión es importante y necesitas explicar mejor el potencial.') + comparison_table()
    else:
        p += '''<section class="section section--tightTop"><div class="grid2"><article class="card card--padded"><h3>Estructura típica</h3><ul class="list"><li>Pregunta inicial y objetivo</li><li>Lectura normativa aplicada</li><li>Potencial y restricciones</li><li>Escenarios razonables</li><li>Conclusión</li></ul></article><article class="card card--padded"><h3>Cómo se lee</h3><p class="muted">No se lee como un documento académico. Se lee como una herramienta para tomar una decisión real.</p></article></div></section>'''
    p += faq_section([
        ('¿Esta guía reemplaza el servicio?','No. Sirve para entender mejor qué hace el servicio y cuándo conviene pedirlo.'),
        ('¿Puedo escribir aunque todavía esté explorando?','Sí.'),
        ('¿Dónde veo los alcances?','En la página de precios y en las páginas específicas Técnica y Comercial.'),
    ])
    p += cta_band()
    p += footer()
    write(rel,p)

# Update /antes-de-comprar existing page to point to new landing while preserving keyword intent
legacy_buy = page_head('Qué revisar antes de comprar un terreno | estudiodecabida.cl','Checklist práctico para revisar antes de comprar un terreno: CIP, normativa, uso de suelo, eficiencia predial y alertas que pueden cambiar la decisión.','/antes-de-comprar/','https://estudiodecabida.cl/assets/images/guia-estudio-cabida.webp','servicio',[], 'internal-page','guide')
legacy_buy += hero('/assets/images/hero-estudio-de-cabida.webp','Guía de precompra','Qué revisar antes de comprar un terreno','Checklist práctico para revisar antes de comprar un terreno: CIP, normativa, uso de suelo, eficiencia predial y alertas que pueden cambiar la decisión.',('Ir a la landing de evaluación','/antes-de-comprar-terreno/'),('Evaluar terreno',WHATSAPP))
legacy_buy += '<div class="wrap"><section class="section section--tightTop"><div class="grid3"><article class="card card--padded"><h3>1. CIP y zonificación</h3><p class="muted">No asumir sin revisar.</p></article><article class="card card--padded"><h3>2. Restricciones críticas</h3><p class="muted">Afectaciones, expropiación, altura, forma y eficiencia real.</p></article><article class="card card--padded"><h3>3. Potencial usable</h3><p class="muted">No todo metro posible es un buen negocio.</p></article></div></section>' + cta_band() + footer()
write('antes-de-comprar/index.html', legacy_buy)

# Minimal stylesheet additions
style_path = ROOT/'css/style.css'
style = style_path.read_text(encoding='utf-8')
append = """

/* --- CRO / SEO EXTENSIONS v34 --- */
[data-page-type] .relatedLinks a{text-decoration:none;color:inherit}
.tableGuide td{color:var(--text-2)}
.tableGuide td:first-child,.tableGuide th:first-child{width:28%}
.priceCard .note{margin-top:auto}
.homeHero__actions .btn{min-width:180px}
@media (max-width: 920px){.tableGuide td:first-child,.tableGuide th:first-child{width:auto}}
"""
if 'CRO / SEO EXTENSIONS v34' not in style:
    style += append
    style_path.write_text(style, encoding='utf-8')

# Tracking JS enhancement
js = '''document.addEventListener('DOMContentLoaded', () => {
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
      const message = lines.length ? `${DEFAULT_MESSAGE}\n\n${lines.join('\n')}` : DEFAULT_MESSAGE;
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
'''
(ROOT/'js/main.js').write_text(js, encoding='utf-8')

# Sitemap refresh (basic)
urls = [
'/', '/precios/','/precio/','/estudio-de-cabida/','/estudio-de-cabida-comercial/','/estudio-de-cabida-tecnica/','/evaluar-terreno/','/antes-de-comprar-terreno/','/cabida-comercial/','/casos/','/contacto/','/que-incluye-un-estudio-de-cabida/','/como-se-hace-un-estudio-de-cabida/','/estudio-tecnico-vs-comercial/','/ejemplo-de-estudio-de-cabida/','/antes-de-comprar/','/como-leer-un-cip/','/factibilidad-normativa/','/que-puedo-construir/','/comunas/','/comunas/las-condes/','/comunas/providencia/','/comunas/vitacura/','/comunas/lo-barnechea/'
]
sitemap='''<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'''
for u in urls:
    sitemap += f'  <url><loc>https://estudiodecabida.cl{u}</loc></url>\n'
sitemap += '</urlset>\n'
(ROOT/'sitemap.xml').write_text(sitemap, encoding='utf-8')

# audit file
report = '''# Auditoría breve vs estrategia

## Qué se mantiene
- Hero visual base del home y su lógica compositiva.
- Sistema visual existente: cards, spacing, gradientes, CTA float, header y footer.
- Tono institucional "Equipo de estudiodecabida.cl".
- Páginas SEO/comuna existentes que ya aportan cobertura.

## Qué se mejora
- Home y Precios pasan de 3 planes a 2 ofertas principales.
- Se empuja Comercial primero y destacado; Técnica sigue sólida.
- Se crea página madre /estudio-de-cabida/ como hub real.
- Se crean páginas específicas Técnica / Comercial.
- Se crean landings Ads: /evaluar-terreno/, /antes-de-comprar-terreno/, /cabida-comercial/.
- Se crean páginas soporte: incluye / cómo se hace / técnico vs comercial / ejemplo.
- Se fortalece interlinking y navegación hacia páginas estratégicas.
- Se deja tracking preparado vía dataLayer/gtag hooks sin romper el sitio.

## Qué se elimina o corrige
- Lógica visible antigua de Diagnóstico Exprés / Estudio Estratégico / Cabida Avanzada en Home y Precios.
- Mensajes que podían desalinear la propuesta con Google Ads y la nueva jerarquía comercial.

## Confirmaciones
- Se respetó Visual-First Preservation Mode: no se rehízo el sistema visual ni se tocó el hero del home fuera de copy y estructura comercial.
- El sitio no se empobreció: se amplió arquitectura, contenido e interlinking sin simplificarlo de forma destructiva.
'''
(ROOT/'AUDITORIA-CAMBIOS.md').write_text(report, encoding='utf-8')
