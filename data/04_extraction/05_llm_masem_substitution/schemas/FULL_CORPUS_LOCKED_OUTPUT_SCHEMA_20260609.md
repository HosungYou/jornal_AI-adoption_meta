# Full-Corpus Locked Output Schema

Date: 2026-06-09

This schema applies to the post-freeze full-corpus Step 5 locked-output
template generated from `full_corpus_step5_task_unit_shell_20260609.csv`.

The current template is:

- `../locked_outputs/full_corpus_locked_output_template_20260609.csv`

No model output is scorable until a completed run file is frozen, listed in
`../locked_outputs/FULL_CORPUS_LOCKED_OUTPUT_MANIFEST_20260609.csv`, and marked
as a locked model output in a future post-authorization manifest update.

## Required Columns

The post-freeze template preserves the 2026-06-06 locked-output scoring shape:

- `run_id`
- `model_provider`
- `model_id`
- `model_version`
- `procedure_id`
- `prompt_version`
- `run_timestamp_utc`
- `temperature`
- `seed`
- `task_unit_id`
- `study_id`
- `llm_task_family`
- `denominator_family`
- `scoring_eligibility`
- `expected_answer_type`
- `evaluation_unit_text`
- `model_input_text`
- `model_answer`
- `model_answer_normalized`
- `model_source_locator`
- `model_source_quote`
- `model_confidence`
- `abstained`
- `error_code`
- `raw_output_ref`
- `locked_answer_status`
- `lock_timestamp_utc`
- `locked_by`
- `notes`

## Leakage Boundary

`evaluation_unit_text` may contain the source-anchored adjudicated human
reference value and adjudication context. It is for scoring and audit only.

`model_input_text` is a redacted task stub. It must not include
`reference_r_value`, the human reference answer, adjudication rationale, or
human consensus labels. Actual model prompts must be generated from the approved
source-rendering/chunking manifest, not from `evaluation_unit_text`.

## Denominator Families

The 2,043 task rows must not be reported as one overall accuracy denominator.
Report separately by:

- `primary_direct_r_or_source_reported_correlation`
- `primary_latent_or_construct_correlation_with_source_type_flag`
- `secondary_beta_or_path_converted_effect_size`

Status-only studies remain corpus accounting records and are not target task
rows.

## Authorization Boundary

This schema and template do not authorize model execution. Execution requires a
researcher-approved run matrix, model selector verification, budget cap, source
rendering/chunking policy, and private-output storage plan.
