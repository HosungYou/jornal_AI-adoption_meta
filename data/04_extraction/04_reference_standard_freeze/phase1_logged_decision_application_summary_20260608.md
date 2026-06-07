# Phase 1 Logged Decision Application Audit Summary

Date: 2026-06-08

Status: application audit generated for 26 Phase 1 studies with logged
decision/progress evidence. This is not a full 213-study freeze and does not
start Step 5.

## Inputs

- `../03_source_document_adjudication/phase1/decision_log_20260424.md`
- `../03_source_document_adjudication/phase1/coding_decision_application_check_20260425.md`
- `full_corpus_freeze_gap_map_20260608.csv`

## Output

- `phase1_logged_decision_application_audit_20260608.csv`
- `phase1_high_confidence_reference_draft_20260608.csv`
- `phase1_high_confidence_reference_draft_status_20260608.csv`
- `phase1_high_confidence_reference_draft_summary_20260608.md`
- `phase1_s191_reconciliation_20260608.md`

## Decision-Level Counts

| Decision level | Studies |
|---|---:|
| `explicit_rule_decision_needs_row_filter_or_source_audit` | 12 |
| `explicit_value_decision_ready_for_reference_draft` | 9 |
| `exclude_study_ready_for_full_freeze_audit` | 3 |
| `phase1_progress_logged_needs_source_value_audit` | 2 |

## Study Groups

| Group | Study IDs | Step 4 implication |
|---|---|---|
| Logged exclusions | S041, S180, S220 | Carry exclusion code/rationale into the full-corpus reference status layer, with routine final audit. |
| Explicit value decisions | S033, S035, S051, S081, S120, S151, S164, S191, S217 | Draft reference rows from the logged coder/source choices, then audit row counts, construct-pair labels, and source type. |
| Explicit rule decisions | S005, S011, S044, S054, S074, S079, S087, S091, S166, S187, S189, S223 | Apply row filters or source-type/construct-mapping audits before row creation. |
| Progress-only logged | S086, S168 | Run source-value audit before any freeze-layer row creation. |

## Interpretation

- The 26 studies now have a Step 4 application/audit layer rather than a single
  undifferentiated "pending application" bucket.
- The highest-confidence sub-batch now includes the three logged exclusions plus
  explicit value-decision studies whose row sets can be audited directly from
  the logged R1/R2 choice, source-corrected values, or the reconciled S191 pairwise
  workbook values.
- S191 is no longer held: 21 R2 direct Table 2 values were recovered from the
  Phase 1 pairwise comparison workbook and checked against the local source PDF.
- Explicit rule decisions are actionable, but they are not yet final
  freeze-layer rows because they require row filters, source-type checks,
  construct-mapping confirmation, orientation checks, or N reconciliation.
- S086 and S168 have Phase 1 progress evidence but no logged final row rule; do
  not advance them to freeze rows without source-value audit.
- The high-confidence reference-draft/status layer now carries 80 row-level
  draft records and 3 logged exclusion status records, with S191 included as a
  reconciled draft row set.

## Recommended Next Action

1. Apply the explicit rule-decision row filters/source audits, starting with
   high-priority S054, S074, S091, and S189.
2. Run source-value audit for S086 and S168.
3. Process residual `batch_1_high_burden` studies from
   `full_corpus_residual_adjudication_triage_20260608.csv`.
4. Keep full-result Step 5 inactive until the intended reference scope is
   frozen.
