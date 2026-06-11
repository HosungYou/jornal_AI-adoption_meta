# Task Family Scoring Rules

Date: 2026-06-06

## Primary rule

Score locked model outputs only after a file is listed in
`locked_outputs/LOCKED_OUTPUT_MANIFEST_20260606.csv` with
`locked_status=locked_model_output`.

## Denominator families

- `direct_r_effect_size_extraction`: numeric effect-size rows. Score with
  absolute error <= 0.005 unless a later protocol sets a different tolerance.
  Rows labeled as `source_blank_r` remain in this primary direct-r extraction
  family when the human consensus supplies a direct-r value; report the
  evidence-quality flag separately.
- `converted_or_model_derived_effect_size`: converted beta/path/source-statistic
  numeric rows. Include these rows in the primary numeric extraction evaluation
  table as an explicit converted/source-type stratum, but do not pool them with
  source-reported direct-r rows or silently import them into the primary MASEM
  direct-r input.
- `metadata_extraction`: primary metadata evidence family. Score with
  both strict exact match and relaxed normalized match unless a field-specific
  parser is added. Report separately from direct-r numeric accuracy.
- `eligibility_or_exclusion_decision`: normalized exact match against the
  reference decision label/value.
- `construct_or_sample_mapping_decision`: normalized exact match.
- `statistic_type_policy_decision`: normalized exact match.
- `structured_human_review_decision`: normalized exact match.

## Not final accuracy denominators

- `source_pointer_only_not_evidence_scored`: source pointer exists but no
  evidence text is available. Exclude from final evidence-content accuracy.
- `not_derivable_trace`: trace-only. Exclude from final accuracy; optionally
  report abstention/triage behavior separately.
- `trace_influence_diagnostic`: trace-only. S072 ANX-EE r=1.0 stays excluded
  from primary scoring.
- `excluded_duplicate_source`: excluded duplicate/unusable source records.
- `human_disagreement_trace`, `absence_or_blank_consensus`, and
  `source_absence_decision`: report only if a later analysis defines a specific
  trace/triage metric.

## Abstention rule

On scorable rows, model abstentions, blank answers, or non-answers count as
incorrect. Report abstention behavior separately so that a model is not rewarded
for avoiding hard scorable rows.

`absence_or_blank_consensus` remains a triage/blank-behavior family rather than
an accuracy denominator.

## Model comparison

Multiple models can be compared by adding one locked output file per
`run_id`/`model_id`/`procedure_id`. The scorer groups results by
`run_id`, `model_provider`, `model_id`, and `denominator_family`.

## Current local execution boundary

As of 2026-06-06 local inspection:

- `codex` CLI is available; the repo-local path was unstable because hooks
  intervened, but a hook-free path produced clean staged full-run shards.
  Model-explicit Codex continuation uses `model_selector=gpt-5.5`; the clean
  manifest now contains `codex:gpt-5.5` for the full `0000-7858` range.
- `claude` CLI is available and produced one-row smoke, 77-row stratified, and
  default-unspecified full-shard locked outputs through 3999. Model-explicit
  Claude continuation uses `model_selector=sonnet`; clean Sonnet shards are
  locked through the full `4000-7858` model-explicit continuation. Earlier
  `6500-6999` session-limit 429 artifacts are diagnostic only and are not in
  the clean manifest.
- `gemini` CLI is available. Model-explicit `gemini-3-flash-preview` clean
  shards are locked through `0000-7249`; the remaining tail was completed with
  the Google AI Studio Gemini API after CLI capacity exhaustion.
- `openai` CLI command was not found.
- No API key values are stored in repository artifacts. Gemini API reruns must
  use `GEMINI_API_KEY` or `GOOGLE_API_KEY` from the local shell environment.

This means model-level comparison should use model-explicit rows, not only CLI
surface names. Existing Claude rows through 3999 and Codex rows through 0249
remain usable as CLI-default diagnostics, but they must not be relabeled as
Sonnet/Opus or GPT-5.5 after locking. Model-explicit continuation starts with
`claude:sonnet` at 4000-4499 and `codex:gpt-5.5` at 0000-0099 after the
backfill rerun. Gemini 3 Flash is now full model-explicit evidence for
`0000-7858`, with CLI/API surface provenance preserved in `model_version` and
`locked_by`.

For current model-explicit interpretation, use
`results/PAPER2_MODEL_EXPLICIT_DENOMINATOR_FAMILY_SUMMARY_20260607.md`.
This table separates Codex GPT-5.5, Claude Sonnet, and Gemini 3 Flash available
rows, plus the direct three-model overlap subset.
