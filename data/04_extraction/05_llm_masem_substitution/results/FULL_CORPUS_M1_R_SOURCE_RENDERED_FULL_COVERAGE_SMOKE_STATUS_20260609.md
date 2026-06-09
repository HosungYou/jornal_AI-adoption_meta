# Full-Corpus M1-R Source-Rendered Full-Coverage Smoke Status

Date: 2026-06-09

Status: balanced full-coverage source-rendered smoke completed and locked. This is a prompt/export/locking/scoring diagnostic only; it is not a full-corpus model run, LLM accuracy result, model comparison, procedure comparison, or MASEM substitution claim.

## Research Stage

- Step 4 frozen human reference is complete.
- Step 5 source materialization and source-rendering coverage are clean.
- This smoke tests whether the source-packet prompt path can produce locked, quote-suppressed, scoreable output across all three denominator families before any full-corpus run.

## Execution Evidence

- Run ID: `paper_b_full_corpus_m1_raw_source_rendered_full_coverage_smoke_20260609`
- Locked output: `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_source_rendered_full_coverage_smoke_20260609.csv`
- Locked output SHA-256: `1bab98efac1eb1a5bbed8453b1e46e1524a308afab62fa645d7c4825a69f514d`
- Provider/model surface: `openai`; `codex:gpt-5.5`.
- Local CLI/version lock: `codex-cli 0.137.0; model_selector=gpt-5.5`.
- Procedure ID: `raw_model_extraction_source_rendered_smoke`
- Prompt version: `paper_b_step5_full_corpus_prompt_v1_20260609_source_packet_full_coverage_smoke`
- Source packet manifest: `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_rendering_full_coverage_manifest_20260609.csv`
- Smoke task list: `data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/source_rendered_full_coverage_smoke_task_ids_20260609.csv`

## Smoke Results

- Rows: 30
- Studies: 3 (`S002`, `S003`, `S007`)
- Denominator family balance: `primary_direct_r_or_source_reported_correlation`=10; `primary_latent_or_construct_correlation_with_source_type_flag`=10; `secondary_beta_or_path_converted_effect_size`=10
- `model_cli_error` rows: 0
- `source_quote_policy_violation` rows: 0
- Nonblank model answers: 13
- Nonblank normalized answers: 13
- Nonblank model source locators: 13
- Nonblank committed source quotes: 0
- Abstentions / insufficient evidence rows: 17
- Smoke diagnostic correct rows under numeric tolerance: 9/30

## Family Diagnostics

| Family | Rows | Scored | Correct | Abstentions | Nonblank answers | Nonblank locators | Nonblank quotes | Smoke diagnostic accuracy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| primary_direct_r_or_source_reported_correlation | 10 | 10 | 0 | 10 | 0 | 0 | 0 | 0.000000 |
| primary_latent_or_construct_correlation_with_source_type_flag | 10 | 10 | 9 | 0 | 10 | 10 | 0 | 0.900000 |
| secondary_beta_or_path_converted_effect_size | 10 | 10 | 0 | 7 | 3 | 3 | 0 | 0.000000 |

## Boundary

- The committed locked output suppresses source quotes; private source packets remain outside Git.
- The model prompt did not receive human reference values or human-adjudicated source locators.
- These 30 rows are deliberately narrow smoke diagnostics. Do not generalize them as Paper B/C full-corpus performance.
- Full-corpus `M1-R`, `M1-P`, `M2-R`, and optional `M3-R` still require explicit run-condition authorization and budget/model-selector confirmation.

## Next Gate

Review the 17 abstentions and 13 nonblank answers for prompt/path behavior. If acceptable, record explicit authorization for full-corpus `M1-R` or define a larger staged shard plan. Do not report accuracy/MASEM substitution claims from this smoke.
