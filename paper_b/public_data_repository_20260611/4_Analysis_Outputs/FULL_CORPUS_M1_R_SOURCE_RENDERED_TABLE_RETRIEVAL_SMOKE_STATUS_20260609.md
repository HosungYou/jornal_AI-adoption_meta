# Full-Corpus M1-R Source-Rendered Table Retrieval Smoke Status

Date: 2026-06-09

## Scope

This is a focused Step 5 retrieval-gate smoke, not a full-corpus model run and not a final LLM accuracy or MASEM substitution result. It retests only S003 direct-r/FLC retrieval and S009/S010 true beta/path retrieval after the source-packet scoring revision.

## Locked Run

- Condition label: `M1-R-SOURCE-SMOKE-TABLE-RETRIEVAL`
- Run ID: `paper_b_full_corpus_m1_raw_source_rendered_table_retrieval_smoke_20260609`
- Model selector: `codex:gpt-5.5` via Codex CLI
- Rows: 25
- Source packet policy: private local packets; source quotes suppressed in committed output
- Locked output SHA-256: `b098f7d54072bcec3161a63e7363f09489bbd3fd946b0e5a6dc147aecc6250da`

## Diagnostic Results

- CLI errors: 0
- Source quote policy violations / committed source quotes: 0
- Nonblank model answers: 18/25
- Nonblank source locators: 23/25
- Abstentions: 7/25
- Route violations: 0/25
- Diagnostic correct rows under numeric tolerance: 17/25

## Category Summary

| Category | Study | Rows | Correct | Abstentions | Nonblank answers | Nonblank locators | Route violations |
|---|---:|---:|---:|---:|---:|---:|---:|
| `direct_r_table_retrieval_retest` | S003 | 10 | 10 | 0 | 10 | 10 | 0 |
| `true_beta_path_table_retrieval_retest` | S009 | 9 | 7 | 1 | 8 | 8 | 0 |
| `true_beta_path_table_retrieval_retest` | S010 | 6 | 0 | 6 | 0 | 5 | 0 |

## Interpretation

- S003 direct-r/FLC retrieval is unblocked in this targeted smoke: all 10 S003 rows returned nonblank page-21 locators and scored correct.
- S009/S010 beta/path retrieval remains partial: the packet revision improved table visibility but still leaves 7 abstentions across true beta/path rows. This remains a retrieval/prompt disambiguation gate before any full-corpus `M1-R` authorization.
- No human reference values or human-adjudicated source locators were inserted into model prompts. Expected values appear only in this post-run diagnostic scoring artifact.

## Next Gate

Do not authorize full-corpus `M1-R`, `M1-P`, `M2-R`, or `M3-R` yet. Review the remaining S009/S010 abstentions, add directed-path alias/context handling if defensible, then rerun a narrower beta/path retrieval smoke or approve an explicit staged shard only after the retrieval caveat is bounded.

## Evidence Files

- `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_rendering_table_retrieval_targets_manifest_20260609.csv`
- `data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/source_rendered_table_retrieval_smoke_task_ids_20260609.csv`
- `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_source_rendered_table_retrieval_smoke_20260609.csv`
- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_source_rendered_table_retrieval_smoke_scored_20260609.csv`
- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_source_rendered_table_retrieval_smoke_status_20260609.csv`
