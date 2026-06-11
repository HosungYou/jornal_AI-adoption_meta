# Paper2 RQ1 Extraction Validity

Date: 2026-06-11

## Boundary

This table evaluates extraction validity by task family and stratum. It does
not collapse the 8,783 task units into one denominator. Codex GPT-5.5 is
the primary prespecified workflow; Claude Sonnet and Gemini 3 Flash are
supplementary cross-model sensitivity evidence.

Abstentions on scorable rows are counted as incorrect and reported as
abstentions. Metadata rows report strict exact match and relaxed normalized
match. Converted beta/path/source-statistic rows are numeric extraction
strata, not source-reported direct-r rows.

## Primary Codex Core Families

| denominator_family | task_stratum | row_n | scored_n | correct_n | accuracy | abstention_n | metadata_strict_accuracy | metadata_relaxed_accuracy | numeric_within_0_005_n | mean_abs_error |
|---|---|---|---|---|---|---|---|---|---|---|
| converted_or_model_derived_effect_size | converted_or_model_derived_beta | 30 | 30 | 0 | 0.000000 | 30 |  |  | 0 |  |
| converted_or_model_derived_effect_size | converted_or_model_derived_beta_path_converted_by_human_consensus | 53 | 53 | 0 | 0.000000 | 53 |  |  | 0 |  |
| converted_or_model_derived_effect_size | converted_or_model_derived_numeric_source_statistic_converted_by_human_consensus | 5 | 5 | 0 | 0.000000 | 5 |  |  | 0 |  |
| direct_r_effect_size_extraction | source_blank_direct_r | 43 | 43 | 0 | 0.000000 | 43 |  |  | 0 |  |
| direct_r_effect_size_extraction | source_reported_direct_r | 323 | 323 | 3 | 0.009288 | 320 |  |  | 3 | 0.000000 |
| metadata_extraction | metadata_ai_tool_name | 56 | 54 | 2 | 0.037037 | 46 | 0.037037 | 0.055556 | 0 |  |
| metadata_extraction | metadata_ai_type | 58 | 58 | 0 | 0.000000 | 54 | 0.000000 | 0.000000 | 0 |  |
| metadata_extraction | metadata_common_method_bias | 55 | 55 | 0 | 0.000000 | 53 | 0.000000 | 0.000000 | 0 |  |
| metadata_extraction | metadata_construct_count | 4 | 3 | 2 | 0.666667 | 1 | 0.666667 | 0.666667 | 0 |  |
| metadata_extraction | metadata_country | 21 | 21 | 0 | 0.000000 | 19 | 0.000000 | 0.000000 | 0 |  |
| metadata_extraction | metadata_data_collection | 6 | 6 | 0 | 0.000000 | 4 | 0.000000 | 0.166667 | 0 |  |
| metadata_extraction | metadata_education_level | 40 | 39 | 3 | 0.076923 | 30 | 0.076923 | 0.102564 | 0 |  |
| metadata_extraction | metadata_first_author | 55 | 55 | 0 | 0.000000 | 55 | 0.000000 | 0.000000 | 0 |  |
| metadata_extraction | metadata_flag | 25 | 25 | 0 | 0.000000 | 24 | 0.000000 | 0.000000 | 0 |  |
| metadata_extraction | metadata_matrix_completeness | 19 | 18 | 0 | 0.000000 | 15 | 0.000000 | 0.000000 | 0 |  |
| metadata_extraction | metadata_notes | 10 | 10 | 0 | 0.000000 | 9 | 0.000000 | 0.000000 | 0 |  |
| metadata_extraction | metadata_sample_size | 7 | 7 | 1 | 0.142857 | 6 | 0.142857 | 0.142857 | 0 |  |
| metadata_extraction | metadata_sample_type | 5 | 5 | 0 | 0.000000 | 5 | 0.000000 | 0.000000 | 0 |  |
| metadata_extraction | metadata_source_type | 18 | 18 | 18 | 1.000000 | 0 | 1.000000 | 1.000000 | 0 |  |
| metadata_extraction | metadata_statistic_count | 5 | 4 | 4 | 1.000000 | 0 | 1.000000 | 1.000000 | 0 |  |
| metadata_extraction | metadata_study_design | 19 | 19 | 16 | 0.842105 | 0 | 0.842105 | 0.842105 | 0 |  |
| metadata_extraction | metadata_theoretical_framework | 9 | 9 | 0 | 0.000000 | 6 | 0.000000 | 0.222222 | 0 |  |
| metadata_extraction | metadata_user_role | 56 | 56 | 1 | 0.017857 | 54 | 0.017857 | 0.017857 | 0 |  |

## Three-Model Overlap Core Families

| model_id | denominator_family | task_stratum | row_n | scored_n | correct_n | accuracy | abstention_n | numeric_within_0_005_n |
|---|---|---|---|---|---|---|---|---|
| claude:sonnet | converted_or_model_derived_effect_size | converted_or_model_derived_beta | 30 | 30 | 0 | 0.000000 | 30 | 0 |
| claude:sonnet | converted_or_model_derived_effect_size | converted_or_model_derived_beta_path_converted_by_human_consensus | 53 | 53 | 0 | 0.000000 | 53 | 0 |
| claude:sonnet | converted_or_model_derived_effect_size | converted_or_model_derived_numeric_source_statistic_converted_by_human_consensus | 5 | 5 | 0 | 0.000000 | 5 | 0 |
| claude:sonnet | direct_r_effect_size_extraction | source_blank_direct_r | 43 | 43 | 0 | 0.000000 | 43 | 0 |
| claude:sonnet | direct_r_effect_size_extraction | source_reported_direct_r | 323 | 323 | 3 | 0.009288 | 320 | 3 |
| claude:sonnet | metadata_extraction | metadata_ai_tool_name | 56 | 53 | 1 | 0.018868 | 47 | 0 |
| claude:sonnet | metadata_extraction | metadata_ai_type | 58 | 57 | 0 | 0.000000 | 54 | 0 |
| claude:sonnet | metadata_extraction | metadata_common_method_bias | 55 | 55 | 1 | 0.018182 | 53 | 0 |
| claude:sonnet | metadata_extraction | metadata_construct_count | 4 | 3 | 3 | 1.000000 | 0 | 0 |
| claude:sonnet | metadata_extraction | metadata_country | 21 | 21 | 0 | 0.000000 | 19 | 0 |
| claude:sonnet | metadata_extraction | metadata_data_collection | 6 | 6 | 1 | 0.166667 | 3 | 0 |
| claude:sonnet | metadata_extraction | metadata_education_level | 40 | 39 | 4 | 0.102564 | 30 | 0 |
| claude:sonnet | metadata_extraction | metadata_first_author | 55 | 55 | 0 | 0.000000 | 55 | 0 |
| claude:sonnet | metadata_extraction | metadata_flag | 25 | 25 | 0 | 0.000000 | 19 | 0 |
| claude:sonnet | metadata_extraction | metadata_matrix_completeness | 19 | 18 | 0 | 0.000000 | 9 | 0 |
| claude:sonnet | metadata_extraction | metadata_notes | 10 | 10 | 0 | 0.000000 | 10 | 0 |
| claude:sonnet | metadata_extraction | metadata_sample_size | 7 | 7 | 1 | 0.142857 | 6 | 0 |
| claude:sonnet | metadata_extraction | metadata_sample_type | 5 | 5 | 0 | 0.000000 | 5 | 0 |
| claude:sonnet | metadata_extraction | metadata_source_type | 18 | 18 | 18 | 1.000000 | 0 | 0 |
| claude:sonnet | metadata_extraction | metadata_statistic_count | 5 | 4 | 4 | 1.000000 | 0 | 0 |
| claude:sonnet | metadata_extraction | metadata_study_design | 19 | 19 | 18 | 0.947368 | 0 | 0 |
| claude:sonnet | metadata_extraction | metadata_theoretical_framework | 9 | 9 | 0 | 0.000000 | 6 | 0 |
| claude:sonnet | metadata_extraction | metadata_user_role | 56 | 56 | 0 | 0.000000 | 54 | 0 |
| codex:gpt-5.5 | converted_or_model_derived_effect_size | converted_or_model_derived_beta | 30 | 30 | 0 | 0.000000 | 30 | 0 |
| codex:gpt-5.5 | converted_or_model_derived_effect_size | converted_or_model_derived_beta_path_converted_by_human_consensus | 53 | 53 | 0 | 0.000000 | 53 | 0 |
| codex:gpt-5.5 | converted_or_model_derived_effect_size | converted_or_model_derived_numeric_source_statistic_converted_by_human_consensus | 5 | 5 | 0 | 0.000000 | 5 | 0 |
| codex:gpt-5.5 | direct_r_effect_size_extraction | source_blank_direct_r | 43 | 43 | 0 | 0.000000 | 43 | 0 |
| codex:gpt-5.5 | direct_r_effect_size_extraction | source_reported_direct_r | 323 | 323 | 3 | 0.009288 | 320 | 3 |
| codex:gpt-5.5 | metadata_extraction | metadata_ai_tool_name | 56 | 54 | 2 | 0.037037 | 46 | 0 |
| codex:gpt-5.5 | metadata_extraction | metadata_ai_type | 58 | 58 | 0 | 0.000000 | 54 | 0 |
| codex:gpt-5.5 | metadata_extraction | metadata_common_method_bias | 55 | 55 | 0 | 0.000000 | 53 | 0 |
| codex:gpt-5.5 | metadata_extraction | metadata_construct_count | 4 | 3 | 2 | 0.666667 | 1 | 0 |
| codex:gpt-5.5 | metadata_extraction | metadata_country | 21 | 21 | 0 | 0.000000 | 19 | 0 |
| codex:gpt-5.5 | metadata_extraction | metadata_data_collection | 6 | 6 | 0 | 0.000000 | 4 | 0 |
| codex:gpt-5.5 | metadata_extraction | metadata_education_level | 40 | 39 | 3 | 0.076923 | 30 | 0 |
| codex:gpt-5.5 | metadata_extraction | metadata_first_author | 55 | 55 | 0 | 0.000000 | 55 | 0 |
| codex:gpt-5.5 | metadata_extraction | metadata_flag | 25 | 25 | 0 | 0.000000 | 24 | 0 |
| codex:gpt-5.5 | metadata_extraction | metadata_matrix_completeness | 19 | 18 | 0 | 0.000000 | 15 | 0 |
| codex:gpt-5.5 | metadata_extraction | metadata_notes | 10 | 10 | 0 | 0.000000 | 9 | 0 |
| codex:gpt-5.5 | metadata_extraction | metadata_sample_size | 7 | 7 | 1 | 0.142857 | 6 | 0 |
| codex:gpt-5.5 | metadata_extraction | metadata_sample_type | 5 | 5 | 0 | 0.000000 | 5 | 0 |
| codex:gpt-5.5 | metadata_extraction | metadata_source_type | 18 | 18 | 18 | 1.000000 | 0 | 0 |
| codex:gpt-5.5 | metadata_extraction | metadata_statistic_count | 5 | 4 | 4 | 1.000000 | 0 | 0 |
| codex:gpt-5.5 | metadata_extraction | metadata_study_design | 19 | 19 | 16 | 0.842105 | 0 | 0 |
| codex:gpt-5.5 | metadata_extraction | metadata_theoretical_framework | 9 | 9 | 0 | 0.000000 | 6 | 0 |
| codex:gpt-5.5 | metadata_extraction | metadata_user_role | 56 | 56 | 1 | 0.017857 | 54 | 0 |
| gemini:gemini-3-flash-preview | converted_or_model_derived_effect_size | converted_or_model_derived_beta | 30 | 30 | 0 | 0.000000 | 30 | 0 |
| gemini:gemini-3-flash-preview | converted_or_model_derived_effect_size | converted_or_model_derived_beta_path_converted_by_human_consensus | 53 | 53 | 0 | 0.000000 | 53 | 0 |
| gemini:gemini-3-flash-preview | converted_or_model_derived_effect_size | converted_or_model_derived_numeric_source_statistic_converted_by_human_consensus | 5 | 5 | 0 | 0.000000 | 5 | 0 |
| gemini:gemini-3-flash-preview | direct_r_effect_size_extraction | source_blank_direct_r | 43 | 43 | 0 | 0.000000 | 43 | 0 |
| gemini:gemini-3-flash-preview | direct_r_effect_size_extraction | source_reported_direct_r | 323 | 323 | 3 | 0.009288 | 320 | 3 |
| gemini:gemini-3-flash-preview | metadata_extraction | metadata_ai_tool_name | 56 | 55 | 1 | 0.018182 | 46 | 0 |
| gemini:gemini-3-flash-preview | metadata_extraction | metadata_ai_type | 58 | 58 | 0 | 0.000000 | 55 | 0 |
| gemini:gemini-3-flash-preview | metadata_extraction | metadata_common_method_bias | 55 | 55 | 0 | 0.000000 | 54 | 0 |
| gemini:gemini-3-flash-preview | metadata_extraction | metadata_construct_count | 4 | 4 | 1 | 0.250000 | 2 | 0 |
| gemini:gemini-3-flash-preview | metadata_extraction | metadata_country | 21 | 21 | 0 | 0.000000 | 19 | 0 |
| gemini:gemini-3-flash-preview | metadata_extraction | metadata_data_collection | 6 | 6 | 1 | 0.166667 | 3 | 0 |
| gemini:gemini-3-flash-preview | metadata_extraction | metadata_education_level | 40 | 40 | 1 | 0.025000 | 31 | 0 |
| gemini:gemini-3-flash-preview | metadata_extraction | metadata_first_author | 55 | 55 | 0 | 0.000000 | 55 | 0 |
| gemini:gemini-3-flash-preview | metadata_extraction | metadata_flag | 25 | 25 | 0 | 0.000000 | 23 | 0 |
| gemini:gemini-3-flash-preview | metadata_extraction | metadata_matrix_completeness | 19 | 19 | 0 | 0.000000 | 16 | 0 |
| gemini:gemini-3-flash-preview | metadata_extraction | metadata_notes | 10 | 10 | 0 | 0.000000 | 10 | 0 |
| gemini:gemini-3-flash-preview | metadata_extraction | metadata_sample_size | 7 | 7 | 1 | 0.142857 | 6 | 0 |
| gemini:gemini-3-flash-preview | metadata_extraction | metadata_sample_type | 5 | 5 | 0 | 0.000000 | 5 | 0 |
| gemini:gemini-3-flash-preview | metadata_extraction | metadata_source_type | 18 | 18 | 18 | 1.000000 | 0 | 0 |
| gemini:gemini-3-flash-preview | metadata_extraction | metadata_statistic_count | 5 | 5 | 2 | 0.400000 | 1 | 0 |
| gemini:gemini-3-flash-preview | metadata_extraction | metadata_study_design | 19 | 19 | 18 | 0.947368 | 0 | 0 |
| gemini:gemini-3-flash-preview | metadata_extraction | metadata_theoretical_framework | 9 | 9 | 0 | 0.000000 | 6 | 0 |
| gemini:gemini-3-flash-preview | metadata_extraction | metadata_user_role | 56 | 56 | 1 | 0.017857 | 54 | 0 |

## Interpretation

- Use the Codex rows as the primary workflow-validity evidence.
- Use the overlap rows only for supplementary cross-model sensitivity.
- High abstention counts are substantive behavior, not missing denominator
  artifacts, because scorable-row abstentions count as incorrect.
- `source_blank_direct_r` remains in the direct-r extraction family but
  should be flagged as weaker source-evidence quality.
- Converted/source-statistic rows should be discussed as numeric recovery
  under source-type separation, not as direct-r equivalence.
