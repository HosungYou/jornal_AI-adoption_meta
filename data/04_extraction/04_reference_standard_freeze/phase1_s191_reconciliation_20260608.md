# S191 Reconciliation Note

Date: 2026-06-08

Status: reconciled into the Phase 1 high-confidence Step 4 reference draft. This is not a full-corpus freeze and does not start Step 5.

## Issue

The Phase 1 decision log says to use R2 direct Table 2 values for S191, but the current combined derived long table contains only R1 correlation rows for S191. The raw R2 workbook also contains the S191 correlation grid with blank value cells.

## Reconciliation Evidence

- `data/04_extraction/03_source_document_adjudication/phase1/decision_log_20260424.md`: 2026-04-29 amendment says to use R2 direct Table 2 values for S191.
- `data/04_extraction/02_pre_adjudication_disagreement/phase1/AI_Adoption_Phase1_Pairwise_Comparison_R1R2_R3R4_20260424.xlsx`: `DECISION_LOG` records `USE_R2_VALUES`; `R1_R2_CORRELATIONS` stores 21 S191 R2 direct Table 2 values in the `R2_beta` column with `R2_source = direct`; `R1_R2_RECHECK_S164_S033` records `USE_R2_DIRECT_VALUE` resolutions.
- Local S191 source PDF Table 2 check: confirms the same Fornell-Larcker off-diagonal values. This PDF remains local and is not added to Git.

## Draft Action

Added 21 S191 row-level records to `phase1_high_confidence_reference_draft_20260608.csv` with `decision_status = included_reference_draft_reconciled_from_pairwise_workbook`.

## Caution

The S191 values are Fornell-Larcker off-diagonal latent correlations. Computer self-efficacy is mapped to `SE` and remains a construct-mapping audit flag before any frozen full-corpus package.
