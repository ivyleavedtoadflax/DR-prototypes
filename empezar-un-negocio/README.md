# Empezar un negocio — drimstack build

Three candidate prototypes of the gob.do "Empezar un negocio" (start a business)
journey, produced by `/drimstack:build`. They exist to be **tested against each
other**, not to be the answer. The output of a build is the starting point for an
alpha; the alpha is what the team learns from testing.

- **Owner (assumed):** OGTIC (cross-government front door on gob.do), coordinating
  MICM/VUF, ONAPI, DGII, TSS and the sector regulators.
- **Cohort (assumed):** first-time founder, no prior company, mixed digital
  literacy, **on a phone.**
- **Standards anchored:** drimstack 1, 3, 4, 5, 7; GOV.UK Design Principles 1, 4, 6, 7.
- **Data:** real service names, links, requirements, costs and times from
  observicios.gob.do (`../permit-detail/services.json`, `../../candidates_classified.csv`)
  and the journey structure from `PLAN.md` / `docs/decision-tree.json`. Nothing about
  a trámite is invented. Identity/payment data is mock and marked "ficticio".

## The three hypotheses

| # | Prototype | The bet it makes |
|---|---|---|
| 1 | **Guía paso a paso** (`prototype-1-guia-paso-a-paso/`) | A curated, ordered list of the 10 steps lets a founder self-navigate and go to each institución's trámite on their own. Better *signposting* to services that already exist. |
| 2 | **Asistente: arma tu plan** (`prototype-2-asistente-plan/`) | Three questions (estructura, hiring, sector) + a GobID lookup produce a *personalised* checklist showing only the steps and permits that apply — personalisation beats a generic list at reducing overwhelm. |
| 3 | **Ventanilla única primero** (`prototype-3-ventanilla-unica/`) | Reframe the whole journey around the **one** transaction that already bundles steps 3–8 (VUF "Crear Empresas"), with the Punto GOB assisted channel up front — one parada + help beats ten steps for first-time founders. |

They are deliberately *different structures*, not three coats of paint: self-serve
signposting vs. personalised wizard vs. single-transaction-with-assistance. Testing
them produces real signal about which mental model fits the citizen.

The chrome (official banner, navy header, alfa banner, footer) is **identical**
across all three — so testing compares the journey, not the styling.

## How to open them

Each prototype is a single self-contained `index.html`. Open in any browser:

```
cd data/work/drimstack-build
python3 -m http.server 8000
# open http://localhost:8000/prototype-1-guia-paso-a-paso/
```

Or open the file directly. Walk each one **on a phone** and on a slow connection —
Standard 3 begins there. Toggle the **"Show assumptions"** button (charcoal banner)
to see what each prototype is betting on.

## What's inside each prototype

- The full gob.do-style flow: **Inicio → (preguntas / pasos) → Compruebe sus
  respuestas → Confirmación / plan** (Variant 1 is signposting, so it ends at the
  trámite hand-off rather than a payment confirmation — an honest design difference).
- One thing per page; "Volver" on every page except Inicio.
- GobID cédula lookup instead of retyping identity (Standard 7). The person it
  "finds" (Ana Lucía Reyes Batista) is **fake** and marked so.
- A toggleable assumptions panel, every claim tagged `[VERIFY WITH USERS / INSTITUCIÓN
  / OGTIC / POLICY / DATA]` or `[KNOWN GAP]`.
- "This is fake" markers on every mock reference number and identity field.

## Regenerate

Pages are generated, not hand-edited:

```
python3 build_prototypes.py   # reads ../permit-detail/{journey,services}.json
```

## Next

- `assumptions.md` — the consolidated list across all three, ranked.
- `test-plan.md` — who to recruit, how many, what good signal looks like.
- After testing, bring feedback into **`/drimstack:iterate`** for the next version.
