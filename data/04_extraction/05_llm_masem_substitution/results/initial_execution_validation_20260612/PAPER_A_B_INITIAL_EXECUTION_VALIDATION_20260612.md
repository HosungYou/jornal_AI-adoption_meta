# Initial Execution Validation for Paper A and Paper B

Date: 2026-06-12

## Inputs

- MASEM input: `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_substitution_rerun_input_n_weighted_all_source_supported_20260612.csv`
- RQ3 task units: `data/04_extraction/05_llm_masem_substitution/results/paper2_rq3_triage_task_units_20260611.csv`
- Construct-set completeness: `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_matrix_construct_set_completeness_20260612.csv`
- Pair coverage: `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_matrix_pair_coverage_after_n_override_20260612.csv`

## Question 1. Paper A moderator feasibility

Initial criterion: a main-candidate moderator needs at least 20 nonmissing studies, at least 2 usable levels, at least 10 studies in the smallest usable level, at least 20 construct pairs represented, and no study-level ambiguity. A sensitivity candidate needs at least 15 nonmissing studies, at least 2 usable levels, at least 5 studies in the smallest usable level, and at least 15 construct pairs represented.

| Moderator | Studies nonmissing | Levels | Smallest level | Pair coverage | Gate | Top levels |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| ai_type | 36 | 2 | 15 | 48 | eligible_main_candidate | generative=21; general=15 |
| common_method_bias | 36 | 2 | 14 | 48 | eligible_main_candidate | not_addressed=22; addressed=14 |
| user_role | 36 | 3 | 2 | 48 | not_feasible_current_input | student=29; instructor=5; both=2 |
| country | 11 | 9 | 1 | 35 | not_feasible_current_input | Saudi Arabia=2; Palestine=2; Nigeria=1; Pakistan=1; Qatar=1; Germany=1; Austria=1; mixed=1 |
| region_derived_initial | 11 | 5 | 1 | 35 | not_feasible_current_input | Middle East=5; South Asia=2; Europe=2; Africa=1; mixed_region=1 |
| education_level | 10 | 2 | 2 | 36 | not_feasible_current_input | mixed=8; graduate=2 |
| theoretical_framework | 2 | 2 | 1 | 10 | not_feasible_current_input | TAM; HISAM; TRI=1; TAM+UTAUT=1 |

Answer: `ai_type` and `common_method_bias` are the only current main-candidate study-level moderators under the first-pass thresholds. `user_role` has enough nonmissing studies but fails level-balance requirements because instructor/both studies are sparse. `education_level`, `country`, initial derived region, and `theoretical_framework` are not feasible from the current input. `year/generative-AI era` cannot be validated from this MASEM input because no year column is present; it requires a bibliographic merge before OSMASEM.

Trust, anxiety, and self-efficacy remain non-moderator constructs. After researcher clarification, they should be audited separately as candidate mediator/mechanism constructs inside the MASEM path model.

Follow-up audit completed: `data/04_extraction/05_llm_masem_substitution/results/paper_a_mediator_feasibility_20260612/PAPER_A_MEDIATOR_FEASIBILITY_AUDIT_20260612.md`.

## Question 2. Paper B cross-model disagreement as RQ3 triage signal

| Metric | Value |
| --- | ---: |
| Multi-model scorable task units | 7859 |
| Cross-model disagreement flagged units | 6592 |
| Review-needed units in scope | 7809 |
| Precision among flagged units | 0.999 |
| Recall of review-needed units | 0.843 |
| Review burden share | 0.839 |
| Baseline review-needed rate | 0.994 |
| Precision lift vs baseline | 1.005 |

Top triage signals by lift:

| Signal | Flagged n | Precision | Recall | Lift |
| --- | ---: | ---: | ---: | ---: |
| blank_behavior_family | 6412 | 1.000 | 0.821 | 1.006 |
| primary_not_scored | 4335 | 1.000 | 0.555 | 1.006 |
| primary_incorrect | 3474 | 1.000 | 0.445 | 1.006 |
| primary_abstention | 979 | 1.000 | 0.125 | 1.006 |
| all_available_models_abstained | 832 | 1.000 | 0.107 | 1.006 |
| source_or_trace_risk | 601 | 1.000 | 0.077 | 1.006 |
| human_disagreement_trace | 467 | 1.000 | 0.060 | 1.006 |
| cross_model_behavior_disagreement | 6592 | 0.999 | 0.843 | 1.005 |

Answer: cross-model disagreement is usable as a main RQ3 descriptive triage dimension, but the first-pass evidence does not support treating it as a standalone high-yield threshold. Precision is high because the baseline review-needed rate is already extremely high, and lift is only about 1.0. It flags many blank/absence-behavior rows and has high recall, but it does not identify the high-consequence direct-r or converted numeric families in this first-pass file. The defensible operationalization is to report cross-model disagreement in the main RQ3 table together with review burden, family-specific coverage, human disagreement, source-risk flags, and primary abstention/error status; do not use it alone as a numeric-extraction triage rule.

## Question 3. Paper B broader TSSEM/MASEM rebuild feasibility

| Overall metric | Value |
| --- | ---: |
| input_rows | 804 |
| rows_with_r_numeric | 804 |
| rows_with_sample_size_numeric | 804 |
| rows_missing_sample_size_numeric | 0 |
| unique_studies | 74 |
| unique_construct_pairs | 51 |
| total_pairs | 45 |
| pairs_with_1plus_n_ready_study | 44 |
| pairs_with_3plus_n_ready_studies | 39 |
| pairs_with_5plus_n_ready_studies | 34 |
| pairs_with_10plus_n_ready_studies | 25 |
| min_n_ready_studies_per_pair | 0 |
| median_n_ready_studies_per_pair | 12 |
| max_n_ready_studies_per_pair | 58 |

Construct-set feasibility:

| Construct set | Construct count | Required pairs | Covered pairs | Complete-case studies | Min pair study count | Validation |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| core6_legacy_tssem_diagnostic | 6 | 15 | 15 | 16 | 22 | candidate_for_main_or_extended_diagnostic |
| core7_add_att | 7 | 21 | 21 | 3 | 10 | sparse_broader_rebuild_probe_only |
| core8_add_tru | 8 | 28 | 28 | 1 | 2 | sparse_broader_rebuild_probe_only |
| core9_add_anx | 9 | 36 | 35 | 0 | 0 | not_ready_current_input |
| theory_target_10 | 10 | 45 | 44 | 0 | 0 | not_ready_current_input |

Answer: the broader rebuild is justified as a staged execution attempt because the N-coverage gate is closed for the source-supported derived input and most construct pairs are represented. It is not yet justified as a replacement for the core-6 diagnostic in the main text because the full 10-construct route has 44/45 covered pairs, zero complete-case studies, and least-covered pairs with no N-ready studies. The defensible next route is to retain core-6 as the completed diagnostic, then attempt `core7_add_att` and `core8_add_tru` as sparse broader probes. Full 9- or 10-construct claims should remain blocked unless a later rebuild closes the missing-pair and complete-case/sparse-identification gates.

## Output files

- `paper_a_moderator_feasibility_20260612.csv`
- `paper_a_moderator_level_counts_20260612.csv`
- `paper_b_rq3_signal_validation_20260612.csv`
- `paper_b_rq3_cross_model_by_family_20260612.csv`
- `paper_b_rq3_review_priority_summary_20260612.csv`
- `paper_b_broader_masem_feasibility_20260612.csv`
- `paper_b_broader_masem_overall_20260612.csv`
- `paper_b_broader_masem_study_pair_thresholds_20260612.csv`
