# Step 5: LLM Comparison and MASEM Substitution

Step 4 has a 2026-06-05 source-anchored tiered reference freeze layer. This
folder now contains the locked-output shell and scoring harness for Step 5.

Do not report current LLM accuracy results or MASEM substitution outputs until a
model/run output file is frozen, listed in the locked-output manifest, and scored
by denominator family.

## Active files

- `schemas/LOCKED_OUTPUT_SCHEMA_20260606.md`: required locked-output fields.
- `scoring_rules/TASK_FAMILY_SCORING_RULES_20260606.md`: denominator and
  scoring policy.
- `locked_outputs/paper2_locked_output_template_20260606.csv`: 8,783-row shell
  keyed to the frozen Paper2 task units.
- `locked_outputs/MODEL_RUN_MATRIX_20260606.csv`: Codex/GPT candidate plus
  Claude and Gemini smoke/stratified/full-shard rows.
- `locked_outputs/LOCKED_OUTPUT_MANIFEST_20260606.csv`: manifest for reference,
  template, and future locked model outputs.
- `RUNBOOK_20260606.md`: low-noise shard resume protocol and validation
  checklist.
- `NEXT_WORKER_HANDOFF_20260606.md`: stop state, next commands, Git deployment
  scope, and commit message template.
- `results/SCORING_STATUS_20260606.md`: current scoring status.
- `results/paper2_locked_output_scored_20260606.csv`: row-level scoring output
  when locked model rows exist.
- `results/paper2_locked_output_score_summary_20260606.csv`: model/family
  summary output when locked model rows exist.
- `results/PAPER2_MODEL_EXPLICIT_DENOMINATOR_FAMILY_SUMMARY_20260607.md`:
  model-explicit denominator-family interpretation table for Codex GPT-5.5 and
  Claude Sonnet, including their overlap subset.
- `MODEL_FAMILY_EXTENSION_PLAN_20260607.md`: Claude Sonnet backfill gate,
  installed CLI model-family inventory, and full-run gate for any added model.

## Current status

The shell is prepared. One-row direct-r smoke outputs are locked for Claude and
Gemini. Claude's 77-row stratified output is also locked. The earlier Gemini
77-row stratified output remains on disk as a diagnostic artifact, but it was
removed from the clean manifest because it contains row-level `model_cli_error`
rows.

Claude full-run execution has clean locked/scored default-CLI shards through
3999 (`0000-0499`, `0500-0999`, `1000-1499`, `1500-1999`, `2000-2499`,
`2500-2999`, `3000-3499`, `3500-3749`, and `3750-3999`). Those earlier rows
did not explicitly record Sonnet/Opus and must be treated as
`claude_code`/default-unspecified unless rerun.

Starting at `4000-4499`, Claude is explicitly fixed to `claude:sonnet`.
Clean Sonnet shards are locked and scored through the full `4000-7858`
model-explicit continuation. Earlier failed `6500-6999` session-limit CSVs
remain diagnostic artifacts and are not in the clean manifest.

These smoke rows are pipeline checks, not final Paper2 accuracy evidence. They
cover one shared task unit (`P2-TASK-00142`) and both models abstained because
the redacted model input did not include the numeric source value.

Codex CLI is present. The original repo-local noninteractive smoke path was not
stable enough to score because repository hooks intervened in the export path.
A hook-free Codex path using `--ignore-user-config`, `--skip-git-repo-check`,
and a temporary working directory has produced clean model-explicit
`codex:gpt-5.5` locked outputs for the full `0000-7858` run.

Gemini 3 Flash is complete for the full `0000-7858` model-explicit range.
Shards `0000-7249` used the Gemini CLI. The `human_disagreement_trace` tail hit
Gemini CLI capacity exhaustion, so `7250-7399`, `7400`, and `7401-7858` were
completed through the Google AI Studio Gemini API with the same
`gemini-3-flash-preview` model selector. CLI/API surface provenance is preserved
in locked-output metadata.

Current clean model-explicit state: `codex:gpt-5.5` is complete for
`0000-7858`; `claude:sonnet` is complete for `4000-7858`;
`gemini:gemini-3-flash-preview` is complete for `0000-7858`.

The 8,783 task units must not be treated as one accuracy denominator. Use
`denominator_family` and `scoring_eligibility`. Current interpretation should
start from
`results/PAPER2_MODEL_EXPLICIT_DENOMINATOR_FAMILY_SUMMARY_20260607.md`, which
separates available model-explicit rows from the Codex/Claude/Gemini 3 Flash
overlap subset.
Treat `direct_r_effect_size_extraction` and `metadata_extraction` as separate
primary evidence families.
