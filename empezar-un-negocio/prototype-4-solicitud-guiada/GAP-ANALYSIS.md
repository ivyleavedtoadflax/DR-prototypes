# Prototype-4 "Solicitud guiada" — mega-form gap analysis

**Question answered:** what fields/options of the real *Ventanilla Única de Formalización*
mega-form (Paso 2, ~69 fields, 23 dropdowns, 5 repeaters, 10–12 sections) are **missing**
from prototype-4's guided wizard.

**Method:** field-level inventory extracted from all 6 persona runs
(`../../../DR-gob.do-momentos-de-vida/docs/ur-ventanilla-formalizacion/runs/persona-1..6`),
consolidated and diffed against `index.html`. Ground truth, not opinion.

**Important framing:** prototype-4 *deliberately* replaces the 69-field mega-form with a
one-thing-per-page wizard (rec 8). So "missing" ≠ "bug". Some cuts are the point. This list
separates **data the real registration genuinely needs** (a real submit fails without it)
from **fidelity/edge items**. Decide per-item whether v2 collects it, defers it, or pre-fills it.

---

## What the real mega-form has, section by section — and prototype-4's coverage

Legend: ✅ in prototype · ⚠️ partial · ❌ missing

### 1 · Datos solicitud de formalización
| Real field | Type | Proto |
|---|---|---|
| Cámara de comercio | select (req) | ❌ |
| Tipo societario (SRL/EIRL/PF) | select (req) | ✅ (via 2-Q helper) |
| ¿Tienes nombre comercial? | select Sí/No | ✅ (reworded) |
| — on **Sí**: Nº certificado, Nombre comercial, **Fecha vencimiento**, **Titular** | text/date | ⚠️ (only cert Nº) |
| — on **No**: Nombre comercial | text | ✅ |
| Actividad principal (CIIU) | lookup (req) | ✅ (as "actividad") |
| Actividad secundaria (CIIU) | lookup (opt) | ❌ |
| Productos y servicios (≥1) | repeater | ❌ |
| Objeto de la empresa | textarea (req) | ❌ |

### 2 · Datos del solicitante
| Real field | Type | Proto |
|---|---|---|
| Tipo de solicitante (SRL-only) | select (req) | ❌ (n/a-ish) |
| Tipo de documentación (Cédula/Pasaporte) | select | ✅ |
| Número cédula / pasaporte | text + JCE lookup | ✅ |
| Nombre / Apellido | text (auto or manual passport) | ✅ |
| **Correo electrónico + Confirmar** | email (req) | ❌ **never collected** |
| **Teléfono** | text (req) | ❌ |
| **Celular** (DR-format enforced) | text (req) | ❌ |
| **Sexo** | select (req) | ❌ |
| **Estado civil** | select (req) | ❌ |
| **Nacionalidad** | select (req) | ❌ |
| Provincia → **Municipio → Sector** cascade | 3× select (req) | ⚠️ (provincia only) |
| Calle / Número | text (req) | ⚠️ (combined "Calle y número") |
| Código postal | text (opt) | ❌ |
| ¿Usted es un representante? | checkbox | ❌ |

### 3 · Datos de la sede — ❌ **whole section missing**
Nombre de la sede (req) · ¿misma dirección que el solicitante? (select) · Teléfono de la empresa (req) · Página web (opt)

### 4 · Gerencia — ❌ **whole section missing**
"Gerente" repeater = full person sub-form (Tipo de accionista, Tipo de cargo [multi-tag],
Tipo de beneficiario, doc identidad, Nombres, Apellidos, correo×2, tel, cel, sexo, estado
civil, nacionalidad, address cascade). *Real form wrongly shows this for single-owner EIRL
then rejects the owner — rec 8 says suppress it for EIRL.*

### 5 · Propietario / Socios / Representantes (SRL) — ❌ **whole section missing** (acknowledged not built)
Socios repeater. Per socio: Tipo de accionista (**Persona/Empresa**), Tipo de relación/cargo
(multi-tag taxonomy: SOCIO / SOCIO INCAPAZ / SOCIO MENOR / MIEMBRO / BENEF FINAL… /
USUARIO ADMIN E-CF / RESPONSABLE CUMPLIMIENTO), Clasificación (GERENTE), Representante TSS
(checkbox), **Cantidad de cuotas**, doc identidad, Nombres/Apellidos (JCE), correo×2, tel,
cel, sexo, estado civil, nacionalidad, address cascade. Mechanics: cuotas auto-sum → "Total
cuota"; "Costo por cuotas" = capital ÷ cuotas; gerente can be a non-owner (MIEMBRO+GERENTE).

### 6 · Datos financieros — ❌ **whole section missing**
Capital aportado / Capital social (req; **mín RD$200, Ley 68-19**) · Cuenta bancaria (req) ·
Total cuota (auto, SRL) · Costo por cuotas (auto, SRL). *Note: the prototype's cost table
assumes RD$100k capital but never asks for capital — DGII 1% depends on it.*

### 7 · Información empresarial — ❌ **whole section missing**
Fecha de inicio de operaciones (date, **future-only** — rec 13 bug) · Fecha de cierre fiscal ·
Duración de la empresa · Duración órgano de gestión (años) · Sucursales · ¿Tiene empleados? (→ TSS)

**PF-only sub-block "Determinación / Obligaciones" (DGII tax classification)** — ❌ missing:
Obtención de ingresos · Pago de servicios/personal · Lugar de actividad · ¿Posee bienes
inmuebles? · ¿Posee título de propiedad? · Ventas para el mercado · Sector económico ·
Capital general (patrimonio). *Collects the data DGII uses for RST/régimen but never outputs the regime.*

### 8 · Referencias comerciales — ❌ missing (repeater)
### 9 · Referencias bancarias — ❌ missing (repeater)

### 10 · Detalles de la factura (comprobante fiscal / NCF) — ❌ **whole section missing**
Tipo de factura (req) · Tipo de documento de identidad · Nombre · Apellido

### 11 · Documentos requeridos a adjuntar — ⚠️ partial
Cédula del solicitante ✅ · Carta Bancaria (EIRL) ✅ · Recibo notario (EIRL) ✅ · Cédulas/
pasaportes de socios (SRL) ✅ · Poder (no-residente) ✅ · **Cédula del gerente** ❌ ·
constitutivos auto-generados (note not surfaced) ❌

### 12 · Revisión de documentos — ❌ missing
Servicios seleccionados (read-only) · Documentos table (Documento | Fecha | **Cant. Original |
Cant. Copias** steppers) — feeds the Paso-3 fee.

---

## Prioritised backlog for v2 (pick from these)

### P0 — real submission fails without it (all users, all company types)
1. **Contact block** — Correo + Confirmar, Teléfono, Celular (DR-format). *Currently faked in the confirm card, never collected.* — small
2. **Full address cascade** — Provincia → Municipio → Sector, split Calle/Número, Código postal. — medium
3. **Capital social + Cuenta bancaria** — drives the DGII 1% and the whole cost table. — small-medium
4. **Datos de la sede** — Nombre de la sede, ¿misma dirección?, Teléfono empresa, Página web. — medium
5. **Información empresarial** — fecha inicio ops (+ the rec-13 "¿ya opera?" fix), cierre fiscal, duración, órgano de gestión, sucursales, ¿empleados? — medium

### P1 — company-type completeness (the path only "works" with these)
6. **SRL socios repeater** — Persona/Empresa, cuotas auto-sum, role taxonomy, non-owner gerente. — large
7. **Gerencia section** — gerente sub-form; **suppress for single-owner EIRL** (rec 8). — medium-large
8. **Persona Física fiscal block** + hide share-capital jargon for PF (rec 13). — medium
9. **Applicant Sexo / Estado civil / Nacionalidad**. — small

### P2 — fiscal, invoice, references, copies
10. **Detalles de la factura (NCF)** — tipo de factura, doc, nombre, apellido. — small-medium
11. **Régimen tributario as a real output** (RST/ITBIS/ISR) — currently only alluded to. — small (content)
12. **Referencias comerciales + bancarias** repeaters. — medium
13. **Revisión de documentos** — copies table (Cant. Original / Copias). — medium
14. **Actividad secundaria + Productos y servicios + Objeto de la empresa**. — small-medium

### P3 — edge & robustness
15. **ONAPI "Sí" full cert sub-form** — Nº, Fecha vencimiento, Titular. — small
16. **Representative (non-resident) as structured fields** + poder upload (proto only warns). — medium
17. **Cédula del gerente** / per-socio doc granularity. — small
18. **Cámara de comercio** selector. — small

---

## The tension to decide first
Prototype-4's whole thesis is *replace* the 69-field monster with one-thing-per-page +
prefill + defer. Naively adding every field back recreates the monster. For each item above,
v2 can: **(a) collect it** (own page/step), **(b) prefill it** from GobID/known data, or
**(c) defer it** to "guardar y continuar" / a caseworker. Recommended default: collect only
what's legally required to submit (P0 + the chosen company-type path), prefill identity/contact
from GobID, defer references/copies. Keep the wizard shape.
