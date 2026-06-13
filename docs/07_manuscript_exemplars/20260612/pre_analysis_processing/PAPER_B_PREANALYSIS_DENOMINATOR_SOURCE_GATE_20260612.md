# Paper B Pre-Analysis Denominator/Source-Packet Gate

Date: 2026-06-12

## Locked Recommendations

- Use the post-freeze 213-study full-corpus Step 5 universe.
- Keep denominator families separate; do not report one pooled accuracy denominator.
- Prioritize restoring/regenerating full-corpus private source packets before submission-grade full-corpus M1-R claims.
- Keep Codex M1-R as the primary workflow condition.
- Retain Claude Sonnet and Gemini as supplementary triage/cross-model disagreement evidence, not as vendor ranking.
- Apply the S009/S010 exception layer in the same scoring pass that scores larger M1-R runs.
- Count abstention on scorable rows as incorrect while reporting abstention as workflow behavior.
- Split pointer-only, source-absence, not-derivable, duplicate-source, and status-only records out of generic numeric accuracy claims.

## Inputs

- `data/04_extraction/05_llm_masem_substitution/full_corpus_step5_task_unit_shell_20260609.csv`
- `data/04_extraction/05_llm_masem_substitution/locked_outputs/full_corpus_locked_output_template_20260609.csv`
- `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_rendering_full_coverage_manifest_20260609.csv`
- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_beta_path_exception_correction_layer_20260611.csv`

## Current Gate Metrics

| metric | value |
| --- | --- |
| Full-corpus task shell rows | 2043 |
| Locked-output template rows | 2043 |
| Manifest study packets expected | 194 |
| Private packets present in workspace | 194 |
| Private packets missing in workspace | 0 |
| Exception-layer rows | 15 |

## Denominator Families

| denominator_family | rows | studies | scoring_eligibility | preanalysis_action |
| --- | --- | --- | --- | --- |
| primary_direct_r_or_source_reported_correlation | 697 | 56 | eligible_after_locked_llm_output:697 | keep_separate_denominator_never_pool |
| primary_latent_or_construct_correlation_with_source_type_flag | 931 | 78 | eligible_after_locked_llm_output_with_source_type_denominator:931 | keep_separate_denominator_never_pool |
| secondary_beta_or_path_converted_effect_size | 415 | 60 | eligible_after_locked_llm_output_with_source_type_denominator:415 | keep_separate_denominator_never_pool |

## Exception-Layer Policy Counts

| policy | rows |
| --- | --- |
| contract_aware_converted_effect_scoring_allowed_after_layer_consumed | 2 |
| exclude_until_explicit_structural_path_evidence_or_reference_correction | 4 |
| manual_source_reference_adjudication_required_no_in_place_freeze_change | 1 |
| reference_contract_caveat_no_in_place_freeze_change | 8 |

## Generic Full-Accuracy Gate Counts

| status | rows |
| --- | --- |
| exclude_from_generic_full_accuracy_denominator | 13 |
| exclude_from_raw_model_answer_generic_scorer | 2 |

## Contract-Aware Gate Counts

| status | rows |
| --- | --- |
| exclude_from_contract_aware_beta_path_gate | 5 |
| hold_raw_beta_diagnostic_only_until_reference_contract_authorized | 8 |
| include_after_exception_layer_consumed | 2 |

## Stop Condition

Full-corpus M1-R source packet availability gate is closed: all manifest studies have private rendered source packets in the workspace. Full-corpus M1-R accuracy and all-row substitution claims remain blocked until the larger M1-R run is scored with the exception-aware wrapper.

## Outputs

- `paper_b_denominator_summary_20260612.csv`
- `paper_b_source_packet_audit_20260612.csv`
- `paper_b_missing_source_packet_queue_20260612.csv`
