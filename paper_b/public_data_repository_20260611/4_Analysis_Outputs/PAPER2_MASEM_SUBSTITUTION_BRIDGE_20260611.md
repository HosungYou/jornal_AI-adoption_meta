# Paper2 MASEM Substitution Bridge

Date: 2026-06-11

## Boundary

This bridge prepares the downstream substitution analysis. It does not claim
that final MASEM substitution has been run, and it does not treat current
LLM locked outputs as autonomous replacements for the human-reference input.

## Baseline Inputs

| Component | Rows | Primary MASEM use | Notes |
|---|---:|---|---|
| paper1_pre_tier_primary_analysis_ready | 822 | no | Pre-tiered primary direct-r file; retained for audit, not final model-ready baseline. |
| paper1_primary_model_ready_tiered_freeze | 804 | yes | Primary human-reference MASEM baseline after tiered exclusions; use before any LLM substitution. |
| paper1_expanded_analysis_ready | 1303 | sensitivity_only | Expanded human-consensus direct-r-form file; not the primary baseline. |
| paper1_sensitivity_converted_analysis_ready | 481 | sensitivity_only | Converted beta/path/source-statistic input; source-type sensitivity only. |
| paper1_all_sets_long | 2606 | no | Long stacked audit file containing primary, expanded, and converted sensitivity rows. |

## Current Codex Numeric Substitution Readiness

| Family | Stratum | Rows | Correct | Abstentions | Status |
|---|---|---:|---:|---:|---|
| converted_or_model_derived_effect_size | converted_or_model_derived_beta | 30 | 0 | 30 | review required |
| converted_or_model_derived_effect_size | converted_or_model_derived_beta_path_converted_by_human_consensus | 53 | 0 | 53 | review required |
| converted_or_model_derived_effect_size | converted_or_model_derived_numeric_source_statistic_converted_by_human_consensus | 5 | 0 | 5 | review required |
| direct_r_effect_size_extraction | source_blank_direct_r | 43 | 0 | 43 | review required |
| direct_r_effect_size_extraction | source_reported_direct_r | 323 | 3 | 320 | limited candidate |

## Bridge Conclusion

- The human-reference baseline is the tiered Paper1 primary model-ready file with 804 rows.
- Current primary Codex locked outputs create 1196 P0 numeric/MASEM review tasks and only 42 low-priority task units after the primary check.
- Therefore the next empirical step is not to substitute all Codex outputs
  directly. The next step is to construct an expert-reviewed
  LLM-assisted input file by replacing only source-verified eligible rows,
  then rerun the MASEM pipeline against the human-reference baseline.
- S072 ANX-EE `r = 1.0` remains primary-excluded and may only be used as
  trace/influence diagnostic.

## Rerun Contract

1. Fit the human-reference MASEM baseline from
   `paper1_direct_r_primary_model_ready_tiered_freeze_20260605.csv`.
2. Build a locked LLM-assisted substitution input only after expert review of
   P0/P1 numeric and source-risk rows.
3. Compare pooled correlations, Stage 2 path coefficients, indirect effects,
   model-fit decisions, and substantive conclusions.
4. Report converted beta/path/source-statistic rows as source-type sensitivity,
   not as source-reported direct-r equivalence.
