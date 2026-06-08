# Full-Corpus Step 4 Research Specification and Work Plan

Date: 2026-06-08

LongTable decision: `decision_mq4i2yhs_ihxexf`

Status: confirmed by the researcher as the active research specification and
work plan for moving from source-document adjudication toward a full-corpus
source-anchored adjudicated human reference standard. This document does not
freeze the full 213-study reference and does not start Step 5.

## Research Direction

The project is building a source-anchored adjudicated human reference standard
for the 213-study Paper B validation corpus. Raw human coder values remain
preserved as pre-adjudication evidence. Step 4 artifacts add a separate
source-checked adjudication layer that records which rows can be carried toward
the reference standard, which rows require exclusion, and which studies still
need manual adjudication.

The reference standard is the prerequisite for Paper B LLM validation, Paper A
MASEM-ready extraction use, and Paper C model/procedure benchmarking. Step 5
result claims remain inactive until the intended reference scope is frozen.

## Current Stage

The project is between Step 3 source-document adjudication and full-corpus Step
4 freeze.

Current Step 4 draft/status layers include:

- 80 Phase 1 high-confidence row-level draft records.
- 3 Phase 1 logged exclusion status records.
- 37 high-priority Phase 1 rule-applied row draft records for
  S054/S074/S091/S189.
- 122 residual batch 1 source-checked row draft records for
  S030/S046/S048/S057/S178/S188/S190.
- 210 residual batch 2 source-checked row draft records for 18 studies.
- 159 residual batch 3 source-checked row draft records for 12 studies.
- 69 manual-blocker resolved row draft records for S015/S066/S099/S200.
- 6 confirmed Phase 2 exclusions in a full-corpus status-draft audit layer.

Current full-freeze blockers:

- 83 generic residual correlation-disagreement studies remain to be adjudicated.
- 8 explicit Phase 1 rule decisions still need row filters/source audits.
- S086 and S168 need source-value audit.
- S074 remains drafted with an ANX/AXT orientation caveat.
- S015/S066/S099/S200 are resolved into row drafts but must retain their
  country-stratum, beta/path, and mixed-evidence caveats in final freeze audit.
- 48 metadata/lightweight studies plus 1 correlation-queue lightweight study
  need status audit.
- Paper C still needs final model set, procedure contrast, and repeated-run
  budget decisions before final benchmark claims.

## Protected Decisions

- Do not edit raw human coder workbooks during adjudication.
- Do not treat draft Step 4 artifacts as a frozen 213-study reference.
- Do not silently close caveated studies such as S015, S066, and S074.
- Use `source-anchored adjudicated human reference standard`; avoid `gold
  standard` except when preserving historical language.
- Keep Step 5 result claims inactive until the intended reference scope is
  frozen.

## Execution Plan

### 1. Residual batch 3 one-coder-only source audit

Goal: check whether one-coder-only correlation rows can be source-verified and
carried into a row-level reference draft.

Status: completed as a Step 4 draft/status layer on 2026-06-08. Twelve studies
were converted into 159 source-checked row-level reference draft records, and
S099/S200 were initially retained as manual follow-up blockers before the
subsequent researcher decision resolved them into the manual-blocker row-draft
layer.

Outputs:

- `full_corpus_residual_batch3_source_audit_20260608.csv`
- `full_corpus_residual_batch3_reference_draft_20260608.csv`
- `full_corpus_residual_batch3_source_audit_summary_20260608.md`
- Updated progress/gap-map/status files.

Decision rules:

- If the one-coder row set matches a source-reported target correlation table,
  create a source-checked row draft and preserve a one-coder-only caveat.
- If the table is HTMT-only, path-only, or construct mapping is not defensible,
  keep the study as manual follow-up or exclusion/status draft.
- If a source PDF is unavailable, record the access blocker rather than
  fabricating a row-level draft.

### 2. Manual follow-up for S015 and S066

Goal: resolve the two batch 2 studies that should not be row-drafted without
explicit adjudication.

Required decisions:

- S015: whether to include Poland only, both country strata as separate records,
  or another prespecified handling rule.
- S066: whether a beta/path conversion is permitted and defensible, or whether
  the study should be excluded from direct-r reference rows.

### 3. Remaining residual correlation-disagreement batches

Goal: process the remaining residual batches with the same source-checked audit
pattern.

Order:

1. `batch_4_moderate`
2. `batch_5_low_burden`

Each batch should produce a study-level audit, row-level draft where
defensible, progress/gap-map updates, and a summary.

### 4. Remaining Phase 1 rule/progress queue

Goal: apply explicit logged decisions and source-value audits that are not yet
converted into full-corpus Step 4 artifacts.

Studies:

- S005
- S011
- S044
- S079
- S086
- S087
- S166
- S168
- S187
- S223

### 5. Lightweight status audit

Goal: close lower-priority full-freeze blockers that do not require high-burden
target-row adjudication.

Scope:

- 48 metadata/lightweight studies.
- 1 correlation-queue lightweight study.

### 6. Full-corpus freeze package

Goal: combine source-checked row drafts, exclusion/status records, and manual
decisions into a frozen full-corpus reference package.

Required checks:

- Every included row has one evidence type.
- Every exclusion has a source-backed rationale or documented rule basis.
- HTMT-only evidence is not used as target correlations.
- Fornell-Larcker diagonal values are not used as correlations.
- Construct mappings and sample/stratum decisions are explicit.
- Draft caveats are either resolved or preserved in the freeze log.
- Checksums, reviewer/date, and freeze log are recorded.

## Next Action

Process residual `batch_4_moderate` from
`full_corpus_residual_adjudication_triage_20260608.csv` or continue the
remaining Phase 1 rule/source-value queue. Keep Step 5 inactive until the full
reference scope is frozen.
