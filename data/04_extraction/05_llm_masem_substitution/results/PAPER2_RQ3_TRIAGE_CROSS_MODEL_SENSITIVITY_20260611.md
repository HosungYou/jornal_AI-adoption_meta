# Paper2 RQ3 Human-Review Triage and Cross-Model Sensitivity

Date: 2026-06-11

## Boundary

RQ3 starts from the full 8,783 task-unit reference universe and left-joins
locked model rows where available. Model behavior is used as
review-prioritization evidence. It does not
rank vendors. Cross-model disagreement is a supplementary triage signal
for identifying task units that need expert review.

## Priority Counts

| Review priority | Task units |
|---|---:|
| P2_blank_behavior_audit | 6412 |
| P0_expert_review_numeric_or_masem | 1196 |
| P1_source_or_human_disagreement_review | 649 |
| P1_review_signal | 483 |
| P3_low_priority_after_primary_check | 42 |
| P2_scoring_completeness_check | 1 |

## Signal Counts

| Signal | Task units |
|---|---:|
| cross_model_behavior_disagreement | 6592 |
| blank_behavior_family | 6412 |
| primary_not_scored | 4335 |
| primary_incorrect | 3474 |
| source_or_trace_risk | 1525 |
| high_consequence_numeric | 1199 |
| primary_abstention | 979 |
| primary_missing_model_row | 924 |
| reference_only_no_locked_model_row | 924 |
| all_available_models_abstained | 832 |
| source_pointer_only_no_evidence_text | 746 |
| human_disagreement_trace | 467 |

## Summary by Priority, Family, and Source Condition

| comparison_scope | review_priority | denominator_family | source_condition | task_n | cross_model_behavior_disagreement_n | primary_incorrect_n | primary_abstention_n | primary_missing_model_row_n | all_available_models_abstained_n |
|---|---|---|---|---|---|---|---|---|---|
| three_model_overlap | P2_blank_behavior_audit | absence_or_blank_consensus | blank_or_absence_consensus | 6412 | 6104 | 2083 | 87 | 0 | 0 |
| three_model_overlap | P1_source_or_human_disagreement_review | human_disagreement_trace | human_disagreement_trace | 467 | 396 | 467 | 20 | 0 | 0 |
| three_model_overlap | P1_review_signal | metadata_extraction | source_evidence_and_locator_present | 428 | 54 | 415 | 381 | 0 | 366 |
| reference_only_no_locked_model_row | P0_expert_review_numeric_or_masem | direct_r_effect_size_extraction | source_pointer_only_direct_r | 375 | 0 | 0 | 0 | 375 | 0 |
| reference_only_no_locked_model_row | P0_expert_review_numeric_or_masem | converted_or_model_derived_effect_size | source_pointer_only_converted_or_source_statistic_secondary_source_statistic_converted_by_human_consensus | 348 | 0 | 0 | 0 | 348 | 0 |
| three_model_overlap | P0_expert_review_numeric_or_masem | direct_r_effect_size_extraction | source_reported_direct_r | 320 | 0 | 320 | 320 | 0 | 320 |
| reference_only_no_locked_model_row | P1_source_or_human_disagreement_review | not_derivable_trace | not_derivable_trace | 103 | 0 | 0 | 0 | 103 | 0 |
| reference_only_no_locked_model_row | P1_source_or_human_disagreement_review | excluded_duplicate_source | excluded_duplicate_source | 75 | 0 | 0 | 0 | 75 | 0 |
| three_model_overlap | P0_expert_review_numeric_or_masem | converted_or_model_derived_effect_size | converted_or_source_statistic_beta_path_converted_by_human_consensus | 53 | 0 | 53 | 53 | 0 | 53 |
| three_model_overlap | P0_expert_review_numeric_or_masem | direct_r_effect_size_extraction | source_blank_direct_r | 43 | 0 | 43 | 43 | 0 | 43 |
| three_model_overlap | P1_review_signal | structured_human_review_decision | source_evidence_and_locator_present | 41 | 28 | 41 | 34 | 0 | 13 |
| three_model_overlap | P3_low_priority_after_primary_check | metadata_extraction | source_evidence_and_locator_present | 39 | 0 | 0 | 0 | 0 | 0 |
| three_model_overlap | P0_expert_review_numeric_or_masem | converted_or_model_derived_effect_size | converted_or_source_statistic_beta | 30 | 0 | 30 | 30 | 0 | 30 |
| reference_only_no_locked_model_row | P0_expert_review_numeric_or_masem | converted_or_model_derived_effect_size | source_pointer_only_converted_or_source_statistic_beta_path_converted_by_human_consensus | 22 | 0 | 0 | 0 | 22 | 0 |
| three_model_overlap | P1_review_signal | statistic_type_policy_decision | source_evidence_and_locator_present | 7 | 5 | 7 | 4 | 0 | 2 |
| three_model_overlap | P0_expert_review_numeric_or_masem | converted_or_model_derived_effect_size | converted_or_source_statistic_numeric_source_statistic_converted_by_human_consensus | 5 | 0 | 5 | 5 | 0 | 5 |
| three_model_overlap | P1_review_signal | eligibility_or_exclusion_decision | source_evidence_and_locator_present | 5 | 0 | 5 | 0 | 0 | 0 |
| three_model_overlap | P1_source_or_human_disagreement_review | source_absence_decision | source_absence_decision | 3 | 3 | 3 | 0 | 0 | 0 |
| three_model_overlap | P3_low_priority_after_primary_check | direct_r_effect_size_extraction | source_reported_direct_r | 3 | 0 | 0 | 0 | 0 | 0 |
| three_model_overlap | P1_review_signal | construct_or_sample_mapping_decision | source_evidence_and_locator_present | 2 | 2 | 2 | 2 | 0 | 0 |
| reference_only_no_locked_model_row | P1_source_or_human_disagreement_review | trace_influence_diagnostic | trace_influence_diagnostic | 1 | 0 | 0 | 0 | 1 | 0 |
| three_model_overlap | P2_scoring_completeness_check | metadata_extraction | source_evidence_and_locator_present | 1 | 0 | 0 | 0 | 0 | 0 |

## Interpretation

- P0 rows are high-consequence numeric or downstream MASEM rows where the
  primary workflow abstained, was incorrect, or the source condition itself
  requires expert review.
- P1 rows include source-risk, human-disagreement, or cross-model behavior
  disagreement signals.
- P2 blank-behavior rows are split from generic P1 review signals because
  they describe triage behavior, not final evidence-content accuracy.
- Reference-only rows without locked model output remain in the task-unit
  universe and are marked as model-coverage gaps rather than dropped.
- Cross-model disagreement is used only to prioritize review load; it is not
  a model or vendor ranking.
