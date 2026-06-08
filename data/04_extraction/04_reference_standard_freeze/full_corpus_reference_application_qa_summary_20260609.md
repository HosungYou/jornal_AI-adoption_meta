# Full-Corpus Reference Application QA Summary

Date: 2026-06-09

Status: full-corpus Step 4 reference application draft and QA layer assembled. This is not final freeze authorization and does not start Step 5.

## Application Outputs

- `full_corpus_reference_application_rows_draft_20260609.csv`
- `full_corpus_reference_application_study_status_20260609.csv`
- `full_corpus_reference_application_qa_findings_20260609.csv`
- `full_corpus_step4_application_progress_20260608.csv`
- `full_corpus_freeze_gap_map_20260608.csv`

## Corpus Counts

- Application rows: 2043
- Study status rows: 213
- Included application-draft studies: 194
- Status-only application-draft studies: 19
- Lightweight coder-agreed rows added: 449
- Partial Phase 1 application-QA completion rows added: 39 (S051: 12, S151: 9, S164: 18)

## Row Source Counts

| Source | Rows |
|---|---:|
| `paper_b_phase2_source_adjudicated_reference_frozen_20260608.csv` | 74 |
| `phase1_high_confidence_reference_draft_20260608.csv` | 80 |
| `phase1_high_priority_rule_reference_draft_20260608.csv` | 37 |
| `phase1_rule_progress_reference_draft_20260608.csv` | 102 |
| `full_corpus_residual_batch1_reference_draft_20260608.csv` | 122 |
| `full_corpus_residual_batch2_reference_draft_20260608.csv` | 210 |
| `full_corpus_residual_batch3_reference_draft_20260608.csv` | 159 |
| `full_corpus_manual_blocker_reference_draft_20260608.csv` | 69 |
| `full_corpus_residual_batch4_phase1_pairA_reference_draft_20260608.csv` | 65 |
| `full_corpus_residual_batch4_phase1_pairB_reference_draft_20260608.csv` | 192 |
| `full_corpus_residual_batch4_phase2_pairC_reference_draft_20260608.csv` | 87 |
| `full_corpus_residual_batch4_phase2_pairD_reference_draft_20260608.csv` | 127 |
| `full_corpus_residual_batch5_reference_draft_20260608.csv` | 231 |
| `lightweight_coder_agreed_rows_from_combined_coder_values_long_20260525.csv` | 449 |
| `application_qa_completion_rows_for_partial_phase1_decisions` | 39 |

## Decision Status Counts

| Row decision status | Rows |
|---|---:|
| `included_coder_agreed_correlation_rows_application_draft` | 449 |
| `included_frozen_reference` | 74 |
| `included_full_corpus_application_completion_from_partial_phase1_decision` | 39 |
| `included_reference_draft_beta_converted` | 11 |
| `included_reference_draft_high_confidence` | 41 |
| `included_reference_draft_manual_blocker_resolved_20260608` | 69 |
| `included_reference_draft_metadata_construct_rule_applied` | 6 |
| `included_reference_draft_metadata_rule_applied` | 6 |
| `included_reference_draft_partial_value_decision` | 7 |
| `included_reference_draft_phase1_rule_progress_source_checked` | 68 |
| `included_reference_draft_phase1_rule_progress_source_checked_beta_conversion_caveat` | 3 |
| `included_reference_draft_phase1_rule_progress_source_checked_htmt_excluded_beta_conversion_caveat` | 11 |
| `included_reference_draft_phase1_rule_progress_source_checked_path_coefficient_caveat` | 5 |
| `included_reference_draft_phase1_rule_progress_source_checked_stress_anx_mapping_caveat` | 15 |
| `included_reference_draft_reconciled_from_pairwise_workbook` | 21 |
| `included_reference_draft_residual_batch1_source_checked` | 73 |
| `included_reference_draft_residual_batch1_source_checked_one_coder` | 49 |
| `included_reference_draft_residual_batch2_source_checked` | 210 |
| `included_reference_draft_residual_batch3_source_checked` | 159 |
| `included_reference_draft_residual_batch4_phase1_pairA_source_checked` | 65 |
| `included_reference_draft_residual_batch4_phase1_pairB_source_checked` | 192 |
| `included_reference_draft_residual_batch4_phase2_pairC_source_checked` | 87 |
| `included_reference_draft_residual_batch4_phase2_pairD_source_checked` | 127 |
| `included_reference_draft_residual_batch5_source_checked` | 231 |
| `included_reference_draft_rule_applied_teacher_only` | 10 |
| `included_reference_draft_source_reported_orientation_flag` | 15 |

## Study Terminal Status Counts

| Application terminal status | Studies |
|---|---:|
| `duplicate_source_status_application_draft` | 2 |
| `excluded_or_no_target_status_application_draft` | 17 |
| `included_reference_application_draft` | 194 |

## Study QA Status Counts

| Study QA status | Studies |
|---|---:|
| `pass` | 132 |
| `pass_status_only` | 19 |
| `pass_with_caveats` | 62 |

## QA Finding Status Counts

| QA finding status | Checks |
|---|---:|
| `pass` | 9 |
| `warn` | 3 |

## Caveats Retained For Final Freeze Review

- S051, S151, and S164 were partial high-confidence drafts; the application QA layer adds missing row coverage but flags those additions for final authorization review.
- S203 uses source-corrected sample size N=251 rather than the alternate coder metadata value N=303.
- S074 retains the ANX/AXT orientation caveat.
- S187 retains the Stress-to-ANX mapping caveat.
- S014, S023, S039, S041, S101, S105, S108, S109, S118, S132, S144, S180, S195, S196, S202, S206, S215, S220, and S224 are status-only in the application layer.
- Path/beta-converted rows, HTMT exclusions, manual-resolution studies S015/S066/S099/S200, S151 UB wording, and status-only exclusions remain visible in the study-status and QA findings layers.

## Gate Status

Step 4 application QA is complete pending final full-corpus freeze authorization. Step 5 remains inactive until a freeze log/authorization records the final reference scope.
