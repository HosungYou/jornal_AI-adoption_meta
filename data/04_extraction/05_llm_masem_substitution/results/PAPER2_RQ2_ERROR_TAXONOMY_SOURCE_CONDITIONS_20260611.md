# Paper2 RQ2 Error Taxonomy and Source Conditions

Date: 2026-06-11

## Boundary

RQ2 describes error classes and source conditions. It is not a vendor
ranking and not a single accuracy denominator. Codex GPT-5.5 is the
primary workflow; Claude/Gemini rows are sensitivity evidence.

## Primary Codex Error Classes by Source Condition

| denominator_family | source_condition | error_class | row_n | scored_n | incorrect_n | correct_n |
|---|---|---|---|---|---|---|
| absence_or_blank_consensus | blank_or_absence_consensus | blank_consensus_nonblank_answer | 1996 | 1996 | 1996 | 0 |
| human_disagreement_trace | human_disagreement_trace | trace_response_behavior | 447 | 447 | 447 | 0 |
| metadata_extraction | source_evidence_and_locator_present | abstention_on_scorable_row | 381 | 381 | 381 | 0 |
| direct_r_effect_size_extraction | source_reported_direct_r | abstention_on_scorable_row | 320 | 320 | 320 | 0 |
| absence_or_blank_consensus | blank_or_absence_consensus | blank_consensus_abstention | 87 | 87 | 87 | 0 |
| converted_or_model_derived_effect_size | converted_or_source_statistic_beta_path_converted_by_human_consensus | abstention_on_scorable_row | 53 | 53 | 53 | 0 |
| direct_r_effect_size_extraction | source_blank_direct_r | abstention_on_scorable_row | 43 | 43 | 43 | 0 |
| structured_human_review_decision | source_evidence_and_locator_present | abstention_on_scorable_row | 34 | 34 | 34 | 0 |
| converted_or_model_derived_effect_size | converted_or_source_statistic_beta | abstention_on_scorable_row | 30 | 30 | 30 | 0 |
| metadata_extraction | source_evidence_and_locator_present | metadata_mismatch | 29 | 29 | 29 | 0 |
| human_disagreement_trace | human_disagreement_trace | abstention_on_scorable_row | 20 | 20 | 20 | 0 |
| structured_human_review_decision | source_evidence_and_locator_present | policy_or_label_mismatch | 7 | 7 | 7 | 0 |
| converted_or_model_derived_effect_size | converted_or_source_statistic_numeric_source_statistic_converted_by_human_consensus | abstention_on_scorable_row | 5 | 5 | 5 | 0 |
| eligibility_or_exclusion_decision | source_evidence_and_locator_present | policy_or_label_mismatch | 5 | 5 | 5 | 0 |
| metadata_extraction | source_evidence_and_locator_present | metadata_relaxed_match_only | 5 | 5 | 5 | 0 |
| statistic_type_policy_decision | source_evidence_and_locator_present | abstention_on_scorable_row | 4 | 4 | 4 | 0 |
| source_absence_decision | source_absence_decision | trace_response_behavior | 3 | 3 | 3 | 0 |
| statistic_type_policy_decision | source_evidence_and_locator_present | policy_or_label_mismatch | 3 | 3 | 3 | 0 |
| construct_or_sample_mapping_decision | source_evidence_and_locator_present | abstention_on_scorable_row | 2 | 2 | 2 | 0 |
| absence_or_blank_consensus | blank_or_absence_consensus | not_scored_no_locked_answer | 4329 | 0 | 0 | 0 |
| direct_r_effect_size_extraction | source_reported_direct_r | numeric_within_0_005 | 3 | 3 | 0 | 3 |
| metadata_extraction | source_evidence_and_locator_present | metadata_strict_match | 47 | 47 | 0 | 47 |
| metadata_extraction | source_evidence_and_locator_present | not_scored_no_locked_answer | 6 | 0 | 0 | 0 |

## Selected Three-Model Overlap Error Classes

| model_id | denominator_family | task_stratum | source_condition | error_class | row_n | incorrect_n |
|---|---|---|---|---|---|---|
| claude:sonnet | construct_or_sample_mapping_decision | source_evidence_and_locator_present | source_evidence_and_locator_present | abstention_on_scorable_row | 2 | 2 |
| claude:sonnet | converted_or_model_derived_effect_size | converted_or_source_statistic_beta | converted_or_source_statistic_beta | abstention_on_scorable_row | 30 | 30 |
| claude:sonnet | converted_or_model_derived_effect_size | converted_or_source_statistic_beta_path_converted_by_human_consensus | converted_or_source_statistic_beta_path_converted_by_human_consensus | abstention_on_scorable_row | 53 | 53 |
| claude:sonnet | converted_or_model_derived_effect_size | converted_or_source_statistic_numeric_source_statistic_converted_by_human_consensus | converted_or_source_statistic_numeric_source_statistic_converted_by_human_consensus | abstention_on_scorable_row | 5 | 5 |
| claude:sonnet | direct_r_effect_size_extraction | source_blank_direct_r | source_blank_direct_r | abstention_on_scorable_row | 43 | 43 |
| claude:sonnet | direct_r_effect_size_extraction | source_reported_direct_r | source_reported_direct_r | abstention_on_scorable_row | 320 | 320 |
| claude:sonnet | human_disagreement_trace | human_disagreement_trace | human_disagreement_trace | abstention_on_scorable_row | 108 | 108 |
| claude:sonnet | metadata_extraction | metadata_ai_tool_name | source_evidence_and_locator_present | abstention_on_scorable_row | 47 | 47 |
| claude:sonnet | metadata_extraction | metadata_ai_tool_name | source_evidence_and_locator_present | metadata_mismatch | 5 | 5 |
| claude:sonnet | metadata_extraction | metadata_ai_type | source_evidence_and_locator_present | abstention_on_scorable_row | 54 | 54 |
| claude:sonnet | metadata_extraction | metadata_ai_type | source_evidence_and_locator_present | metadata_mismatch | 3 | 3 |
| claude:sonnet | metadata_extraction | metadata_common_method_bias | source_evidence_and_locator_present | abstention_on_scorable_row | 53 | 53 |
| claude:sonnet | metadata_extraction | metadata_common_method_bias | source_evidence_and_locator_present | metadata_mismatch | 1 | 1 |
| claude:sonnet | metadata_extraction | metadata_country | source_evidence_and_locator_present | abstention_on_scorable_row | 19 | 19 |
| claude:sonnet | metadata_extraction | metadata_country | source_evidence_and_locator_present | metadata_mismatch | 2 | 2 |
| claude:sonnet | metadata_extraction | metadata_data_collection | source_evidence_and_locator_present | abstention_on_scorable_row | 3 | 3 |
| claude:sonnet | metadata_extraction | metadata_data_collection | source_evidence_and_locator_present | metadata_mismatch | 2 | 2 |
| claude:sonnet | metadata_extraction | metadata_education_level | source_evidence_and_locator_present | abstention_on_scorable_row | 30 | 30 |
| claude:sonnet | metadata_extraction | metadata_education_level | source_evidence_and_locator_present | metadata_mismatch | 4 | 4 |
| claude:sonnet | metadata_extraction | metadata_first_author | source_evidence_and_locator_present | abstention_on_scorable_row | 55 | 55 |
| claude:sonnet | metadata_extraction | metadata_flag | source_evidence_and_locator_present | abstention_on_scorable_row | 19 | 19 |
| claude:sonnet | metadata_extraction | metadata_flag | source_evidence_and_locator_present | metadata_mismatch | 6 | 6 |
| claude:sonnet | metadata_extraction | metadata_matrix_completeness | source_evidence_and_locator_present | abstention_on_scorable_row | 9 | 9 |
| claude:sonnet | metadata_extraction | metadata_matrix_completeness | source_evidence_and_locator_present | metadata_mismatch | 9 | 9 |
| claude:sonnet | metadata_extraction | metadata_notes | source_evidence_and_locator_present | abstention_on_scorable_row | 10 | 10 |
| claude:sonnet | metadata_extraction | metadata_sample_size | source_evidence_and_locator_present | abstention_on_scorable_row | 6 | 6 |
| claude:sonnet | metadata_extraction | metadata_sample_type | source_evidence_and_locator_present | abstention_on_scorable_row | 5 | 5 |
| claude:sonnet | metadata_extraction | metadata_study_design | source_evidence_and_locator_present | metadata_mismatch | 1 | 1 |
| claude:sonnet | metadata_extraction | metadata_theoretical_framework | source_evidence_and_locator_present | abstention_on_scorable_row | 6 | 6 |
| claude:sonnet | metadata_extraction | metadata_theoretical_framework | source_evidence_and_locator_present | metadata_mismatch | 1 | 1 |
| claude:sonnet | metadata_extraction | metadata_user_role | source_evidence_and_locator_present | abstention_on_scorable_row | 54 | 54 |
| claude:sonnet | metadata_extraction | metadata_user_role | source_evidence_and_locator_present | metadata_mismatch | 2 | 2 |
| claude:sonnet | source_absence_decision | source_absence_decision | source_absence_decision | abstention_on_scorable_row | 3 | 3 |
| claude:sonnet | statistic_type_policy_decision | source_evidence_and_locator_present | source_evidence_and_locator_present | abstention_on_scorable_row | 7 | 7 |
| claude:sonnet | structured_human_review_decision | source_evidence_and_locator_present | source_evidence_and_locator_present | abstention_on_scorable_row | 41 | 41 |
| codex:gpt-5.5 | construct_or_sample_mapping_decision | source_evidence_and_locator_present | source_evidence_and_locator_present | abstention_on_scorable_row | 2 | 2 |
| codex:gpt-5.5 | converted_or_model_derived_effect_size | converted_or_source_statistic_beta | converted_or_source_statistic_beta | abstention_on_scorable_row | 30 | 30 |
| codex:gpt-5.5 | converted_or_model_derived_effect_size | converted_or_source_statistic_beta_path_converted_by_human_consensus | converted_or_source_statistic_beta_path_converted_by_human_consensus | abstention_on_scorable_row | 53 | 53 |
| codex:gpt-5.5 | converted_or_model_derived_effect_size | converted_or_source_statistic_numeric_source_statistic_converted_by_human_consensus | converted_or_source_statistic_numeric_source_statistic_converted_by_human_consensus | abstention_on_scorable_row | 5 | 5 |
| codex:gpt-5.5 | direct_r_effect_size_extraction | source_blank_direct_r | source_blank_direct_r | abstention_on_scorable_row | 43 | 43 |
| codex:gpt-5.5 | direct_r_effect_size_extraction | source_reported_direct_r | source_reported_direct_r | abstention_on_scorable_row | 320 | 320 |
| codex:gpt-5.5 | human_disagreement_trace | human_disagreement_trace | human_disagreement_trace | abstention_on_scorable_row | 20 | 20 |
| codex:gpt-5.5 | metadata_extraction | metadata_ai_tool_name | source_evidence_and_locator_present | abstention_on_scorable_row | 46 | 46 |
| codex:gpt-5.5 | metadata_extraction | metadata_ai_tool_name | source_evidence_and_locator_present | metadata_mismatch | 5 | 5 |
| codex:gpt-5.5 | metadata_extraction | metadata_ai_type | source_evidence_and_locator_present | abstention_on_scorable_row | 54 | 54 |
| codex:gpt-5.5 | metadata_extraction | metadata_ai_type | source_evidence_and_locator_present | metadata_mismatch | 4 | 4 |
| codex:gpt-5.5 | metadata_extraction | metadata_common_method_bias | source_evidence_and_locator_present | abstention_on_scorable_row | 53 | 53 |
| codex:gpt-5.5 | metadata_extraction | metadata_common_method_bias | source_evidence_and_locator_present | metadata_mismatch | 2 | 2 |
| codex:gpt-5.5 | metadata_extraction | metadata_construct_count | source_evidence_and_locator_present | abstention_on_scorable_row | 1 | 1 |
| codex:gpt-5.5 | metadata_extraction | metadata_country | source_evidence_and_locator_present | abstention_on_scorable_row | 19 | 19 |
| codex:gpt-5.5 | metadata_extraction | metadata_country | source_evidence_and_locator_present | metadata_mismatch | 2 | 2 |
| codex:gpt-5.5 | metadata_extraction | metadata_data_collection | source_evidence_and_locator_present | abstention_on_scorable_row | 4 | 4 |
| codex:gpt-5.5 | metadata_extraction | metadata_data_collection | source_evidence_and_locator_present | metadata_mismatch | 1 | 1 |
| codex:gpt-5.5 | metadata_extraction | metadata_education_level | source_evidence_and_locator_present | abstention_on_scorable_row | 30 | 30 |
| codex:gpt-5.5 | metadata_extraction | metadata_education_level | source_evidence_and_locator_present | metadata_mismatch | 5 | 5 |
| codex:gpt-5.5 | metadata_extraction | metadata_first_author | source_evidence_and_locator_present | abstention_on_scorable_row | 55 | 55 |
| codex:gpt-5.5 | metadata_extraction | metadata_flag | source_evidence_and_locator_present | abstention_on_scorable_row | 24 | 24 |
| codex:gpt-5.5 | metadata_extraction | metadata_flag | source_evidence_and_locator_present | metadata_mismatch | 1 | 1 |
| codex:gpt-5.5 | metadata_extraction | metadata_matrix_completeness | source_evidence_and_locator_present | abstention_on_scorable_row | 15 | 15 |
| codex:gpt-5.5 | metadata_extraction | metadata_matrix_completeness | source_evidence_and_locator_present | metadata_mismatch | 3 | 3 |

## Interpretation

- The dominant RQ2 pattern is abstention on scorable rows, which should be
  reported as model behavior and not treated as missing data.
- `source_blank_direct_r` is retained in primary direct-r extraction but
  marked as weaker source-evidence quality.
- Converted beta/path/source-statistic rows are high-consequence numeric
  extraction strata with source-type separation.
- Trace and blank-consensus families describe review/triage behavior rather
  than final evidence-content accuracy.
