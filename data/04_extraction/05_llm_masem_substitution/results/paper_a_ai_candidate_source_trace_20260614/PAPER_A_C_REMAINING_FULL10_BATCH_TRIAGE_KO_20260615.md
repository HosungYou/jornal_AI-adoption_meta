# Paper A/C remaining full10 batch triage

Date: 2026-06-15

## Researcher decision carried forward

- `S121 threat appraisal -> full10 ANX`: not approved by researcher.
- Consequence: `S121-1 ANX-PE=-0.23` and `S121-2 ANX-PE=-0.08` are rejected for supplemental input despite being source-visible in Figure 2.

## Batch scope

- Reviewed pair-by-pair work already completed: `03_FC-PE`, `04_ATT-PE`, `05_PE-SE`, `06_PE-TRU`, `07_ANX-PE`.
- Remaining C-tier queue rows triaged in this batch: 413
- Remaining pair labels triaged: 36
- Rule: no value enters Paper A supplemental input until researcher confirms source value, evidence type, and source location.

## Batch decision counts

- construct_mapping_audit_required_not_promote: 2
- excluded_no_construct_human_supported: 41
- excluded_one_construct_not_human_supported: 357
- excluded_researcher_rejected_PKC_to_SE_mapping: 6
- numeric_cell_candidate_pending_researcher_confirmation: 7

## Remaining pair-label coverage

- 08_BI-PE: 1
- 09_PE-UB: 6
- 11_EE-FC: 2
- 12_ATT-EE: 13
- 13_EE-SE: 13
- 14_EE-TRU: 10
- 15_ANX-EE: 14
- 17_EE-UB: 7
- 18_FC-SI: 2
- 19_ATT-SI: 13
- 20_SE-SI: 13
- 21_SI-TRU: 9
- 22_ANX-SI: 14
- 23_BI-SI: 1
- 24_SI-UB: 6
- 25_ATT-FC: 14
- 26_FC-SE: 15
- 27_FC-TRU: 12
- 28_ANX-FC: 15
- 29_BI-FC: 3
- 30_FC-UB: 8
- 31_ATT-SE: 17
- 32_ATT-TRU: 19
- 33_ANX-ATT: 16
- 34_ATT-BI: 13
- 35_ATT-UB: 19
- 36_SE-TRU: 16
- 37_ANX-SE: 14
- 38_BI-SE: 13
- 39_SE-UB: 16
- 40_ANX-TRU: 17
- 41_BI-TRU: 10
- 42_TRU-UB: 13
- 43_ANX-BI: 14
- 44_ANX-UB: 19
- 45_BI-UB: 6

## Source-visible numeric-cell shortlist

These are the only rows from the remaining batch with a batch-safe numeric cell candidate. They are not yet supplemental input.

| study_id | pair | value | evidence type | source locator | status |
| --- | --- | --- | --- | --- | --- |
| S048 | BI-FC | 0.424 | source_reported_pearson_correlation_matrix | S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; INT x FC | pending researcher confirmation |
| S048 | BI-PE | 0.659 | source_reported_pearson_correlation_matrix | S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; INT x PE | pending researcher confirmation |
| S048 | BI-SI | 0.626 | source_reported_pearson_correlation_matrix | S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; INT x SI | pending researcher confirmation |
| S048 | EE-UB | 0.398 | source_reported_pearson_correlation_matrix | S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; EE x USE | pending researcher confirmation |
| S048 | FC-UB | 0.340 | source_reported_pearson_correlation_matrix | S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; FC x USE | pending researcher confirmation |
| S048 | SI-UB | 0.589 | source_reported_pearson_correlation_matrix | S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; SI x USE | pending researcher confirmation |
| S048 | TRU-UB | 0.442 | source_reported_pearson_correlation_matrix | S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; TRU x USE | pending researcher confirmation |

## Closed or held groups

- `S004` SE-related priority rows are closed for now because they depend on `PKC/perceived knowledge -> SE`, which the researcher did not approve.
- `S072` priority rows are held for construct-mapping audit because the source matrix labels are `PC`, `RA`, and `VU`, not direct full10 `ANX`, `ATT`, or `UB` labels.
- The large majority of remaining rows are excluded at construct-support gate: at least one target construct is not human/frozen-supported for that study.

## Output files

- `paper_a_C_remaining_full10_batch_triage_20260615.csv`
- `paper_a_C_remaining_full10_batch_review_shortlist_20260615.csv`
- Updated confirmation template: `paper_a_human_confirmation_template_from_ai_trace_20260614.csv`
- Updated workbook: `PAPER_A_AI_CANDIDATE_REVIEW_WORKBOOK_20260614.xlsx`

## Next analytic condition

Do not rerun model-family MASEM from these rows until the researcher explicitly confirms the seven `S048` source-visible values or rejects them.
