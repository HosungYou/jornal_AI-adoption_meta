# Paper B Source-Adjudication Decisions Before Reference Freeze

Date: 2026-06-08

Status: researcher-confirmed adjudication decisions for Step 3. These decisions
do not complete the Step 4 source-anchored adjudicated human reference standard
freeze and do not authorize Step 5 LLM comparison or MASEM substitution.

## Decision

The following source-adjudication rules are accepted for the Paper B Phase 1+2
validation corpus:

1. Use `S195` as the canonical duplicate audit row and mark `S206` as duplicate
   of `S195`.
2. Do not retain `S014` indirect mediated effects through perceived risk as
   direct target-pair reference values.
3. Preserve `S021` pre/post values as separate `T1` and `T2` strata if the
   study is retained.
4. Treat `S121` student and teacher estimates as separate samples if teacher
   values are extracted.
5. Exclude `S202` from the Paper B target MASEM matrix because AI-driven LMS
   administrative automation is outside the current AI-adoption target universe.
6. Treat `S014` academic researchers/faculty as an eligible educational
   population under the Paper B population rule.
7. Treat `S014`, `S021`, `S056`, and `S092` as source-accessible for Step 3
   because their PDFs were found in the local OneDrive PDF archive and copied to
   the ignored local adjudication source-PDF folder. This source access does not
   itself freeze extractable values.

## Assignment Check

The source-review studies in this decision set were assigned in the combined
Phase 1+2 study review queue as follows:

| Study | Phase block | Pair | Coders | Current source-access status |
|---|---|---|---|---|
| `S014` | Phase 2 | Pair C | R1 + R4 | PDF available in ignored local source-PDF folder; population eligibility confirmed; source-value decision logged as no usable direct target-pair value |
| `S021` | Phase 2 | Pair D | R2 + R3 | PDF and Springer online supplement available in ignored local source-PDF folder; Supplementary Table S4 is `f Squared` only; researcher decision is to include the limited main-PDF primary Model 1 T1/T2 row set |
| `S056` | Phase 2 | Pair D | R2 + R3 | PDF available in ignored local source-PDF folder; source-value decision logged with Table 2 source-corrected values |
| `S092` | Phase 2 | Pair D | R2 + R3 | PDF available in ignored local source-PDF folder; source-value decision logged with Table 3 standardized betas and Step 4 Peterson-Brown converted values |
| `S121` | Phase 2 | Pair D | R2 + R3 | Local PDF present; Figure 2 checked; student/teacher row set transcribed in Step 3 artifact with two R2 student value corrections recorded |
| `S195` | Phase 2 | Pair C | R1 + R4 | Local PDF present; duplicate/exclusion decision logged |
| `S202` | Phase 2 | Pair D | R2 + R3 | Local PDF present; target-matrix exclusion decision logged |
| `S206` | Phase 2 | Pair D | R2 + R3 | Local PDF present; duplicate of `S195`; duplicate/exclusion decision logged |

Evidence source:
`data/04_extraction/02_pre_adjudication_disagreement/combined/derived/combined_study_review_queue_20260525.csv`.

## Operational Implications

- `S195` and `S206` now have a phase 2 decision-log entry for the canonical
  duplicate relationship and exclusion/no-target-row rationale.
- `S202` now has a phase 2 decision-log entry for target-matrix exclusion under
  the focal-technology boundary rule.
- `S021`, if retained, must be represented as separate T1/T2 strata rather than
  a pooled pre/post row set.
- `S121`, if both groups are retained, must be represented as separate student
  and teacher samples rather than a pooled mixed-sample row.
- `S014`, `S056`, and `S092` now have source-value decision-log entries for
  Step 3. These entries still must be applied only through the Step 4 reference
  draft, not through raw coder workbook edits.
- The Step 4 freeze audit reconstructed `S092` original betas from Table 3 and
  corrected the draft `r_value` cells to Peterson-Brown converted values.
- `S021` supplement/online-resource access is resolved; `Supplementary Table
  S4` is an `f Squared` effect-size table, and S021 should now enter the Step 4
  draft through the limited main-PDF primary Model 1 T1/T2 beta-converted row
  set.
- `S121` now has a separate student/teacher Figure 2 row-set artifact, with the
  identified `FC-UB` and `PE-SE` student candidate corrections recorded and
  `SE` carried as a medium-confidence subjective-competence/self-efficacy
  mapping.

## Remaining Follow-Up Before Freeze

1. Apply the logged `S014`, `S021`, `S056`, `S092`, and `S121` decisions only
   in the Step 4 reference-standard draft.
2. In Step 4, preserve S021 `T1`/`T2` strata, mark S021 rows as
   `beta_converted`, and keep the AIAS-4-to-`ATT` mapping-confidence flag.

## Boundary

No raw human coder workbooks should be edited to reflect these decisions.
Apply decisions only through the source-adjudication log and the later frozen
source-anchored adjudicated human reference standard.
