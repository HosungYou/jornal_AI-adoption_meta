# Paper2 R/metaSEM Readiness Check

Date: 2026-06-12

## Status

- R version: R version 4.6.0 (2026-04-24)
- Platform: aarch64-apple-darwin25.4.0
- Stage status: `ready_for_full_tssem`
- Input file: `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_substitution_rerun_input_n_pdf_override_20260612.csv`
- Required R packages available: 9/9
- Input rows: 804
- Rows with `r_numeric`: 804/804
- Rows with `sample_size_numeric`: 804/804
- Rows missing `sample_size_numeric`: 0/804

## Claim Boundary

The current input carries numeric sample sizes for all rows, so remaining TSSEM readiness depends on analysis-specification decisions rather than N coverage.

The approved PDF-supported N override closes the N-coverage gate for this derived input. This evidence supports N-weighted TSSEM/OSMASEM execution readiness, while substantive all-construct claims remain gated by matrix sparsity, identification, source-type, and model-specification checks.

## Output Tables

- `paper2_r_package_status_20260612.csv`
- `paper2_masem_readiness_overall_20260612.csv`
- `paper2_masem_readiness_by_scenario_20260612.csv`
- `paper2_masem_readiness_by_action_20260612.csv`
