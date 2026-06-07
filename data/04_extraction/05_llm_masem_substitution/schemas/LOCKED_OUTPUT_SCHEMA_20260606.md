# Locked Output Schema

Date: 2026-06-06

This schema is the only accepted input shape for Paper2 LLM scoring. A model
run is not scorable until its output file is frozen, listed in
`../locked_outputs/LOCKED_OUTPUT_MANIFEST_20260606.csv`, and marked
`locked_status=locked_model_output`.

## Required keys

- `run_id`: unique run identifier, stable across all rows from one model/procedure.
- `model_provider`: `openai`, `anthropic`, `google`, or another explicit provider.
- `model_id`: exact model family/name used for comparison.
- `model_version`: exact dated/versioned model where available.
- `procedure_id`: procedure condition, for example `raw_model_extraction` or
  `stateful_harness`.
- `prompt_version`: prompt/schema version used for the task.
- `run_timestamp_utc`: run timestamp.
- `temperature`: generation temperature.
- `seed`: seed if supported.
- `task_unit_id`: must match the frozen Paper2 reference task unit.
- `evaluation_unit_text`: frozen evaluation text from the reference packet. This
  may contain human consensus text and must not be used as the model prompt.
- `model_input_text`: redacted model-facing input. This excludes human
  consensus, `statistic_value`, and `decision_label`.
- `model_answer`: model answer as returned after parsing.
- `model_answer_normalized`: normalized answer used for scoring when available.
- `model_source_locator`: source table/page/row locator found by the model.
- `model_source_quote`: short source text if the run captures evidence text.
- `model_confidence`: model confidence or blank.
- `abstained`: `true`/`false` style value.
- `error_code`: extraction/runtime error if any.
- `raw_output_ref`: pointer to private raw transcript/output storage.
- `locked_answer_status`: must be `locked` for the row to be scored.
- `lock_timestamp_utc`: when the row was locked.
- `locked_by`: person/procedure that locked the run.
- `notes`: optional.

## Scoring boundary

Rows whose reference `scoring_eligibility` does not start with
`eligible_after_locked_llm_output` are not final accuracy denominator rows.
They remain trace/exclusion/sensitivity records.

The 8,783 task units must not be reported as one accuracy denominator. Report by
`denominator_family` and model/procedure condition.
