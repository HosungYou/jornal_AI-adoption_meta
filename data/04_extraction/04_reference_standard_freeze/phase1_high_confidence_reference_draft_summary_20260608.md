# Phase 1 High-Confidence Reference Draft Summary

Date: 2026-06-08

Status: high-confidence Phase 1 Step 4 reference-draft sub-batch generated and S191 reconciled. This is not a frozen full-corpus reference and does not start Step 5.

## Inputs

- `../03_source_document_adjudication/phase1/decision_log_20260424.md`
- `../03_source_document_adjudication/phase1/coding_decision_application_check_20260425.md`
- `../02_pre_adjudication_disagreement/combined/derived/combined_coder_values_long_20260525.csv`
- `../02_pre_adjudication_disagreement/phase1/AI_Adoption_Phase1_Pairwise_Comparison_R1R2_R3R4_20260424.xlsx`
- Local S191 source PDF Table 2 check (not committed)
- `phase1_logged_decision_application_audit_20260608.csv`

## Outputs

- `phase1_high_confidence_reference_draft_20260608.csv`
- `phase1_high_confidence_reference_draft_status_20260608.csv`
- `phase1_s191_reconciliation_20260608.md`

## Draft Counts

| Item | Count |
|---|---:|
| Row-level draft records | 80 |
| Included studies with full row-set drafts | 6 |
| Included studies with partial value-decision drafts | 3 |
| Logged exclusions carried to status draft | 3 |
| Studies held for reconciliation | 0 |

## Row Draft by Study

| Study ID | Draft rows | Draft scope |
|---|---:|---|
| S033 | 6 | R1 beta-converted Table 5 row set |
| S035 | 21 | R1 direct Table 4 full target row set |
| S051 | 3 | three explicitly logged R1-only direct correlations only |
| S081 | 10 | R1 direct Table 4 full target row set |
| S120 | 5 | five R1 beta-converted weighted subgroup paths |
| S151 | 1 | source-corrected FC-UB=.558 only |
| S164 | 3 | three source-corrected construct correlations only |
| S191 | 21 | R2 direct Table 2 Fornell-Larcker off-diagonal values reconciled from comparison workbook and PDF |
| S217 | 10 | R1 direct Table 4 full target row set |

## Study Status Draft

| Status | Studies |
|---|---|
| Excluded study status draft | S041, S180, S220 |
| Reconciled into row draft | S191 |

## Interpretation

- This draft advances the highest-confidence portion of the 26 Phase 1 logged decision/progress studies into a Step 4 row/status layer.
- S191 is no longer held: 21 R2 direct Table 2 values were recovered from the Phase 1 pairwise comparison workbook and checked against the local source PDF.
- It intentionally does not claim full-study completeness for S051, S151, or S164 because the logged decisions identify specific corrected rows rather than complete final row sets.
- Logged exclusions are carried as study-level status draft records rather than row-level correlation records.
- Full-result Step 5 remains inactive until the intended reference scope is frozen.

## Recommended Next Action

1. Apply explicit Phase 1 rule-decision row filters/source audits for the 12 remaining rule-decision studies, starting with high-priority S054, S074, S091, and S189.
2. Run source-value audit for S086 and S168.
3. Process residual `batch_1_high_burden` studies from `full_corpus_residual_adjudication_triage_20260608.csv`.
4. Keep full-result Step 5 inactive until the intended reference scope is frozen.
