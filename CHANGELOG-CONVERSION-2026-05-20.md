# Cambios de conversión aplicados

- Se dejó el formulario como CTA principal para evaluar terreno.
- Se mantuvo WhatsApp como vía secundaria/flotante.
- Se reemplazó el formulario anterior que solo armaba un mensaje de WhatsApp por un formulario real con campos `name` y envío externo vía FormSubmit.
- Se agregó `/gracias/` como página de agradecimiento para medir conversión y generar confianza post-envío.
- Se agregaron eventos `form_start`, `form_submit` y `generate_lead` al `dataLayer`.
- Se retiraron montos cerrados de `/precios/` y se transformó la página en una cotización según terreno, comuna, antecedentes, objetivo y complejidad.
- `/precio/` ahora redirige a `/precios/` para no dividir autoridad SEO.

## Nota técnica

El formulario usa temporalmente `chechelnitzky@gmail.com` como correo de recepción mediante FormSubmit. Si el correo definitivo es otro, cambiar el atributo `action` del formulario en `/contacto/index.html`.


## Ajuste posterior - correo y trazabilidad
- Correo receptor del formulario actualizado a `chechelnitzky@gmail.com`.
- Se agregaron campos ocultos para identificar el origen del lead: `sitio`, `marca`, `tipo_de_lead`, `formulario`, `pagina_origen`, `url_origen`, `referrer` y UTMs.
- Esto permite juntar leads en un solo correo/archivo sin perder de qué web o campaña vienen.
