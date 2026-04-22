from pathlib import Path
from urllib.parse import quote
import shutil, html

ROOT = Path('/mnt/data/sitefinal')
SRC = Path('/mnt/data/sitework')
if ROOT.exists():
    shutil.rmtree(ROOT)
shutil.copytree(SRC, ROOT)

BASE='https://estudiodecabida.cl'
PHONE='56976052356'

def wa(msg):
    return f'https://wa.me/{PHONE}?text={quote(msg)}'

def read_css():
    return ''


def header(active='', wa_link=None):
    wa_link = wa_link or wa('Hola, estoy evaluando un terreno y quiero revisar si conviene antes de invertir.')
    cls=lambda n: 'active' if active==n else ''
    return f'''<header class="siteHeader">
  <div class="wrap siteHeader__inner">
    <a class="brand" href="/" aria-label="Ir a la portada de estudiodecabida.cl">
      <span class="brand__top">Equipo de</span>
      <span class="brand__name">estudiodecabida.cl</span>
    </a>
    <nav class="nav" aria-label="Principal"><a href="/estudio-de-cabida/" class="{cls('servicio')}">Servicio</a><a href="/precios/" class="{cls('precios')}">Precios</a><a href="/casos/" class="{cls('casos')}">Casos</a><a href="/contacto/" class="{cls('contacto')}">Contacto</a></nav>
    <a class="btn btn--primary siteHeader__cta" href="{wa_link}" target="_blank" rel="noopener" data-track="whatsapp_click" data-track-label="header_cta">Evaluar terreno</a>
    <button class="siteHeader__toggle" type="button" data-menu-toggle aria-label="Abrir menú" aria-expanded="false">☰</button>
  </div>
  <div class="wrap">
    <div class="mobileMenu" data-mobile-menu>
      <a href="/estudio-de-cabida/">Servicio</a><a href="/precios/">Precios</a><a href="/casos/">Casos</a><a href="/contacto/">Contacto</a>
      <a class="btn btn--primary" href="{wa_link}" target="_blank" rel="noopener" data-track="whatsapp_click" data-track-label="mobile_header_cta">Evaluar terreno</a>
    </div>
  </div>
</header>'''


def footer(wa_link=None):
    wa_link = wa_link or wa('Hola, estoy evaluando un terreno y quiero revisar si conviene antes de invertir.')
    return f'''</main>
<footer class="footer">
<div class="wrap footer__inner">
<div class="footer__brand">
<div class="footer__title">Equipo de estudiodecabida.cl</div>
<p class="small">Confirmamos si un terreno sostiene o no la decisión que tienes delante.</p>
<div class="footer__meta">
<span>Santiago, Chile</span>
<span><a href="{wa_link}" rel="noopener" target="_blank" data-track="whatsapp_click" data-track-label="footer_cta">Envíanos el terreno</a></span>
<span>Dirección, rol o CIP. Respuesta rápida por WhatsApp.</span>
</div>
</div>
<div class="footer__cols">
<div>
<div class="footer__heading">Servicio</div>
<ul><li><a href="/estudio-de-cabida/">Servicio principal</a></li><li><a href="/estudio-de-cabida-comercial/">Cabida comercial</a></li><li><a href="/estudio-de-cabida-tecnica/">Cabida técnica</a></li><li><a href="/precios/">Precios</a></li></ul>
</div>
<div>
<div class="footer__heading">Guías clave</div>
<ul><li><a href="/antes-de-comprar-terreno/">Antes de comprar un terreno</a></li><li><a href="/como-leer-un-cip/">Cómo leer un CIP</a></li><li><a href="/que-puedo-construir/">Qué puedo construir en mi terreno</a></li><li><a href="/estudio-tecnico-vs-comercial/">Técnica vs Comercial</a></li></ul>
</div>
<div>
<div class="footer__heading">Comunas</div>
<ul><li><a href="/comunas/">Por comuna</a></li><li><a href="/comunas/region-metropolitana/">Región Metropolitana</a></li><li><a href="/comunas/las-condes/">Las Condes</a></li><li><a href="/comunas/providencia/">Providencia</a></li><li><a href="/comunas/vitacura/">Vitacura</a></li><li><a href="/comunas/lo-barnechea/">Lo Barnechea</a></li></ul>
</div>
</div>
</div>
</footer>
<a aria-label="Abrir WhatsApp" class="waFloat" href="{wa_link}" rel="noopener" target="_blank" data-track="whatsapp_click" data-track-label="floating_whatsapp">
<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M20.52 3.48A11.8 11.8 0 0 0 12.1 0C5.58 0 .28 5.3.28 11.82c0 2.08.55 4.11 1.58 5.89L0 24l6.48-1.7a11.8 11.8 0 0 0 5.62 1.43h.01c6.52 0 11.82-5.3 11.82-11.82 0-3.16-1.23-6.13-3.41-8.43Zm-8.42 18.25h-.01a9.83 9.83 0 0 1-5-1.37l-.36-.22-3.85 1.01 1.03-3.75-.24-.38A9.8 9.8 0 0 1 2.28 11.82C2.28 6.4 6.68 2 12.1 2c2.62 0 5.08 1.02 6.93 2.87a9.74 9.74 0 0 1 2.88 6.95c0 5.42-4.4 9.91-9.81 9.91Zm5.38-7.37c-.29-.14-1.71-.84-1.98-.94-.26-.1-.45-.14-.64.15-.19.29-.74.94-.91 1.13-.17.19-.34.22-.63.07-.29-.14-1.2-.44-2.29-1.41-.85-.76-1.42-1.7-1.58-1.99-.17-.29-.02-.45.12-.59.13-.13.29-.34.43-.5.14-.17.19-.29.29-.48.1-.19.05-.36-.02-.5-.07-.14-.64-1.55-.88-2.13-.23-.56-.47-.49-.64-.49-.16-.01-.35-.01-.54-.01s-.5.07-.76.36c-.26.29-1 1-1 2.45s1.03 2.85 1.17 3.05c.14.19 2.02 3.08 4.89 4.32.68.29 1.21.47 1.63.6.69.22 1.31.19 1.8.12.55-.08 1.71-.7 1.95-1.37.24-.67.24-1.25.17-1.37-.07-.12-.26-.19-.55-.34Z"></path></svg>
</a>
<script src="/js/main.js"></script>
</body>
</html>'''


def head(title, desc, canonical, og, active='', page_type='general'):
    return f'''<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/><title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"/><meta name="robots" content="index, follow, max-image-preview:large"/><link rel="canonical" href="{BASE}{canonical}"/><meta property="og:type" content="website"/><meta property="og:site_name" content="estudiodecabida.cl"/><meta property="og:title" content="{html.escape(title)}"/><meta property="og:description" content="{html.escape(desc)}"/><meta property="og:url" content="{BASE}{canonical}"/><meta property="og:image" content="{BASE}{og}"/><meta name="twitter:card" content="summary_large_image"/><meta name="theme-color" content="#0f1722"/><link href="/assets/favicon.png" rel="icon" type="image/png"/><link href="/assets/favicon.png" rel="apple-touch-icon"/><link href="/css/style.css" rel="stylesheet"/><link href="/css/home-hero.css" rel="stylesheet"/></head><body class="{'internal-page' if canonical != '/' else ''}" data-page-type="{page_type}">{header(active)}<main class="page">'''


def pills_html(pills):
    return ''.join(f'<span>{html.escape(p)}</span>' for p in pills)


def home_hero(kicker,title,lead,wa_link,cta2_text,cta2_href):
    return f'''<div class="wrap wrap--hero"><section class="homeHeroSection"><div class="homeHero" aria-labelledby="page-hero-title"><div class="homeHero__bg" aria-hidden="true"><img class="homeHero__art" src="/assets/images/hero-home.webp" alt="" /></div><div class="homeHero__inner"><div class="homeHero__copy"><div class="homeHero__kicker"><span class="dot"></span> {kicker}</div><h1 id="page-hero-title">{title}</h1><p class="homeHero__lead">{lead}</p><p class="muted" style="margin-top:0">Después de comprar, ya no puedes corregir la decisión.</p><p class="muted" style="margin-top:-10px">Una zona puede permitir algo. Eso no significa que tu terreno lo soporte.</p><div class="homeHero__actions"><a class="btn btn--primary" href="{wa_link}" target="_blank" rel="noopener" data-track="whatsapp_click" data-track-label="hero_primary">Envíanos el terreno y lo revisamos</a><a class="btn btn--ghost" href="{cta2_href}" data-track="cta_click" data-track-label="hero_secondary">{cta2_text}</a></div><div class="formHelp" style="margin-top:14px">Dirección, rol o CIP. Respuesta rápida por WhatsApp.</div><div class="homeHero__trust">{pills_html(['Antes de comprar','Antes de ofertar','Antes de diseñar','Antes de comprometer capital'])}</div></div><div class="homeHero__panelWrap"><div class="homeHero__badge">Certeza normativa</div><div class="homeHero__panel"><div class="homeHero__panelHead"><span class="homeHero__panelLabel">Base de decisión antes de invertir</span><strong>Menos intuición. Más claridad normativa.</strong></div><div class="homeHero__panelGrid"><article class="homeHeroCard"><span class="homeHeroCard__eyebrow">Qué se puede hacer</span><strong>Uso de suelo y compatibilidades reales</strong><p>Evita asumir programas que la norma no admite o condiciona.</p></article><article class="homeHeroCard"><span class="homeHeroCard__eyebrow">Qué no conviene asumir</span><strong>Altura, constructibilidad y límites críticos</strong><p>Aterriza el potencial antes de prometer metros o rentabilidad.</p></article><article class="homeHeroCard"><span class="homeHeroCard__eyebrow">Riesgos</span><strong>Restricciones que cambian el negocio</strong><p>Detecta afectaciones o condiciones que pueden bajar el valor real del terreno.</p></article><article class="homeHeroCard homeHeroCard--accent"><span class="homeHeroCard__eyebrow">Decisión</span><strong>Avanzar, renegociar o descartar</strong><p>La cabida ordena la siguiente jugada con más criterio y menos ruido.</p></article></div></div></div></div></div></section>'''


def internal_hero(asset,kicker,title,lead,pills,wa_link,cta1='Envíanos el terreno y lo revisamos',cta2=('Ver precios','/precios/'), micro='Dirección, rol o CIP. Respuesta rápida por WhatsApp.'):
    trust = f'<div class="homeHero__trust">{pills_html(pills)}</div>' if pills else ''
    return f'''<div class="wrap wrap--hero"><section class="homeHeroSection"><div class="homeHero" aria-labelledby="page-hero-title"><div class="homeHero__bg" aria-hidden="true"><img class="homeHero__art" src="{asset}" alt="" /></div><div class="homeHero__inner"><div class="homeHero__copy"><div class="homeHero__kicker"><span class="dot"></span> {kicker}</div><h1 id="page-hero-title">{title}</h1><p class="homeHero__lead">{lead}</p>{trust}<div class="homeHero__actions"><a class="btn btn--primary" href="{wa_link}" target="_blank" rel="noopener" data-track="whatsapp_click" data-track-label="hero_primary">{cta1}</a><a class="btn btn--ghost" href="{cta2[1]}" data-track="cta_click" data-track-label="hero_secondary">{cta2[0]}</a></div><div class="formHelp" style="margin-top:14px">{micro}</div></div></div></div></section><div class="wrap">'''


def section(title, lead=None, eyebrow=None, content=''):
    ew = f'<p class="eyebrow">{eyebrow}</p>' if eyebrow else ''
    lead_html = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<section class="section"><div class="section__head"><div>{ew}<h2>{title}</h2>{lead_html}</div></div>{content}</section>'


def cards_grid(items, cols=3):
    cls = 'grid3' if cols==3 else 'grid2'
    html_items=[]
    for it in items:
        title = it['title']; text=it['text']; icon=it.get('icon'); eyebrow=it.get('eyebrow')
        parts=['<article class="card card--padded">']
        if icon: parts.append(f'<div class="iconBox">{icon}</div>')
        if eyebrow: parts.append(f'<p class="eyebrow" style="margin-bottom:10px">{eyebrow}</p>')
        parts.append(f'<h3>{title}</h3><p class="muted">{text}</p></article>')
        html_items.append(''.join(parts))
    return f'<div class="{cls}">' + ''.join(html_items) + '</div>'


def offer_cards(home=False):
    sec_title='No estás eligiendo un plan. Estás definiendo cuánto riesgo quieres asumir.' if home else 'Qué incluye cada alcance cuando la decisión importa.'
    lead='Ambos estudios sirven para decidir. La diferencia está en cuánto necesitas profundizar la lectura y cuánto necesitas comunicarla cuando la inversión no se juega solo en tu cabeza.' if home else 'Los dos alcances sirven para decidir. La diferencia está en cuánto necesitas profundizar la lectura y cuánto necesitas comunicarla cuando hay inversión, terceros o comparación entre oportunidades.'
    return f'''<section class="section"><div class="section__head"><div><p class="eyebrow">Alcances</p><h2>{sec_title}</h2><p class="lead">{lead}</p></div></div><div class="grid2"><article class="priceCard priceCard--featured has-badge"><div class="priceCard__topbar"><div class="pill">Desde $890.000</div><div class="priceCard__badge">Más recomendado</div></div><div class="priceCard__name">Estudio de Cabida Comercial</div><p class="muted">Para decisiones donde hay inversión relevante, comparación entre oportunidades o terceros que necesitan entender la jugada.</p><ul class="list list--compact"><li>Todo lo de la Técnica</li><li>Visualización del potencial real</li><li>Al menos una imagen tipo render conceptual</li><li>Visualizaciones adicionales según caso</li><li>Reunión de revisión</li></ul><p class="muted"><strong>Es el que eligen quienes no pueden equivocarse.</strong></p><div class="note"><strong>Desde $890.000</strong><br/>La mayoría de los casos cae entre $890.000 y $1.490.000.</div><div class="hero__actions"><a class="btn btn--primary" href="{wa('Hola, quiero cotizar un Estudio de Cabida Comercial para un terreno.')}" target="_blank" rel="noopener">Cotizar Comercial</a><a class="btn" href="/estudio-de-cabida-comercial/">Ver alcance</a></div></article><article class="priceCard"><div class="priceCard__topbar"><div class="pill">Desde $490.000</div><div class="priceCard__badge" style="background:#eef5ff;color:#3f6eb4">Para validar rápido</div></div><div class="priceCard__name">Estudio de Cabida Técnica</div><p class="muted">Para validar si el terreno tiene sentido antes de profundizar o encargar más trabajo.</p><ul class="list list--compact"><li>Análisis normativo aplicado</li><li>Revisión de CIP, zonificación y restricciones</li><li>Cuadros de superficies</li><li>Esquemas normativos y volumétricos simples</li><li>Reunión de revisión</li></ul><p class="muted"><strong>Suficiente para decidir. Sin pagar por capas que todavía no necesitas.</strong></p><div class="note"><strong>Desde $490.000</strong><br/>La mayoría de los casos cae entre $490.000 y $790.000.</div><div class="hero__actions"><a class="btn btn--primary" href="{wa('Hola, quiero cotizar un Estudio de Cabida Técnica para un terreno.')}" target="_blank" rel="noopener">Cotizar Técnica</a><a class="btn" href="/estudio-de-cabida-tecnica/">Ver alcance</a></div></article></div></section>'''


def faq(items):
    ds=''.join(f'<details class="faqItem" {"open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i,(q,a) in enumerate(items))
    return f'<section class="section"><div class="section__head"><div><p class="eyebrow">FAQ</p><h2>Preguntas que conviene despejar antes de avanzar.</h2></div></div><div class="faqList">{ds}</div></section>'


def cta_final(title,text,wa_link, secondary=None):
    sec = f'<section class="section ctaBand"><div><p class="eyebrow">Siguiente paso</p><h2>{title}</h2><p class="lead">{text}</p></div><div class="hero__actions"><a class="btn btn--primary" href="{wa_link}" target="_blank" rel="noopener">Envíanos el terreno y lo revisamos</a>'
    if secondary:
        sec += f'<a class="btn" href="{secondary[1]}">{secondary[0]}</a>'
    sec += '</div></section></div>'
    return sec


def write(rel, html_text):
    path = ROOT/rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html_text, encoding='utf-8')

# PAGE GENERATORS
home_wa = wa('Hola, estoy evaluando un terreno y quiero revisar si conviene antes de invertir.')
home = head('Estudio de cabida en Santiago | Confirma si un terreno conviene antes de invertir','Estudio de cabida para inversión inmobiliaria en Santiago. Revisamos CIP, normativa urbana, restricciones y potencial real del predio antes de comprar, ofertar o desarrollar.','/','/assets/images/hero-home.webp','', 'home')
home += home_hero('Estudio de cabida para inversión inmobiliaria','Confirma si un terreno conviene antes de invertir.','Leemos CIP, normativa urbana, restricciones y potencial real del predio para definir si conviene avanzar, ajustar o descartar antes de comprometer capital.', home_wa, 'Ver qué incluye el estudio','/estudio-de-cabida/')
home += section('Hay operaciones que se ven buenas… hasta que el terreno se lee bien.','La mayoría de los errores no está en el precio. Está en asumir un potencial que el predio no sostiene.','Primer scroll', cards_grid([
    {'title':'Metros que no caben','text':'Se proyectan superficies que se achican cuando entran en juego distanciamientos, forma del predio, ocupación y restricciones reales. Lo que parecía rentable puede dejar de serlo.'},
    {'title':'Zonas bien leídas, terrenos mal leídos','text':'La zona puede dar una primera impresión correcta y aun así esconder una mala lectura del terreno específico. Ahí es donde el mercado suele inflar expectativas.'},
    {'title':'Potenciales inflados','text':'Lo que se ve atractivo en una conversación, una publicación o un render no siempre resiste una lectura seria. Una compra mal leída se vuelve cara muy rápido.'},
    {'title':'Restricciones que aparecen tarde','text':'Expropiaciones, afectaciones, compatibilidades, geometrías difíciles y condiciones urbanas aparecen justo cuando corregir ya cuesta plata y tiempo.'},
]) + '<p class="lead" style="margin-top:18px">No es falta de información. Es falta de una lectura aplicada.</p>')
home += section('No es un informe. Es una decisión bien tomada.','La normativa se puede encontrar. Lo difícil es leerla contra un terreno real, un objetivo concreto y una inversión que todavía se puede cuidar.','Qué hacemos exactamente', cards_grid([
    {'icon':'01','title':'Qué restricciones afectan el terreno','text':'Uso de suelo, altura, constructibilidad, ocupación, distanciamientos, afectaciones y condiciones que cambian la viabilidad. Lo que no cabe en la norma tampoco cabe en el negocio.'},
    {'icon':'02','title':'Qué potencial real tiene','text':'No modelamos un proyecto ideal. Evaluamos lo que realmente se puede ejecutar. El terreno real siempre termina corrigiendo la intuición.'},
    {'icon':'03','title':'Qué decisión cambia','text':'La cabida ordena si conviene avanzar, renegociar, descartar o profundizar. Cuando la decisión todavía se puede cambiar, la cabida vale más.'},
],3))
home += section('Este análisis no sirve igual en cualquier etapa.','Sirve más cuando la decisión todavía se puede cambiar.','Cuándo más valor entrega', cards_grid([
    {'title':'Antes de comprar','text':'Valida si el terreno sostiene la idea y el valor que aparenta tener. Lo que parece una buena oportunidad no siempre resiste una lectura seria.'},
    {'title':'Antes de ofertar','text':'Permite ajustar la oferta contra restricciones y potencial real. Una mala lectura acá se paga dos veces: en el precio y en la salida.'},
    {'title':'Antes de diseñar','text':'Evita que el proyecto arranque sobre supuestos débiles. Antes de dibujar metros, conviene medir restricciones.'},
    {'title':'Antes de presentar una oportunidad','text':'Ordena un caso frente a socios, clientes o inversionistas. Donde el mercado promete, la norma pone límites.'},
],2))
home += offer_cards(home=True)
home += section('Lo que parecía obvio deja de serlo.',None,'Qué cambia después de una buena cabida', cards_grid([
    {'title':'El terreno real reemplaza la intuición','text':'La conversación deja de depender de lo que parecía posible y pasa a depender de lo que el predio sostiene de verdad.'},
    {'title':'La comparación entre opciones se vuelve seria','text':'Dos terrenos con precios parecidos pueden tener valores reales muy distintos cuando se leen bien. El valor del terreno cambia cuando cambia su lectura.'},
    {'title':'Lo que no conviene comprar también es una buena decisión','text':'Frenar a tiempo no es perder una oportunidad. Es evitar una mala.'},
    {'title':'La siguiente etapa se ordena mejor','text':'Si el terreno tiene sentido, el siguiente paso parte sobre una base más limpia. Si no lo tiene, todavía estás a tiempo.'},
    {'title':'La oportunidad se defiende mejor','text':'Cuando no basta con entender el terreno, también necesitas defender la oportunidad. Ahí cambia la conversación.'},
],3))
home += section('Casos donde una buena cabida cambió la operación.','', 'Casos resumidos', cards_grid([
    {'title':'Lo Barnechea / línea de expropiación','text':'Parecía un terreno apto para varias viviendas. Lo que apareció fue una afectación que reducía de forma importante el aprovechamiento real. La compra dejó de tener el atractivo que parecía tener.'},
    {'title':'Santiago Centro / bodega + oficinas','text':'Parecía un programa mixto razonable. Lo que apareció fue que la mezcla útil debía ajustarse para que el caso cerrara mejor. El proyecto seguía vivo, pero con otra estrategia.'},
    {'title':'Lo Barnechea / conjunto armónico','text':'Parecía una condición secundaria. Lo que apareció fue que restricciones y beneficios heredados cambiaban la lectura completa. La decisión pasó a depender de una interpretación más fina.'},
],3) + '<div style="margin-top:18px"><a class="btn" href="/casos/">Ver casos reales</a></div>')
home += section('Guías para entender mejor antes de arriesgar mal.','Sirven para ordenar preguntas. Cuando hay un terreno real sobre la mesa, conviene revisarlo aplicado.','Guías', '<div class="relatedLinks"><a class="card card--padded" href="/antes-de-comprar-terreno/"><h3>Antes de comprar un terreno</h3><p class="muted">Revisar guía</p></a><a class="card card--padded" href="/como-leer-un-cip/"><h3>Cómo leer un CIP</h3><p class="muted">Revisar guía</p></a><a class="card card--padded" href="/que-puedo-construir/"><h3>Qué puedo construir en mi terreno</h3><p class="muted">Revisar guía</p></a><a class="card card--padded" href="/estudio-tecnico-vs-comercial/"><h3>Técnica vs Comercial</h3><p class="muted">Comparar alcances</p></a><a class="card card--padded" href="/como-se-hace-un-estudio-de-cabida/"><h3>Cómo se hace una buena cabida</h3><p class="muted">Ver proceso</p></a><a class="card card--padded" href="/comunas/"><h3>Estudio de cabida por comuna</h3><p class="muted">Ver comunas</p></a></div>')
home += faq([
    ('¿Qué es un estudio de cabida?','Es una lectura normativa y estratégica que aterriza qué se puede hacer en un terreno, qué restricciones lo afectan y qué decisión tiene sentido antes de invertir.'),
    ('¿Sirve antes de comprar un terreno?','Sí. Ahí es donde más valor entrega, porque la decisión todavía se puede corregir.'),
    ('¿Garantiza aprobación municipal?','No. No reemplaza permisos ni garantiza aprobación. Sí ordena mucho mejor la decisión y reduce errores de lectura.'),
    ('¿Cuál alcance conviene?','Cuando hay inversión relevante, comparación entre opciones o necesidad de mostrar el caso a terceros, el Comercial suele ser la mejor lectura.'),
    ('¿Qué antecedentes hacen falta?','Dirección, rol o CIP suele bastar para partir. Si hay planos o antecedentes adicionales, mejor.'),
    ('¿Cuánto tarda normalmente?','Depende del alcance y del caso. Se orienta rápido por WhatsApp según los antecedentes iniciales.'),
])
home += cta_final('Si ya estás evaluando un terreno, este es el momento.','Después de comprar, ya no estás validando una decisión. Estás corrigiéndola. Lo caro no es el estudio. Lo caro es equivocarse con el terreno.', home_wa, ('Ver qué incluye el estudio','/estudio-de-cabida/'))
home += footer(home_wa)
write('index.html', home)

# service page
def service_like(path,title,desc,h1,lead,pills,wa_msg,sections,active='servicio',asset='/assets/images/hero-estudio-de-cabida.webp',cta2=('Ver precios','/precios/'),page_type='service'):
    wa_link=wa(wa_msg)
    html_doc = head(title,desc,path,asset,active,page_type)
    html_doc += internal_hero(asset,'Servicio principal' if active=='servicio' else 'Guía de apoyo',h1,lead,pills,wa_link,'Envíanos el terreno y lo revisamos',cta2,'Dirección, rol o CIP. Respuesta rápida por WhatsApp.')
    html_doc += ''.join(sections)
    html_doc += footer(wa_link)
    write(path.strip('/') + '/index.html' if path != '/' else 'index.html', html_doc)

service_sections = [
section('El problema no suele estar en la norma. Suele estar en cómo se la lee.','Una zona puede permitir algo. Pero cada terreno tiene condiciones que cambian completamente la lectura. Ahí se inflan metros, se malinterpretan usos, se subestiman restricciones y se compra con una seguridad que no existe.','Qué problema resuelve', '<p class="lead">No basta con mirar la zona. Hay que leer lo que cambia la decisión.</p>'),
section('Lo que el mercado suele sobreestimar.',None,'Qué se suele leer mal', cards_grid([
    {'title':'Potencial por zona','text':'Se asume que si la zona admite algo, el terreno también lo sostiene en la práctica.'},
    {'title':'Metros y cabida útil','text':'Se promete superficie sin aterrizar distanciamientos, forma, ocupación y condicionantes reales.'},
    {'title':'Restricciones menos obvias','text':'Afectaciones, expropiaciones, compatibilidades, accesos o condiciones especiales entran tarde y cambian el caso completo.'},
    {'title':'Capacidad de defender la oportunidad','text':'Una cosa es entender el terreno. Otra muy distinta es poder mostrar por qué la lectura resiste.'},
],2)),
section('Qué se revisa cuando la lectura tiene que servir de verdad.','No es un listado de normas sueltas. Es una lectura cruzada entre CIP, normativa urbana, geometría del predio, restricciones y objetivo del caso.','Qué revisa el estudio', cards_grid([
    {'title':'Uso de suelo y compatibilidades','text':'Lo que admite o no admite la norma para el objetivo que tienes delante.'},
    {'title':'Altura, constructibilidad y ocupación','text':'Los parámetros que suelen inflar expectativas cuando se leen mal.'},
    {'title':'Distanciamientos y capacidad real del predio','text':'Cómo la forma y el cuerpo del terreno alteran la cabida útil.'},
    {'title':'Expropiaciones, afectaciones y condiciones especiales','text':'Restricciones que pueden cambiar precio, programa o viabilidad.'},
    {'title':'Potencial razonable según el objetivo','text':'Lo que realmente se puede ejecutar, no lo que sería ideal dibujar.'},
    {'title':'Siguiente paso recomendado','text':'Avanzar, ajustar, descartar o profundizar con otra capa de trabajo.'},
],3) + '<p class="lead" style="margin-top:18px">No basta con tener el documento. Hay que leer lo que cambia la decisión.</p>'),
section('Qué entrega realmente la cabida.',None,'Qué recibes', cards_grid([
    {'title':'Lectura normativa aplicada','text':'Una lectura del terreno específico, no una lista fría de valores.'},
    {'title':'Restricciones críticas y alertas','text':'Alertas que pueden alterar precio, programa o viabilidad.'},
    {'title':'Potencial razonable','text':'Una estimación seria según norma y condición real del predio.'},
    {'title':'Conclusión útil','text':'Avanzar, ajustar, descartar o profundizar sobre una base más limpia.'},
],2) + '<p class="lead" style="margin-top:18px">No es un informe. Es una decisión bien tomada.</p>'),
offer_cards(home=False),
section('Casos reales donde la lectura cambió la jugada.',None,'Casos mini', cards_grid([
    {'title':'Varias viviendas que ya no cabían igual','text':'Un terreno parecía apto para varias viviendas. Una afectación cambió de forma importante su valor real.'},
    {'title':'Programa mixto que seguía vivo, pero no igual','text':'Un programa mixto parecía viable tal como venía. La cabida mostró que seguía vivo, pero no bajo la misma lógica.'},
    {'title':'Condición urbana heredada que sí importaba','text':'Una condición urbana heredada parecía secundaria. Terminó redefiniendo restricciones y oportunidades.'},
],3) + '<div style="margin-top:18px"><a class="btn" href="/casos/">Ver casos reales</a></div>'),
faq([
    ('¿Qué diferencia hay entre revisar un CIP y hacer una cabida?','El CIP entrega información base. La cabida cruza esa información con el terreno real y la transforma en una lectura que sirve para decidir.'),
    ('¿Sirve si todavía no tengo todo resuelto?','Sí. De hecho, sirve más cuando la decisión todavía se puede mover.'),
    ('¿La cabida reemplaza un permiso?','No. Ordena una base seria para decidir si vale la pena seguir.'),
    ('¿Conviene pedirla antes de comprar?','Sí. Después de comprar, el margen de corrección es mucho menor.'),
]),
cta_final('Si el terreno ya está sobre la mesa, conviene leerlo bien antes de seguir cargándole tiempo, plata o expectativas.','Dirección, rol o CIP. Respuesta rápida por WhatsApp.', wa('Hola, quiero entender qué estudio conviene para evaluar un terreno.'), ('Ver precios','/precios/'))
]
service_like('/estudio-de-cabida/','Servicio de estudio de cabida | Qué hace cuando la decisión importa','Qué hace un estudio de cabida y por qué conviene pedirlo antes de invertir. CIP, normativa urbana, restricciones y potencial real aplicados al terreno.','Qué hace un estudio de cabida cuando la decisión importa de verdad.','No revisa solo normativa. Traduce el terreno en una lectura aplicable: qué se puede hacer, qué no, y si conviene avanzar antes de invertir más tiempo, plata o expectativas.',['Lectura aplicada','Antes de comprar','Decisión con terceros'],'Hola, quiero entender qué estudio conviene para evaluar un terreno.',service_sections)

# prices
precios_wa=wa('Hola, quiero cotizar un Estudio de Cabida Comercial para un terreno.')
precios = head('Precios estudio de cabida | Cabida Técnica y Comercial','Rangos orientativos para estudio de cabida Técnica y Comercial. Define qué nivel de lectura conviene según la inversión, la urgencia y la decisión.','/precios/','/assets/images/hero-estudio-de-cabida.webp','precios','pricing')
precios += internal_hero('/assets/images/hero-estudio-de-cabida.webp','Precios','No estás comprando un estudio. Estás definiendo cuánto riesgo quieres asumir.','Los dos alcances sirven para decidir. La diferencia está en cuánto necesitas profundizar la lectura y cuánto necesitas comunicarla cuando hay inversión, terceros o comparación entre oportunidades.',['Más recomendado','Para inversión seria','Para validar rápido'],precios_wa,'Cotizar Comercial',('Cotizar Técnica',wa('Hola, quiero cotizar un Estudio de Cabida Técnica para un terreno.')),'Con dirección, rol, comuna y objetivo, se orienta rápido el alcance correcto.')
precios += section('El precio importa. La lectura que te falta, más.', 'Lo caro no es el estudio. Lo caro es equivocarse con el terreno. Por eso la decisión no pasa solo por cuánto cuesta el análisis, sino por cuánta incertidumbre te conviene despejar antes de avanzar.','Intro')
precios += offer_cards(home=False)
precios += section('Qué cambia de verdad entre una y otra.',None,'Comparación narrativa', cards_grid([
    {'title':'Cuándo conviene la Comercial','text':'Cuando el terreno entra en comparación con otras alternativas, cuando la inversión es relevante o cuando hay que explicar y defender mejor la oportunidad.'},
    {'title':'Cuándo conviene la Técnica','text':'Cuando la prioridad es validar rápido si el terreno sostiene o no la decisión inicial.'},
    {'title':'Qué cambia frente a terceros','text':'La Técnica ordena la lectura. La Comercial la hace más defendible.'},
    {'title':'Qué cambia en profundidad visual','text':'La Técnica aterriza. La Comercial además muestra.'},
    {'title':'Qué cambia en velocidad de decisión','text':'Ambas aceleran una decisión mejor leída. La Comercial reduce mejor las dudas cuando hay más ojos mirando.'},
],2))
precios += section('El precio exacto no depende solo del tamaño del terreno.','Influyen la complejidad normativa, la cantidad de incertidumbre a despejar, el nivel de profundidad requerido, la necesidad de visualización y el objetivo concreto del caso. Depende de cuánta incertidumbre hay que despejar y cuánta lectura necesita la decisión.','Qué define el precio')
precios += faq([
    ('¿Por qué trabajan con rangos?','Porque no todos los terrenos exigen el mismo nivel de lectura ni el mismo nivel de desarrollo visual.'),
    ('¿La Técnica se queda corta?','No. Sirve bien cuando la decisión inicial es validar si el terreno tiene sentido. La Comercial entra cuando además necesitas mostrar y defender la oportunidad.'),
    ('¿Cuál conviene para una decisión importante?','En escenarios de inversión seria, el Comercial suele ser la lectura más completa.'),
    ('¿Se puede escribir antes de comprar?','Sí. De hecho, ese es uno de los mejores momentos para hacerlo.'),
    ('¿Cuánto demora?','Depende del alcance y del caso. Se orienta rápido con antecedentes básicos.'),
])
precios += cta_final('Con dirección, rol, comuna y una idea breve del objetivo, se puede orientar rápido el alcance correcto.','Si el terreno ya está en evaluación, conviene despejar la incertidumbre antes de que la decisión avance sola.', precios_wa, ('Envíanos el terreno y lo revisamos', wa('Hola, estoy evaluando un terreno y quiero revisar si conviene antes de invertir.')))
precios += footer(precios_wa)
write('precios/index.html', precios)
write('precio/index.html', precios)

# cases
cases_wa = wa('Hola, leí la página y quiero revisar un terreno concreto.')
cases = head('Casos reales de estudio de cabida | Decisiones que cambiaron a tiempo','Casos reales donde una buena cabida cambió la decisión: afectaciones, restricciones, programa mixto y lectura aplicada del terreno.','/casos/','/assets/images/hero-estudio-de-cabida.webp','casos','cases')
cases += internal_hero('/assets/images/hero-estudio-de-cabida.webp','Casos reales','Casos donde una buena cabida cambió la decisión.','La cabida no siempre entrega un sí o un no. Muchas veces desmonta una expectativa, corrige una estrategia o evita una compra que parecía buena.',['Casos reales','Lectura aplicada','Decisión con terceros'],cases_wa,'Envíanos el terreno y lo revisamos',('Ver precios','/precios/'),'Si ya estás evaluando un terreno, mejor escribir antes de mover la decisión.')
for t, body in [
('Lo Barnechea / línea de expropiación','<p><strong>Lo que parecía</strong><br/>Un terreno atractivo para varias viviendas, con una lectura preliminar suficientemente buena como para avanzar.</p><p><strong>Lo que apareció al leerlo bien</strong><br/>Una línea de expropiación alteraba de forma relevante el aprovechamiento real del predio.</p><p><strong>Qué cambió</strong><br/>El potencial dejó de justificar el entusiasmo inicial.</p><p><strong>Decisión final</strong><br/>La operación perdió atractivo y la lectura del caso cambió antes de comprometerse más.</p><p><strong>Qué demuestra</strong><br/>Una afectación tardía puede destruir valor que antes parecía evidente.</p>'),
('Santiago Centro / bodega + oficinas','<p><strong>Lo que parecía</strong><br/>Un proyecto mixto razonable tal como estaba planteado.</p><p><strong>Lo que apareció al leerlo bien</strong><br/>La mezcla útil del programa necesitaba un ajuste importante para que el caso cerrara mejor.</p><p><strong>Qué cambió</strong><br/>La oportunidad seguía viva, pero no bajo el mismo programa.</p><p><strong>Decisión final</strong><br/>Se reordenó la estrategia en vez de seguir una mala versión del proyecto.</p><p><strong>Qué demuestra</strong><br/>No todos los hallazgos obligan a frenar. A veces el valor está en corregir la jugada a tiempo.</p>'),
('Lo Barnechea / conjunto armónico','<p><strong>Lo que parecía</strong><br/>Una condición urbana heredada que no parecía decisiva para una vivienda.</p><p><strong>Lo que apareció al leerlo bien</strong><br/>Restricciones y beneficios asociados cambiaban de forma relevante la interpretación del predio.</p><p><strong>Qué cambió</strong><br/>La lectura normativa dejó de ser lineal y pasó a exigir otra estrategia.</p><p><strong>Decisión final</strong><br/>El proyecto se redefinió sobre una base más seria.</p><p><strong>Qué demuestra</strong><br/>Hay casos donde el valor no está en una respuesta rápida, sino en una lectura más fina.</p>')]:
    cases += section(t,None,'Caso', f'<article class="card card--padded">{body}</article>')
cases += cta_final('Lo importante no es solo detectar un problema.','A veces el valor está en encontrar una forma más inteligente de avanzar. O en tener una razón sólida para no hacerlo.',cases_wa,('Ver precios','/precios/'))
cases += footer(cases_wa)
write('casos/index.html', cases)

# contact
contact_wa=wa('Hola, quiero enviar un terreno para orientar el siguiente paso.')
contact = head('Evaluar terreno | Enviar dirección, rol o CIP','Envíanos dirección, rol o CIP del terreno. Orientamos rápido el siguiente paso y el alcance que conviene para revisar la oportunidad.','/contacto/','/assets/images/hero-estudio-de-cabida.webp','contacto','contact')
contact += internal_hero('/assets/images/hero-estudio-de-cabida.webp','Contacto','Envíanos el terreno y conversemos antes de que la decisión avance sola.','Con dirección, rol, CIP o incluso una referencia básica, ya se puede orientar el siguiente paso. Cuando el terreno todavía se está evaluando, una buena lectura vale mucho más.',['Respuesta rápida','Antes de comprar','Riesgo alto'],contact_wa,'Escribir por WhatsApp',('Ver precios','/precios/'),'No necesitas tener todo resuelto para escribir. Respuesta dentro del día hábil.')
contact += '<section class="section section--tightTop"><div class="grid2"><div class="formCard"><p class="lead">Si todavía no compras, mejor escribir ahora. Después de comprar, ya no puedes corregir la decisión con el mismo margen.</p><form data-whatsapp-form><div class="formGrid"><div class="field"><label>Tu nombre</label><input type="text" placeholder="Tu nombre"/></div><div class="field"><label>Correo de contacto</label><input type="email" placeholder="Correo de contacto"/></div><div class="field"><label>WhatsApp</label><input type="text" placeholder="WhatsApp"/></div><div class="field"><label>Comuna del terreno</label><input type="text" placeholder="Comuna del terreno"/></div><div class="field"><label>Dirección, rol o identificación del predio</label><input type="text" placeholder="Dirección, rol o identificación del predio"/></div><div class="field"><label>¿Qué estás evaluando?</label><select><option>Comprar terreno</option><option>Ofertar</option><option>Comparar opciones</option><option>Desarrollar proyecto</option><option>Presentar a socios o inversionistas</option><option>Otro</option></select></div><div class="field"><label>¿Qué tienes hoy?</label><select><option>Dirección</option><option>Rol</option><option>CIP</option><option>Plano</option><option>Ninguno todavía</option></select></div></div><div class="formHelp">No necesitas tener todo resuelto para escribir. Si ya hay un terreno sobre la mesa, se puede orientar el siguiente paso.</div><div style="margin-top:14px"><a class="btn btn--primary btn--full" href="'+contact_wa+'" target="_blank" rel="noopener">Enviar evaluación</a></div><p class="formHelp" style="margin-top:12px">Respuesta dentro del día hábil.</p></form></div><div class="stack"><article class="card card--padded"><h3>Qué ayuda a partir más rápido</h3><ul class="list"><li>Dirección, rol o CIP</li><li>Comuna del terreno</li><li>Objetivo principal</li><li>Plazo o urgencia</li></ul></article><article class="card card--padded"><h3>Mensaje de cierre</h3><p class="muted">Lo que parece una buena oportunidad no siempre resiste una lectura seria. Si el terreno ya está en conversación, conviene revisarlo antes de comprometer más tiempo, plata o expectativas.</p></article></div></div></section>'
contact += footer(contact_wa)
write('contacto/index.html', contact)

# Guides and SEO satellite

guides = []

def guide(path,title,desc,h1,lead,pills,wa_msg,sections,cta2=('Ver servicio','/estudio-de-cabida/')):
    wa_link=wa(wa_msg)
    doc = head(title,desc,path,'/assets/images/hero-estudio-de-cabida.webp','servicio','guide')
    doc += internal_hero('/assets/images/hero-estudio-de-cabida.webp','Guía de apoyo',h1,lead,pills,wa_link,'Envíanos el terreno y lo revisamos',cta2)
    doc += ''.join(sections)
    doc += footer(wa_link)
    write(path.strip('/') + '/index.html', doc)

common_wa='Hola, leí la página y quiero revisar un terreno concreto.'

guide('/antes-de-comprar-terreno/','Antes de comprar un terreno | Qué revisar antes de invertir','Antes de comprar un terreno conviene revisar CIP, normativa urbana, restricciones y potencial real. Lo que se ve atractivo no siempre sostiene la operación.','Antes de comprar un terreno, conviene saber qué manda de verdad sobre él.','Ubicación y precio no bastan. Un terreno puede verse atractivo y aun así sostener bastante menos de lo que parece.',['Antes de comprar','Riesgo alto','Lectura aplicada'],common_wa,[
section('Lo que suele enamorar primero.', 'Buena comuna, precio competitivo, potencial aparente, conversación optimista. Es normal que la primera impresión se construya ahí.'),
section('Lo que suele aparecer después.','Distanciamientos, afectaciones, límites reales del predio, usos mal interpretados o una cabida bastante menor a la imaginada. Lo que parece una buena oportunidad no siempre resiste una lectura seria.'),
section('Lo que cuesta caro leer tarde.','Pagar de más, ofertar sobre una expectativa inflada, diseñar sobre un supuesto débil o comprometerse con un terreno cuyo valor real era otro.'),
section('Qué conviene revisar de verdad.','CIP, normativa urbana, uso de suelo, altura, constructibilidad, distanciamientos, expropiaciones, afectaciones y capacidad real del predio según el objetivo del caso.'),
section('Cómo cambia la compra.','Cuando la lectura es aplicada, la intuición se ordena. A veces confirma la operación. Otras veces la corrige. Y a veces la detiene antes de que se vuelva cara.'),
cta_final('Cuando la decisión todavía se puede cambiar, la cabida vale más.','Dirección, rol o CIP. Respuesta rápida por WhatsApp.',wa(common_wa),('Ver qué incluye el estudio','/estudio-de-cabida/'))
],('Ver qué incluye el estudio','/estudio-de-cabida/'))

guide('/como-leer-un-cip/','Cómo leer un CIP | Qué mirar antes de comprar un terreno','Cómo leer un CIP sin sacar conclusiones apuradas. Qué datos importan, cuáles engañan y por qué el documento no basta por sí solo.','Cómo leer un CIP sin sacar conclusiones apuradas.','El Certificado de Informaciones Previas no vale por sí solo. Vale por cómo se interpreta frente al terreno y al objetivo que se está evaluando.',['CIP','Lectura aplicada','Antes de comprar'],common_wa,[
section('Por qué el CIP suele sobreinterpretarse.','Tener el documento no es lo mismo que entender la decisión. Muchas veces se toma una cifra, una zonificación o una condición aislada y se la convierte en certeza demasiado rápido.'),
section('Qué datos sí pesan.','Uso de suelo, altura, constructibilidad, ocupación, líneas oficiales, afectaciones y cualquier condición que limite la capacidad real del predio.'),
section('Qué datos engañan cuando se leen solos.','Una cifra aislada puede dar una falsa sensación de claridad. Lo mismo pasa cuando se lee la zona sin cruzarla con la forma, accesos, restricciones y objetivo del caso.'),
section('Qué falta para convertir documento en decisión.','Cruzar CIP, normativa urbana, predio real y objetivo concreto. Ahí recién el documento deja de ser un papel y pasa a ser una lectura útil.'),
cta_final('No basta con tener el documento. Hay que leer lo que cambia la decisión.','Dirección, rol o CIP. Respuesta rápida por WhatsApp.',wa(common_wa),('Ver servicio','/estudio-de-cabida/'))
])

guide('/que-puedo-construir/','Qué puedo construir en mi terreno | Qué lo determina de verdad','Qué puedes construir en un terreno depende de uso de suelo, altura, constructibilidad, ocupación, forma del predio y restricciones reales.','Qué puedes construir en un terreno y qué lo determina de verdad.','La respuesta no está en una cifra ni en una intuición. Está en cómo conversan norma, geometría, restricciones y objetivo real del proyecto.',['Uso de suelo','Constructibilidad','Lectura aplicada'],common_wa,[
section('No es solo cuántos pisos o cuántos metros.','La lectura correcta no sale de mirar una sola variable. Sale de entender cómo se cruzan varias restricciones sobre un predio real.'),
section('Variables que realmente mandan.','Uso de suelo, altura, constructibilidad, ocupación, distanciamientos, forma del terreno, afectaciones, expropiaciones, accesos y objetivo del proyecto.'),
section('Qué suele leerse mal.','Se asume que la zona lo resuelve todo, que la constructibilidad se traduce directo en metros útiles o que una idea atractiva ya tiene sustento normativo. El terreno real siempre termina corrigiendo la intuición.'),
section('Qué tiene sentido intentar.','La pregunta importante no es solo qué se puede hacer. Es qué tiene sentido intentar. Ahí cambia la calidad de la decisión.'),
cta_final('No modelamos un proyecto ideal. Evaluamos lo que realmente se puede ejecutar.','Dirección, rol o CIP. Respuesta rápida por WhatsApp.',wa(common_wa),('Cómo leer un CIP','/como-leer-un-cip/'))
],('Cómo leer un CIP','/como-leer-un-cip/'))

guide('/estudio-tecnico-vs-comercial/','Técnica vs Comercial | Qué diferencia hay y cuál conviene','Diferencias entre cabida Técnica y Comercial. Define cuál conviene según la inversión, la claridad requerida y la necesidad de defender la oportunidad.','Técnica vs Comercial: cuál conviene según la decisión que tienes delante.','Las dos opciones sirven. La diferencia está en cuánto necesitas profundizar, visualizar y defender la oportunidad cuando la decisión no es solo tuya.',['Más recomendado','Decisión con terceros','Para validar rápido'],'Hola, quiero cotizar un Estudio de Cabida Comercial para un terreno.',[
section('Qué tienen en común.','Ambas aterrizan normativa, CIP, restricciones y potencial del terreno. Las dos sirven para evitar decisiones basadas en intuición suelta.'),
section('Qué cambia realmente.','La Técnica valida. La Comercial además ordena y muestra mejor la oportunidad. La diferencia real no es “más cosas”. Es cuánto necesitas entender y defender.'),
section('Cuándo conviene cada una.',None,None,cards_grid([
    {'title':'Técnica','text':'Cuando la prioridad es despejar rápido si el terreno tiene o no sentido.'},
    {'title':'Comercial','text':'Cuando hay inversión relevante, comparación entre opciones o terceros que necesitan entender la jugada.'},
    {'title':'Frase clave','text':'El Comercial suele ser la mejor decisión cuando no solo necesitas entender el terreno, sino también mostrarlo con claridad.'},
],3)),
cta_final('La Técnica ordena una decisión. La Comercial la hace más defendible.','Dirección, rol o CIP. Respuesta rápida por WhatsApp.',wa('Hola, quiero cotizar un Estudio de Cabida Comercial para un terreno.'),('Cotizar Técnica',wa('Hola, quiero cotizar un Estudio de Cabida Técnica para un terreno.')))
],('Ver precios','/precios/'))

guide('/como-se-hace-un-estudio-de-cabida/','Cómo se hace un estudio de cabida | Proceso y lectura aplicada','Cómo se construye un estudio de cabida: desde CIP y normativa hasta restricciones, potencial real y decisión de inversión.','Cómo se construye una buena cabida.','No sale de copiar la norma. Sale de cruzarla con un terreno real, una hipótesis concreta y una decisión que todavía se puede cambiar.',['Proceso aplicado','CIP','Lectura aplicada'],common_wa,[
section('Del dato bruto a la lectura aplicada.','Se parte por antecedentes duros: dirección, rol, CIP, zonificación, restricciones y geometría del terreno. Pero el valor no está en recopilar datos. Está en cómo se los cruza.'),
section('Qué se revisa primero.','Normativa urbana, uso de suelo, altura, constructibilidad, ocupación, distanciamientos, afectaciones y condiciones específicas del predio.'),
section('Qué variables cambian la conclusión.','La forma del terreno, la presencia de restricciones menos obvias, el objetivo del proyecto y la distancia entre lo que se quiere hacer y lo que realmente se puede ejecutar.'),
section('Qué diferencia una buena cabida de una lectura superficial.','Una buena cabida no responde rápido por ansiedad. Responde bien porque cruza las variables correctas. No modelamos lo ideal. Evaluamos lo que realmente se puede ejecutar.'),
cta_final('No basta con tener los datos. Hay que leer lo que cambia la decisión.','Dirección, rol o CIP. Respuesta rápida por WhatsApp.',wa(common_wa),('Ver servicio','/estudio-de-cabida/'))
])

guide('/que-incluye-un-estudio-de-cabida/','Qué incluye un estudio de cabida | Lectura aplicada del terreno','Qué se revisa, qué se entrega, qué no incluye y por qué la diferencia entre información y criterio aplicado importa.','Qué incluye un estudio de cabida cuando la decisión todavía se puede cuidar.','No reúne datos por reunir. Ordena información, restricciones y potencial en una lectura útil para decidir.',['Lectura aplicada','Respuesta rápida','Antes de comprar'],common_wa,[
section('Qué se revisa.','CIP, zonificación, uso de suelo, altura, constructibilidad, ocupación, distanciamientos, afectaciones, capacidad real del predio y coherencia entre la idea y la norma.'),
section('Qué se entrega.','Una lectura normativa aplicada, alertas críticas, potencial razonable, conclusión clara y recomendación de siguiente paso. En el Comercial, además, una capa visual para comunicar mejor la oportunidad.'),
section('Qué no incluye.','No reemplaza permisos, no garantiza aprobación municipal y no dibuja un proyecto ideal para forzar una respuesta. Evalúa lo que realmente se puede ejecutar.'),
section('Por qué importa.','La diferencia entre un dato y una decisión no está en el documento. Está en la lectura aplicada.'),
cta_final('Si hay un terreno real sobre la mesa, conviene revisarlo aplicado.','Dirección, rol o CIP. Respuesta rápida por WhatsApp.',wa(common_wa),('Ver precios','/precios/'))
])

guide('/ejemplo-de-estudio-de-cabida/','Ejemplo de estudio de cabida | Cómo se lee y qué decisiones habilita','Cómo se lee un ejemplo de estudio de cabida y qué decisiones ayuda a tomar antes de invertir, ofertar o desarrollar.','Ejemplo de estudio de cabida: cómo se lee y por qué cambia la decisión.','Un buen ejemplo no sirve para admirar un formato. Sirve para entender cómo una lectura ordenada cambia una compra, una oferta o un proyecto.',['Casos reales','Lectura aplicada','Decisión con terceros'],common_wa,[
section('Qué suele contener un ejemplo serio.','Pregunta inicial, lectura normativa aplicada, restricciones críticas, potencial razonable, escenarios y una conclusión que aterriza la decisión.'),
section('Cómo se lee bien.','No como un documento académico. Se lee como una herramienta para responder una pregunta concreta: qué cabe de verdad, qué riesgos pesan y qué decisión cambia.'),
section('Qué decisiones habilita.','Avanzar con más seguridad, renegociar con fundamento, descartar a tiempo o profundizar sobre una base mucho más limpia.'),
section('Qué valor demuestra.','Muestra que el estudio no vive en la teoría. Vive en la calidad de la decisión que deja instalada.'),
cta_final('Cuando un terreno importa, el ejemplo útil es el que termina aterrizando una decisión real.','Dirección, rol o CIP. Respuesta rápida por WhatsApp.',wa(common_wa),('Ver servicio','/estudio-de-cabida/'))
])

# Commune pages
def commune(path,title,desc,h1,lead,pills,wa_msg,local_error,review,when,final_text,cta2=('Ver precios','/precios/')):
    wa_link=wa(wa_msg)
    doc=head(title,desc,path,'/assets/images/hero-estudio-de-cabida.webp','servicio','commune')
    doc += internal_hero('/assets/images/hero-estudio-de-cabida.webp','Cobertura local',h1,lead,pills,wa_link,h1.replace('Estudio de cabida en ','Evaluar terreno en ').replace(' para evaluar terrenos con más criterio.',''),cta2,'Dirección, rol o CIP. Respuesta rápida por WhatsApp.')
    doc += section('Por qué una lectura local cambia la decisión.',local_error,'Contexto local')
    doc += section('Qué revisa el estudio aquí.',review,'Lectura aplicada')
    doc += section('Cuándo conviene escribir.',when,'Momento')
    doc += cta_final(final_text,'Dirección, rol o CIP. Respuesta rápida por WhatsApp.',wa_link,cta2)
    doc += footer(wa_link)
    write(path.strip('/') + '/index.html', doc)

mother_wa=wa('Hola, quiero evaluar un terreno en Región Metropolitana.')
comunas = head('Estudio de cabida por comuna en Santiago y Región Metropolitana','Evaluamos terrenos por comuna con foco en Región Metropolitana. CIP, normativa urbana y potencial real del predio antes de comprar, ofertar o desarrollar.','/comunas/','/assets/images/hero-estudio-de-cabida.webp','servicio','communes')
comunas += internal_hero('/assets/images/hero-estudio-de-cabida.webp','Cobertura','Estudio de cabida por comuna: leer bien el terreno también es leer su contexto.','La norma se aplica sobre un predio concreto, pero la lectura de oportunidad cambia mucho según la comuna, el contexto urbano y el tipo de decisión.',['Región Metropolitana','Lectura local','Antes de comprar'],mother_wa,'Envíanos el terreno y lo revisamos',('Ver comunas','#comunas-lista'),'No basta con la regla general. Conviene entender dónde suele distorsionarse la intuición en cada contexto.')
comunas += section('Por qué la lectura local importa.','No basta con conocer la regla general. Conviene entender dónde suele distorsionarse la intuición en cada contexto. En algunas comunas pesa más la expectativa de densificación. En otras, la compatibilidad, la escala, la topografía o el valor defendible.','Contexto local')
comunas += '<section class="section" id="comunas-lista"><div class="section__head"><div><p class="eyebrow">Comunas</p><h2>Dónde se concentra gran parte del trabajo.</h2></div></div><div class="relatedLinks"><a class="card card--padded" href="/comunas/region-metropolitana/"><h3>Región Metropolitana</h3><p class="muted">Dos terrenos pueden parecer comparables y exigir lecturas completamente distintas.</p></a><a class="card card--padded" href="/comunas/las-condes/"><h3>Las Condes</h3><p class="muted">El valor del suelo vuelve cara cualquier sobreestimación.</p></a><a class="card card--padded" href="/comunas/providencia/"><h3>Providencia</h3><p class="muted">Una buena ubicación no siempre viene acompañada de una lectura simple.</p></a><a class="card card--padded" href="/comunas/vitacura/"><h3>Vitacura</h3><p class="muted">Cada restricción pesa más cuando también pesa más el valor en juego.</p></a><a class="card card--padded" href="/comunas/lo-barnechea/"><h3>Lo Barnechea</h3><p class="muted">La norma escrita rara vez cuenta sola la historia del terreno.</p></a></div></section>'
comunas += cta_final('Cuando el contexto local cambia la lectura, conviene revisarlo antes de avanzar.','Dirección, rol o CIP. Respuesta rápida por WhatsApp.',mother_wa,('Ver servicio','/estudio-de-cabida/'))
comunas += footer(mother_wa)
write('comunas/index.html', comunas)

commune('/comunas/las-condes/','Estudio de cabida en Las Condes | Evalúa un terreno antes de invertir','Estudio de cabida en Las Condes para revisar CIP, normativa urbana, restricciones y potencial real del terreno antes de comprar, ofertar o desarrollar.','Estudio de cabida en Las Condes para evaluar terrenos con más criterio.','En Las Condes, el valor del suelo hace que sobreestimar un terreno salga especialmente caro.',['Las Condes','Para inversión seria','Riesgo alto'],'Hola, quiero evaluar un terreno en Las Condes.','La expectativa de densificación o de alto valor futuro suele inflar la lectura inicial. El terreno real termina ajustando esa intuición.','CIP, normativa urbana, restricciones del predio, cabida útil, potencial razonable y todo lo que pueda alterar valor, programa o defendibilidad del caso.','Antes de comprar, ofertar, comparar alternativas o mostrar una oportunidad a terceros.','En Las Condes, una sobreestimación chica puede costar mucho.')
commune('/comunas/providencia/','Estudio de cabida en Providencia | Evalúa un terreno antes de invertir','Estudio de cabida en Providencia para revisar CIP, normativa urbana, restricciones y potencial real del terreno antes de comprar, ofertar o desarrollar.','Estudio de cabida en Providencia para evaluar terrenos con más criterio.','En Providencia, una buena ubicación no siempre viene acompañada de una lectura simple.',['Providencia','Lectura local','Antes de comprar'],'Hola, quiero evaluar un terreno en Providencia.','La mezcla entre compatibilidad de uso, escala urbana y presión sobre el suelo puede volver engañosa una primera impresión demasiado optimista.','CIP, normativa urbana, compatibilidades, restricciones del terreno, capacidad real del predio y consistencia entre idea y norma.','Cuando el terreno parece bien ubicado, pero todavía no está claro si esa ventaja resiste una lectura aplicada.','En Providencia, ubicación y viabilidad no siempre viajan juntas.',('Ver servicio','/estudio-de-cabida/'))
commune('/comunas/vitacura/','Estudio de cabida en Vitacura | Evalúa un terreno antes de invertir','Estudio de cabida en Vitacura para revisar CIP, normativa urbana, restricciones y potencial real del terreno antes de comprar, ofertar o desarrollar.','Estudio de cabida en Vitacura para evaluar terrenos con más criterio.','En Vitacura, cada restricción pesa más porque también pesa más el valor que se está defendiendo.',['Vitacura','Para inversión seria','Valor defendible'],'Hola, quiero evaluar un terreno en Vitacura.','Una lectura demasiado optimista puede inflar valor o programa sobre una base más frágil de lo que parece.','CIP, normativa urbana, restricciones del predio, capacidad real de desarrollo y todo lo que incida en una lectura defendible del caso.','Antes de comprar, ofertar o presentar una oportunidad donde cada limitante puede mover bastante la decisión.','En Vitacura, un detalle menor puede mover mucho valor.',('Ver casos reales','/casos/'))
commune('/comunas/lo-barnechea/','Estudio de cabida en Lo Barnechea | Evalúa un terreno antes de invertir','Estudio de cabida en Lo Barnechea para revisar CIP, normativa urbana, restricciones, topografía y potencial real del terreno antes de comprar, ofertar o desarrollar.','Estudio de cabida en Lo Barnechea para evaluar terrenos con más criterio.','En Lo Barnechea, la norma escrita rara vez cuenta sola la historia del terreno.',['Lo Barnechea','Topografía','Lectura local'],'Hola, quiero evaluar un terreno en Lo Barnechea.','Pendientes, geometría, accesos y condiciones físicas pueden cambiar la lectura de una forma que el papel por sí solo no anticipa.','CIP, normativa urbana, restricciones específicas, forma del predio, condiciones físicas relevantes y capacidad real del terreno para sostener la idea planteada.','Cuando el terreno parece atractivo, pero depende demasiado de una lectura fina para confirmar si vale la pena avanzar.','En Lo Barnechea, la diferencia entre intuición y lectura aplicada puede ser decisiva.',('Ver servicio','/estudio-de-cabida/'))
commune('/comunas/region-metropolitana/','Estudio de cabida en Región Metropolitana | Evalúa un terreno antes de invertir','Estudio de cabida en Región Metropolitana para revisar CIP, normativa urbana, restricciones y potencial real del terreno antes de comprar, ofertar o desarrollar.','Estudio de cabida en Región Metropolitana para evaluar terrenos con más criterio.','En la Región Metropolitana, dos terrenos pueden parecer comparables y exigir lecturas completamente distintas.',['Región Metropolitana','Lectura local','Antes de comprar'],'Hola, quiero evaluar un terreno en Región Metropolitana.','Se extrapolan expectativas entre comunas, se igualan suelos que no juegan con las mismas reglas y se compra por comparación aparente.','CIP, normativa urbana, restricciones del predio, contexto local y todo lo que altere la oportunidad real del caso.','Antes de comprar, comparar, ofertar o priorizar alternativas dentro de la RM.','En la Región Metropolitana, la intuición comparativa suele fallar más de lo que parece.',('Ver comunas','/comunas/'))

# additional pages for consistency
for rel, h1, lead, pills, wa_msg in [
('/estudio-de-cabida-comercial/','Estudio de Cabida Comercial para decisiones donde no conviene improvisar.','Cuando no basta con entender el terreno: también necesitas mostrar el potencial con claridad y defender mejor la oportunidad.',['Más recomendado','Para inversión seria','Decisión con terceros'],'Hola, quiero cotizar un Estudio de Cabida Comercial para un terreno.'),
('/estudio-de-cabida-tecnica/','Estudio de Cabida Técnica para validar rápido si el terreno tiene sentido.','Despeja la base normativa del caso y ordena la decisión inicial sin sumar capas que todavía no hacen falta.',['Para validar rápido','Lectura aplicada','Antes de comprar'],'Hola, quiero cotizar un Estudio de Cabida Técnica para un terreno.'),
('/evaluar-terreno/','Evalúa un terreno antes de comprar, ofertar o invertir.','Una buena lectura no reemplaza la decisión. La mejora. Cuando el terreno importa, conviene revisarlo antes de seguir cargándole tiempo, plata o expectativas.',['Antes de comprar','Riesgo alto','Lectura aplicada'],'Hola, estoy evaluando un terreno y quiero revisar si conviene antes de invertir.'),
('/cabida-comercial/','Cabida comercial para mostrar mejor el potencial del terreno.','Base normativa seria más una capa visual que ordena la conversación frente a socios, clientes o inversionistas.',['Más recomendado','Decisión con terceros','Para inversión seria'],'Hola, quiero cotizar un Estudio de Cabida Comercial para un terreno.'),
('/factibilidad-normativa/','Factibilidad normativa: qué cambia la decisión de verdad.','No basta con leer la zona. La factibilidad normativa se juega en cómo esa regla conversa con el terreno real, sus restricciones y el objetivo del caso.',['Normativa urbana','Lectura aplicada','Antes de comprar'],'Hola, leí la guía y quiero revisar un terreno concreto.'),
('/errores-de-cabida/','Errores de cabida que suelen costar caro.','Muchos errores no aparecen por falta de documentos, sino por una lectura optimista del potencial y una lectura débil de las restricciones.',['Casos reales','Riesgo alto','Lectura aplicada'],'Hola, leí la guía y quiero revisar un terreno concreto.'),
('/antes-de-comprar/','Qué revisar antes de comprar un terreno.','La primera intuición rara vez alcanza. Conviene revisar el predio antes de comprometer precio, tiempo o expectativas.',['Antes de comprar','Riesgo alto','Lectura aplicada'],'Hola, leí la guía y quiero revisar un terreno concreto.'),
]:
    wa_link=wa(wa_msg)
    doc=head(h1+' | estudiodecabida.cl',lead,rel,'/assets/images/hero-estudio-de-cabida.webp','servicio','guide')
    doc += internal_hero('/assets/images/hero-estudio-de-cabida.webp','Guía / alcance',h1,lead,pills,wa_link,'Envíanos el terreno y lo revisamos',('Ver servicio','/estudio-de-cabida/'))
    doc += section('Qué cambia cuando la lectura es aplicada.','La diferencia entre una buena intuición y una buena decisión está en cómo se cruzan norma, terreno real, restricciones y objetivo del caso.')
    doc += section('Dónde suele fallar la lectura rápida.','En la extrapolación de zona, en metros inflados, en restricciones que aparecen tarde y en asumir que el caso se explica solo.')
    doc += section('Por qué conviene escribir temprano.','Cuando la decisión todavía se puede mover, el estudio vale más. Después, corregir suele costar bastante más que leer bien a tiempo.')
    doc += cta_final('Si ya hay un terreno concreto, conviene revisarlo aplicado.','Dirección, rol o CIP. Respuesta rápida por WhatsApp.',wa_link,('Ver precios','/precios/'))
    doc += footer(wa_link)
    write(rel.strip('/') + '/index.html', doc)

# styles append for some minor spacing
css = (ROOT/'css/style.css').read_text(encoding='utf-8')
extra = """
.formHelp{color:var(--text-3)}
.hero__actions{display:flex;gap:14px;flex-wrap:wrap}
@media (max-width: 760px){
  .homeHero__copy .muted{font-size:15px;line-height:1.55}
  .hero__actions .btn{width:100%;justify-content:center}
  .section__head .lead{max-width:none}
}
"""
if extra not in css:
    (ROOT/'css/style.css').write_text(css + '\n' + extra, encoding='utf-8')

# main.js replace default whatsapp message if any generic sitewide? keep as is

# sitemap minimal regen
urls = ['','estudio-de-cabida/','precios/','precio/','casos/','contacto/','antes-de-comprar-terreno/','como-leer-un-cip/','que-puedo-construir/','estudio-tecnico-vs-comercial/','como-se-hace-un-estudio-de-cabida/','que-incluye-un-estudio-de-cabida/','ejemplo-de-estudio-de-cabida/','comunas/','comunas/region-metropolitana/','comunas/las-condes/','comunas/providencia/','comunas/vitacura/','comunas/lo-barnechea/','estudio-de-cabida-comercial/','estudio-de-cabida-tecnica/','evaluar-terreno/','cabida-comercial/','factibilidad-normativa/','errores-de-cabida/','antes-de-comprar/']
sitemap='''<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'''+''.join(f'<url><loc>{BASE}/{u}</loc></url>\n' for u in urls)+ '</urlset>'
(ROOT/'sitemap.xml').write_text(sitemap, encoding='utf-8')
