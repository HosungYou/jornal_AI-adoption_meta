# Paper2 R/metaSEM Readiness Check

Date: 2026-06-11

## Status

- R version: R version 4.6.0 (2026-04-24)
- Platform: aarch64-apple-darwin25.4.0
- Stage status: `r_environment_ready_n_eligible_subset_approved_all_row_blocked`
- Input file: `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_substitution_rerun_input_n_reconciled_20260611.csv`
- Required R packages available: 9/9
- Input rows: 804
- Rows with `r_numeric`: 804/804
- Rows with `sample_size_numeric`: 741/804
- Rows missing `sample_size_numeric`: 63/804

## Claim Boundary

The local R environment is ready for Paper2 meta-analytic scripting: `Rscript`, `OpenMx`, and `metaSEM` load successfully. The approved missing-N rule allows N-weighted analyses on the source-supported eligible subset, but the current input is not ready for an all-row final TSSEM Stage 1/Stage 2 claim because 63 of 804 rows still lack numeric `sample_size_numeric`.

Under the approved missing-N exclusion rule, excluded missing-N rows remain outside N-weighted TSSEM weighting until a later source check supplies numeric N. This evidence supports deterministic substitution-input readiness, pooled-correlation sensitivity checks, and N-eligible subset diagnostics, not all-row SEM path/model-fit stability.

## Output Tables

- `paper2_r_package_status_20260611.csv`
- `paper2_masem_readiness_overall_20260611.csv`
- `paper2_masem_readiness_by_scenario_20260611.csv`
- `paper2_masem_readiness_by_action_20260611.csv`
