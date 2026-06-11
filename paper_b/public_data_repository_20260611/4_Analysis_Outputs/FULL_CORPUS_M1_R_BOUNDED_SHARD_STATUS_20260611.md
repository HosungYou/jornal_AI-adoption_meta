# Full-Corpus M1-R Bounded Shard Status

Date: 2026-06-11

## Research Stage

- Step 4 source-anchored full-corpus reference freeze remains complete.
- This is a bounded post-freeze `M1-R` staged shard, not a full-corpus
  accuracy, model-comparison, or MASEM substitution-stability claim.
- Private source packets were regenerated for the 10 selected studies and kept
  under the ignored private source-rendering folder.

## Execution Evidence

- Run ID: `paper_b_full_corpus_m1_raw_bounded_shard_0090_20260611`
- Locked output:
  `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_bounded_shard_0090_20260611.csv`
- Task bundle:
  `data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/source_rendered_bounded_m1r_shard_task_ids_20260611.csv`
- Source packet manifest:
  `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_rendering_bounded_m1r_shard_packet_manifest_20260611.csv`
- Source packet status:
  `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/SOURCE_RENDERING_BOUNDED_M1R_SHARD_PACKET_STATUS_20260611.md`
- Provider/model surface: `openai`; `codex:gpt-5.5` via Codex CLI.
- Local CLI/version lock: `codex-cli 0.139.0`.
- Procedure ID: `raw_model_extraction_source_rendered_bounded_shard`
- Prompt version:
  `paper_b_step5_full_corpus_prompt_v1_20260609_source_packet_bounded_shard`
- Manifest registration:
  `data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_LOCKED_OUTPUT_MANIFEST_20260609.csv`

## Locked Output Checks

- Rows: 90
- Locked rows: 90/90
- `model_cli_error` rows: 0/90
- Source quote policy violations: 0/90
- Nonblank model answers: 65/90
- Abstentions / insufficient-evidence rows: 25/90
- Nonblank source locators: 73/90
- Nonblank raw-beta fields: 11/90
- Nonblank converted-effect fields: 11/90

## Generic Numeric Scoring

Scoring artifact:
`data/04_extraction/05_llm_masem_substitution/results/paper_b_full_corpus_m1_raw_scored_20260611.csv`

Summary artifact:
`data/04_extraction/05_llm_masem_substitution/results/paper_b_full_corpus_m1_raw_score_summary_20260611.csv`

| Denominator family | Rows | Correct | Accuracy |
|---|---:|---:|---:|
| `primary_direct_r_or_source_reported_correlation` | 30 | 15 | 0.500000 |
| `primary_latent_or_construct_correlation_with_source_type_flag` | 30 | 27 | 0.900000 |
| `secondary_beta_or_path_converted_effect_size` | 30 | 13 | 0.433333 |

## Exception-Aware Gate

Exception-layer artifacts:

- `data/04_extraction/05_llm_masem_substitution/results/paper_b_full_corpus_m1_raw_exception_layer_scored_20260611.csv`
- `data/04_extraction/05_llm_masem_substitution/results/paper_b_full_corpus_m1_raw_exception_layer_scored_summary_20260611.csv`

The exception-layer wrapper now processes 191 total locked rows across the
registered post-freeze `M1-R` smoke/probe/shard outputs. The bounded shard rows
are scored in the generic numeric scorer; rows without a matching beta/path
exception-layer record remain outside the contract-aware beta/path exception
denominator. Across all registered post-freeze rows, 45 rows match the
exception layer and 2 rows are contract-aware scored as correct.

## Boundary

- Do not report this 90-row shard as full-corpus LLM accuracy.
- Do not use this shard alone to claim MASEM substitution stability.
- Report it as staged source-rendered evidence with denominator-family
  boundaries and with beta/path exception-layer gating preserved.
