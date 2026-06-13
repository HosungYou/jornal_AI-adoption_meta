# Paper A MASEM Execution Attempt

Date: 2026-06-14

Input: `data/04_extraction/05_llm_masem_substitution/results/paper_a_latest_human_workbook_audit_20260614/paper_a_latest_human_workbook_direct_r_input_20260614.csv`

## Execution strategy

This run attempts actual Paper A TSSEM/MASEM routes using the N-ready 804-row input. For each route it attempts `metaSEM::tssem1` with partial study matrices, falls back to fixed-effects Stage 1 if needed, then attempts `tssem2` with a theory-guided path model. Independently, it creates pairwise random-effects pooled correlations for every available construct pair so the Stage 1 evidence remains usable even when full structural estimation fails.

## Route summary

| Route | Constructs | Required pairs | Observed pairs | Missing/unestimated pairs | Single-study pairs | Min pair k | Partial studies | Complete-case studies | TSSEM1 | Stage 2 | Pairwise min eigen | Boundary |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | --- |
| paper_a_core7_att_mediation | PE,EE,SI,FC,ATT,BI,UB | 21 | 21 | 0 | 0 | 20 | 175 | 4 | failed | not_run | 0.3209 | Primary feasible ATT mediation route if TSSEM converges. |
| paper_a_trust6_mechanism | PE,EE,SI,TRU,BI,UB | 15 | 15 | 0 | 0 | 13 | 176 | 8 | failed | not_run | 0.3613 | AI-specific TRU mechanism route; SI path should be sensitivity if unstable. |
| paper_a_full10_theory_target | PE,EE,SI,FC,ATT,SE,TRU,ANX,BI,UB | 45 | 45 | 0 | 0 | 3 | 179 | 0 | failed | not_run | 0.1597 | Full 10-construct theory target; expected to be sparse and must not be overclaimed if estimation fails. |

## Claim boundary

Use converged Stage 2 outputs only where both TSSEM1 and TSSEM2 succeed. If TSSEM2 fails but pairwise Stage 1 pooling exists, report the evidence as pooled-correlation/input-readiness evidence rather than a final structural path model. Full 10-construct claims require successful structural estimation and should not be inferred from pairwise pooled correlations alone.

## Output files

- `paper_a_masem_execution_summary_20260614.csv`
- per-route `*_pairwise_random_effects_stage1_20260614.csv`
- per-route `*_pairwise_pooled_matrix_20260614.csv`
- per-route `*_stage2_paths_20260614.csv` and `*_stage2_fit_indices_20260614.csv` when Stage 2 succeeds
