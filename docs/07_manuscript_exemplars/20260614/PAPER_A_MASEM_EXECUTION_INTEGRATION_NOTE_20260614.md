# Paper A MASEM Execution Integration Note

Date: 2026-06-14

## Target result

This note records the first actual Paper A TSSEM/MASEM execution attempt after the researcher-approved route decisions. It is a claim-boundary artifact for manuscript integration, not a final results table.

## Execution evidence

Primary report: `data/04_extraction/05_llm_masem_substitution/results/paper_a_masem_execution_20260614/PAPER_A_MASEM_EXECUTION_ATTEMPT_20260614.md`

Summary CSV: `data/04_extraction/05_llm_masem_substitution/results/paper_a_masem_execution_20260614/paper_a_masem_execution_summary_20260614.csv`

Script: `scripts/analysis/run_paper_a_masem_execution_20260614.R`

Input: `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_substitution_rerun_input_n_weighted_all_source_supported_20260612.csv`

## Result

| Route | Pair coverage | Partial studies | Complete-case studies | TSSEM1 | Stage 2 | Interpretation |
| --- | ---: | ---: | ---: | --- | --- | --- |
| `paper_a_core7_att_mediation` | 21/21 | 71 | 3 | Failed | Not run | Attitude mediation remains theory-feasible but not structurally estimated. |
| `paper_a_trust6_mechanism` | 15/15 | 72 | 6 | Failed | Not run | Trust remains a candidate AI-specific mechanism, not a confirmed mediator. |
| `paper_a_full10_theory_target` | 44/45 | 74 | 0 | Failed | Not run | Full 10-construct model remains the primary theory target but is not estimable from the current sparse partial matrices. |

All three `metaSEM::tssem1` attempts failed because the implied covariance was not positive definite under sparse partial-matrix input. The fixed-effects fallback also failed. Therefore, no Stage 2 path coefficients, indirect effects, or model-fit statistics should be reported from this run.

## Manuscript boundary

Paper A can now truthfully state that an actual structural MASEM attempt was made. It cannot yet claim final MASEM results. The manuscript should use this run to justify a feasibility/limitation statement unless a subsequent approved route converges.

Acceptable language:

- Pairwise pooled correlation and route-coverage artifacts were generated.
- The full 10-construct route remains the theory target.
- Sparse matrix structure prevented converged TSSEM/MASEM estimation in the current file.

Do not claim:

- Final Stage 1 TSSEM pooled matrix from `metaSEM`.
- Stage 2 path coefficients.
- Confirmed mediation for ATT, TRU, SE, or ANX.
- Full 10-construct model fit.

## Next method choice needed

Before Paper A can become submission-ready as a final MASEM results manuscript, one of these routes must be selected and executed:

1. Full10 densification: return to source/workbook extraction and add matrix information for missing or sparse construct pairs, especially the full10 route.
2. Reduced complete-case diagnostic: run a clearly labeled reduced model where complete-case support is defensible, without treating it as the full10 primary result.
3. Pooled-correlation sensitivity model: fit a structural model to pairwise pooled correlations as an explicitly non-primary sensitivity route, with strong caveats about dependence and missingness.

Recommended default: retain full10 as the primary theory target and treat any reduced or pooled route as diagnostic/sensitivity unless the researcher explicitly changes the primary estimand.
