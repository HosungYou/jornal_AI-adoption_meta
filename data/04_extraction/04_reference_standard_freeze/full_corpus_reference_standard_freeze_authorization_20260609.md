# Full-Corpus Source-Anchored Reference Freeze Authorization

Freeze date: 2026-06-09

Freeze scope: full 213-study Paper B validation corpus.

Status: authorized and frozen as the full-corpus source-anchored adjudicated human reference standard, with retained caveats. This authorization supersedes the previous full-corpus application-QA pending state and does not start Step 5 by itself.

Final reviewer: Hosung / researcher, approval recorded in the Codex thread on 2026-06-09 with explicit instruction to preserve S051/S151/S164 partial-completion, S203 N=251, S074/S187, path/beta, HTMT, manual-resolution, and status-only caveats.

Artifact commit hash: recorded by the Git commit that adds this authorization package; embedding the hash inside this file would change the hash. The final pushed commit is reported in the Codex completion message.

## Frozen Files

- `full_corpus_reference_standard_frozen_20260609.csv`
- `full_corpus_reference_standard_study_status_frozen_20260609.csv`
- `full_corpus_reference_standard_freeze_caveat_register_20260609.csv`
- `CHECKSUMS_FULL_CORPUS_FREEZE_20260609.csv`
- `post_freeze_corrections_full_corpus_20260609.md`

## Supporting Application/QA Files

- `full_corpus_reference_application_rows_draft_20260609.csv`
- `full_corpus_reference_application_study_status_20260609.csv`
- `full_corpus_reference_application_qa_findings_20260609.csv`
- `full_corpus_reference_application_qa_summary_20260609.md`
- `full_corpus_step4_application_progress_20260608.csv`
- `full_corpus_freeze_gap_map_20260608.csv`

## Corpus Counts

| Item | Count |
|---|---:|
| Frozen target rows | 2043 |
| Frozen study-status records | 213 |
| Included frozen-reference studies | 194 |
| Excluded/no-target frozen status studies | 17 |
| Duplicate-source frozen status studies | 2 |
| Application QA checks passed | 9 |
| Application QA warnings retained as caveats | 3 |

## Freeze Eligibility Decision

The QA caveats do not block final freeze because they are bounded, source/audit-visible, and carried into the frozen row/status/caveat register. The frozen package is authorized under these conditions:

- S051/S151/S164 partial-completion rows are frozen as caveat-bearing application-QA completions.
- S203 is frozen with N=251 as the valid/effective analysis sample.
- S074 ANX/AXT orientation and S187 Stress-to-ANX mapping caveats remain visible.
- Path/beta-converted rows and HTMT exclusions remain visible and must be handled as evidence-type caveats.
- S015/S066/S099/S200 manual-resolution provenance remains visible.
- Status-only studies remain in corpus accounting but receive zero target rows.

## Status-Only Studies

The following studies are frozen as status-only records and do not contribute target rows:

`S014, S023, S039, S041, S101, S105, S108, S109, S118, S132, S144, S180, S195, S196, S202, S206, S215, S220, S224`

## Row Decision Status Counts

| Frozen row decision status | Rows |
|---|---:|
| `included_frozen_beta_or_path_conversion_caveat` | 19 |
| `included_frozen_coder_agreed_correlation_row` | 449 |
| `included_frozen_htmt_exclusion_caveat` | 11 |
| `included_frozen_manual_resolution_caveat` | 69 |
| `included_frozen_orientation_caveat` | 15 |
| `included_frozen_partial_phase1_completion_caveat` | 39 |
| `included_frozen_partial_phase1_logged_value_caveat` | 7 |
| `included_frozen_reference_high_confidence` | 41 |
| `included_frozen_reference_metadata_construct_rule_applied` | 6 |
| `included_frozen_reference_metadata_rule_applied` | 6 |
| `included_frozen_reference_phase1_rule_progress_source_checked` | 68 |
| `included_frozen_reference_reconciled_from_pairwise_workbook` | 21 |
| `included_frozen_reference_residual_batch1_source_checked` | 73 |
| `included_frozen_reference_residual_batch1_source_checked_one_coder` | 49 |
| `included_frozen_reference_residual_batch2_source_checked` | 210 |
| `included_frozen_reference_residual_batch3_source_checked` | 159 |
| `included_frozen_reference_residual_batch4_phase1_pairA_source_checked` | 65 |
| `included_frozen_reference_residual_batch4_phase1_pairB_source_checked` | 192 |
| `included_frozen_reference_residual_batch4_phase2_pairC_source_checked` | 87 |
| `included_frozen_reference_residual_batch4_phase2_pairD_source_checked` | 127 |
| `included_frozen_reference_residual_batch5_source_checked` | 231 |
| `included_frozen_reference_rule_applied_teacher_only` | 10 |
| `included_frozen_reference_scoped_phase2_carried_forward` | 74 |
| `included_frozen_stress_anx_mapping_caveat` | 15 |

## Step 5 Gate

This freeze authorizes the reference standard. It does not, by itself, create or rerun Step 5 LLM comparison or MASEM substitution artifacts. Step 5 should use `full_corpus_reference_standard_frozen_20260609.csv` only after a separate post-freeze run/analysis gate confirms the intended model/procedure scope and denominator-family reporting plan.

## Post-Freeze Corrections

Post-freeze corrections, if any, must be recorded in `post_freeze_corrections_full_corpus_20260609.md` with date, reason, affected rows, reviewer, and downstream rerun implications.
