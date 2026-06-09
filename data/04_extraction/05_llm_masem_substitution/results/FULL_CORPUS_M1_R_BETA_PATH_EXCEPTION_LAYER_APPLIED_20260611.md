# Full-Corpus M1-R Beta/Path Exception-Layer Applied

Date: 2026-06-11

## Scope

This artifact records the first Step 5 post-processing pass that consumes the
beta/path exception-correction layer for the 15-row S009/S010 contract probe.
It applies **no new model runs** and performs no human-reference edits.

Inputs:

- `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_source_rendered_beta_path_contract_probe_20260611.csv`
- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_beta_path_exception_correction_layer_20260611.csv`

Outputs:

- `data/04_extraction/05_llm_masem_substitution/results/paper_b_full_corpus_m1_raw_source_rendered_beta_path_contract_probe_20260611_exception_layer_applied_20260611.csv`
- `data/04_extraction/05_llm_masem_substitution/results/paper_b_full_corpus_m1_raw_source_rendered_beta_path_contract_probe_20260611_exception_layer_applied_summary_20260611.csv`

## Runtime Gate Behavior

For each of 15 probe rows:

- rows in `reference_contract_caveat_no_in_place_freeze_change` are excluded from
  generic full-accuracy scoring and labeled `not_scored_reference_contract_caveat`.
- `manual_source_reference_adjudication_required_no_in_place_freeze_change` is
  excluded with `not_scored_manual_source_reference_adjudication_required`.
- `exclude_until_explicit_structural_path_evidence_or_reference_correction` is
  excluded with `not_scored_no_explicit_structural_path_evidence`.
- `contract_aware_converted_effect_scoring_allowed_after_layer_consumed` is
  contract-aware scored against `converted_effect_value` and `frozen_value`.

## Result Summary

- Input rows: `15`
- Contract-bridge rows included in generic denominator: `0`
- Contract-aware included rows: `2`
- Contract-aware scored rows: `2`
- Contract-aware correct rows: `2`
- `not_scored_reference_contract_caveat`: `8`
- `not_scored_manual_source_reference_adjudication_required`: `1`
- `not_scored_no_explicit_structural_path_evidence`: `4`
- `scored_contract_aware_converted_effect`: `2`

No rows were missing from the exception layer in this 15-row probe.

## Status

This execution does not authorize a larger full-corpus M1-R run by itself.
It is a consumed-gate artifact: full-corpus accuracy claims remain blocked until
any larger M1-R shard explicitly applies this gate logic and records it in the
scoring workflow/runbook.
