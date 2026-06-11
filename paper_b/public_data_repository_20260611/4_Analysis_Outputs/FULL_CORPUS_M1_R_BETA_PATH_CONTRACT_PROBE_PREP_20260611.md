# Full-Corpus M1-R Beta/Path Contract Probe Preparation

Date: 2026-06-11

## Scope

This preparation step creates the leakage-safe `M1-R-BETA-PATH-CONTRACT-PROBE`
gate for the S009/S010 beta/path rows identified in the 2026-06-11 contract
review. It does not execute a model run, authorize full-corpus `M1-R`, or
support accuracy, model-comparison, or MASEM substitution claims.

## Prepared Artifacts

- Probe overlay:
  `data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/source_rendered_beta_path_contract_probe_task_ids_20260611.csv`
- Runner patch:
  `scripts/llm_scoring_20260606/run_model_locked_output_batch.py`
- Diagnostic scorer:
  `scripts/llm_scoring_20260606/score_beta_path_contract_probe.py`
- Gate review input:
  `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_beta_path_contract_review_20260611.csv`

## Contract Decisions

The probe overlay contains 15 S009/S010 task rows. It preserves leakage
boundaries by setting `human_reference_value_in_prompt=false` and by excluding
human reference values and human-adjudicated source locators from prompt text.

For these rows, the active path metadata is source-directed rather than inferred
from construct-pair order. The overlay also adds
`beta_output_policy=raw_beta_in_model_answer_converted_effect_in_model_answer_normalized`.

When this policy is present, the runner asks the model to:

- recover the raw source standardized beta/path coefficient;
- put the raw beta/path coefficient in `raw_beta_value` and `model_answer`;
- compute the Peterson-Brown converted effect and put it in
  `converted_effect_value` and `model_answer_normalized`;
- set `conversion_method=peterson_brown_2005_beta_plus_0.05_sign_lambda`;
- abstain if no explicit source-directed path coefficient exists for the
  requested path and sample context;
- reject IPMA, importance, total-effect, indirect-effect, HTMT, and
  discriminant-validity tables as path-coefficient evidence.

## Diagnostic Scoring Boundary

`score_beta_path_contract_probe.py` is a contract diagnostic scorer, not a final
accuracy scorer. It separates:

- S010-style rows where raw beta recovery should be scored against the
  Peterson-Brown implied raw beta and the converted effect should be scored
  against the frozen reference value;
- S009 rows where the frozen `beta_converted_peterson_brown` label behaves like
  raw beta and must remain a reference-contract caveat;
- S009 `FC-UB` and S010 `FC-UB` rows that require source/reference QA before
  use as any full accuracy gate.

## Gate Status

Full-corpus `M1-R` remains blocked. The next defensible action is to authorize
and run only this 15-row beta/path contract probe with a specific model selector,
budget, private source-packet directory, and no committed raw source quotes. The
result should then be scored with the contract-aware diagnostic scorer before
any larger staged shard or full-corpus run is considered.
