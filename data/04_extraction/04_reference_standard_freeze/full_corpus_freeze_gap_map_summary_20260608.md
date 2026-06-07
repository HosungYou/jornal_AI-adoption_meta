# Full-Corpus Step 4 Freeze Gap Map Summary

Date: 2026-06-08

Status: gap map generated. This is not a full 213-study freeze and does not start Step 5.

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

## Gap Category Counts

| Gap category | Studies |
|---|---:|
| `correlation_disagreement_pending_adjudication` | 124 |
| `metadata_only_or_no_correlation_gap_pending_lightweight_audit` | 48 |
| `phase1_logged_decision_or_progress_pending_step4_application` | 26 |
| `scoped_phase2_frozen` | 8 |
| `source_checked_confirmed_exclusion_pending_full_freeze_application` | 6 |
| `correlation_queue_lightweight_audit_pending` | 1 |

## Phase by Gap Category

| Phase | Gap category | Studies |
|---|---|---:|
| `phase1` | `correlation_disagreement_pending_adjudication` | 62 |
| `phase1` | `correlation_queue_lightweight_audit_pending` | 1 |
| `phase1` | `metadata_only_or_no_correlation_gap_pending_lightweight_audit` | 11 |
| `phase1` | `phase1_logged_decision_or_progress_pending_step4_application` | 26 |
| `phase2` | `correlation_disagreement_pending_adjudication` | 62 |
| `phase2` | `metadata_only_or_no_correlation_gap_pending_lightweight_audit` | 37 |
| `phase2` | `scoped_phase2_frozen` | 8 |
| `phase2` | `source_checked_confirmed_exclusion_pending_full_freeze_application` | 6 |

## Interpretation

- `scoped_phase2_frozen` studies are already covered by the scoped Phase 2 freeze package.
- `phase1_logged_decision_or_progress_pending_step4_application` studies now have a dedicated application audit layer. They are split into logged exclusions, explicit value decisions, explicit rule decisions requiring row filters/source audits, and progress-only studies requiring source-value audit.
- The highest-confidence Phase 1 subset now has a draft row/status layer: 59 row-level records for S033/S035/S051/S081/S120/S151/S164/S217, exclusion status records for S041/S180/S220, and an S191 reconciliation hold.
- `source_checked_confirmed_exclusion_pending_full_freeze_application` studies have source-checked exclusion evidence but are not yet part of a full-corpus freeze package.
- `correlation_disagreement_pending_adjudication` studies remain the largest full-freeze blocker because their one-coder-only or numeric/source differences still need triage before a defensible 213-study reference freeze.
- `metadata_only_or_no_correlation_gap_pending_lightweight_audit` studies are lower-priority for target-row adjudication, but still need status/metadata audit before full freeze.

## Phase 1 Logged Decision Audit Counts

| Decision level | Studies |
|---|---:|
| `explicit_rule_decision_needs_row_filter_or_source_audit` | 12 |
| `explicit_value_decision_ready_for_reference_draft` | 9 |
| `exclude_study_ready_for_full_freeze_audit` | 3 |
| `phase1_progress_logged_needs_source_value_audit` | 2 |

## Recommended Next Action

Prioritize the full-corpus freeze work in this order:

1. Reconcile S191 R2 Table 2 values before row creation.
2. Carry confirmed source-checked exclusions into the full-corpus audit layer.
3. Apply explicit Phase 1 rule-decision row filters/source audits.
4. Triage remaining correlation-disagreement studies by one-coder-only and numeric/source-difference burden.
5. Run lightweight metadata/status audit for studies without target-row disagreement.
6. Only after the intended full reference scope is frozen should Step 5 generate result claims.
