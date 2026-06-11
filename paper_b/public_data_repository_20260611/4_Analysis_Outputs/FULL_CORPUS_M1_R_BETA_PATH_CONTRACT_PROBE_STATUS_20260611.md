# Full-Corpus M1-R Beta/Path Contract Probe Status

Date: 2026-06-11

## Scope

This status report records the 15-row `M1-R-BETA-PATH-CONTRACT-PROBE` run for
S009/S010 beta/path rows. It is a diagnostic gate for source-directed path
metadata and raw-beta versus Peterson-Brown converted-effect output handling.
It is not a full-corpus `M1-R` run and does not support final accuracy,
model-comparison, or MASEM substitution claims.

## Run Condition

- Model condition: `codex:gpt-5.5`
- CLI surface: `codex-cli 0.137.0; model_selector=gpt-5.5`
- Procedure: `raw_model_extraction_source_rendered_beta_path_contract_probe`
- Prompt version:
  `full_corpus_task_route_overlay_v5_beta_path_contract_probe_20260611`
- Task overlay:
  `data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/source_rendered_beta_path_contract_probe_task_ids_20260611.csv`
- Private source packets:
  `data/04_extraction/07_paper_c_harness_benchmark/private/source_renderings_20260609_table_retrieval/source_packets/`
- Locked output:
  `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_source_rendered_beta_path_contract_probe_20260611.csv`

The run used source quotes suppression. No source-document text is committed in
the locked-output source quote field.

## Execution Summary

| Metric | Count |
|---|---:|
| Probe rows | 15 |
| Model CLI errors | 0 |
| Source quote policy violations | 0 |
| Nonblank raw beta fields | 11 |
| Nonblank converted effect fields | 11 |
| Abstentions | 4 |

## Contract Diagnostic Summary

Diagnostic scorer:
`scripts/llm_scoring_20260606/score_beta_path_contract_probe.py`

Scored artifacts:

- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_beta_path_contract_probe_scored_20260611.csv`
- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_beta_path_contract_probe_summary_20260611.csv`

| Contract probe status | Rows |
|---|---:|
| `source_directed_raw_recovered_reference_contract_caveat` | 5 |
| `raw_recovered_reference_contract_caveat` | 3 |
| `contract_pass_raw_and_converted` | 2 |
| `scored_abstention` | 4 |
| `source_value_reference_qa_unresolved` | 1 |

## Interpretation

The probe confirms that source-directed path metadata fixes the S009 direction
failure mode: eight S009 rows recover raw source beta values that match the
frozen numeric value within tolerance. This does not clear S009 for final
accuracy scoring, because those rows still expose a reference-contract caveat:
the frozen `beta_converted_peterson_brown` label behaves like a raw beta label.

S009 `FC-UB` remains unresolved. The model recovered a source-directed raw beta
that does not match either the frozen value or the Peterson-Brown implied raw
beta. This row still requires source/reference QA before use as an accuracy gate.

For S010, two rows pass the intended contract: raw beta matches the
Peterson-Brown implied raw beta and the converted effect matches the frozen
reference value. Four S010 rows abstained rather than using IPMA/importance
values, which is the safer behavior under this probe contract. Those abstentions
leave S010 source coverage/source-value completeness unresolved for the affected
paths.

## Gate Decision

Full-corpus `M1-R` remains blocked. The next defensible step is a bounded
source/reference QA pass for the beta/path contract, focused on:

- S009 reference-contract classification for rows labeled
  `beta_converted_peterson_brown` but behaving like raw beta;
- S009 `FC-UB` directed-value mismatch;
- S010 source-packet/table completeness for the abstained Nordic path rows;
- preserving the rule that IPMA, importance, total-effect, indirect-effect,
  HTMT, and discriminant-validity tables are not path-coefficient evidence.

No larger staged shard should be run until these contract issues are resolved or
explicitly bounded as caveats for a reduced-scope run.
