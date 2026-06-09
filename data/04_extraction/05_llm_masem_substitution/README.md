# Step 5: LLM Comparison and MASEM Substitution

Step 4 has a full-corpus source-anchored adjudicated human reference freeze
authorized on 2026-06-09. This folder contains the locked-output shell, scoring
harness, legacy pre-full-corpus model-explicit artifacts, and the post-freeze
gate artifacts for Step 5.

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
- `POST_FREEZE_STEP5_GATE_20260609.md`: post-freeze gate after the full-corpus
  reference freeze.
- `FULL_CORPUS_POST_FREEZE_INPUT_MANIFEST_20260609.csv`: input/reference
  manifest for post-freeze Step 5.
- `full_corpus_step5_task_unit_shell_20260609.csv`: 2,043 target-row task shell
  generated from the frozen full-corpus reference.
- `full_corpus_step5_status_only_shell_20260609.csv`: 19 status-only corpus
  accounting records that do not generate target task rows.
- `locked_outputs/full_corpus_locked_output_template_20260609.csv`: 2,043-row
  post-freeze locked-output template with blank model answer fields.
- `locked_outputs/FULL_CORPUS_MODEL_PROCEDURE_RUN_MATRIX_20260609.csv`:
  Paper B/C model/procedure conditions; `M1-R-SMOKE` has been authorized and
  registered, while full-corpus conditions remain pending researcher approval.
- `locked_outputs/FULL_CORPUS_PRE_RUN_AUTHORIZATION_PACKET_20260609.md`:
  approval record and smoke execution evidence for the first post-freeze
  executable condition.
- `schemas/FULL_CORPUS_LOCKED_OUTPUT_SCHEMA_20260609.md`: post-freeze schema,
  denominator-family, and leakage-boundary rule.
- `results/FULL_CORPUS_M1_R_SMOKE_STATUS_20260609.md`: post-freeze
  `M1-R-SMOKE` status; this is a schema/export/locking preflight, not an
  accuracy result.
- `results/FULL_CORPUS_M1_R_SOURCE_RENDERED_SMOKE_STATUS_20260609.md`:
  source-packet prompt/export preflight on the current PDF-available subset;
  this is not an accuracy result.

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

Current clean model-explicit legacy state: `codex:gpt-5.5` is complete for
`0000-7858`; `claude:sonnet` is complete for `4000-7858`;
`gemini:gemini-3-flash-preview` is complete for `0000-7858`.

These model-explicit artifacts were built before the 2026-06-09 full-corpus
reference freeze. They must not be reported as final full-corpus accuracy unless
they are explicitly re-keyed and revalidated against
`../04_reference_standard_freeze/full_corpus_reference_standard_frozen_20260609.csv`.

Post-freeze task shell state: `full_corpus_step5_task_unit_shell_20260609.csv`
contains 2,043 target-row task units. The post-freeze locked-output template and
model/procedure run matrix are prepared. `M1-R-SMOKE` was authorized and
executed on 30 stratified rows using `codex:gpt-5.5` through
`codex-cli 0.137.0`; the locked output is registered in
`locked_outputs/FULL_CORPUS_LOCKED_OUTPUT_MANIFEST_20260609.csv`.

The `M1-R-SMOKE` rows all abstained with `insufficient_evidence`, as expected
for the current source-rendering placeholder/task-stub setup. This proves the
post-freeze runner/export/manifest path only. It is not a scoring rerun, LLM
accuracy result, model comparison, procedure comparison, or MASEM substitution
claim. No full-corpus model run is authorized yet.

A second source-rendered smoke has been run for the currently PDF-available
subset (`S021`, `S056`, `S092`): 6 rows, all in
`secondary_beta_or_path_converted_effect_size`, using private source packets
stored under the ignored Paper C private folder. The run produced nonblank model
answers and source locators without committing source quotes. This validates the
private source-packet prompt/export path only. Full-corpus `M1-R` remains
blocked until source rendering coverage exists for the intended target scope or
a smaller PDF-available subset is explicitly authorized.

A full target-shell source coverage audit has now been attempted against the
OneDrive archive. Study-ID PDF filename coverage exists for all 194 post-freeze
target studies, but local text rendering still succeeds for only 3 studies / 18
target rows. The remaining 191 studies / 2,025 target rows fail local PDF
read/materialization with `Operation timed out`. This blocks full-corpus `M1-R`
execution until the OneDrive PDFs are locally materialized or equivalent
share-safe source renderings are available.

A share-safe materialization action package has been prepared for those 191
blocked studies: 10 batches prioritized by target-row burden, a study-level gap
manifest, and a local checker that reports readability/materialization status
without committing PDF paths or source text. A 3-study checker smoke on the
first high-priority batch still returns `not_materialized_or_read_timeout`.
The full 191-study checker now also returns `not_materialized_or_read_timeout`
for all 191 studies after checking that the available CLI surface cannot execute
the OneDrive `MarkPinned` context action. The next gate is local
OneDrive/Finder materialization followed by checker and source-rendering reruns.
A follow-up Finder/OneDrive attempt partially materialized the main PDF archive:
16 studies / 376 target rows became `materialized_text_extractable`, while 175
studies / 1,649 target rows remain blocked. This does not authorize full-corpus
model execution or accuracy claims.

A later batch-focused follow-up found Batch 02 clean at 20/20 studies and
306/306 target rows, while Batch 01 improved to 16/20 studies and 401/492 target
rows. Batches 03-04 remain mostly blocked, so full-corpus model execution and
accuracy claims remain unauthorized.

Finder/OneDrive download requests were then submitted for the four remaining
Batch 01 blockers (`S157`, `S036`, `S088`, `S190`). `S157` and `S190`
subsequently became text-extractable, and after OneDrive was restarted again
`S036` and `S088` also became text-extractable. Batch 01 is now clean at 20/20
studies and 492/492 target rows. Batches 03-04 remain mostly blocked, so this
does not authorize model execution.

The 8,783 task units must not be treated as one accuracy denominator. Use
`denominator_family` and `scoring_eligibility`. Current interpretation should
start from
`results/PAPER2_MODEL_EXPLICIT_DENOMINATOR_FAMILY_SUMMARY_20260607.md`, which
separates available model-explicit rows from the Codex/Claude/Gemini 3 Flash
overlap subset.
Treat `direct_r_effect_size_extraction` and `metadata_extraction` as separate
primary evidence families.
