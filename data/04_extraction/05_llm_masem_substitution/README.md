# Step 5: LLM Comparison and MASEM Substitution

Step 4 has a full-corpus source-anchored adjudicated human reference freeze
authorized on 2026-06-09. This folder contains the locked-output shell, scoring
harness, legacy pre-full-corpus model-explicit artifacts, and the post-freeze
gate artifacts for Step 5.

Report only locked/scored results by task family and denominator family. A
bounded core-6 complete-case R/metaSEM TSSEM diagnostic has been run for the
Paper1 human-reference baseline versus the expert-reviewed LLM-assisted primary
input. It supports a narrow diagnostic stability claim for that subset only; do
not claim final all-construct/all-row SEM substitution stability. The approved
missing-N rule permits N-weighted SEM only on source-supported N-eligible rows;
all-row SEM wording requires source-supported numeric N for every SEM input row.

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
- `results/FULL_CORPUS_M1_R_BETA_PATH_EXCEPTION_LAYER_APPLIED_20260611.md`: first
  full-corpus exception-layer application record for the 15-row beta/path
  contract probe.
- `results/FULL_CORPUS_M1_R_BETA_PATH_EXCEPTION_CORRECTION_LAYER_20260611.md` and
  `results/FULL_CORPUS_M1_R_BETA_PATH_CONTRACT_REVIEW_20260611.md`: route/probe
  review artifacts for the post-freeze beta/path gating path.
- `results/full_corpus_m1_r_beta_path_exception_correction_layer_20260611.csv`:
  exception-correction task-family policy table consumed by the full-corpus
  scorer wrapper.
- `locked_outputs/model_runs/paper_b_full_corpus_m1_raw_source_rendered_full_coverage_smoke_20260609.csv`:
  30-row balanced full-coverage source-rendered smoke locked output.
- `results/FULL_CORPUS_M1_R_SOURCE_RENDERED_FULL_COVERAGE_SMOKE_STATUS_20260609.md`:
  balanced source-packet prompt/export/scoring diagnostic across all three
  denominator families; this is not a full-corpus accuracy result.
- `locked_outputs/model_runs/paper_b_full_corpus_m1_raw_bounded_shard_0090_20260611.csv`:
  90-row bounded post-freeze source-rendered `M1-R` locked output with
  `model_cli_error=0` and source quotes suppressed.
- `results/FULL_CORPUS_M1_R_BOUNDED_SHARD_STATUS_20260611.md`:
  staged bounded-shard execution and scoring status; this is not a full-corpus
  accuracy result or MASEM substitution-stability claim.
- `results/paper_b_full_corpus_m1_raw_scored_20260611.csv`,
  `results/paper_b_full_corpus_m1_raw_score_summary_20260611.csv`,
  `results/paper_b_full_corpus_m1_raw_exception_layer_scored_20260611.csv`, and
  `results/paper_b_full_corpus_m1_raw_exception_layer_scored_summary_20260611.csv`:
  outputs from the new full-corpus M1-R exception-aware scorer wrapper.
- `../../../docs/06_decisions/2026-06-11_Paper_B_Canonical_Reference_and_Model_Framing.md`:
  accepted canonical reference, scoring-boundary, and model-framing decisions
  for the legacy pre-full-corpus Step 5 evidence package.
- `results/PAPER2_RQ1_EXTRACTION_VALIDITY_20260611.md`: extraction-validity
  results by denominator family and source/conversion stratum for the legacy
  8,783-task-unit package.
- `results/paper2_rq1_extraction_validity_20260611.csv`: machine-readable RQ1
  table.
- `results/PAPER2_RQ2_ERROR_TAXONOMY_SOURCE_CONDITIONS_20260611.md`:
  error-taxonomy and source-condition summary.
- `results/paper2_rq2_error_taxonomy_source_conditions_20260611.csv`:
  machine-readable RQ2 table.
- `results/PAPER2_RQ3_TRIAGE_CROSS_MODEL_SENSITIVITY_20260611.md`:
  human-review triage and supplementary cross-model sensitivity summary.
- `results/paper2_rq3_triage_summary_20260611.csv`: machine-readable RQ3
  summary table.
- `results/paper2_rq3_triage_task_units_20260611.csv`: task-unit-level RQ3
  triage table.
- `results/PAPER2_MASEM_SUBSTITUTION_BRIDGE_20260611.md`: bridge from Paper 2
  locked-output results to downstream Paper 1 MASEM substitution readiness.
- `results/paper2_masem_substitution_bridge_20260611.csv`: machine-readable
  bridge table.
- `results/PAPER2_P0_P1_EXPERT_REVIEW_20260611.md`: expert-review layer for
  P0/P1 numeric and source-risk task units.
- `results/paper2_p0_p1_expert_review_20260611.csv`: machine-readable P0/P1
  expert-review layer.
- `results/PAPER2_MASEM_SUBSTITUTION_RERUN_20260611.md`: deterministic
  expert-reviewed substitution-input and pooled-correlation sensitivity rerun.
- `results/paper2_masem_substitution_rerun_input_20260611.csv`: model-ready
  expert-reviewed LLM-assisted primary input.
- `results/PAPER2_MASEM_SAMPLE_SIZE_RECONCILIATION_20260611.md`: deterministic
  sample-size reconciliation from the 2026-06-09 frozen full-corpus reference.
- `results/PAPER2_MISSING_N_AND_CLAIM_BOUNDARY_DECISION_20260611.md`: approved
  missing-N exclusion rule, sample-size hierarchy, and manuscript claim
  boundary.
- `results/paper2_masem_substitution_rerun_input_n_reconciled_20260611.csv`:
  derived MASEM rerun input with numeric N filled where source-supported.
- `results/paper2_masem_substitution_rerun_input_n_weighted_eligible_20260611.csv`:
  N-weighted eligible subset after excluding rows still missing numeric N.
- `results/paper2_masem_substitution_rerun_pair_impact_20260611.csv`:
  pair-level pooled-correlation impact table.
- `results/paper2_masem_substitution_rerun_summary_20260611.csv`: rerun summary
  table.
- `results/pdf_source_text_audit_20260611/PAPER2_POINTER_ONLY_PDF_SOURCE_TEXT_AUDIT_20260611.md`:
  PDF text audit for P0/P1 rows that previously had source pointers but no
  evidence text.
- `results/r_masem_readiness_20260611/PAPER2_R_MASEM_READINESS_20260611.md`:
  local R/OpenMx/metaSEM package and input-readiness check for the Paper2
  substitution input.
- `results/r_tssem_substitution_20260611/PAPER2_TSSEM_SUBSTITUTION_DIAGNOSTIC_20260611.md`:
  bounded core-6 complete-case TSSEM diagnostic comparing the Paper1
  human-reference baseline with the expert-reviewed LLM-assisted primary input.
- `../../../paper_b/manuscript/PAPER_B_METHODS_RESULTS_DRAFT_20260611.md`:
  methods/results draft for the task-contingent LLM augmentation manuscript.

## Current status

The shell is prepared. One-row direct-r smoke outputs are locked for Claude and
Gemini. Claude's 77-row stratified output is also locked. The earlier Gemini
77-row stratified output remains on disk as a diagnostic artifact, but it was
removed from the clean manifest because it contains row-level `model_cli_error`
rows.

Claude full-run execution originally had clean locked/scored default-CLI shards
through 3999. Those earlier rows did not explicitly record Sonnet/Opus and are
retained only as `claude_code`/default-unspecified audit provenance. On
2026-06-11, `0000-3999` was rerun as explicit `claude:sonnet` in 16 clean
backfill shards with no `model_cli_error` rows, and the one-row backfill probe
was marked as excluded from final scoring to avoid duplicate task-unit coverage.

Clean Sonnet shards are now locked and scored through the full `0000-7858`
model-explicit range. Earlier failed `6500-6999` session-limit CSVs remain
diagnostic artifacts and are not in the clean manifest.

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
in locked-output metadata. The one-row `7400` API shard has a legacy `probe`
filename, but it is included only because it is registered as a clean locked
model output in `locked_outputs/LOCKED_OUTPUT_MANIFEST_20260606.csv`.

Current clean model-explicit state: `codex:gpt-5.5`, `claude:sonnet`, and
`gemini:gemini-3-flash-preview` are all complete for `0000-7858` with 7,859
unique task units per model and no duplicate task-unit coverage.

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
private source-packet prompt/export path only. This partial smoke did not
authorize a full-corpus model run or accuracy claim.

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
studies and 492/492 target rows.

Batch 04 subsequently cleared after repeated wait-based checker reruns while
OneDrive was active. Across Batches 01-04, 62/80 studies and 1,036/1,306 target
rows are text-extractable; Batch 03 remains blocked at 18 studies / 270 target
rows. This does not authorize model execution.

Batch 03 subsequently cleared after `S126`, `S127`, and `S128` were resolved
from readable local Downloads archive copies placed in the ignored local
source-PDF folder. Batches 01-04 are now clean at 80/80 studies and 1,306/1,306
target rows.

The full 191-study materialization/readability sweep then cleared after the 49
remaining blockers were resolved from readable local Downloads archive copies
placed in the ignored source-PDF folder. The final checker reports 191/191 gap
studies and 2,025/2,025 gap rows text-extractable. Full source-rendering
coverage has also been rerun and is clean for 194/194 target studies and
2,043/2,043 target rows. Model execution remains unauthorized until a specific
source-rendered condition, exact model selector, and budget are approved.

A balanced 30-row `M1-R-SOURCE-SMOKE-FULL-COVERAGE` has now been executed with
private source packets for `S002`, `S003`, and `S007`, covering 10 rows in each
denominator family. The run completed with `model_cli_error=0`, source quote
policy violations=0, nonblank answers=13, abstentions=17, and committed source
quotes=0. Smoke diagnostic scoring is recorded in
`results/FULL_CORPUS_M1_R_SOURCE_RENDERED_FULL_COVERAGE_SMOKE_STATUS_20260609.md`.
This remains a prompt/export/locking/scoring diagnostic only, not a full-corpus
accuracy result or MASEM substitution claim.

The follow-up prompt/path review is recorded in
`results/FULL_CORPUS_STEP5_PROMPT_PATH_REVIEW_20260609.md`. It classifies the
30-row smoke as 9 positive-control successes, 1 matrix-cell selection error, 10
S003 direct-r abstentions probably tied to source-packet table coverage, and 10
S007 beta/path-route conflicts caused by non-path frozen reference evidence
being routed through the beta/path task family. A full-shell beta-family routing
audit found 146/415 beta-family rows with non-path reference evidence. Full
`M1-R` remains blocked pending revised packet/routing smoke. The targeted
`M1-R-SOURCE-SMOKE-REVISED` task bundle is prepared as
`../07_paper_c_harness_benchmark/06_rerun_bundles/source_rendered_revised_smoke_task_ids_20260609.csv`
with 40 rows balanced across latent positive controls, direct-r packet retrieval,
non-path secondary route review, and true beta/path controls.

The 40-row `M1-R-SOURCE-SMOKE-REVISED` has now been executed with a route
overlay and revised private source-packet stubs. It completed with
`model_cli_error=0`, source quote policy violations=0, nonblank answers=23,
abstentions=17, committed source quotes=0, route violations=0, and 21/40
diagnostic correct rows. The route overlay resolved the prior non-path
secondary/beta-path conflict in this smoke, but S003 direct-r rows still
abstained 10/10 and true beta/path controls remain partial. Full `M1-R` remains
blocked pending packet/table retrieval review.

A focused 25-row `M1-R-SOURCE-SMOKE-TABLE-RETRIEVAL` has now been executed after
expanding the source-packet scoring terms and PDF search paths. It completed
with `model_cli_error=0`, source quote policy violations=0, nonblank answers=18,
abstentions=7, committed source quotes=0, route violations=0, and 17/25
diagnostic correct rows. S003 direct-r/FLC retrieval is unblocked at 10/10
correct, but S009/S010 true beta/path retrieval remains partial. Full `M1-R`
remains blocked pending beta/path alias/context disambiguation and a narrower
follow-up gate or explicit staged-shard authorization.

`score_full_corpus_m1_r_with_exception_layer.py` has now been wired into
`RUNBOOK_20260606.md` as the post-freeze M1-R scorer gate. The full-corpus
wrapper now parses full-corpus reference-record IDs correctly and processes 191
registered post-freeze smoke/probe/shard rows. The 90-row bounded source-
rendered shard has 90/90 locked rows, `model_cli_error=0`, source quote policy
violations=0, 65/90 nonblank answers, and 25/90 abstentions. Generic numeric
scoring by denominator family is direct/source-r 15/30, latent/construct
correlation 27/30, and secondary beta/path 13/30. The exception-layer gate still
restricts contract-aware beta/path interpretation to matching exception-layer
records, with 45 total exception-layer hits and 2/2 contract-aware converted-
effect rows correct across the registered post-freeze outputs.

This bounded shard is staged source-rendered evidence only. It should not be
reported as full-corpus LLM accuracy, model-comparison evidence, or SEM
substitution-stability evidence.

The 8,783 task units must not be treated as one accuracy denominator. Use
`denominator_family` and `scoring_eligibility`. Current interpretation should
start from
`results/PAPER2_MODEL_EXPLICIT_DENOMINATOR_FAMILY_SUMMARY_20260607.md`, which
separates available model-explicit rows from the Codex/Claude/Gemini 3 Flash
overlap subset.
Treat `direct_r_effect_size_extraction` and `metadata_extraction` as separate
primary evidence families.

Accepted 2026-06-11 boundary decisions: OneDrive
`Paper2_Human_Final_Consensus_20260605_v2` is the canonical human consensus
package; S072 ANX-EE `r = 1.0` is trace/influence diagnostic only;
`source_blank_r` direct-r rows remain in primary direct-r extraction; converted
beta/path/source-statistic rows enter numeric extraction evaluation only as an
explicit converted/source-type stratum; Claude/Gemini are supplementary
cross-model sensitivity, not a vendor ranking.

2026-06-11 RQ status: RQ1 extraction validity, RQ2 error taxonomy/source
conditions, RQ3 human-review triage plus cross-model sensitivity, and the MASEM
substitution bridge have been generated from the locked/scored model outputs.
The bridge supports a bounded manuscript claim about review triage and
augmentation readiness; it does not yet support unsupervised replacement of the
human reference standard in the downstream MASEM.

2026-06-11 P0/P1 expert-review and deterministic substitution rerun status:
1,845 P0/P1 task units were reviewed, including 1,196 P0 numeric/MASEM rows and
649 P1 source or human-disagreement rows. The expert-reviewed LLM-assisted
primary input contains 804 rows. It applies 3 exact numeric replacements, all of
which match the frozen human-reference values, so nonzero primary value deltas
are 0. The primary pooled-correlation comparison has max absolute delta 0.000000
and no structural edges with nonzero change. Source-risk exclusion and converted
input augmentation remain sensitivity diagnostics with max absolute pooled-r
deltas of 0.407000 and 0.116229 respectively.

2026-06-11 PDF source-text audit status: all 746 P0/P1 pointer-only source rows
had local PDFs located and extractable text. The audit found 245 rows with both
numeric value and construct-pair terms in the extracted PDF text, 336 rows with
the numeric value found but pair terms not on the best page, 163 rows with
construct/source context but no numeric value hit, and 2 rows with no target hit.
These are source-text audit layers, not overwrites of the frozen human reference.

2026-06-11 R/metaSEM status: the local environment now provides `Rscript`
4.6.0, `OpenMx` 2.22.11, and `metaSEM` 1.5.0. The 804-row expert-reviewed
substitution input has `r_numeric` for all rows. A deterministic sample-size
reconciliation layer fills numeric N for 741/804 rows from the 2026-06-09
frozen full-corpus reference. The approved missing-N rule excludes the remaining
63 rows from N-weighted TSSEM/MASEM weighting until later source checking
supplies numeric N. A bounded core-6 complete-case TSSEM diagnostic was run on
PE, EE, SI, FC, BI, and UB:
baseline and expert-reviewed LLM-assisted inputs both converged in Stage 1 REM
and Stage 2, with 15 complete-case studies, 225 aggregated pair rows, maximum
pooled-r delta 0.00000000, and identical path/fit results. This is diagnostic
N-eligible subset evidence only; final all-construct/all-row
structural-path/model-fit claims still require the final approved TSSEM/MASEM
specification and source-supported numeric N for every SEM input row.
