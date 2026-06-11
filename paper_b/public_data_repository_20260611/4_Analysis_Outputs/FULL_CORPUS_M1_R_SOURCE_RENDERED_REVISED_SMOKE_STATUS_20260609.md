# Full-Corpus M1-R Source-Rendered Revised Smoke Status

Date: 2026-06-09

Status: 40-row revised source-rendered smoke completed and locked. This is a prompt/path/routing diagnostic only; it is not a full-corpus model run, LLM accuracy result, model comparison, procedure comparison, or MASEM substitution claim.

## Execution Evidence

- Run ID: `paper_b_full_corpus_m1_raw_source_rendered_revised_smoke_20260609`
- Locked output: `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_source_rendered_revised_smoke_20260609.csv`
- Locked output SHA-256: `1f7955ff30cdc1627f11e25083da353365f28efb63f078e6155238cd355de5ce`
- Provider/model surface: `openai`; `codex:gpt-5.5`.
- Local CLI/version lock: `codex-cli 0.137.0; model_selector=gpt-5.5`.
- Procedure ID: `raw_model_extraction_source_rendered_revised_smoke`
- Prompt version: `paper_b_step5_full_corpus_prompt_v2_20260609_source_packet_route_overlay_revised_smoke`
- Revised task bundle: `data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/source_rendered_revised_smoke_task_ids_20260609.csv`
- Revised private source packet manifest: `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_rendered_revised_smoke_packet_manifest_20260609.csv`

## Smoke Results

- Rows: 40
- Revised category balance: `direct_r_packet_retrieval_challenge`=10; `latent_positive_control`=10; `non_path_secondary_route_review`=10; `true_beta_path_control`=10
- `model_cli_error` rows: 0
- `source_quote_policy_violation` rows: 0
- Nonblank model answers: 23
- Nonblank model source locators: 23
- Nonblank committed source quotes: 0
- Abstentions / insufficient-evidence rows: 17
- Smoke diagnostic correct rows under numeric tolerance: 21/40

## Category Diagnostics

| Revised smoke category | Rows | Scored | Correct | Abstentions | Nonblank answers | Nonblank locators | Nonblank quotes | Route violations | Smoke diagnostic accuracy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| direct_r_packet_retrieval_challenge | 10 | 10 | 0 | 10 | 0 | 0 | 0 | 0 | 0.000000 |
| latent_positive_control | 10 | 10 | 9 | 0 | 10 | 10 | 0 | 0 | 0.900000 |
| non_path_secondary_route_review | 10 | 10 | 6 | 4 | 6 | 6 | 0 | 0 | 0.600000 |
| true_beta_path_control | 10 | 10 | 6 | 3 | 7 | 7 | 0 | 0 | 0.600000 |

## Boundary

- The committed locked output suppresses source quotes; private revised source packets remain outside Git.
- The model prompt did not receive human reference values or human-adjudicated source locators.
- The revised route overlay changed downstream model instructions only; it did not change frozen human reference values.
- Do not generalize this 40-row smoke as Paper B/C full-corpus performance.

## Gate Interpretation

- The route overlay eliminated the prior S007 beta/path-route conflict for non-path secondary rows: route violations were 0 in the revised smoke.
- Direct-r S003 rows still abstained, indicating that packet/table coverage or source rendering for that specific direct-correlation matrix remains unresolved.
- True beta/path controls produced partial nonblank answers but still include abstentions; this requires source-packet/table coverage review before full-corpus execution.

## Next Gate

Do not authorize full-corpus `M1-R` yet. The next action is to revise packet/table retrieval for direct-r and true beta/path controls, then rerun a small revised smoke or a focused retrieval-only smoke before scaling.
