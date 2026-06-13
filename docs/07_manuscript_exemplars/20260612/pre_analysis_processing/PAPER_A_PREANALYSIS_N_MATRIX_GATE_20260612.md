# Paper A Pre-Analysis N/Matrix Gate

Date: 2026-06-12

## Locked Recommendations

- Keep the 10-construct model as the theory target.
- Use pairwise source-supported N when available; otherwise use source-supported analytic sample N.
- If no defensible N can be recovered, exclude the row from primary N-weighted TSSEM/OSMASEM and retain it only in sensitivity/readiness ledgers.
- Exclude converted beta/path/source-statistic rows from the primary model; use them only in sensitivity analyses.
- Run a matrix sparsity and identification audit before any final TSSEM/OSMASEM claim.

## Input

`/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/Paper1_MASEM_Working_20260605/09_model_ready_tiered_freeze/paper1_direct_r_primary_model_ready_tiered_freeze_20260605.csv`

## Current Gate Metrics

| metric | value |
| --- | --- |
| Input rows | 804 |
| Usable 10-construct rows with valid r | 796 |
| Rows with numeric N | 42 |
| Rows missing numeric N | 754 |
| Rows with reconciled numeric N | 733 |
| Rows missing after reconciliation | 63 |
| Rows with PDF-recovered N candidate | 63 |
| Rows still missing after PDF source check | 0 |
| Studies with PDF-recovered N candidate | 7 |
| Studies represented | 74 |
| Construct-pair coverage | 44/45 |
| Complete 10-construct studies | 0 |
| Studies with >=15 pairs | 26 |

## Weakest Pair Coverage

| construct_pair | rows | studies | rows_with_numeric_n | rows_missing_numeric_n | rows_with_reconciled_numeric_n | rows_missing_after_reconciliation | rows_with_reconciled_or_pdf_n_candidate | rows_missing_after_pdf_source_check | primary_gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ANX-TRU | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | not_estimable_without_imputation_or_model_reduction |
| SE-TRU | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | n_reconciled_ready |
| ANX-FC | 2 | 2 | 0 | 2 | 2 | 0 | 2 | 0 | n_reconciled_ready |
| ANX-SE | 2 | 2 | 0 | 2 | 2 | 0 | 2 | 0 | n_reconciled_ready |
| ANX-UB | 2 | 2 | 0 | 2 | 2 | 0 | 2 | 0 | n_reconciled_ready |
| ATT-TRU | 2 | 2 | 0 | 2 | 2 | 0 | 2 | 0 | n_reconciled_ready |
| ANX-BI | 3 | 3 | 0 | 3 | 3 | 0 | 3 | 0 | n_reconciled_ready |
| ANX-EE | 3 | 3 | 0 | 3 | 2 | 1 | 3 | 0 | pdf_n_override_candidate_pending_confirmation |
| ANX-SI | 3 | 3 | 0 | 3 | 2 | 1 | 3 | 0 | pdf_n_override_candidate_pending_confirmation |
| ANX-PE | 4 | 4 | 0 | 4 | 3 | 1 | 4 | 0 | pdf_n_override_candidate_pending_confirmation |
| FC-TRU | 4 | 4 | 0 | 4 | 4 | 0 | 4 | 0 | n_reconciled_ready |
| ATT-SE | 5 | 5 | 0 | 5 | 4 | 1 | 5 | 0 | pdf_n_override_candidate_pending_confirmation |

## Existing N Reconciliation Adoption

The repo already contains a deterministic N reconciliation derived from the 2026-06-09 frozen full-corpus reference:

`data/04_extraction/05_llm_masem_substitution/results/paper2_masem_sample_size_reconciliation_20260611.csv`

| status | rows |
| --- | --- |
| filled_from_full_corpus_reference_pair | 626 |
| filled_from_full_corpus_reference_study_unique | 23 |
| filled_from_s121_stratum_reference | 42 |
| missing_n_excluded_from_n_weighted_masem | 63 |
| retained_existing_input_n | 42 |

## Residual Missing-N Studies After Reconciliation

| study_id | rows |
| --- | --- |
| S028 | 10 |
| S100 | 2 |
| S145 | 6 |
| S185 | 14 |
| S194 | 15 |
| S208 | 10 |
| S218 | 6 |

## PDF Source-Check Result for Residual N

| study_id | residual_rows | pdf_recovered_sample_size | source_check_status | recommended_action_after_source_check |
| --- | --- | --- | --- | --- |
| S028 | 10 | 508 | pdf_study_level_n_candidate_found | apply_pdf_study_level_n_override_to_primary_n_weighted_masem |
| S100 | 2 | 682 | pdf_study_level_n_candidate_found | apply_pdf_study_level_n_override_to_primary_n_weighted_masem |
| S145 | 6 | 374 | pdf_study_level_n_candidate_found | apply_pdf_study_level_n_override_to_primary_n_weighted_masem |
| S185 | 14 | 298 | pdf_study_level_n_candidate_found | apply_pdf_study_level_n_override_to_primary_n_weighted_masem |
| S194 | 15 | 469 | pdf_study_level_n_candidate_found | apply_pdf_study_level_n_override_to_primary_n_weighted_masem |
| S208 | 10 | 526 | pdf_study_level_n_candidate_found | apply_pdf_study_level_n_override_to_primary_n_weighted_masem |
| S218 | 6 | 242 | pdf_study_level_n_candidate_found | apply_pdf_study_level_n_override_to_primary_n_weighted_masem |

## Researcher Confirmation Gate

The missing-N exclusion rule remains the default only when no defensible source
N can be recovered. The PDF source check found study-level analytic/sample N
candidates for all 63 residual rows across 7 studies. Before final model input
mutation, the researcher must approve applying these PDF-recovered study-level
N values. The reason is methodological: N changes TSSEM/MASEM weighting, so
either applying a study-level override or excluding rows is a claim-boundary
decision that must be explicit.

## Stop Condition

All-row primary N-weighted TSSEM/OSMASEM is no longer blocked by source
availability for N, but it remains blocked until the researcher approves the
PDF-recovered N override. If approved, all 796 usable 10-construct rows have a
numeric N candidate before the separate matrix/identification gate.

## Outputs

- `paper_a_n_matrix_pair_audit_20260612.csv`
- `paper_a_n_matrix_study_audit_20260612.csv`
- `paper_a_n_reconciliation_adoption_audit_20260612.csv`
- `paper_a_residual_n_source_check_20260612.csv`
- `paper_a_residual_missing_n_row_queue_20260612.csv`
- `paper_a_residual_missing_n_study_queue_20260612.csv`
