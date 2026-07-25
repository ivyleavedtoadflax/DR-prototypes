# Consolidated assumptions — Empezar un negocio build

Every assumption the three prototypes make that isn't yet evidence-led. Ranked by
how badly the journey breaks if the assumption is wrong. Each prototype also carries
its own subset in its right-hand panel.

Tags: `[USERS]` test with citizens · `[INSTITUCIÓN]` confirm with the owning body
(MICM/VUF, ONAPI, DGII, TSS, MITUR) · `[OGTIC]` platform team · `[POLICY]` legal
(Ley 479-08, Ley 172-13, Ley 107-13) · `[DATA]` analytics/research · `[GAP]` known
placeholder.

## Highest risk — wrong here and the journey fails

1. `[USERS]` **Which mental model fits?** Ordered list (V1) vs. personalised plan
   (V2) vs. one-transaction-with-help (V3). This is the whole reason there are three
   prototypes. Everything else is secondary. (Standard 1)
2. `[INSTITUCIÓN]` **The VUF bundle is real and current** — Crear Empresas
   (vu.formalizate.gob.do) actually does ONAPI → Registro Mercantil → 1% → RNC → TSS
   in one transaction. V3 is built entirely on this; V1/V2 state it. Sourced from
   PLAN.md + the VUF home page; needs MICM confirmation it still holds in 2026.
3. `[OGTIC]` **GobID can pre-fill a founder's identity before any company exists**
   (persona física via cédula/JCE) and hand it to VUF without re-auth. All three
   assume no retyping. (Standard 7)
4. `[POLICY]` **Applicability rules in V2 are legally right**: PF skips constitution
   (step 4) and the 1% (step 5); the 1% is SRL-only; TSS (step 8) only if hiring.
   (Ley 479-08) A wrong rule means the personalised plan omits a required step.

## Medium risk — wrong here and content misleads

5. `[INSTITUCIÓN]` The 4 Turismo establishment permits (hospedaje 4855, A&B 4850,
   giftshop 4875, spa 4897) are the correct set for "a place guests visit", and the
   requisitos / costos / tiempos scraped from observicios are current.
6. `[USERS]` First-time founders can answer "estructura" (PF/EIRL/SRL) up front (V2),
   or the flow must tolerate "no estoy seguro" and still produce a useful plan.
7. `[USERS]` Leading with Punto GOB / *462 (V3) reads as reassurance, not as "the
   digital service is too hard to use alone". (Standard 3)
8. `[DATA]` Drop-off in today's multi-institution journey is high enough to justify
   V3's single-transaction reframing. Currently unmeasured.
9. `[USERS]` Sending citizens out to each institución's own portal mid-journey (V1)
   doesn't lose them. (Standard 5)

## Lower risk / known gaps

10. `[GAP]` Only the Turismo → establecimiento permit branch is built. The other 5
    sectors and the tourism sub-branches (tours, projects, gambling, leisure) are stubs.
11. `[GAP]` V2 shows one representative plan (SRL + hiring + tourism); it does not
    compute the plan from the actual answers (a prototype, not the service).
12. `[POLICY]` Storing a founder's answers and emailing a "plan" (V2) and passing
    identity gob.do → VUF → observicios (V3) are permitted under Ley 172-13 for this
    purpose. (Standard 11)
13. `[DATA]` Three questions (V2) are the right number to personalise usefully —
    could need fewer (less friction) or more (sharper plan).
14. `[INSTITUCIÓN]` The 8-step order and the step→institución mapping (ONAPI, DGII,
    Cámara, TSS) are current and complete for the "most people" path.

## Cross-cutting (all three)

- `[USERS]` Plain-language labels ("¿De qué trata su negocio?" not "Seleccione la
  actividad económica CIIU") feel respectful, not patronising. (Standard 4)
- `[USERS]` The mobile layout works on a real phone on a slow connection outside the
  capital. (Standard 3, 5) — verify on-device, not just in a narrow browser window.
- `[POLICY]` Showing another portal's trámite (observicios, VUF) from gob.do, with its
  real cost, is permitted and the links are stable.
