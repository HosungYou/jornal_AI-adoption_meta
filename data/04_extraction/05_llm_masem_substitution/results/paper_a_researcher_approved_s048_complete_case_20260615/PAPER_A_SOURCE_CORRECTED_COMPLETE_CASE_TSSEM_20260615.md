# Paper A researcher-approved S048 complete-case TSSEM diagnostic

Date: 2026-06-15

Input: `/Users/newhosung/Academic/2026/AI Adoption Meta Analysis/data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_supplement_20260615/paper_a_source_corrected_plus_researcher_approved_anx_tru_pe_se_s048_input_20260615.csv`

## Summary

| Route | Candidate complete cases | Positive-definite complete cases | Stage 1 | Stage 2 | Boundary |
| --- | ---: | ---: | --- | --- | --- |
| paper_a_core7_att_mediation | 4 | 4 | converged | converged | Complete-case ATT mediation diagnostic only; not full10 primary. |
| paper_a_trust6_mechanism | 7 | 7 | converged | converged | Complete-case TRU mechanism diagnostic; defensible only as reduced sensitivity route. |
| paper_a_full10_theory_target | 0 | 0 | not_run | not_run | Full10 primary target; not estimable without complete-case or defensible missing-data route. |

## Interpretation boundary

This is a diagnostic complete-case rerun after researcher-approved S048 staging plus ANX/TRU and S121 PE-SE supplements. Full10 remains non-estimable by complete-case TSSEM because it has zero complete-case studies. Reduced trust6/core7 routes may be reported only as sensitivity or diagnostic routes unless the researcher changes the primary model claim.

## Output files

- `paper_a_source_corrected_complete_case_summary_20260615.csv`
- per-route `*_complete_case_matrix_eigen_20260615.csv`
- per-route `*_complete_case_stage2_paths_20260615.csv` and `*_complete_case_stage2_fit_indices_20260615.csv` when Stage 2 succeeds
