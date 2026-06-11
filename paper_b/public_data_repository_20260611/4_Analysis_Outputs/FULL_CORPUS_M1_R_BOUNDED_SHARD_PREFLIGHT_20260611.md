# Full-Corpus M1-R Bounded Shard Preflight

Date: 2026-06-11

## Scope

This artifact prepares a bounded post-freeze `M1-R` source-rendered
shard candidate after the beta/path exception-aware scorer was wired.
It does not execute a model and does not support an accuracy, model-
comparison, or MASEM substitution claim.

## Candidate Shard

- Task rows: `90`
- Unique studies: `10`
- Direct/source r rows: `30`
- Latent/construct correlation rows: `30`
- Beta/path converted-effect rows: `30`
- Selection mode: `reused_existing_task_id_bundle`
- Previous locked-output task IDs excluded: `141`
- Generic beta/path exception task IDs excluded: `15`

Candidate task bundle:

- `data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/source_rendered_bounded_m1r_shard_task_ids_20260611.csv`

## Source Packet Preflight

- Source packet directory checked: `data/04_extraction/07_paper_c_harness_benchmark/private/source_renderings_20260609_full_coverage/source_packets`
- Directory exists: `true`
- Studies with packet in this workspace: `10`
- Studies missing packet in this workspace: `0`
- Missing study preview: `none`

## Gate Decision

Status: `ready_for_authorized_model_run`.

The required private source packets are present in this workspace.
The bounded `M1-R` shard may be executed with `--require-source-packet`,
`--suppress-source-quotes`, and the exception-aware scorer. This remains
a staged shard gate, not full-corpus accuracy or substitution evidence.

## Recovery Command After Private Packets Are Restored

```sh
run_id=paper_b_full_corpus_m1_raw_bounded_shard_0090_20260611
python3 scripts/llm_scoring_20260606/run_model_locked_output_batch.py \
  --provider codex \
  --model-selector gpt-5.5 \
  --template data/04_extraction/05_llm_masem_substitution/locked_outputs/full_corpus_locked_output_template_20260609.csv \
  --manifest data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_LOCKED_OUTPUT_MANIFEST_20260609.csv \
  --task-ids-file data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/source_rendered_bounded_m1r_shard_task_ids_20260611.csv \
  --source-packet-dir data/04_extraction/07_paper_c_harness_benchmark/private/source_renderings_20260609_full_coverage/source_packets \
  --require-source-packet \
  --suppress-source-quotes \
  --prompt-version paper_b_step5_full_corpus_prompt_v1_20260609_source_packet_bounded_shard \
  --procedure-id raw_model_extraction_source_rendered_bounded_shard \
  --run-id "$run_id" \
  --chunk-size 10 \
  --timeout 900 \
  --register \
  --fail-on-model-cli-error

python3 scripts/llm_scoring_20260606/score_full_corpus_m1_r_with_exception_layer.py \
  --manifest data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_LOCKED_OUTPUT_MANIFEST_20260609.csv
```

The follow-up scoring command must remain exception-aware. Do not report
full-corpus accuracy or substitution stability from this bounded shard
alone; report it as a staged source-rendered run with denominator-family
and exception-layer boundaries.
