# Full-Corpus M1-R Source-Rendered Table-Retrieval Smoke Status

Date: 2026-06-10

## Research Stage

- Step 4 source-anchored reference freeze remains complete.
- Step 5 source-materialization/readability gates are unblocked for all target studies.
- This smoke tests the retrieval-directed, source-rendered path for `S003` direct-r and true beta/path tasks only; it is still a diagnostic, not a full-corpus accuracy claim.

## Execution Evidence

- Run ID: `paper_b_full_corpus_m1_raw_source_rendered_table_retrieval_smoke_20260610`
- Locked output: `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_source_rendered_table_retrieval_smoke_20260610.csv`
- Locked output SHA-256: `a1b50048807738aba5f2f72b85bfe290ccc8191ee969146cf008cb355ac3645c`
- Provider/model surface: `openai`; `codex_cli:default_unspecified` via Codex CLI.
- Local CLI/version lock: `codex-cli 0.137.0`.
- Procedure ID: `raw_model_extraction_source_rendered_table_retrieval_smoke`
- Prompt version: `paper_b_step5_full_corpus_prompt_v3_20260609_table_retrieval_smoke`
- Task file: `data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/source_rendered_table_retrieval_smoke_task_ids_20260609.csv`
- Manifest row: `source_rendered_table_retrieval_smoke_locked_output`

## Smoke Results

- Rows: 25
- Correct rows under numeric tolerance: 13/25
- Abstentions / insufficient evidence rows: 6/25
- Nonblank model answers: 19/25
- Nonblank source locators: 19/25
- Route violations: 0/25
| Category | Study | Rows | Correct | Abstentions | Nonblank answers | Nonblank locators | Route violations |
|---|---:|---:|---:|---:|---:|---:|---:|
| direct_r_table_retrieval_retest | S003 | 10 | 10 | 0 | 10 | 10 | 0 |
| true_beta_path_table_retrieval_retest | S009 | 9 | 3 | 5 | 4 | 4 | 0 |
| true_beta_path_table_retrieval_retest | S010 | 6 | 0 | 1 | 5 | 5 | 0 |

## Boundary

- Committed locked output suppresses source quotes; private source packets remain outside Git.
- Human reference values and human-adjudicated source locators were not inserted into prompts.
- The scoped retrieval-diagnostics remain limited to prompt/path behavior for these 25 rows.
- Do not treat these rows as full-corpus LLM performance or final substitution evidence.
