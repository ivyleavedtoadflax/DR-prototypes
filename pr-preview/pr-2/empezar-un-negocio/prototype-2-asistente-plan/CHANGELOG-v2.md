# Prototype 2 — Asistente: arme su plan — changelog

## v2 — 2026-07-24

**What changed:** Added real cost and time to each of the eight formation steps.

Directly answers the top finding from the Ventanilla Única research run
(`docs/ur-ventanilla-formalizacion/runs/persona-1/report.md`): *"Make cost honest"* —
the real service advertises "GRATIS" and then contradicts it. v2 shows the real picture
up front, before the founder invests effort.

### Per-step cost + time (2026 reference figures)

| # | Step | Cost | Time | Source |
|---|------|------|------|--------|
| 1 | Compruebe que está listo | Gratis | minutos | — (internal step) |
| 2 | Elija su estructura legal (SRL) | Gratis | orientación | — (internal step) |
| 3 | Reserve nombre comercial (ONAPI) | RD$4,755 | 1 día lab. | onapi.gov.do |
| 4 | Documentos de constitución (notario) | RD$15,000–35,000 | 1–5 días | Cámara de Comercio Sto. Dgo. / notary market |
| 5 | Pague el 1% de constitución (DGII) | 1% del capital, mín. RD$1,000 | el mismo día | Ley 173-07, art. 10 (DGII) |
| 6 | Registro Mercantil (Cámara de Comercio) | RD$8,000–15,000 (según capital) | 3–15 días | camaraprovinciasantodomingo.do tarifario |
| 7 | Obtenga su RNC (DGII) | Gratis | 6–7 días lab. | dgii.gov.do |
| 8 | Regístrese como empleador (TSS) | Gratis | 5 días lab. | tss.gob.do |

**Totals shown in the UI:** desde RD$28,000 (+1% del capital) · 3 a 6 semanas.

### Notes / caveats
- Figures are **2026 reference values**, flagged in the assumptions panel with a
  `Verify with data` tag — not marked `fake-data`, because they come from real sources,
  but they need confirming before being quoted to a user.
- Steps 4 and 6 scale with the company's authorized capital and the chosen notary — the
  ranges reflect that, they are not a single quote.
- EIRL and foreign companies are exempt from the 1% (step 5). The plan currently models an
  SRL that is hiring; a full build would recompute per the founder's actual answers
  (already listed as a known gap in the assumptions panel).

### Files
- `index-v2.html` — the iteration. `index.html` (v1) is unchanged, kept for comparison.

## v2.1 — 2026-07-24

**What changed:** Extended the same cost + time treatment to paso 9 (sector permits)
and paso 10 (growth services) — previously bare links with no cost/time shown.

### Cost + time added

| Step | Service | Cost | Time | Source (observicios.gob.do id) |
|------|---------|------|------|---------------------------------|
| 9 | Licencia — Establecimiento de hospedaje | RD$5,000–30,000 | 45 días lab. | 4855 |
| 9 | Licencia — Expendio de alimentos y bebidas | RD$2,000–10,000 (discotecas RD$20,000) | 45 días lab. | 4850 |
| 9 | Licencia — Giftshop | RD$1,000–8,000 | 10–20 min ⚠ | 4875 |
| 9 | Licencia — Centro de masajes (Spa) | RD$25,000 | 45 días lab. | 4897 |
| 10 | Préstamos Mipymes (PROMIPYME) | Gratis (solicitud) | 3–5 días lab. | 5842 |
| 10 | Certificaciones CONFOTUR | Gratis | 5 días lab. | 4802 |

### Notes / caveats
- Figures pulled from `gob.do-scraping/docs/exports/observicios-service-detail.csv`
  (`cost` / `response_time` columns), same repo that sourced the paso 1–8 figures.
  Flagged `Verify with data` in the assumptions panel, same as the formation steps.
- ⚠ The giftshop record's time (10–20 minutos) is inconsistent with its three sibling
  MITUR licences, all 45 días laborables — likely a data-entry error in the source
  export. Flagged explicitly in the assumptions panel; needs confirming with MITUR.
