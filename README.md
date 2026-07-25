# DR prototypes

Clickable HTML prototypes of Dominican government services, in the gob.do /
drimstack house style. Each is a self-contained `index.html` — open it in a
browser, no build step.

**▶ Live: <https://ivyleavedtoadflax.github.io/DR-prototypes/>** — the landing
page (`index.html`) lists them all.

## Projects

### Empezar un negocio
Start-a-business journey (a *momento de vida* on the gob.do Portal Único).

| Prototype | Idea |
|-----------|------|
| [1 · Guía paso a paso](https://ivyleavedtoadflax.github.io/DR-prototypes/empezar-un-negocio/prototype-1-guia-paso-a-paso/index.html) | The full step-by-step guide |
| [2 · Asistente: arme su plan](https://ivyleavedtoadflax.github.io/DR-prototypes/empezar-un-negocio/prototype-2-asistente-plan/index-v2.html) | Personalised checklist — three questions, only the steps that apply. **v2** adds real cost + time per step ([v1](https://ivyleavedtoadflax.github.io/DR-prototypes/empezar-un-negocio/prototype-2-asistente-plan/index.html), [changelog](empezar-un-negocio/prototype-2-asistente-plan/CHANGELOG-v2.md)) |
| [3 · Ventanilla única](https://ivyleavedtoadflax.github.io/DR-prototypes/empezar-un-negocio/prototype-3-ventanilla-unica/index.html) | Single-window transactional flow |
| [4 · Solicitud guiada](https://ivyleavedtoadflax.github.io/DR-prototypes/empezar-un-negocio/prototype-4-solicitud-guiada/index.html) | **Research-driven end-to-end redesign** of the full trámite, from a 6-persona study of the live Ventanilla Única — honest cost/tax before the form, a company-type helper, an accessible step-by-step wizard, and a working passport/non-resident path. **v2** covers the full mega-form ([v1](https://ivyleavedtoadflax.github.io/DR-prototypes/empezar-un-negocio/prototype-4-solicitud-guiada/index-v1.html), [gap analysis](empezar-un-negocio/prototype-4-solicitud-guiada/GAP-ANALYSIS.md)) |

### Certificación de Uso de Suelo (ADN)
Construction-permit content for the **Ayuntamiento del Distrito Nacional**
(adn.gob.do). `REVIEW.md` is the content review that briefed these;
`_house-style.html` is the shared style reference.

| Prototype | Idea |
|-----------|------|
| [1 · Página de servicio](https://ivyleavedtoadflax.github.io/DR-prototypes/certificacion-uso-de-suelo/prototype-1-pagina-de-servicio/index.html) | Rewrite the service page |
| [2 · Reúna documentos](https://ivyleavedtoadflax.github.io/DR-prototypes/certificacion-uso-de-suelo/prototype-2-reune-documentos/index.html) | Help the applicant gather documents first |
| [3 · Solicitud en línea](https://ivyleavedtoadflax.github.io/DR-prototypes/certificacion-uso-de-suelo/prototype-3-solicitud-en-linea/index.html) | Take the whole trámite online |

Every prototype carries an inline "alfa" banner and an assumptions panel — they
are prototypes for testing, not real services.

## Reviewing changes

Open a pull request and a bot comments a link to a live preview of that branch
at `…github.io/DR-prototypes/pr-preview/pr-N/`. Click it to see the prototypes
rendered before merging; it updates on every push and is deleted when the PR
closes. Merging to `main` republishes the live site.
