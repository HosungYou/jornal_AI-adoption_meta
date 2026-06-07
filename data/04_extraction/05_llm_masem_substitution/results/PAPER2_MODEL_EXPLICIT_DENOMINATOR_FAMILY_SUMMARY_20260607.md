# Paper2 Model-Explicit Denominator-Family Summary

Date: 2026-06-07

## Boundary

This is not an overall LLM accuracy table. Paper2 task units are split by
`denominator_family` and interpretation tier. Trace, blank/absence, and
source-type sensitivity rows should not be collapsed into a single
substitution-validity claim.

## Model Coverage

- `codex:gpt-5.5`: model-explicit full range `0000-7858`.
- `claude:sonnet`: model-explicit continuation range `4000-7858`.
- `gemini:gemini-3-flash-preview`: model-explicit partial clean range
  `0000-7249`; `7250-7858` remains blocked by Gemini CLI capacity
  exhaustion on `human_disagreement_trace` as of 2026-06-07.
- `overlap_codex_gpt55_claude_sonnet`: only task units present in both
  model-explicit outputs; use this for direct model comparison.

## Summary Table

| Scope | Model | Family | Tier | Rows | Scored | Correct | Abstain | Accuracy | Not scored |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| model_explicit_available_rows | claude:sonnet | absence_or_blank_consensus | triage_or_blank_behavior | 2714 | 416 | 0 | 0 | 0.000000 | 2298 |
| model_explicit_available_rows | claude:sonnet | converted_or_model_derived_effect_size | source_type_sensitivity | 53 | 53 | 0 | 53 | 0.000000 | 0 |
| model_explicit_available_rows | claude:sonnet | direct_r_effect_size_extraction | primary_numeric_evidence | 276 | 276 | 0 | 276 | 0.000000 | 0 |
| model_explicit_available_rows | claude:sonnet | human_disagreement_trace | trace_only_not_primary_accuracy | 467 | 467 | 0 | 108 | 0.000000 | 0 |
| model_explicit_available_rows | claude:sonnet | metadata_extraction | primary_metadata_evidence | 349 | 349 | 0 | 349 | 0.000000 | 0 |
| model_explicit_available_rows | codex:gpt-5.5 | absence_or_blank_consensus | triage_or_blank_behavior | 6412 | 2083 | 0 | 87 | 0.000000 | 4329 |
| model_explicit_available_rows | codex:gpt-5.5 | construct_or_sample_mapping_decision | review_decision | 2 | 2 | 0 | 2 | 0.000000 | 0 |
| model_explicit_available_rows | codex:gpt-5.5 | converted_or_model_derived_effect_size | source_type_sensitivity | 88 | 88 | 0 | 88 | 0.000000 | 0 |
| model_explicit_available_rows | codex:gpt-5.5 | direct_r_effect_size_extraction | primary_numeric_evidence | 366 | 366 | 3 | 363 | 0.008197 | 0 |
| model_explicit_available_rows | codex:gpt-5.5 | eligibility_or_exclusion_decision | review_decision | 5 | 5 | 0 | 0 | 0.000000 | 0 |
| model_explicit_available_rows | codex:gpt-5.5 | human_disagreement_trace | trace_only_not_primary_accuracy | 467 | 467 | 0 | 20 | 0.000000 | 0 |
| model_explicit_available_rows | codex:gpt-5.5 | metadata_extraction | primary_metadata_evidence | 468 | 462 | 47 | 381 | 0.101732 | 6 |
| model_explicit_available_rows | codex:gpt-5.5 | source_absence_decision | triage_or_blank_behavior | 3 | 3 | 0 | 0 | 0.000000 | 0 |
| model_explicit_available_rows | codex:gpt-5.5 | statistic_type_policy_decision | review_decision | 7 | 7 | 0 | 4 | 0.000000 | 0 |
| model_explicit_available_rows | codex:gpt-5.5 | structured_human_review_decision | review_decision | 41 | 41 | 0 | 34 | 0.000000 | 0 |
| model_explicit_available_rows | gemini:gemini-3-flash-preview | absence_or_blank_consensus | triage_or_blank_behavior | 6412 | 5931 | 0 | 5532 | 0.000000 | 481 |
| model_explicit_available_rows | gemini:gemini-3-flash-preview | construct_or_sample_mapping_decision | review_decision | 2 | 2 | 0 | 0 | 0.000000 | 0 |
| model_explicit_available_rows | gemini:gemini-3-flash-preview | converted_or_model_derived_effect_size | source_type_sensitivity | 89 | 89 | 0 | 89 | 0.000000 | 0 |
| model_explicit_available_rows | gemini:gemini-3-flash-preview | direct_r_effect_size_extraction | primary_numeric_evidence | 366 | 366 | 3 | 363 | 0.008197 | 0 |
| model_explicit_available_rows | gemini:gemini-3-flash-preview | eligibility_or_exclusion_decision | review_decision | 5 | 5 | 0 | 0 | 0.000000 | 0 |
| model_explicit_available_rows | gemini:gemini-3-flash-preview | metadata_extraction | primary_metadata_evidence | 326 | 325 | 44 | 244 | 0.135385 | 1 |
| model_explicit_available_rows | gemini:gemini-3-flash-preview | source_absence_decision | triage_or_blank_behavior | 3 | 3 | 0 | 0 | 0.000000 | 0 |
| model_explicit_available_rows | gemini:gemini-3-flash-preview | statistic_type_policy_decision | review_decision | 7 | 7 | 0 | 2 | 0.000000 | 0 |
| model_explicit_available_rows | gemini:gemini-3-flash-preview | structured_human_review_decision | review_decision | 41 | 41 | 0 | 13 | 0.000000 | 0 |
| overlap_codex_gpt55_claude_sonnet | claude:sonnet | absence_or_blank_consensus | triage_or_blank_behavior | 2714 | 416 | 0 | 0 | 0.000000 | 2298 |
| overlap_codex_gpt55_claude_sonnet | claude:sonnet | converted_or_model_derived_effect_size | source_type_sensitivity | 53 | 53 | 0 | 53 | 0.000000 | 0 |
| overlap_codex_gpt55_claude_sonnet | claude:sonnet | direct_r_effect_size_extraction | primary_numeric_evidence | 276 | 276 | 0 | 276 | 0.000000 | 0 |
| overlap_codex_gpt55_claude_sonnet | claude:sonnet | human_disagreement_trace | trace_only_not_primary_accuracy | 467 | 467 | 0 | 108 | 0.000000 | 0 |
| overlap_codex_gpt55_claude_sonnet | claude:sonnet | metadata_extraction | primary_metadata_evidence | 349 | 349 | 0 | 349 | 0.000000 | 0 |
| overlap_codex_gpt55_claude_sonnet | codex:gpt-5.5 | absence_or_blank_consensus | triage_or_blank_behavior | 2714 | 813 | 0 | 37 | 0.000000 | 1901 |
| overlap_codex_gpt55_claude_sonnet | codex:gpt-5.5 | converted_or_model_derived_effect_size | source_type_sensitivity | 53 | 53 | 0 | 53 | 0.000000 | 0 |
| overlap_codex_gpt55_claude_sonnet | codex:gpt-5.5 | direct_r_effect_size_extraction | primary_numeric_evidence | 276 | 276 | 0 | 276 | 0.000000 | 0 |
| overlap_codex_gpt55_claude_sonnet | codex:gpt-5.5 | human_disagreement_trace | trace_only_not_primary_accuracy | 467 | 467 | 0 | 20 | 0.000000 | 0 |
| overlap_codex_gpt55_claude_sonnet | codex:gpt-5.5 | metadata_extraction | primary_metadata_evidence | 349 | 349 | 0 | 348 | 0.000000 | 0 |
| overlap_codex_gpt55_claude_sonnet | gemini:gemini-3-flash-preview | absence_or_blank_consensus | triage_or_blank_behavior | 2714 | 2283 | 0 | 2002 | 0.000000 | 431 |
| overlap_codex_gpt55_claude_sonnet | gemini:gemini-3-flash-preview | converted_or_model_derived_effect_size | source_type_sensitivity | 53 | 53 | 0 | 53 | 0.000000 | 0 |
| overlap_codex_gpt55_claude_sonnet | gemini:gemini-3-flash-preview | direct_r_effect_size_extraction | primary_numeric_evidence | 276 | 276 | 0 | 276 | 0.000000 | 0 |
| overlap_codex_gpt55_claude_sonnet | gemini:gemini-3-flash-preview | metadata_extraction | primary_metadata_evidence | 207 | 207 | 0 | 207 | 0.000000 | 0 |

## Interpretation Notes

- Use `direct_r_effect_size_extraction` as the cleanest primary numeric
  evidence family.
- Use `metadata_extraction` as a primary metadata evidence family,
  but report it separately from direct-r because it uses normalized
  exact-match rather than numeric tolerance scoring.
- Treat `converted_or_model_derived_effect_size` as a source-type
  sensitivity family, not as direct-r equivalence.
- Treat `absence_or_blank_consensus`, `source_absence_decision`, and
  `human_disagreement_trace` as triage/trace behavior unless a later
  protocol defines a separate metric.
- Current zero-heavy accuracy patterns should be interpreted against the
  redacted evidence available to the model and the task-family scoring
  rule, not as a standalone model-quality verdict.
