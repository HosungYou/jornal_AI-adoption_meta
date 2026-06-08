# Full-Corpus M1-R Smoke Status

Date: 2026-06-09

Status: `M1-R-SMOKE` was researcher-authorized and executed as a
post-freeze Step 5 schema/export/locking preflight. This is not a full-corpus
model run and does not authorize any LLM accuracy, model-comparison,
procedure-comparison, or MASEM substitution claim.

## Authorization Locked

- Condition: `M1-R-SMOKE` only.
- Provider/model surface: `openai`; `codex:gpt-5.5`.
- Local CLI/version lock: `codex-cli 0.137.0; model_selector=gpt-5.5`.
- Scope: 30 rows, stratified 10/10/10 across denominator families.
- Prompt leakage boundary: no human reference values and no human-adjudicated
  source locators in prompts.
- Raw-output policy: raw transcripts are not committed; locked structured CSV
  is share-safe and registered.
- Repeatability subset: `paper_c_repeatability_subset_v1_20260609` remains
  frozen for later repeated-run checks.

## Execution Evidence

- Locked output:
  `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_smoke_20260609.csv`
- SHA-256:
  `8a84601dec4f603e52300efbad41fa5fdecd6223131914e0cc555a2cb26dae7f`
- Run timestamp: `2026-06-08T23:21:11Z`
- Rows: 30
- Denominator-family balance:
  - `primary_direct_r_or_source_reported_correlation`: 10
  - `primary_latent_or_construct_correlation_with_source_type_flag`: 10
  - `secondary_beta_or_path_converted_effect_size`: 10
- `model_cli_error` rows: 0
- `locked_answer_status=locked` rows: 30
- Manifest registration: true

## Interpretation

All 30 rows abstained with `error_code=insufficient_evidence`. This is expected
for this smoke scope because the current post-freeze task stubs intentionally
exclude the human reference value and do not yet include locked source-document
chunks. The smoke therefore proves that the post-freeze template, runner,
provenance fields, structured output path, and manifest registration work; it
does not test extraction accuracy.

## Next Gate

Before any full-corpus `M1-R` run, finalize and lock the source rendering and
chunking bundle that can be provided to the model without exposing human
reference values or human-adjudicated source locators. A second source-rendered
smoke is recommended before running all 2,043 target rows.
