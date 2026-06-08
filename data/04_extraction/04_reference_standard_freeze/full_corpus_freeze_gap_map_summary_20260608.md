# Full-Corpus Step 4 Freeze Gap Map Summary

Date: 2026-06-08

Status: gap map generated and extended with residual batch 1 and batch 2 source-checked row drafts/status decisions. This is not a full 213-study freeze and does not start Step 5.

## Inputs

- `../02_pre_adjudication_disagreement/combined/derived/combined_study_review_queue_20260525.csv`
- `../02_pre_adjudication_disagreement/combined/derived/combined_correlation_review_queue_20260525.csv`
- `../02_pre_adjudication_disagreement/combined/derived/combined_coder_values_long_20260525.csv`
- `../03_source_document_adjudication/phase1/decision_log_20260424.md`
- `../03_source_document_adjudication/phase1/coding_decision_application_check_20260425.md`
- `../03_source_document_adjudication/phase2/phase2_exclusion_source_check_20260525.md`
- `../03_source_document_adjudication/phase2/phase2_source_check_candidates_20260525.csv`
- `paper_b_phase2_source_adjudicated_reference_frozen_20260608.csv`
- `paper_b_phase2_step4_decision_application_audit_20260608.csv`

## Output

- `full_corpus_freeze_gap_map_20260608.csv`
- `phase1_logged_decision_application_audit_20260608.csv`
- `phase1_logged_decision_application_summary_20260608.md`
- `phase1_high_confidence_reference_draft_20260608.csv`
- `phase1_high_confidence_reference_draft_status_20260608.csv`
- `phase1_high_confidence_reference_draft_summary_20260608.md`
- `phase1_s191_reconciliation_20260608.md`
- `phase2_confirmed_exclusion_full_corpus_audit_20260608.csv`
- `phase1_rule_progress_audit_queue_20260608.csv`
- `phase1_high_priority_rule_audit_20260608.csv`
- `phase1_high_priority_rule_reference_draft_20260608.csv`
- `phase1_high_priority_rule_audit_summary_20260608.md`
- `full_corpus_residual_adjudication_triage_20260608.csv`
- `full_corpus_residual_batch1_source_audit_20260608.csv`
- `full_corpus_residual_batch1_reference_draft_20260608.csv`
- `full_corpus_residual_batch1_source_audit_summary_20260608.md`
- `full_corpus_residual_batch2_source_audit_20260608.csv`
- `full_corpus_residual_batch2_reference_draft_20260608.csv`
- `full_corpus_residual_batch2_source_audit_summary_20260608.md`
- `full_corpus_step4_application_progress_20260608.csv`
- `full_corpus_step4_bundled_progress_summary_20260608.md`

## Gap Category Counts

| Gap category | Studies |
|---|---:|
| `correlation_disagreement_pending_adjudication` | 97 |
| `metadata_only_or_no_correlation_gap_pending_lightweight_audit` | 48 |
| `phase1_logged_decision_or_progress_pending_step4_application` | 26 |
| `residual_batch2_source_checked_reference_draft_pending_full_freeze_application` | 18 |
| `scoped_phase2_frozen` | 8 |
| `residual_batch1_source_checked_reference_draft_pending_full_freeze_application` | 7 |
| `source_checked_confirmed_exclusion_pending_full_freeze_application` | 6 |
| `residual_batch2_manual_followup_required_before_reference_draft` | 2 |
| `correlation_queue_lightweight_audit_pending` | 1 |

## Phase by Gap Category

| Phase | Gap category | Studies |
|---|---|---:|
| `phase1` | `correlation_disagreement_pending_adjudication` | 45 |
| `phase1` | `correlation_queue_lightweight_audit_pending` | 1 |
| `phase1` | `metadata_only_or_no_correlation_gap_pending_lightweight_audit` | 11 |
| `phase1` | `phase1_logged_decision_or_progress_pending_step4_application` | 26 |
| `phase1` | `residual_batch1_source_checked_reference_draft_pending_full_freeze_application` | 6 |
| `phase1` | `residual_batch2_manual_followup_required_before_reference_draft` | 1 |
| `phase1` | `residual_batch2_source_checked_reference_draft_pending_full_freeze_application` | 10 |
| `phase2` | `correlation_disagreement_pending_adjudication` | 52 |
| `phase2` | `metadata_only_or_no_correlation_gap_pending_lightweight_audit` | 37 |
| `phase2` | `residual_batch1_source_checked_reference_draft_pending_full_freeze_application` | 1 |
| `phase2` | `residual_batch2_manual_followup_required_before_reference_draft` | 1 |
| `phase2` | `residual_batch2_source_checked_reference_draft_pending_full_freeze_application` | 8 |
| `phase2` | `scoped_phase2_frozen` | 8 |
| `phase2` | `source_checked_confirmed_exclusion_pending_full_freeze_application` | 6 |

## Interpretation

- `scoped_phase2_frozen` studies are already covered by the scoped Phase 2 freeze package.
- `phase1_logged_decision_or_progress_pending_step4_application` studies have a dedicated application audit layer and the highest-priority rule subset has been partly converted to row-level drafts.
- The highest-confidence Phase 1 subset has a draft row/status layer: 80 row-level records for S033/S035/S051/S081/S120/S151/S164/S191/S217 and exclusion status records for S041/S180/S220.
- The high-priority Phase 1 rule subset has 37 row-level draft records for S054/S074/S091/S189; S074 remains orientation-flagged rather than fully routine.
- The residual batch 1 source audit adds 122 row-level draft records for S030/S046/S048/S057/S178/S188/S190; these are source-checked drafts, not a final full-corpus freeze.
- The residual batch 2 source audit adds 210 row-level draft records for 18 studies and separates S015/S066 into manual follow-up blockers before row drafting.
- `source_checked_confirmed_exclusion_pending_full_freeze_application` studies have been carried into `phase2_confirmed_exclusion_full_corpus_audit_20260608.csv` as status-draft exclusions, but they are not yet part of a frozen full-corpus package.
- `correlation_disagreement_pending_adjudication` remains the largest generic full-freeze blocker at 97 studies after batch 2.
- `metadata_only_or_no_correlation_gap_pending_lightweight_audit` studies are lower-priority for target-row adjudication, but still need status/metadata audit before full freeze.

## Phase 1 Logged Decision Audit Counts

| Decision level | Studies |
|---|---:|
| `explicit_rule_decision_needs_row_filter_or_source_audit` | 12 |
| `explicit_value_decision_ready_for_reference_draft` | 9 |
| `exclude_study_ready_for_full_freeze_audit` | 3 |
| `phase1_progress_logged_needs_source_value_audit` | 2 |

## Step 4 Application Progress Counts

| Progress status | Studies |
|---|---:|
| `correlation_disagreement_pending_adjudication` | 97 |
| `metadata_only_or_no_correlation_gap_pending_lightweight_audit` | 48 |
| `residual_batch2_source_checked_reference_draft` | 18 |
| `phase1_high_confidence_reference_draft_or_exclusion_status` | 12 |
| `phase1_rule_decision_row_filter_or_source_audit_queue` | 8 |
| `scoped_phase2_frozen` | 8 |
| `residual_batch1_source_checked_reference_draft` | 7 |
| `phase2_confirmed_exclusion_full_corpus_status_draft` | 6 |
| `phase1_rule_reference_draft_completed` | 3 |
| `phase1_progress_only_source_value_audit_queue` | 2 |
| `residual_batch2_manual_followup_required` | 2 |
| `correlation_queue_lightweight_audit_pending` | 1 |
| `phase1_rule_reference_draft_orientation_caveat` | 1 |

## Step 4 Status Counts

| Step 4 status | Studies |
|---|---:|
| `pre_adjudication_disagreement_not_frozen` | 97 |
| `not_frozen_lightweight_audit_pending` | 48 |
| `decision_logged_not_frozen_full_corpus` | 26 |
| `source_checked_reference_draft_not_frozen_full_corpus` | 25 |
| `frozen_scoped_package` | 8 |
| `source_checked_not_frozen_full_corpus` | 6 |
| `source_checked_manual_followup_not_frozen_full_corpus` | 2 |
| `pre_adjudication_correlation_queue_not_frozen` | 1 |

## Recommended Next Action

Prioritize the full-corpus freeze work in this order:

1. Process residual `batch_3_one_coder_only` studies from `full_corpus_residual_adjudication_triage_20260608.csv`.
2. Resolve `S015` and `S066` manual follow-up decisions before final full-corpus freeze.
3. Continue the remaining Phase 1 rule/progress audit queue when needed: S005, S011, S044, S079, S086, S087, S166, S168, S187, and S223.
4. Run lightweight metadata/status audit for studies without target-row disagreement.
5. Only after the intended full reference scope is frozen should Step 5 generate result claims.
