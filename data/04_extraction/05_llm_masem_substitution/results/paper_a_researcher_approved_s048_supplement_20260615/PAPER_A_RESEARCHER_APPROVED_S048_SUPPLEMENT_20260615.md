# Paper A researcher-approved S048 supplemental staging

Date: 2026-06-15

## Decision recorded

The researcher approved the seven S048 source-visible Pearson correlation cells from Table 2 for Paper A supplemental analysis. This does not mutate the Paper B source-anchored adjudicated human reference standard.

## Approved S048 values

- `BI-FC` = `0.424` (S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; INT x FC)
- `BI-PE` = `0.659` (S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; INT x PE)
- `BI-SI` = `0.626` (S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; INT x SI)
- `EE-UB` = `0.398` (S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; EE x USE)
- `FC-UB` = `0.340` (S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; FC x USE)
- `SI-UB` = `0.589` (S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; SI x USE)
- `TRU-UB` = `0.442` (S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; TRU x USE)

## Staging result

- Upstream input rows: `836`
- Output input rows: `836`
- Existing S048 rows promoted: `7`
- New supplemental rows inserted: `0`
- Analysis input: `data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_supplement_20260615/paper_a_source_corrected_plus_researcher_approved_anx_tru_pe_se_s048_input_20260615.csv`
- Approved rows: `data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_supplement_20260615/paper_a_researcher_approved_s048_rows_20260615.csv`
- Decision table: `data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_supplement_20260615/paper_a_researcher_approved_s048_promotion_decisions_20260615.csv`
- Filled confirmation template: `data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_supplement_20260615/paper_a_human_confirmation_template_s048_approved_20260615.csv`

## Boundary

These rows are eligible for Paper A model-family MASEM reruns as researcher-approved supplemental input. Rejected or held mappings remain excluded: S004 PKC->SE, S121 threat appraisal->ANX, and S072 construct-mapping audit rows.
- Workbook: `data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_supplement_20260615/PAPER_A_S048_RESEARCHER_APPROVAL_WORKBOOK_20260615.xlsx`
