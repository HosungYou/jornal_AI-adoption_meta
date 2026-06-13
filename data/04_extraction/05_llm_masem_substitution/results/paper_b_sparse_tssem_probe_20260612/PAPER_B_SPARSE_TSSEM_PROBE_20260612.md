# Paper B Sparse TSSEM Probe

Date: 2026-06-12

Input: `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_substitution_rerun_input_n_weighted_all_source_supported_20260612.csv`

## Probe boundary

These probes are not main-text all-construct claims. They test whether the selected broader route can move beyond the completed core-6 diagnostic under a conservative complete-case matrix rule.

## Results

| Probe | Constructs | Complete-case studies | Stage 1 status | Stage 2 status | Error | Claim boundary |
| --- | --- | ---: | --- | --- | --- | --- |
| core7_add_att | PE,EE,SI,FC,ATT,BI,UB | 3 | completed | failed | Stage2: "aCov" is not positive definite. | Stage 1 probe completed; do not promote to main-text extension unless Stage 2 specification and stability are separately accepted. |
| core8_add_tru | PE,EE,SI,FC,ATT,TRU,BI,UB | 1 | not_run_insufficient_complete_case_studies | not_run |  | Sparse probe only; not enough complete-case studies for conservative TSSEM probe. |

## Manuscript implication

Core-6 remains the completed SEM diagnostic. The core7_add_att probe completed Stage 1 but failed the Stage 2 path-model probe because the asymptotic covariance matrix was not positive definite. The core8_add_tru probe lacked enough complete-case studies for conservative TSSEM. Broader construct sets should therefore remain sparse probes unless later model-specific diagnostics support stronger reporting.
