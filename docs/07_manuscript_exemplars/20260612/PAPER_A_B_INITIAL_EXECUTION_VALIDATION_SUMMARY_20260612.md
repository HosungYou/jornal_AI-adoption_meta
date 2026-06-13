# Paper A/B Initial Execution Validation Summary

Date: 2026-06-12

LongTable mode: evidence-first checkpoint after researcher decision sync

Primary output report: `data/04_extraction/05_llm_masem_substitution/results/initial_execution_validation_20260612/PAPER_A_B_INITIAL_EXECUTION_VALIDATION_20260612.md`

## Question 1. Which Paper A moderators are feasible?

First-pass data source: `paper2_masem_substitution_rerun_input_n_weighted_all_source_supported_20260612.csv`.

Criterion used:

1. at least 20 nonmissing studies,
2. at least 2 usable levels,
3. at least 10 studies in the smallest usable level,
4. at least 20 construct pairs represented,
5. no study-level ambiguity.

Result:

| Candidate | Studies nonmissing | Smallest level | First-pass status |
| --- | ---: | ---: | --- |
| `ai_type` | 36 | 15 | Main-candidate moderator |
| `common_method_bias` | 36 | 14 | Main-candidate statistically; likely better as QC/sensitivity unless researcher wants it in main text |
| `user_role` | 36 | 2 | Not feasible because instructor/both levels are sparse |
| `education_level` | 10 | 2 | Not feasible |
| `country` / derived region | 11 | 1 | Not feasible without broader cultural coding |
| `theoretical_framework` | 2 | 1 | Not feasible |

Answer: Trust, anxiety, and self-efficacy are not moderators in the current Paper A model. The researcher clarified that they should be evaluated as mediator/mechanism constructs inside the MASEM path model. The only first-pass main-candidate moderator matching the substantive route is `ai_type`. `common_method_bias` is empirically eligible but should probably be reported as methodological/QC sensitivity rather than a theory moderator unless the researcher explicitly wants it in the main model.

Resolved execution issue: `year/generative-AI era` was not present in the current MASEM input, so a bibliographic year merge was run from `full_corpus_freeze_gap_map_20260608.csv`. The merge found 66 studies with year, all post-2023, and 8 missing year. Therefore the pre/post generative-era moderator is not currently feasible.

## Paper A mediator correction added after researcher clarification

Additional audit: `data/04_extraction/05_llm_masem_substitution/results/paper_a_mediator_feasibility_20260612/PAPER_A_MEDIATOR_FEASIBILITY_AUDIT_20260612.md`.

Result:

1. `ATT` is the strongest standard mediator: `PE/EE/SI/FC -> ATT -> BI` are main indirect candidates.
2. `TRU` is a main AI-specific mediator candidate for `PE -> TRU -> BI` and `EE -> TRU -> BI`; `SI -> TRU -> BI` is sensitivity-level.
3. `SE` is sensitivity-level only for current indirect-effect testing.
4. `ANX` is underpowered or not identified for confirmed mediation in the current input.

## Question 2. Can cross-model disagreement operate as main RQ3 evidence?

First-pass data source: `paper2_rq3_triage_task_units_20260611.csv`.

Result:

| Metric | Value |
| --- | ---: |
| Multi-model task units | 7,859 |
| Cross-model disagreement flagged units | 6,592 |
| Review-needed units | 7,809 |
| Precision among flagged units | 0.999 |
| Recall of review-needed units | 0.843 |
| Review burden share | 0.839 |
| Baseline review-needed rate | 0.994 |
| Precision lift over baseline | 1.005 |

Answer: Cross-model disagreement can remain in main RQ3, but not as a standalone high-yield threshold. The review-needed baseline is already extremely high, so precision is high for almost every signal. Cross-model disagreement is mainly a descriptive triage dimension showing where model behavior diverges, especially in blank/absence behavior. It does not identify high-consequence direct-r or converted numeric extraction rows in this first-pass file.

Recommended RQ3 wording: cross-model disagreement is one main triage signal, reported alongside human disagreement, source-risk flags, primary abstention/error status, review burden, and denominator family. It should not be framed as a standalone detector or vendor comparison.

## Question 3. Can the broader TSSEM/MASEM rebuild extend or replace core-6?

First-pass data sources:

1. `paper2_masem_matrix_construct_set_completeness_20260612.csv`
2. `paper2_masem_matrix_pair_coverage_after_n_override_20260612.csv`
3. `paper2_masem_substitution_rerun_input_n_weighted_all_source_supported_20260612.csv`

Overall gate:

| Metric | Value |
| --- | ---: |
| Input rows | 804 |
| Rows with r | 804 |
| Rows with numeric N | 804 |
| Unique studies | 74 |
| Pair slots in 10-construct model | 45 |
| Pairs with at least 1 N-ready study | 44 |
| Pairs with at least 5 N-ready studies | 34 |
| Pairs with at least 10 N-ready studies | 25 |

Construct-set feasibility:

| Construct set | Complete-case studies | Min pair study count | First-pass status |
| --- | ---: | ---: | --- |
| `core6_legacy_tssem_diagnostic` | 16 | 22 | Completed diagnostic / strongest route |
| `core7_add_att` | 3 | 10 | Sparse broader probe only |
| `core8_add_tru` | 1 | 2 | Sparse broader probe only |
| `core9_add_anx` | 0 | 0 | Not ready |
| `theory_target_10` | 0 | 0 | Not ready |

Answer: The broader rebuild was attempted only as staged probing. The core-6 diagnostic remains the completed main-text SEM evidence. `core7_add_att` completed conservative complete-case Stage 1 with 3 studies but failed the Stage 2 path-model probe because `aCov` was not positive definite. `core8_add_tru` had only 1 complete-case study and was not runnable as a TSSEM path diagnostic. Full 9- or 10-construct claims remain blocked by missing/sparse pair coverage and zero complete-case studies.

## Required researcher checkpoints

These are the remaining high-risk choices after the first-pass analysis:

1. Should Paper A main moderator reporting use `ai_type` only, or `ai_type` plus `common_method_bias` with `common_method_bias` labeled as methodological/QC sensitivity?
2. Should Paper B RQ3 explicitly say cross-model disagreement is a main descriptive triage dimension but not a standalone high-yield numeric-extraction detector?
3. Should Paper B RQ4 use staged SEM reporting: core-6 as completed main diagnostic, core7/core8 as sparse probes if they converge, and core9/core10 blocked unless a later rebuild improves coverage?
