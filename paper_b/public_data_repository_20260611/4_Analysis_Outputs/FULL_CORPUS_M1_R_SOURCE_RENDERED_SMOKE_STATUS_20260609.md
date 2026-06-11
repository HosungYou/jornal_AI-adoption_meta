# Full-Corpus M1-R Source-Rendered Smoke Status

Date: 2026-06-09

Status: source-rendered smoke completed for the currently available local PDF
subset. This validates the private source-packet prompt/export path only. It is
not a full-corpus model run, scoring rerun, LLM accuracy result, model
comparison, procedure comparison, or MASEM substitution claim.

## Source Rendering Coverage

- Private rendered source packets: 3 studies (`S021`, `S056`, `S092`).
- Covered post-freeze target rows: 18 rows.
- Source-rendered smoke rows selected: 6 rows, 2 per rendered study.
- Denominator family covered: `secondary_beta_or_path_converted_effect_size`
  only.
- Rendered source text storage: local/private ignored path only.
- Share-safe source manifest:
  `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_rendering_available_pdf_manifest_20260609.csv`
- Smoke task list:
  `data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/source_rendered_smoke_task_ids_20260609.csv`

## Execution Evidence

- Run ID: `paper_b_full_corpus_m1_raw_source_rendered_smoke_20260609`
- Locked output:
  `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_source_rendered_smoke_20260609.csv`
- SHA-256:
  `90c767335de11ab29679cab5505a532439d3ec5f2a72b6a4ee3861193b34c027`
- Run timestamp: `2026-06-08T23:43:33Z`
- Provider/model surface: `openai`; `codex:gpt-5.5`.
- Local CLI/version lock: `codex-cli 0.137.0; model_selector=gpt-5.5`.
- Prompt version:
  `paper_b_step5_full_corpus_prompt_v1_20260609_source_packet_smoke`
- Procedure ID: `raw_model_extraction_source_rendered_smoke`

## Smoke Results

- Rows: 6
- `model_cli_error` rows: 0
- `source_quote_policy_violation` rows: 0
- Nonblank model answers: 6
- Nonblank model source locators: 6
- Nonblank model source quotes: 0
- Manifest registration: true

## Interpretation

The previous stub-only smoke showed that the model properly abstains when no
source chunks are supplied. This source-rendered smoke shows that the same
locked-output path can carry private source packets, produce structured answers,
preserve page/chunk locator provenance, and keep `model_source_quote` blank so
committed locked output does not include source-document text.

This is still only a preflight. It covers three PDF-available studies and one
denominator family. Its original source-coverage blocker has since been
superseded by full source-rendering coverage clearance and the balanced 30-row
full-coverage source-rendered smoke. Full-corpus `M1-R`, `M1-P`, `M2-R`, and
optional `M3-R` now remain blocked by prompt/path review and explicit
run-condition authorization, not by source rendering coverage.

## Next Gate

Superseded by the full source-rendering coverage clearance and the balanced
30-row full-coverage source-rendered smoke:

- `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_rendering_full_coverage_manifest_20260609.csv`
- `data/04_extraction/05_llm_masem_substitution/results/FULL_CORPUS_M1_R_SOURCE_RENDERED_FULL_COVERAGE_SMOKE_STATUS_20260609.md`

Do not treat either smoke as a full-corpus accuracy or MASEM substitution claim.
