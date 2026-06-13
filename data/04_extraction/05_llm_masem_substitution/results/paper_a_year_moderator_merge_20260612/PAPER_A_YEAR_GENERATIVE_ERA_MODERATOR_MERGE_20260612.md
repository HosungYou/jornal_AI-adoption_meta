# Paper A Year / Generative-Era Moderator Merge

Date: 2026-06-12

MASEM input: `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_substitution_rerun_input_n_weighted_all_source_supported_20260612.csv`
Year source: `data/04_extraction/04_reference_standard_freeze/full_corpus_freeze_gap_map_20260608.csv`

## Rule

- `post_2023_generative_ai_era`: publication year >= 2023.
- `pre_2023_or_non_generative_era`: publication year < 2023.

## Coverage

- Study IDs in MASEM input: 74
- Study IDs with year after merge: 66
- Study IDs missing year after merge: 8
- Era moderator gate status: `not_feasible_current_input`

| Era | Study count | Median construct pairs | Min pairs | Max pairs |
| --- | ---: | ---: | ---: | ---: |
| post_2023_generative_ai_era | 66 | 10.0 | 1 | 28 |
| missing_year | 8 | 12.0 | 6 | 21 |

## Interpretation

The year/generative-era moderator is `not_feasible_current_input` under the first-pass merge. If retained, it should be treated as a true study-level moderator distinct from the mediator/mechanism constructs.
