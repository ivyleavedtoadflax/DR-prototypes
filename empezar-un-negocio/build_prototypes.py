#!/usr/bin/env python3
"""drimstack /build — 3 candidate prototypes of the "Empezar un negocio" journey.

Fresh build, separate from data/work/permit-detail/. Reuses the REAL journey data
(../permit-detail/journey.json) and scraped permit detail (services.json) so no
service name, requirement, cost or time is invented. Inlines the gobdo- house-style
tokens from the drimstack brief-to-prototypes skill; chrome is identical across all
three so the team tests the journey, not the chrome.

    python3 build_prototypes.py
"""
import json, html
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE.parent / "permit-detail"
J = json.loads((SRC / "journey.json").read_text())
SVC = {s["id"]: s for s in json.loads((SRC / "services.json").read_text())["services"]}
STEPS = {s["n"]: s for s in J["steps"]}
def e(s): return html.escape(s, quote=False)

# House style is usted; the reused journey.json copy is in tú. Curated, order-
# sensitive tú->usted normalisation over just the strings we reuse (safe for this
# small known corpus — not a general translator).
_USTED = [
  ("Forma tu empresa", "Forme su empresa"), ("Te guiamos paso a paso y te enlazamos", "Le guiamos paso a paso y le enlazamos"),
  ("Antes de registrar tu empresa, confirma que tienes", "Antes de registrar su empresa, confirme que tiene"),
  ("con qué cubrir tus costos fijos", "con qué cubrir sus costos fijos"),
  ("Decide si operarás", "Decida si operará"), ("Tu elección define", "Su elección define"),
  ("Busca coincidencias y aparta tu Nombre Comercial", "Busque coincidencias y aparte su Nombre Comercial"),
  ("Redacta el acto constitutivo, legalízalo ante notario y ante la PGR, y obtén", "Redacte el acto constitutivo, legalícelo ante notario y ante la PGR, y obtenga"),
  ("Paga el impuesto", "Pague el impuesto"),
  ("Inscribe tu empresa", "Inscriba su empresa"), ("de tu provincia", "de su provincia"),
  ("Activa tu Registro Nacional del Contribuyente (RNC) en la DGII. Si eres Persona Física, elige", "Active su Registro Nacional del Contribuyente (RNC) en la DGII. Si es Persona Física, elija"),
  ("Si vas a contratar personal, registra tu empresa", "Si va a contratar personal, registre su empresa"),
  ("los permisos sectoriales que aplican a tu actividad", "los permisos sectoriales que aplican a su actividad"),
  ("Saber a qué se dedicará tu negocio.", "Saber a qué se dedicará su negocio."),
  ("agrupados por lo que necesitas", "agrupados por lo que necesita"),
  ("Tu RNC activo para algunos apoyos", "Su RNC activo para algunos apoyos"),
  ("Una idea clara de tu actividad y de tus finanzas iniciales.", "Una idea clara de su actividad y de sus finanzas iniciales."),
  ("Saber si trabajarás solo o con socios, y el capital con el que empiezas.", "Saber si trabajará solo o con socios, y el capital con el que empieza."),
  ("Uno o varios nombres alternativos y tu documento de identidad.", "Uno o varios nombres alternativos y su documento de identidad."),
  ("Registro Mercantil vigente y documentos de constitución.", "Registro Mercantil vigente y documentos de constitución."),
  ("RNC activo y los datos de tus primeros empleados.", "RNC activo y los datos de sus primeros empleados."),
  ("Tú mismo", "Usted mismo"),
  ("Comprueba que estás listo", "Compruebe que está listo"),
  ("Elige tu estructura legal", "Elija su estructura legal"),
  ("Reserva tu nombre comercial", "Reserve su nombre comercial"),
  ("Prepara tus documentos de constitución", "Prepare sus documentos de constitución"),
  ("Paga el 1% de constitución", "Pague el 1% de constitución"),
  ("Regístrate en el Registro Mercantil", "Regístrese en el Registro Mercantil"),
  ("Obtén tu RNC", "Obtenga su RNC"),
  ("Regístrate como empleador", "Regístrese como empleador"),
  ("¿Necesitas un permiso para operar?", "¿Necesita un permiso para operar?"),
  ("Haz crecer tu negocio", "Haga crecer su negocio"),
  ("Según tu actividad", "Según su actividad"),
  ("depende de tu tipo de sociedad", "depende de su tipo de sociedad"),
  ("de tus empleados", "de sus empleados"),
]
def U(s):
    for a, b in _USTED:
        s = s.replace(a, b)
    return s
J["intro"] = U(J["intro"]); J["vuf_note"] = U(J["vuf_note"])
for _s in J["steps"]:
    for _k in ("title", "aplica", "desc", "quien", "necesitas", "link_label"):
        if _k in _s: _s[_k] = U(_s[_k])

CSS = r"""
* { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --gobdo-navy: #003876; --gobdo-navy-dark: #00274F; --gobdo-red: #D50910; --gobdo-red-dark: #A50710;
  --gobdo-off-white: #F7F7F7; --gobdo-charcoal: #212529; --gobdo-white: #FFFFFF;
  --gobdo-grey-light: #DDDDDD; --gobdo-grey-mid: #6B6B6B; --gobdo-green: #2CB34A;
  --gobdo-success-bg: #E9F7EC; --gobdo-bluegrey: #194A84;
}
html { font-size: 16px; }
body { font-family: 'Poppins', system-ui, sans-serif; background: var(--gobdo-off-white); color: var(--gobdo-charcoal); line-height: 1.5; min-height: 100vh; display: flex; flex-direction: column; }
.gobdo-official-banner { background: var(--gobdo-navy); color: var(--gobdo-white); font-size: 13px; padding: 8px 24px; text-align: center; letter-spacing: 0.5px; }
.gobdo-header { background: var(--gobdo-navy); padding: 18px 24px; display: flex; align-items: center; gap: 24px; border-bottom: 3px solid var(--gobdo-red); }
.gobdo-header__escudo { width: 36px; height: 36px; background: var(--gobdo-white); color: var(--gobdo-navy); display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 13px; letter-spacing: 1px; }
.gobdo-header__title { font-size: 22px; font-weight: 700; color: var(--gobdo-white); text-decoration: none; }
.gobdo-header__service { font-size: 14px; color: var(--gobdo-white); margin-left: auto; text-align: right; }
.gobdo-status-banner--alfa { background: var(--gobdo-white); padding: 12px 24px; font-size: 15px; display: flex; align-items: center; gap: 12px; border-bottom: 1px solid var(--gobdo-grey-light); }
.gobdo-status-banner--alfa strong { background: var(--gobdo-charcoal); color: var(--gobdo-white); padding: 3px 10px; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; font-weight: 700; }
.drimstack-banner { background: var(--gobdo-charcoal); color: var(--gobdo-white); padding: 10px 24px; font-size: 14px; display: flex; align-items: center; justify-content: space-between; gap: 16px; }
.drimstack-banner__variant { font-weight: 600; }
.drimstack-banner button { background: var(--gobdo-red); color: var(--gobdo-white); border: 0; padding: 6px 14px; font-weight: 700; font-size: 13px; cursor: pointer; font-family: inherit; }
main.gobdo-container { max-width: 720px; width: 100%; margin: 32px auto; padding: 0 24px; flex: 1; }
.gobdo-back-link { display: inline-block; color: var(--gobdo-navy); margin-bottom: 24px; font-size: 16px; text-decoration: underline; cursor: pointer; background: none; border: 0; padding: 0; font-family: inherit; }
.gobdo-back-link::before { content: "\2190  "; }
.gobdo-caption { font-size: 14px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; color: var(--gobdo-navy); margin-bottom: 8px; display:block; }
h1 { font-size: 36px; font-weight: 700; line-height: 1.2; margin-bottom: 20px; color: var(--gobdo-navy); }
h2 { font-size: 22px; font-weight: 600; margin-bottom: 12px; margin-top: 24px; }
p { margin-bottom: 16px; font-size: 18px; }
ul.gobdo-list { padding-left: 20px; margin-bottom: 16px; }
ul.gobdo-list li { font-size: 18px; margin-bottom: 6px; }
.gobdo-form-group { margin-bottom: 28px; }
.gobdo-label, .gobdo-fieldset-legend { display: block; font-weight: 700; margin-bottom: 6px; color: var(--gobdo-charcoal); }
.gobdo-label { font-size: 20px; }
.gobdo-fieldset-legend { font-size: 24px; margin-bottom: 12px; }
.gobdo-hint { display: block; color: var(--gobdo-grey-mid); margin-bottom: 12px; font-size: 16px; }
.gobdo-input, .gobdo-select { width: 100%; max-width: 480px; padding: 10px 12px; font-size: 18px; border: 2px solid var(--gobdo-charcoal); font-family: inherit; background: var(--gobdo-white); }
.gobdo-input--short { max-width: 220px; }
.gobdo-input--error { border-color: var(--gobdo-red); }
.gobdo-radio { display: flex; align-items: flex-start; gap: 12px; border: 2px solid var(--gobdo-grey-light); background: var(--gobdo-white); padding: 16px; margin-bottom: 12px; cursor: pointer; font-size: 18px; }
.gobdo-radio:hover { border-color: var(--gobdo-navy); }
.gobdo-radio input { margin-top: 4px; width: 22px; height: 22px; flex-shrink: 0; }
.gobdo-radio__hint { display:block; color: var(--gobdo-grey-mid); font-size: 15px; margin-top: 4px; }
.gobdo-error-summary { background: var(--gobdo-white); border: 4px solid var(--gobdo-red); padding: 16px 20px; margin-bottom: 24px; }
.gobdo-error-summary h2 { margin-top: 0; font-size: 20px; }
.gobdo-error-summary ul { padding-left: 20px; }
.gobdo-error-summary a { color: var(--gobdo-red); font-weight: 600; }
.gobdo-error-message { display: block; color: var(--gobdo-red); font-weight: 600; font-size: 16px; margin-bottom: 8px; }
.gobdo-visually-hidden { position: absolute; width: 1px; height: 1px; margin: 0; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0; }
.gobdo-btn { background: var(--gobdo-red); color: var(--gobdo-white); border: 0; padding: 12px 24px; font-size: 18px; font-weight: 600; cursor: pointer; font-family: inherit; box-shadow: 0 2px 0 var(--gobdo-red-dark); text-decoration: none; display: inline-block; }
.gobdo-btn:hover { background: var(--gobdo-red-dark); }
.gobdo-btn--secondary { background: var(--gobdo-navy); box-shadow: 0 2px 0 var(--gobdo-navy-dark); }
.gobdo-btn--secondary:hover { background: var(--gobdo-navy-dark); }
.gobdo-btn--start { padding: 16px 32px; font-size: 20px; }
.gobdo-actions { display: flex; gap: 16px; flex-wrap: wrap; margin-top: 24px; align-items: center; }
.gobdo-summary-list { border: 1px solid var(--gobdo-grey-light); margin-bottom: 24px; background: var(--gobdo-white); }
.gobdo-summary-list__row { display: flex; border-bottom: 1px solid var(--gobdo-grey-light); padding: 16px; font-size: 16px; }
.gobdo-summary-list__row:last-child { border-bottom: 0; }
.gobdo-summary-list__key { width: 38%; font-weight: 700; padding-right: 12px; }
.gobdo-summary-list__value { width: 42%; padding-right: 12px; }
.gobdo-summary-list__actions { width: 20%; text-align: right; }
.gobdo-summary-list__actions a { color: var(--gobdo-navy); cursor: pointer; text-decoration: underline; }
.gobdo-callout { background: var(--gobdo-white); border-left: 6px solid var(--gobdo-navy); padding: 16px 20px; margin-bottom: 24px; }
.gobdo-callout--success { background: var(--gobdo-success-bg); border-color: var(--gobdo-green); }
.gobdo-callout--help { background: var(--gobdo-off-white); border-color: var(--gobdo-charcoal); }
.gobdo-id-card { background: var(--gobdo-white); border: 2px solid var(--gobdo-navy); padding: 20px; margin-bottom: 24px; }
.gobdo-id-card h3 { font-size: 22px; margin-bottom: 12px; }
.gobdo-id-card dl { display: grid; grid-template-columns: 140px 1fr; gap: 6px 12px; font-size: 16px; }
.gobdo-id-card dt { font-weight: 700; }
.gobdo-steplist { list-style: none; padding: 0; margin-bottom: 24px; }
.gobdo-step { display: flex; gap: 16px; align-items: flex-start; background: var(--gobdo-white); border: 1px solid var(--gobdo-grey-light); border-left: 6px solid var(--gobdo-navy); padding: 16px; margin-bottom: 12px; cursor: pointer; text-align: left; width: 100%; font-family: inherit; }
.gobdo-step:hover { border-left-color: var(--gobdo-red); }
.gobdo-step--optional { border-left-style: dashed; }
.gobdo-step__num { flex-shrink: 0; width: 40px; height: 40px; border-radius: 50%; background: var(--gobdo-navy); color: var(--gobdo-white); font-weight: 700; font-size: 18px; display: flex; align-items: center; justify-content: center; }
.gobdo-step--optional .gobdo-step__num { background: var(--gobdo-white); color: var(--gobdo-navy); border: 2px solid var(--gobdo-navy); }
.gobdo-step__body { flex: 1; }
.gobdo-step__title { font-size: 19px; font-weight: 600; color: var(--gobdo-navy); margin-bottom: 2px; }
.gobdo-step__desc { font-size: 15px; color: var(--gobdo-grey-mid); }
.gobdo-step__aplica { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: var(--gobdo-bluegrey); }
.gobdo-divider { display:flex; align-items:center; gap:12px; margin: 24px 0 16px; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: var(--gobdo-grey-mid); }
.gobdo-divider::after { content:""; flex:1; border-top: 1px solid var(--gobdo-grey-light); }
.gobdo-tag { display:inline-block; background: var(--gobdo-success-bg); color: var(--gobdo-navy); border:1px solid var(--gobdo-green); font-size: 12px; font-weight:700; padding: 2px 8px; border-radius: 10px; text-transform: uppercase; letter-spacing:0.5px; }
.gobdo-check-item { display:flex; gap:12px; padding: 12px 0; border-bottom: 1px solid var(--gobdo-grey-light); font-size: 17px; }
.gobdo-check-item__mark { color: var(--gobdo-green); font-weight: 700; }
.gobdo-check-item--skip { color: var(--gobdo-grey-mid); }
.gobdo-footer { background: var(--gobdo-navy); color: var(--gobdo-white); padding: 32px 24px; margin-top: 48px; font-size: 14px; }
.gobdo-footer__inner { max-width: 1200px; margin: 0 auto; display: flex; flex-wrap: wrap; gap: 24px; justify-content: space-between; }
.gobdo-footer a { color: var(--gobdo-white); }
.gobdo-footer__escudo { width: 40px; height: 40px; background: var(--gobdo-white); color: var(--gobdo-navy); display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 12px; }
.fake-data { display: inline-block; background: var(--gobdo-off-white); border: 1px dashed var(--gobdo-grey-mid); padding: 1px 4px; font-size: 0.95em; }
.drimstack-assumptions { position: fixed; right: -440px; top: 0; width: 420px; height: 100vh; background: var(--gobdo-white); border-left: 3px solid var(--gobdo-charcoal); padding: 24px; overflow-y: auto; transition: right 0.25s ease-out; z-index: 100; box-shadow: -2px 0 8px rgba(0,0,0,0.1); }
.drimstack-assumptions--open { right: 0; }
.drimstack-assumptions__close { position: absolute; top: 16px; right: 16px; background: var(--gobdo-charcoal); color: var(--gobdo-white); border: 0; width: 32px; height: 32px; font-size: 18px; cursor: pointer; font-family: inherit; }
.drimstack-assumptions h2 { font-size: 20px; margin-bottom: 12px; margin-top: 0; }
.drimstack-assumptions h3 { font-size: 13px; margin: 18px 0 8px; text-transform: uppercase; letter-spacing: 0.5px; color: var(--gobdo-grey-mid); }
.drimstack-assumptions p { font-size: 13px; margin-bottom: 12px; }
.drimstack-assumptions ul { padding-left: 0; list-style: none; }
.drimstack-assumptions li { margin-bottom: 14px; font-size: 13px; line-height: 1.5; }
.verify-tag { display: inline-block; color: var(--gobdo-white); font-size: 10px; padding: 2px 6px; font-weight: 700; margin-right: 6px; text-transform: uppercase; letter-spacing: 0.5px; background: var(--gobdo-charcoal); }
.verify-tag--user { background: var(--gobdo-navy); }
.verify-tag--inst { background: var(--gobdo-bluegrey); }
.verify-tag--ogtic { background: var(--gobdo-charcoal); }
.verify-tag--policy { background: var(--gobdo-red); }
.verify-tag--data { background: var(--gobdo-green); }
.verify-tag--gap { background: var(--gobdo-grey-mid); }
.page { display: none; }
.page--active { display: block; }
@media (max-width: 720px) {
  main.gobdo-container { padding: 0 16px; margin: 16px auto; }
  h1 { font-size: 28px; } h2 { font-size: 20px; } p, ul.gobdo-list li { font-size: 17px; }
  .drimstack-assumptions { width: 100vw; right: -100vw; }
  .gobdo-summary-list__row { flex-direction: column; }
  .gobdo-summary-list__key, .gobdo-summary-list__value, .gobdo-summary-list__actions { width: 100%; padding: 4px 0; text-align: left; }
  .gobdo-header { flex-wrap: wrap; } .gobdo-header__service { margin-left: 0; flex-basis: 100%; text-align:left; }
  .gobdo-id-card dl { grid-template-columns: 1fr; } .gobdo-id-card dt { margin-top: 8px; }
}
"""

SCRIPT = r"""
function goTo(id) {
  document.querySelectorAll('.page').forEach(function(p){ p.classList.remove('page--active'); });
  var el = document.getElementById(id);
  if (el) { el.classList.add('page--active'); window.scrollTo(0, 0); }
}
function toggleAssumptions() {
  var panel = document.getElementById('assumptions');
  panel.classList.toggle('drimstack-assumptions--open');
  panel.setAttribute('aria-hidden', !panel.classList.contains('drimstack-assumptions--open'));
}
function requireRadio(name, next, summaryId) {
  var chosen = document.querySelector('input[name="'+name+'"]:checked');
  var summary = document.getElementById(summaryId);
  if (!chosen) {
    if (summary) { summary.hidden = false; summary.focus(); }
    return;
  }
  if (summary) summary.hidden = true;
  goTo(next);
}
"""

def head(title, variant_n, variant_name):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(title)} – gob.do</title>
<!--
  drimstack prototype – Variant {variant_n} of 3 – {variant_name}
  Generated by: brief-to-prototypes skill, on the "Empezar un negocio" brief (OGTIC front door)
  Anchored to the drimstack service standards: 1 (meet user needs), 3 (everyone can use it),
    4 (simple, relatable language), 5 (works first time), 7 (open, interoperable platforms)
  Anchored to GOV.UK Design Principles: 1, 4, 6, 7
  Real service names/links/requirements from observicios.gob.do (data/candidates_classified.csv,
    permit-detail/services.json). Assumptions surfaced in the right-hand panel. Data marked fake is fake.
-->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap">
<style>{CSS}</style>
</head>
<body>
<div class="gobdo-official-banner">Un servicio del Gobierno de la República Dominicana</div>
<header class="gobdo-header">
  <div class="gobdo-header__escudo">RD</div>
  <a href="#" class="gobdo-header__title">gob.do</a>
  <span class="gobdo-header__service">Empezar un negocio</span>
</header>
<div class="gobdo-status-banner gobdo-status-banner--alfa">
  <strong>alfa</strong>
  <span>Esto es un prototipo. No lo use para un trámite real. <a href="#" onclick="toggleAssumptions(); return false;" style="color: var(--gobdo-navy);">Díganos qué piensa</a>.</span>
</div>
<div class="drimstack-banner" lang="en">
  <span><span class="drimstack-banner__variant">Variant {variant_n} of 3</span> · {variant_name}</span>
  <button onclick="toggleAssumptions()">Show assumptions</button>
</div>
<main class="gobdo-container">
"""

FOOTER = """</main>
<footer class="gobdo-footer">
  <div class="gobdo-footer__inner">
    <div>
      <p style="margin-bottom: 8px;"><strong>gob.do</strong> · Portal Único de Servicios</p>
      <p style="margin-bottom: 0; font-size: 13px;">Prototipo drimstack en el estilo del Portal Único, con OGTIC. No es un servicio oficial.</p>
    </div>
    <div>
      <p style="margin-bottom: 8px;"><a href="#">Portal Único (gob.do)</a> · <a href="#">Punto GOB</a> · <a href="#">Centro de Contacto *462</a> · <a href="#">Política de privacidad</a></p>
      <p style="margin-bottom: 0; font-size: 13px;">© 2026 Gobierno de la República Dominicana</p>
    </div>
    <div class="gobdo-footer__escudo">RD</div>
  </div>
</footer>
"""

def aside(inner):
    return f"""<aside id="assumptions" class="drimstack-assumptions" aria-hidden="true" lang="en">
  <button class="drimstack-assumptions__close" onclick="toggleAssumptions()" aria-label="Close assumptions panel">×</button>
  <h2>Assumptions to verify</h2>
  <p>Every claim this prototype makes that isn't yet evidence-led. Test in research and stakeholder review.</p>
  {inner}
</aside>
<script>{SCRIPT}</script>
</body></html>"""

def a_user(t): return f'<li><span class="verify-tag verify-tag--user">Verify with users</span> {t}</li>'
def a_inst(t): return f'<li><span class="verify-tag verify-tag--inst">Verify with institución</span> {t}</li>'
def a_ogtic(t): return f'<li><span class="verify-tag verify-tag--ogtic">Verify with OGTIC</span> {t}</li>'
def a_policy(t): return f'<li><span class="verify-tag verify-tag--policy">Verify with policy</span> {t}</li>'
def a_data(t): return f'<li><span class="verify-tag verify-tag--data">Verify with data</span> {t}</li>'
def a_gap(t): return f'<li><span class="verify-tag verify-tag--gap">Known gap</span> {t}</li>'

def back(to): return f'<button class="gobdo-back-link" onclick="goTo(\'{to}\')">Volver</button>'
def page(pid, inner, active=False):
    cls = "page page--active" if active else "page"
    return f'<section id="{pid}" class="{cls}">{inner}</section>\n'

ID_CARD = """<div class="gobdo-id-card">
  <h3><span class="fake-data">Ana Lucía Reyes Batista</span> <span class="gobdo-tag">datos ficticios</span></h3>
  <dl>
    <dt>Cédula</dt><dd class="fake-data">001-1234567-8</dd>
    <dt>Provincia</dt><dd class="fake-data">Santo Domingo</dd>
    <dt>Correo</dt><dd class="fake-data">a.reyes@example.do</dd>
    <dt>Teléfono</dt><dd class="fake-data">809-555-0148</dd>
  </dl>
</div>"""

HELP_CALLOUT = """<div class="gobdo-callout gobdo-callout--help">
  <strong>Si prefiere que le ayuden</strong>
  <p style="margin-top: 8px; margin-bottom: 0;">Vaya a un <strong>Punto GOB</strong> o marque <strong>*462</strong> y alguien hace el trámite con usted, sin costo.</p>
</div>"""

def cedula_page(pid, back_to, next_pid, intro):
    return page(pid, f"""{back(back_to)}
  <h1>¿Cuál es su cédula?</h1>
  <p>{intro}</p>
  <div class="gobdo-form-group">
    <label class="gobdo-label" for="ced-{pid}">Número de cédula</label>
    <span class="gobdo-hint">Está en el frente de su cédula. Puede escribirla con o sin guiones.</span>
    <input class="gobdo-input gobdo-input--short" id="ced-{pid}" type="text" value="001-1234567-8" autocomplete="off">
  </div>
  <p style="font-size:14px;color:var(--gobdo-grey-mid);">Con su cédula buscamos su nombre y datos de contacto en GobID. No tendrá que escribirlos.</p>
  <div class="gobdo-actions"><button class="gobdo-btn" onclick="goTo('{next_pid}')">Continuar</button></div>""")

def confirmar_page(pid, back_to, next_pid):
    return page(pid, f"""{back(back_to)}
  <h1>¿Es usted?</h1>
  <p>Encontramos un registro con esa cédula. Compruebe los datos.</p>
  {ID_CARD}
  <div class="gobdo-actions">
    <button class="gobdo-btn" onclick="goTo('{next_pid}')">Sí, soy yo</button>
    <button class="gobdo-btn gobdo-btn--secondary" onclick="alert('En un servicio real esto abriría una pantalla de ayuda.')">Hay un error</button>
  </div>""")

# ---------- permit branch (shared by P1) ----------
def permit_detail_page(pid, sid, back_to):
    s = SVC[sid]
    reqs = "".join(f'<li>{e(r)}</li>' for r in s["requisitos"])
    steps = "".join(f'<li>{e(st)}</li>' for st in s["procedimiento"])
    costo = e(s["costo"]) + (f' <span style="color:var(--gobdo-grey-mid);font-size:15px;">({e(s["costo_detalle"])})</span>' if s["costo_detalle"] else "")
    return page(pid, f"""{back(back_to)}
  <span class="gobdo-caption">Paso 9 · Permiso</span>
  <h1>{e(s['name'])}</h1>
  <p>{e(s['summary'])}</p>
  <div class="gobdo-callout"><strong>Tiempo:</strong> {e(s['tiempo'])} &nbsp;·&nbsp; <strong>Costo:</strong> {costo} &nbsp;·&nbsp; <strong>Institución:</strong> {e(s['institution'])}</div>
  <h2>Requisitos ({len(s['requisitos'])})</h2>
  <ul class="gobdo-list">{reqs}</ul>
  <h2>Cómo se solicita</h2>
  <ul class="gobdo-list">{steps}</ul>
  <p style="font-size:15px;color:var(--gobdo-grey-mid);">El trámite se completa en el portal UCTT-MITUR, no en gob.do.</p>
  <div class="gobdo-actions">
    <a class="gobdo-btn" href="{e(s['url'])}" target="_blank" rel="noopener">Ir al trámite oficial</a>
    <button class="gobdo-btn gobdo-btn--secondary" onclick="goTo('{back_to}')">Volver a mis permisos</button>
  </div>""")

TOUR = [("4855","hospedaje"),("4850","alimentos"),("4875","giftshop"),("4897","spa")]
def permit_results_page(pid, back_to, detail_prefix):
    cards = ""
    for sid, slug in TOUR:
        s = SVC[sid]
        cards += f"""<button class="gobdo-step" onclick="goTo('{detail_prefix}{sid}')">
      <span class="gobdo-step__body"><span class="gobdo-step__title">{e(s['name'])}</span>
      <span class="gobdo-step__desc">{e(s['institution'])} · Ver requisitos, costo y tiempo</span></span>
      <span aria-hidden="true" style="font-size:24px;color:var(--gobdo-navy);">›</span></button>"""
    return page(pid, f"""{back(back_to)}
  <span class="gobdo-caption">Paso 9 · Sus permisos</span>
  <h1>Permisos para su establecimiento turístico</h1>
  <p>Estos son los trámites que suelen aplicar a hoteles, restaurantes, bares, tiendas de regalos y spas. Los requisitos, costos y tiempos se toman del trámite oficial.</p>
  {cards}
  <div class="gobdo-actions"><button class="gobdo-btn gobdo-btn--secondary" onclick="goTo('{back_to}')">Cambiar mis respuestas</button></div>""")


# ============================ PROTOTYPE 1 ============================
# "Guía paso a paso" — self-serve signposting. The 10 steps as a navigable
# hub; each step links out to its real trámite. Hypothesis: a curated ordered
# list lets a first-time founder self-navigate without a wizard.
def build_p1():
    P = []
    # Start
    P.append(page("page-inicio", f"""
  <h1>Empezar un negocio</h1>
  <p>{e(J['intro'])}</p>
  <h2>Cómo funciona</h2>
  <p>Le mostramos los pasos en orden. Usted hace cada trámite en la institución que corresponde. Puede parar y volver cuando quiera.</p>
  <div class="gobdo-callout"><strong>Un dato útil</strong><p style="margin:8px 0 0;">{e(J['vuf_note'])}</p></div>
  {HELP_CALLOUT}
  <div class="gobdo-actions"><button class="gobdo-btn gobdo-btn--start" onclick="goTo('page-pasos')">Ver los pasos</button></div>""", active=True))
    # Steps list
    rows = ""
    for n in range(1, 11):
        s = STEPS[n]
        optional = n >= 9
        target = "perm-q1" if n == 9 else f"paso-{n}"
        rows += f"""<button class="gobdo-step {'gobdo-step--optional' if optional else ''}" onclick="goTo('{target}')">
      <span class="gobdo-step__num">{n}</span>
      <span class="gobdo-step__body"><span class="gobdo-step__title">{e(s['title'])}</span>
      <span class="gobdo-step__desc">{e(s['desc'][:95])}{'…' if len(s['desc'])>95 else ''}</span></span>
      <span class="gobdo-step__aplica">{e(s['aplica'])}</span></button>"""
        if n == 8:
            rows += '<div class="gobdo-divider">Opcional, según su negocio</div>'
    P.append(page("page-pasos", f"""{back('page-inicio')}
  <span class="gobdo-caption">Guía paso a paso</span>
  <h1>Los pasos</h1>
  <p>Los pasos 1 a 8 forman su empresa. Los pasos 9 y 10 dependen de su actividad.</p>
  <div class="gobdo-steplist">{rows}</div>"""))
    # Step detail pages 1-8, 10
    for n in list(range(1, 9)) + [10]:
        s = STEPS[n]
        extra = ""
        if s.get("extra_links"):
            extra = '<p style="font-size:15px;">' + " · ".join(f'<a href="{e(l["link"])}" target="_blank" rel="noopener" style="color:var(--gobdo-navy);">{e(l["label"])}</a>' for l in s["extra_links"]) + "</p>"
        if n == 10:
            groups = ""
            for g in J["grow_groups"]:
                items = ""
                for it in g["items"]:
                    sug = f' <span class="gobdo-tag">Sugerido: {e(it["sugerido"])}</span>' if it.get("sugerido") else ""
                    items += f'<li><a href="{e(it["link"])}" target="_blank" rel="noopener" style="color:var(--gobdo-navy);">{e(it["name"])}</a> — {e(it["inst"])}{sug}</li>'
                groups += f'<h2>{e(g["title"])}</h2><ul class="gobdo-list">{items}</ul>'
            P.append(page(f"paso-{n}", f"""{back('page-pasos')}
  <span class="gobdo-caption">Paso 10 de 10 · Opcional</span>
  <h1>{e(s['title'])}</h1>
  <p>{e(s['desc'])}</p>{groups}
  <div class="gobdo-actions"><button class="gobdo-btn gobdo-btn--secondary" onclick="goTo('page-pasos')">Volver a los pasos</button></div>"""))
            continue
        tgt = "_blank" if s["link"].startswith("http") else "_self"
        P.append(page(f"paso-{n}", f"""{back('page-pasos')}
  <span class="gobdo-caption">Paso {n} de 10 · {e(s['mode'])}</span>
  <h1>{e(s['title'])}</h1>
  <p><strong>Aplica a:</strong> {e(s['aplica'])}</p>
  <p>{e(s['desc'])}</p>
  <div class="gobdo-callout"><strong>Quién:</strong> {e(s['quien'])}<br><strong>Qué necesita:</strong> {e(s['necesitas'])}</div>
  <div class="gobdo-actions"><a class="gobdo-btn" href="{e(s['link'])}" target="{tgt}" rel="noopener">{e(s['link_label'])}</a>
  <button class="gobdo-btn gobdo-btn--secondary" onclick="goTo('page-pasos')">Volver a los pasos</button></div>
  {extra}"""))
    # Permit branch (step 9)
    q1opts = [("Turismo, restaurantes, alojamiento, entretenimiento o juegos de azar","perm-q2"),
              ("Transporte de personas o mercancías","perm-nomatch"),
              ("Importación, exportación o zonas francas","perm-nomatch"),
              ("Salud, alimentos, agro, pesca o recursos naturales","perm-nomatch"),
              ("Finanzas, seguros o inversiones","perm-nomatch"),
              ("Otra actividad","perm-nomatch")]
    b1 = "".join(f'<button class="gobdo-step" onclick="goTo(\'{t}\')"><span class="gobdo-step__body"><span class="gobdo-step__title" style="font-size:17px;">{e(o)}</span></span><span style="font-size:24px;color:var(--gobdo-navy);">›</span></button>' for o,t in q1opts)
    P.append(page("perm-q1", f"""{back('page-pasos')}
  <span class="gobdo-caption">Paso 9 de 10 · Permisos</span>
  <h1>¿De qué trata su negocio?</h1>
  <p>Con 1 o 2 preguntas le mostramos solo los permisos que le aplican. La mayoría de los negocios no necesita ninguno.</p>
  {b1}"""))
    q2opts = [("Un lugar que visitan los clientes: hotel, restaurante, bar, tienda de regalos o spa","perm-results"),
              ("Tours, excursiones, aventura o agencia de viajes","perm-nomatch"),
              ("Un proyecto turístico o de construcción","perm-nomatch"),
              ("Casino, apuestas, lotería o juegos de azar","perm-nomatch"),
              ("Parque de diversiones, billar o local similar","perm-nomatch")]
    b2 = "".join(f'<button class="gobdo-step" onclick="goTo(\'{t}\')"><span class="gobdo-step__body"><span class="gobdo-step__title" style="font-size:17px;">{e(o)}</span></span><span style="font-size:24px;color:var(--gobdo-navy);">›</span></button>' for o,t in q2opts)
    P.append(page("perm-q2", f"""{back('perm-q1')}
  <span class="gobdo-caption">Paso 9 de 10 · Permisos</span>
  <p><span class="gobdo-tag">Turismo, restaurantes, alojamiento…</span></p>
  <h1>¿Qué tipo de negocio de turismo o entretenimiento?</h1>
  {b2}"""))
    P.append(permit_results_page("perm-results", "perm-q2", "perm-"))
    for sid, slug in TOUR:
        P.append(permit_detail_page(f"perm-{sid}", sid, "perm-results"))
    P.append(page("perm-nomatch", f"""{back('perm-q1')}
  <h1>Esa rama no está en este prototipo</h1>
  <p>Este alfa construye solo la rama de <strong>Turismo → un lugar que visitan los clientes</strong> como ejemplo. Las demás actividades usarían el mismo patrón de 1–2 preguntas.</p>
  <div class="gobdo-actions"><button class="gobdo-btn" onclick="goTo('perm-q1')">Volver a la pregunta</button></div>"""))

    asums = f"""<h3>About the user</h3><ul>
    {a_user('First-time founders can self-navigate a 10-step list and go to each trámite on their own, without a guided wizard. (Standard 1)')}
    {a_user('People understand which optional steps (9, 10) apply to them from the "Aplica a" label alone. (Standard 4)')}
    {a_user('Sending citizens out to each institución\'s own portal (ONAPI, DGII, TSS) mid-journey does not lose them. (Standard 5)')}
    </ul><h3>About the data</h3><ul>
    {a_inst('The 8-step order and the "steps 3–8 = one VUF transaction" claim are current for 2026. (from PLAN.md / formalizate)')}
    {a_inst('The 4 Turismo establishment permits (hospedaje, A&B, giftshop, spa) are the right set for "a place guests visit", and their requisitos/costos are current on observicios.')}
    {a_data('Most new businesses genuinely need no sector permit — the copy states this; the proportion is unmeasured.')}
    </ul><h3>About the platform</h3><ul>
    {a_ogtic('gob.do can host a cross-government front door that deep-links into ONAPI, DGII, TSS and observicios trámites. (Standard 7)')}
    {a_gap('Only the Turismo→establecimiento permit branch is built; the other 5 sectors and tourism sub-branches are stubs.')}
    </ul><h3>About policy</h3><ul>
    {a_policy('Listing another portal\'s trámite (observicios, VUF) from gob.do is permitted and the links are stable.')}
    </ul>"""
    write("prototype-1-guia-paso-a-paso", "Empezar un negocio", 1, "Guía paso a paso (self-serve signposting)", "".join(P), asums)


# ============================ PROTOTYPE 2 ============================
# "Asistente: arma tu plan" — GobID lookup + 3 questions → Compruebe sus
# respuestas → a personalised checklist of only the steps and permits that
# apply. Hypothesis: personalisation beats a generic list for reducing overwhelm.
def build_p2():
    P = []
    P.append(page("page-inicio", f"""
  <h1>Arme su plan para empezar</h1>
  <p>Responda tres preguntas y le armamos una lista con <strong>solo los pasos que le tocan a usted</strong> — sin la lista larga que no le aplica.</p>
  <h2>Antes de empezar</h2>
  <p>Va a necesitar su cédula. Con ella buscamos su nombre y contacto; no los escribe otra vez.</p>
  {HELP_CALLOUT}
  <div class="gobdo-actions"><button class="gobdo-btn gobdo-btn--start" onclick="goTo('page-cedula')">Comenzar</button></div>""", active=True))
    P.append(cedula_page("page-cedula", "page-inicio", "page-confirmar", "Con su cédula preparamos su plan a su nombre."))
    P.append(confirmar_page("page-confirmar", "page-cedula", "page-estructura"))
    # Q1 estructura
    P.append(page("page-estructura", f"""{back('page-confirmar')}
  <div id="err-est" class="gobdo-error-summary" role="alert" tabindex="-1" hidden><h2>Hay un problema</h2><ul><li><a href="#est1" onclick="document.getElementById('est1').focus();return false;">Elija una opción para continuar</a></li></ul></div>
  <span class="gobdo-caption">Pregunta 1 de 3</span>
  <h1>¿Cómo quiere operar su negocio?</h1>
  <p>Si no está seguro, elija la primera. Podrá cambiarlo después con orientación.</p>
  <label class="gobdo-radio"><input type="radio" name="estructura" id="est1" value="PF"><span>Yo solo, como Persona Física (PF)<span class="gobdo-radio__hint">Lo más sencillo. No hace falta acto de constitución ni el 1%.</span></span></label>
  <label class="gobdo-radio"><input type="radio" name="estructura" value="EIRL"><span>Una empresa de un solo dueño (EIRL)</span></label>
  <label class="gobdo-radio"><input type="radio" name="estructura" value="SRL"><span>Una empresa con socios (SRL)<span class="gobdo-radio__hint">Necesita acto de constitución y pagar el 1% del capital.</span></span></label>
  <div class="gobdo-actions"><button class="gobdo-btn" onclick="requireRadio('estructura','page-contratar','err-est')">Continuar</button></div>"""))
    # Q2 contratar
    P.append(page("page-contratar", f"""{back('page-estructura')}
  <div id="err-con" class="gobdo-error-summary" role="alert" tabindex="-1" hidden><h2>Hay un problema</h2><ul><li><a href="#con1" onclick="document.getElementById('con1').focus();return false;">Elija una opción para continuar</a></li></ul></div>
  <span class="gobdo-caption">Pregunta 2 de 3</span>
  <h1>¿Va a contratar empleados?</h1>
  <label class="gobdo-radio"><input type="radio" name="contratar" id="con1" value="si"><span>Sí, voy a contratar</span></label>
  <label class="gobdo-radio"><input type="radio" name="contratar" value="no"><span>No, por ahora trabajo solo</span></label>
  <div class="gobdo-actions"><button class="gobdo-btn" onclick="requireRadio('contratar','page-sector','err-con')">Continuar</button></div>"""))
    # Q3 sector
    secopts = [("turismo","Turismo, restaurantes, alojamiento o entretenimiento","page-sector-turismo"),
               ("otro","Otra actividad","page-comprobar")]
    secb = "".join(f'<label class="gobdo-radio"><input type="radio" name="sector" value="{v}" id="sec-{v}"><span>{e(l)}</span></label>' for v,l,_ in secopts)
    P.append(page("page-sector", f"""{back('page-contratar')}
  <div id="err-sec" class="gobdo-error-summary" role="alert" tabindex="-1" hidden><h2>Hay un problema</h2><ul><li><a href="#sec-turismo" onclick="document.getElementById('sec-turismo').focus();return false;">Elija una opción para continuar</a></li></ul></div>
  <span class="gobdo-caption">Pregunta 3 de 3</span>
  <h1>¿De qué trata su negocio?</h1>
  <p>Con esto le mostramos solo los permisos de su sector. (Este alfa desarrolla el sector Turismo como ejemplo.)</p>
  {secb}
  <div class="gobdo-actions"><button class="gobdo-btn" onclick="branchSector()">Continuar</button></div>"""))
    P.append(page("page-sector-turismo", f"""{back('page-sector')}
  <span class="gobdo-caption">Turismo</span>
  <h1>¿Qué tipo de negocio de turismo?</h1>
  <label class="gobdo-radio"><input type="radio" name="turtipo" value="lugar" checked><span>Un lugar que visitan los clientes: hotel, restaurante, bar, tienda de regalos o spa</span></label>
  <label class="gobdo-radio"><input type="radio" name="turtipo" value="otro"><span>Otro tipo (tours, proyecto, casino, parque)</span></label>
  <div class="gobdo-actions"><button class="gobdo-btn" onclick="goTo('page-comprobar')">Continuar</button></div>"""))
    # Compruebe (representative answers)
    P.append(page("page-comprobar", f"""{back('page-sector-turismo')}
  <h1>Compruebe sus respuestas</h1>
  <p>Revise antes de ver su plan.</p>
  <div class="gobdo-summary-list">
    <div class="gobdo-summary-list__row"><div class="gobdo-summary-list__key">Nombre</div><div class="gobdo-summary-list__value fake-data">Ana Lucía Reyes Batista</div><div class="gobdo-summary-list__actions"><a onclick="goTo('page-cedula')">Cambiar</a></div></div>
    <div class="gobdo-summary-list__row"><div class="gobdo-summary-list__key">Estructura</div><div class="gobdo-summary-list__value">Empresa con socios (SRL)</div><div class="gobdo-summary-list__actions"><a onclick="goTo('page-estructura')">Cambiar</a></div></div>
    <div class="gobdo-summary-list__row"><div class="gobdo-summary-list__key">Va a contratar</div><div class="gobdo-summary-list__value">Sí</div><div class="gobdo-summary-list__actions"><a onclick="goTo('page-contratar')">Cambiar</a></div></div>
    <div class="gobdo-summary-list__row"><div class="gobdo-summary-list__key">Actividad</div><div class="gobdo-summary-list__value">Turismo · un lugar que visitan los clientes</div><div class="gobdo-summary-list__actions"><a onclick="goTo('page-sector')">Cambiar</a></div></div>
  </div>
  <div class="gobdo-actions"><button class="gobdo-btn" onclick="goTo('page-plan')">Ver mi plan</button></div>"""))
    # Plan (Confirmation)
    def chk(t): return f'<div class="gobdo-check-item"><span class="gobdo-check-item__mark">✓</span><span>{t}</span></div>'
    def skip(t): return f'<div class="gobdo-check-item gobdo-check-item--skip"><span>—</span><span>{t} <em>(no le aplica)</em></span></div>'
    permlinks = "".join(f'<li><a href="{e(SVC[sid]["url"])}" target="_blank" rel="noopener" style="color:var(--gobdo-navy);">{e(SVC[sid]["name"])}</a></li>' for sid,_ in TOUR)
    P.append(page("page-plan", f"""
  <div class="gobdo-callout gobdo-callout--success"><h1 style="margin-bottom:8px;">Su plan para empezar</h1><p style="margin-bottom:0;">Guardado como <strong class="fake-data">PLAN-2026-00817</strong>. Le enviamos una copia a <span class="fake-data">a.reyes@example.do</span>.</p></div>
  <h2>Sus pasos para formar la empresa</h2>
  {chk('1. Compruebe que está listo')}
  {chk('2. Elija su estructura legal — <strong>SRL</strong>')}
  {chk('3. Reserve su nombre comercial (ONAPI)')}
  {chk('4. Prepare sus documentos de constitución (SRL)')}
  {chk('5. Pague el 1% de constitución (SRL)')}
  {chk('6. Regístrese en el Registro Mercantil')}
  {chk('7. Obtenga su RNC (DGII)')}
  {chk('8. Regístrese como empleador (TSS) — <strong>porque va a contratar</strong>')}
  <p style="font-size:15px;margin-top:8px;">Los pasos 3 a 8 los puede hacer juntos en el portal <strong>Crear Empresas (VUF)</strong>.</p>
  <h2>Permisos de su sector (paso 9)</h2>
  <p>Para un establecimiento turístico suelen aplicar:</p>
  <ul class="gobdo-list">{permlinks}</ul>
  <h2>Para crecer (paso 10)</h2>
  <ul class="gobdo-list">
    <li><a href="https://observicios.gob.do/services/5842" target="_blank" rel="noopener" style="color:var(--gobdo-navy);">Préstamos Mipymes</a> — PROMIPYME</li>
    <li><a href="https://observicios.gob.do/services/4802" target="_blank" rel="noopener" style="color:var(--gobdo-navy);">Certificaciones CONFOTUR</a> — Ministerio de Turismo <span class="gobdo-tag">Sugerido: Turismo</span></li>
  </ul>
  <div class="gobdo-actions"><button class="gobdo-btn gobdo-btn--secondary" onclick="alert('En un servicio real esto guardaría su plan en su cuenta gob.do.')">Guardar mi plan</button></div>"""))

    asums = f"""<h3>About the user</h3><ul>
    {a_user('A personalised checklist ("solo lo que le toca") reduces overwhelm more than the full list, for a first-time founder. This is the core hypothesis vs Variant 1. (Standard 1)')}
    {a_user('Founders can answer estructura (PF/EIRL/SRL) up front — or the plan must tolerate "no estoy seguro". (Standard 4)')}
    {a_user('People trust a plan that hides steps as much as one that shows everything — hiding step 4/5 for a PF does not feel like something is missing. (Standard 5)')}
    </ul><h3>About the data</h3><ul>
    {a_inst('The applicability rules are right: PF skips constitution (4) and the 1% (5); TSS (8) only if hiring; the 1% is SRL-only. (Ley 479-08)')}
    {a_inst('The 4 Turismo permits and their observicios links are the correct set for a tourism establishment.')}
    {a_data('The three questions (estructura, hiring, sector) are enough to personalise usefully — more questions may be needed, or fewer.')}
    </ul><h3>About the platform</h3><ul>
    {a_ogtic('GobID returns name + contact from the cédula for a persona-física founder before any company exists. (Standard 7)')}
    {a_ogtic('A saved "plan" can live in the citizen\'s gob.do account and be revisited.')}
    {a_gap('The prototype shows one representative plan (SRL + hiring + tourism); it does not compute the plan from the actual answers.')}
    </ul><h3>About policy</h3><ul>
    {a_policy('Storing the founder\'s answers and emailing a plan is permitted under Ley 172-13 for this purpose. (Standard 11)')}
    </ul>"""
    write("prototype-2-asistente-plan", "Arme su plan", 2, "Asistente: arme su plan (personalised checklist)", "".join(P), asums)


# ============================ PROTOTYPE 3 ============================
# "Ventanilla única primero" — reframe the journey around the ONE existing VUF
# "Crear Empresas" transaction (steps 3–8) + the Punto GOB assisted channel.
# Hypothesis: framing as one transaction + help reduces drop-off vs 10 steps.
def build_p3():
    P = []
    P.append(page("page-inicio", f"""
  <h1>Empezar un negocio</h1>
  <p><strong>Casi todo se hace en un solo lugar.</strong> El registro de su empresa — nombre, Registro Mercantil, el 1%, RNC y empleador — es un solo trámite en el portal <strong>Crear Empresas</strong>.</p>
  <p>Le acompañamos antes (dos decisiones) y después (permisos y apoyos), pero el registro es una sola parada.</p>
  <div class="gobdo-callout gobdo-callout--help"><strong>¿Prefiere hacerlo acompañado?</strong><p style="margin:8px 0 0;">En un <strong>Punto GOB</strong> lo hacen con usted, gratis. O marque <strong>*462</strong> y le guían por teléfono. No tiene que hacerlo solo.</p></div>
  <div class="gobdo-actions"><button class="gobdo-btn gobdo-btn--start" onclick="goTo('page-cedula')">Empezar por internet</button>
  <button class="gobdo-btn gobdo-btn--secondary" onclick="alert('En un servicio real esto mostraría el Punto GOB más cercano en un mapa.')">Buscar un Punto GOB</button></div>""", active=True))
    P.append(cedula_page("page-cedula", "page-inicio", "page-confirmar", "Con su cédula preparamos su registro a su nombre en Crear Empresas."))
    P.append(confirmar_page("page-confirmar", "page-cedula", "page-listo"))
    P.append(page("page-listo", f"""{back('page-confirmar')}
  <span class="gobdo-caption">Su registro</span>
  <h1>Esto es lo que hará hoy</h1>
  <p>Antes de registrar, ya debe tener dos cosas decididas:</p>
  <ul class="gobdo-list">
    <li><strong>Su estructura</strong> — Persona Física, EIRL o SRL (Ley 479-08)</li>
    <li><strong>Un nombre</strong> — para apartarlo en la ONAPI</li>
  </ul>
  <div class="gobdo-callout"><strong>En un solo trámite (Crear Empresas):</strong>
  <ul class="gobdo-list" style="margin:8px 0 0;">
    <li>Reserva del nombre comercial (ONAPI)</li>
    <li>Registro Mercantil (Cámara de Comercio)</li>
    <li>Pago del 1% de constitución (DGII, si es SRL)</li>
    <li>Su RNC (DGII)</li>
    <li>Registro como empleador (TSS, si va a contratar)</li>
  </ul></div>
  <p style="font-size:15px;color:var(--gobdo-grey-mid);">Los permisos de su sector y los apoyos para crecer vienen después — se los mostramos al final.</p>
  <div class="gobdo-actions"><button class="gobdo-btn" onclick="goTo('page-comprobar')">Continuar</button></div>"""))
    P.append(page("page-comprobar", f"""{back('page-listo')}
  <h1>Compruebe sus respuestas</h1>
  <p>Revise antes de ir a Crear Empresas.</p>
  <div class="gobdo-summary-list">
    <div class="gobdo-summary-list__row"><div class="gobdo-summary-list__key">Nombre</div><div class="gobdo-summary-list__value fake-data">Ana Lucía Reyes Batista</div><div class="gobdo-summary-list__actions"><a onclick="goTo('page-cedula')">Cambiar</a></div></div>
    <div class="gobdo-summary-list__row"><div class="gobdo-summary-list__key">Cédula</div><div class="gobdo-summary-list__value fake-data">001-1234567-8</div><div class="gobdo-summary-list__actions"><a onclick="goTo('page-cedula')">Cambiar</a></div></div>
    <div class="gobdo-summary-list__row"><div class="gobdo-summary-list__key">Qué hará ahora</div><div class="gobdo-summary-list__value">Registrar su empresa en Crear Empresas (VUF)</div><div class="gobdo-summary-list__actions"></div></div>
  </div>
  <div class="gobdo-actions"><button class="gobdo-btn" onclick="goTo('page-confirmacion')">Ir a Crear Empresas</button></div>"""))
    P.append(page("page-confirmacion", f"""
  <div class="gobdo-callout gobdo-callout--success"><h1 style="margin-bottom:8px;">Le estamos llevando a Crear Empresas</h1><p style="margin-bottom:0;">Su referencia es <strong class="fake-data">EN-2026-04471</strong>. Anótela o tómele una foto.</p></div>
  <p style="font-size:15px;color:var(--gobdo-grey-mid);"><span class="fake-data">En este prototipo el enlace a Crear Empresas es ficticio.</span></p>
  <h2>Qué pasa ahora</h2>
  <ul class="gobdo-list">
    <li>Complete el registro en <strong>Crear Empresas (VUF)</strong>. Guarde su referencia.</li>
    <li>Cuando termine, le mostramos <strong>si su actividad necesita algún permiso</strong> (paso 9).</li>
    <li>Y los <strong>apoyos para crecer</strong>: financiamiento, incentivos y formación (paso 10).</li>
    <li>¿Se traba? Vaya a un <strong>Punto GOB</strong> o marque <strong>*462</strong> con su referencia.</li>
  </ul>
  <div class="gobdo-actions">
    <button class="gobdo-btn gobdo-btn--secondary" onclick="alert('En un servicio real esto abriría el cuestionario de permisos (paso 9).')">Ver si necesito permisos</button>
    <button class="gobdo-btn gobdo-btn--secondary" onclick="alert('En un servicio real esto abriría los apoyos para crecer (paso 10).')">Ver apoyos para crecer</button>
  </div>""", active=False))

    asums = f"""<h3>About the user</h3><ul>
    {a_user('Framing the journey as ONE transaction ("casi todo en un solo lugar") + a visible assisted channel reduces drop-off for first-time founders vs presenting 10 discrete steps. Core hypothesis vs Variants 1 & 2. (Standard 1, 5)')}
    {a_user('Leading with Punto GOB / *462 is reassuring, not a signal that "the digital service is too hard". (Standard 3)')}
    {a_user('Founders arrive already able to decide estructura and a name, or bounce at the "esto es lo que hará hoy" page. (Standard 4)')}
    </ul><h3>About the data</h3><ul>
    {a_inst('Crear Empresas (VUF, vu.formalizate.gob.do) really does bundle ONAPI → Registro Mercantil → 1% → RNC → TSS in one transaction, for SRL/EIRL/PF. (PLAN.md, confirmed from the VUF home page)')}
    {a_inst('MICM/VUF would accept a hand-off carrying the citizen\'s GobID identity so they do not re-enter it. (Standard 7)')}
    {a_data('Drop-off in the current multi-institution journey is high enough to justify the single-transaction framing — needs analytics.')}
    </ul><h3>About the platform</h3><ul>
    {a_ogtic('gob.do can deep-link into VUF with an authenticated GobID session so the founder is not re-authenticated. (Standard 7)')}
    {a_ogtic('A shared reference number can follow the founder across gob.do → VUF → observicios permits.')}
    {a_gap('Permits (step 9) and grow (step 10) are shown as "después" stubs here, not built out — they live in Variant 1.')}
    </ul><h3>About policy</h3><ul>
    {a_policy('Passing GobID identity from gob.do to the MICM VUF transaction is permitted under Ley 172-13. (Standard 11)')}
    </ul>"""
    write("prototype-3-ventanilla-unica", "Empezar un negocio", 3, "Ventanilla única primero (single transaction + assisted)", "".join(P), asums)


def write(slug, title, n, variant_name, pages_html, asums_html):
    branch_js = "<script>function branchSector(){var c=document.querySelector('input[name=sector]:checked');var s=document.getElementById('err-sec');if(!c){s.hidden=false;s.focus();return;}s.hidden=true;goTo(c.value==='turismo'?'page-sector-turismo':'page-comprobar');}</script>"
    doc = head(title, n, variant_name) + pages_html + FOOTER + aside(asums_html) + (branch_js if n == 2 else "")
    outdir = HERE / slug
    outdir.mkdir(exist_ok=True)
    (outdir / "index.html").write_text(doc)
    print(f"wrote {slug}/index.html")


def main():
    build_p1(); build_p2(); build_p3()


if __name__ == "__main__":
    main()
