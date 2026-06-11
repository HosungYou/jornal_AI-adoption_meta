# Paper2 R/metaSEM Readiness Check

Date: 2026-06-11

## Status

- R version: R version 4.6.0 (2026-04-24)
- Platform: aarch64-apple-darwin25.4.0
- Stage status: `r_environment_ready_input_sample_size_blocked`
- Required R packages available: 9/9
- Input rows: 804
- Rows with `r_numeric`: 804/804
- Rows with `sample_size_numeric`: 49/804
- Rows missing `sample_size_numeric`: 755/804

## Claim Boundary

The local R environment is ready for Paper2 meta-analytic scripting: `Rscript`, `OpenMx`, and `metaSEM` load successfully. The current expert-reviewed substitution input is not yet ready for a final full TSSEM Stage 1/Stage 2 claim because most primary rows do not carry `sample_size_numeric`.

Until sample sizes are completed or a documented missing-N exclusion rule is applied, the current evidence supports deterministic substitution-input readiness and pooled-correlation sensitivity checks, not final SEM path/model-fit stability.

## Output Tables

- `paper2_r_package_status_20260611.csv`
- `paper2_masem_readiness_overall_20260611.csv`
- `paper2_masem_readiness_by_scenario_20260611.csv`
- `paper2_masem_readiness_by_action_20260611.csv`
