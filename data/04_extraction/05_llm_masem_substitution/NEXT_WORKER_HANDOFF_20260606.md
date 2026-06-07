# Next Worker Handoff: Paper2 LLM Locked Outputs

## Stop state

All model CLI processes were stopped. No active `codex exec`, `gemini --prompt`,
`claude -p`, or `run_model_locked_output_batch.py` process should be running.

Current clean manifest state:

- Locked model outputs in manifest: 109
- Scoring status: `scored_locked_outputs`
- Row-level output rows: 16047
- Scored rows: 5898
- Claude clean default-unspecified shards: `0000-3999`
- Claude clean Sonnet shards: `4000-7858`
- Codex clean default-unspecified shards: `0000-0249`
- Codex clean GPT-5.5 shards: `0000-7858`
- Gemini full run: not started; stratified diagnostic contained row-level
  `model_cli_error`, and a later direct 1-row diagnostic timed out after
  repeated `You have exhausted your capacity on this model.` retries.

Gemini stratified/retry/probe CSVs with row-level CLI errors are not in the
clean manifest because they are diagnostic artifacts, not clean locked model
outputs.

## Why the CLI work was slow

The current runner uses noninteractive CLI calls. Each chunk starts a new CLI
process and sends the prompt plus a task JSON payload. This is slow because each
process pays startup, model setup, prompt parsing, and JSON output overhead.

A persistent single-process CLI session would be faster in principle, but it is
not currently used because the scoring harness needs deterministic,
machine-readable, one-batch-in/one-CSV-out behavior. Interactive or resumed
sessions can drift, retain context, or mix outputs unless a separate protocol is
implemented and tested.

Safe rerun guidance:

- Claude Sonnet and Codex GPT-5.5 full model-explicit ranges are complete; use
  new CLI runs only for targeted reruns or audits.
- Keep Claude reruns at 250-row shards and 50-row chunks.
- Keep Codex reruns at 100-row shards and 10-row chunks.
- Do not continue Gemini full runs until a 1-row probe has no
  `model_cli_error`.

## Next commands

Claude Sonnet full model-explicit coverage is complete. Use this command shape
only for targeted reruns:

```bash
python3 scripts/llm_scoring_20260606/run_model_locked_output_batch.py \
  --provider claude \
  --model-selector sonnet \
  --run-id paper2_claude_sonnet_full_allfamilies_6500_6749_rerun_YYYYMMDD \
  --offset 6500 \
  --limit 250 \
  --chunk-size 50 \
  --timeout 900 \
  --max-budget-usd 3.00 \
  --register
```

Codex GPT-5.5 full model-explicit coverage is complete. Use this shape only
for targeted reruns:

```bash
python3 scripts/llm_scoring_20260606/run_model_locked_output_batch.py \
  --provider codex \
  --model-selector gpt-5.5 \
  --run-id paper2_codex_gpt55_full_allfamilies_0000_0099_rerun_YYYYMMDD \
  --offset 0 \
  --limit 100 \
  --chunk-size 10 \
  --timeout 300 \
  --register
```

Gemini should only be probed, not full-run:

```bash
python3 scripts/llm_scoring_20260606/run_model_locked_output_batch.py \
  --provider gemini \
  --run-id paper2_gemini_probe1_retry_20260606 \
  --offset 0 \
  --limit 1 \
  --chunk-size 1 \
  --timeout 480
```

## Clean registration rule

Register and keep a model-run file only when:

- expected row count is present;
- `error_code` has no `model_cli_error`;
- the manifest has `locked_status=locked_model_output`;
- `score_locked_outputs.py` completes afterward.

If a file has `model_cli_error`, remove it from the manifest before reporting
the clean state. The failed CSV may remain on disk as local diagnostic evidence,
but it is not clean evidence.

## Git deployment scope

Commit only share-safe scaffold, locked outputs, scoring outputs, and scripts.
Do not include raw private PDFs, API keys, temporary process logs, or
unmanifested failed model-run probes unless the team explicitly wants local
diagnostic artifacts in Git.

Recommended include list:

```text
scripts/llm_scoring_20260606/
data/04_extraction/05_llm_masem_substitution/README.md
data/04_extraction/05_llm_masem_substitution/RUNBOOK_20260606.md
data/04_extraction/05_llm_masem_substitution/NEXT_WORKER_HANDOFF_20260606.md
data/04_extraction/05_llm_masem_substitution/schemas/
data/04_extraction/05_llm_masem_substitution/scoring_rules/
data/04_extraction/05_llm_masem_substitution/locked_outputs/LOCKED_OUTPUT_MANIFEST_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/MODEL_RUN_MATRIX_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/paper2_locked_output_template_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_smoke_direct_r_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_gemini_smoke_direct_r_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_stratified10_allfamilies_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_gemini_stratified10_allfamilies_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_full_allfamilies_0000_0499_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_full_allfamilies_0500_0999_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_full_allfamilies_1000_1499_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_full_allfamilies_1500_1999_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_full_allfamilies_2000_2499_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_full_allfamilies_2500_2999_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_full_allfamilies_3000_3499_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_full_allfamilies_3500_3749_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_codex_full_allfamilies_0000_0049_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_codex_full_allfamilies_0050_0099_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_codex_full_allfamilies_0100_0149_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_full_allfamilies_3750_3999_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_codex_full_allfamilies_0150_0249_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_sonnet_full_allfamilies_4000_4499_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_codex_gpt55_full_allfamilies_0250_0349_20260606.csv
data/04_extraction/05_llm_masem_substitution/results/
data/04_extraction/WORKFLOW_STATUS_LOG.md
```

Recommended exclude list:

```text
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/*probe*.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/*dryrun*.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/*retry_probe*.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_full_allfamilies_3500_3999_20260606.csv
data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper2_codex_smoke_direct_r_20260606.csv
```

## Validation

Run this before handoff or commit:

```bash
python3 scripts/llm_scoring_20260606/score_locked_outputs.py && \
git diff --check && \
python3 -m py_compile scripts/llm_scoring_20260606/*.py && \
python3 -m json.tool \
  data/04_extraction/05_llm_masem_substitution/schemas/MODEL_ANSWER_SCHEMA_20260606.json >/dev/null
```

Expected current result:

```text
status=scored_locked_outputs
locked_output_files=109
scored_rows=5898
```

## Commit message template

Use the repository Lore protocol:

```text
Lock staged Paper2 LLM scoring outputs for reproducible continuation

Constraint: Final LLM accuracy and MASEM substitution claims remain blocked until full locked outputs are complete by denominator family.
Rejected: Commit failed probe outputs as clean evidence | they include model_cli_error or hook-interrupted paths.
Confidence: medium
Scope-risk: moderate
Directive: Continue provider runs only through clean shard registration and remove any session-limit shard from the manifest before reporting.
Tested: score_locked_outputs.py; git diff --check; py_compile scripts/llm_scoring_20260606/*.py; MODEL_ANSWER_SCHEMA_20260606.json parsed with json.tool
Not-tested: Full Claude/Codex/Gemini completion; Gemini clean full-run path
```
