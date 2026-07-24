# DR prototypes

Clickable HTML prototypes of Dominican government services, in the gob.do /
drimstack house style. Each is a self-contained `index.html` — open it in a
browser, no build step.

## Projects

### `empezar-un-negocio/` — Empezar un negocio
Start-a-business journey (a *momento de vida* on the gob.do Portal Único).
Source: the `DR-gob.do-momentos-de-vida` build.

| Prototype | Idea |
|-----------|------|
| `prototype-1-guia-paso-a-paso/` | The full step-by-step guide |
| `prototype-2-asistente-plan/` | Personalised checklist — three questions, only the steps that apply. **`index-v2.html`** adds real cost + time per step (see `CHANGELOG-v2.md`) |
| `prototype-3-ventanilla-unica/` | Single-window transactional flow |

### `certificacion-uso-de-suelo/` — Certificación de Uso de Suelo (ADN)
Construction-permit content for the **Ayuntamiento del Distrito Nacional**
(adn.gob.do). Source: the `ADN-scraper` repo. `REVIEW.md` is the content
review that briefed these; `_house-style.html` is the shared style reference.

| Prototype | Idea |
|-----------|------|
| `prototype-1-pagina-de-servicio/` | Rewrite the service page |
| `prototype-2-reune-documentos/` | Help the applicant gather documents first |
| `prototype-3-solicitud-en-linea/` | Take the whole trámite online |

## Browse them all

```bash
cd ~/repos/DR/DR-prototypes
python3 -m http.server 8000
# then open http://localhost:8000/
```

## Provenance

These are **copies**, organised here as a common home. The originals still live in:
- `~/repos/DR-gob.do-momentos-de-vida/data/work/drimstack-build/`
- `~/repos/DR/ADN-scraper/prototypes/` (the scraper stays with its own repo)

Every prototype carries an inline "alfa" banner and an assumptions panel — they
are prototypes for testing, not real services.
