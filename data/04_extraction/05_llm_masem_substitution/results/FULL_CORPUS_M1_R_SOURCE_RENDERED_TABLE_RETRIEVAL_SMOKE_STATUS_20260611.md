# Full-Corpus M1-R Source-Rendered Table-Retrieval Smoke Status

Date: 2026-06-11

## Research Stage

- Step 4 source-anchored reference freeze remains complete.
- Step 5 source-materialization/readability gates are unblocked for the target studies.
- This smoke tests the retrieval-directed, source-rendered path for focused S003/S009/S010 categories; it is a diagnostic, not a full-corpus accuracy claim.

## Execution Evidence

- Run ID: `paper_b_full_corpus_m1_raw_source_rendered_table_retrieval_smoke_20260611`
- Locked output: `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_source_rendered_table_retrieval_smoke_20260611.csv`
- Provider/model surface: `openai`; `codex:gpt-5.5` via Codex CLI.
- Local CLI/version lock: `codex-cli 0.137.0`.
- Procedure ID: `raw_model_extraction_source_rendered_table_retrieval_smoke`
- Prompt version: `paper_b_step5_full_corpus_prompt_v4_20260611_table_retrieval_smoke`
- Task file: `data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/source_rendered_table_retrieval_smoke_task_ids_20260609.csv`
- Manifest row: `source_rendered_table_retrieval_smoke_locked_output`

## Smoke Results

- Rows: 25
- Correct rows under numeric tolerance: 3/25
- Abstentions / insufficient evidence rows: 20/25
- Nonblank model answers: 5/25
- Nonblank source locators: 5/25
- Route violations: 0/25
| Category | Study | Rows | Correct | Abstentions | Nonblank answers | Nonblank locators | Route violations |
|---|---:|---:|---:|---:|---:|---:|---:|
| direct_r_table_retrieval_retest | S003 | 10 | 0 | 10 | 0 | 0 | 0 |
| true_beta_path_table_retrieval_retest | S009 | 9 | 3 | 5 | 4 | 4 | 0 |
| true_beta_path_table_retrieval_retest | S010 | 6 | 0 | 5 | 1 | 1 | 0 |

## Boundary

- Committed locked output suppresses source quotes; private source packets remain outside Git.
- Human reference values and human-adjudicated source locators were not inserted into prompts.
- This diagnostic remains limited to prompt/path behavior for focused 25 retrieval rows.
- Do not treat these rows as full-corpus LLM performance or final substitution evidence.
