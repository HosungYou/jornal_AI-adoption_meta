# Full-Corpus Step 5 Pre-Run Authorization Packet

Date: 2026-06-09

Status: `M1-R-SMOKE` and the earlier partial `M1-R-SOURCE-SMOKE` were
researcher-authorized and executed. Full source-rendering coverage is now clean,
but this packet does not authorize any full-corpus model execution.

## Prepared Artifacts

- `full_corpus_locked_output_template_20260609.csv`: 2,043 unlocked target task
  rows.
- `FULL_CORPUS_MODEL_PROCEDURE_RUN_MATRIX_20260609.csv`: planned model/procedure
  conditions.
- `FULL_CORPUS_LOCKED_OUTPUT_MANIFEST_20260609.csv`: checksum manifest for
  current pre-run artifacts.
- `../schemas/FULL_CORPUS_LOCKED_OUTPUT_SCHEMA_20260609.md`: post-freeze locked
  output schema and leakage boundary.
- `../../07_paper_c_harness_benchmark/00_manifest/source_rendering_chunking_manifest_20260609.csv`:
  source rendering/chunking policy placeholder.
- `../../07_paper_c_harness_benchmark/06_rerun_bundles/repeatability_subset_manifest_20260609.csv`:
  120-row repeatability subset with 40 rows from each denominator family.

## Run Matrix Summary

| Condition | Role | Status |
|---|---|---|
| `M1-R-SMOKE` | Small stratified raw-model preflight | Authorized, executed, and manifest-registered |
| `M1-R` | Primary raw model baseline | Source rendering ready; pending approval |
| `M1-P` | Same-model stateful research harness/procedure contrast | Pending approval |
| `M2-R` | Cross-model raw comparison | Pending approval |
| `M3-R` | Optional third-family raw robustness check | Pending approval |
| `M1-R-SOURCE-SMOKE` | Private source-packet prompt/export preflight | Authorized, executed, and manifest-registered |
| `M1-R-SOURCE-SMOKE-FULL-COVERAGE` | Balanced full-coverage source-packet preflight | Authorized, executed, scored diagnostically, and manifest-registered |

All model selectors remain `to verify` before execution. The matrix preserves
prior candidate families from legacy scaffold work, but final model selectors
must be checked and recorded on the run date.

Update after researcher approval: `M1-R-SMOKE` was locked to
`codex:gpt-5.5` through `codex-cli 0.137.0` and executed on 30 stratified
post-freeze rows. The remaining full-corpus/procedure/model-comparison rows are
still not authorized.

Second update: `M1-R-SOURCE-SMOKE` was executed for the current PDF-available
subset (`S021`, `S056`, `S092`) using private source packets with source quotes
suppressed in committed output. This validates the source-packet prompt/export
path only; it does not authorize full-corpus execution.

Third update: a full target-shell source coverage audit found archive filename
coverage for all 194 target studies, but local text rendering still produced
private packets for only 3 studies / 18 target rows. The remaining 191 studies /
2,025 target rows failed local PDF read/materialization with `Operation timed
out`. This blocks full-corpus `M1-R` until the archive PDFs are locally
materialized or equivalent share-safe source renderings are available.

Fourth update: after the 49 remaining materialization blockers were resolved
from readable local Downloads archive copies placed in the ignored local
source-PDF folder, the full materialization checker reported 191/191 gap
studies and 2,025/2,025 target rows `materialized_text_extractable`. The full
source-rendering coverage audit was then rerun and produced private packets for
194/194 target studies covering all 2,043 target rows. This clears the prior
source materialization/readability blocker but does not authorize model
execution.

Fifth update: after the researcher instructed Codex to proceed with the next
task, `M1-R-SOURCE-SMOKE-FULL-COVERAGE` was executed on 30 balanced
source-rendered rows (`S002`, `S003`, `S007`; 10 rows per denominator family)
using `codex:gpt-5.5`. The locked output was manifest-registered and
diagnostically scored. This validates the full-coverage source-packet
prompt/export/scoring path only; it does not authorize full-corpus execution or
any LLM accuracy/MASEM substitution claim.

## Authorization Decision Recorded

The researcher approved Codex's recommended next step on 2026-06-09:

1. First executable condition: `M1-R-SMOKE` only.
2. Exact provider/model surface for the smoke: `openai`; `codex:gpt-5.5`.
3. Local CLI/version lock: `codex-cli 0.137.0; model_selector=gpt-5.5`.
4. Budget/scope: smoke-only 30-row preflight; no full-corpus run authorized.
5. Source rendering/chunking policy: no human reference value and no
   human-adjudicated source locator in prompts.
6. Private raw-output policy: raw transcripts not committed; locked structured
   CSV may be registered.
7. Repeatability subset: the 120-row 40/40/40 subset remains frozen for later
   repeated-run stability checks.

## Smoke Execution Evidence

- Run ID: `paper_b_full_corpus_m1_raw_smoke_20260609`
- Locked output:
  `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_smoke_20260609.csv`
- Status summary:
  `data/04_extraction/05_llm_masem_substitution/results/FULL_CORPUS_M1_R_SMOKE_STATUS_20260609.md`
- Rows: 30, balanced 10/10/10 across denominator families.
- `model_cli_error` rows: 0.
- Manifest registration: true.
- Interpretation: all 30 rows abstained with `insufficient_evidence` because
  this smoke used the current task stubs without source-document chunks.

## Source-Rendered Smoke Evidence

- Run ID: `paper_b_full_corpus_m1_raw_source_rendered_smoke_20260609`
- Locked output:
  `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_source_rendered_smoke_20260609.csv`
- Status summary:
  `data/04_extraction/05_llm_masem_substitution/results/FULL_CORPUS_M1_R_SOURCE_RENDERED_SMOKE_STATUS_20260609.md`
- Source rendering manifest:
  `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_rendering_available_pdf_manifest_20260609.csv`
- Rows: 6, across `S021`, `S056`, and `S092`.
- Denominator family: `secondary_beta_or_path_converted_effect_size` only.
- `model_cli_error` rows: 0.
- Source quote policy violations: 0.
- Nonblank model answers: 6.
- Nonblank committed source quotes: 0.
- Manifest registration: true.

## Full-Coverage Source-Rendered Smoke Evidence

- Run ID:
  `paper_b_full_corpus_m1_raw_source_rendered_full_coverage_smoke_20260609`
- Locked output:
  `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_source_rendered_full_coverage_smoke_20260609.csv`
- Status summary:
  `data/04_extraction/05_llm_masem_substitution/results/FULL_CORPUS_M1_R_SOURCE_RENDERED_FULL_COVERAGE_SMOKE_STATUS_20260609.md`
- Source rendering manifest:
  `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_rendering_full_coverage_manifest_20260609.csv`
- Rows: 30, balanced 10/10/10 across the three denominator families.
- Studies: `S002`, `S003`, and `S007`.
- `model_cli_error` rows: 0.
- Source quote policy violations: 0.
- Nonblank model answers: 13.
- Abstentions / insufficient-evidence rows: 17.
- Nonblank committed source quotes: 0.
- Smoke diagnostic correct rows under numeric tolerance: 9/30.
- Manifest registration: true.

## Full Coverage Materialization Audit

- Coverage manifest:
  `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_rendering_full_coverage_manifest_20260609.csv`
- Coverage status:
  `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/SOURCE_RENDERING_FULL_COVERAGE_STATUS_20260609.md`
- Target studies audited: 194.
- Private packets successfully rendered: 194 studies / 2,043 target rows.
- Local rendering/materialization failures: 0 studies / 0 target rows.
- Final materialization checker:
  `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_pdf_materialization_check_full_after_local_downloads_copy_20260609.csv`.
- Interpretation: the prior source materialization/readability blocker is
  cleared. Model execution still requires a separate researcher authorization
  for the exact condition, model selector, and budget.

## Approval Items

Before any model condition is run, the researcher must approve:

1. The first executable condition, recommended as `M1-R-SMOKE`.
2. Exact model selector and provider surface for `M1`.
3. Whether `M2-R` and optional `M3-R` are in scope for the first full-corpus
   comparison.
4. Budget cap for smoke and full-corpus runs.
5. Source rendering/chunking policy, including whether model prompts may receive
   human-adjudicated source locators. Current default: no.
6. Private raw-output storage path and share-safe output policy.
7. Whether the 120-row repeatability subset is accepted as frozen for repeated
   run stability checks.

## Non-Claims

- No post-freeze full-corpus model run has been executed.
- No scoring rerun has been executed.
- No LLM accuracy, model comparison, procedure comparison, or MASEM
  substitution result is current.
- Legacy pre-full-corpus outputs remain scaffold evidence unless explicitly
  re-keyed and revalidated against the 2026-06-09 frozen reference.

## Recommended Next Decision

The balanced full-coverage source-rendered smoke has now been reviewed. The
active next decision is not a larger shard or full-corpus `M1-R`; it is a
revised prompt/path smoke:

- `data/04_extraction/05_llm_masem_substitution/results/FULL_CORPUS_M1_R_SOURCE_RENDERED_FULL_COVERAGE_SMOKE_STATUS_20260609.md`
- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_source_rendered_full_coverage_smoke_scored_20260609.csv`
- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_source_rendered_full_coverage_smoke_status_20260609.csv`
- `data/04_extraction/05_llm_masem_substitution/results/FULL_CORPUS_STEP5_PROMPT_PATH_REVIEW_20260609.md`
- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_source_rendered_smoke_prompt_path_review_20260609.csv`
- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_step5_beta_family_routing_audit_20260609.csv`
- `data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/source_rendered_revised_smoke_task_ids_20260609.csv`

The review found 9 positive-control successes, 1 matrix-cell selection error,
10 direct-r abstentions probably tied to source-packet table coverage, and 10
S007 beta/path-route conflicts where non-path frozen reference evidence was
routed through the beta/path task family. The full-shell routing audit found
146/415 beta-family rows with non-path reference evidence. These are downstream
model-input route conflicts, not human-reference value changes.

The full-corpus `M1-R`, `M1-P`, `M2-R`, and optional `M3-R` conditions remain
blocked pending source-packet/routing remediation, exact provider/model selector,
budget cap, and run authorization. Do not report LLM accuracy, model comparison,
procedure comparison, or MASEM substitution claims until a locked model output is
generated, manifest-registered, and scored against the frozen reference.

Follow-up checker status: the full 191-study materialization gap was checked
again after attempting to identify a CLI hydration route. All 191 studies still
returned `not_materialized_or_read_timeout`, and the available local CLI surface
did not execute the OneDrive `MarkPinned` context action. The next gate remains
OneDrive/Finder local materialization followed by checker and source-rendering
coverage reruns.

Finder/OneDrive follow-up: after starting OneDrive and clicking the Finder
not-downloaded control for the main `PDFs` archive folder, 16 studies / 376
target rows became text-extractable. The remaining 175 studies / 1,649 target
rows still block full-corpus `M1-R`, `M1-P`, and `M2-R`.

Batch follow-up: Batch 02 is now fully text-extractable, and Batch 01 improved
to 16/20 studies. Across Batches 01-04, 39/80 studies and 751/1,306 target rows
are text-extractable, but 41 studies / 555 rows still return
`not_materialized_or_read_timeout`. This does not authorize any full-corpus
model execution.

Batch 01 blocker request follow-up: download requests were submitted through
Finder/OneDrive for `S157`, `S036`, `S088`, and `S190`. After partial OneDrive
completion, `S157` and `S190` became `materialized_text_extractable`, while
`S036` and `S088` still returned `not_materialized_or_read_timeout` at that
intermediate checkpoint. Batch 01 was then 18/20 studies and 450/492 target
rows text-extractable; the remaining Batch 01 blocker was 2 studies / 42 target
rows. This did not authorize any full-corpus model execution.

OneDrive restart follow-up: after OneDrive was restarted again, `S036` and
`S088` also became `materialized_text_extractable`. Batch 01 is now clean at
20/20 studies and 492/492 target rows. Batch 04 subsequently cleared after
repeated wait-based checker reruns while OneDrive was active. Across Batches
01-04, 62/80 studies and 1,036/1,306 target rows are text-extractable; Batch 03
remains blocked at 18 studies / 270 target rows. This still does not authorize
any full-corpus model execution.

Batch 03 clearance follow-up: `S126`, `S127`, and `S128` were resolved from
readable local Downloads archive copies placed in the ignored local source-PDF
folder. Batches 01-04 are now clean at 80/80 studies and 1,306/1,306 target
rows. This cleared the first four materialization priority batches but did not
authorize any full-corpus model execution.

Full materialization/source-rendering follow-up: the full 191-study
materialization/readability sweep initially found 49 remaining blockers. All 49
were resolved by readable local Downloads archive copies into the ignored
source-PDF folder, after which the final full checker reported 191/191 gap
studies and 2,025/2,025 target rows text-extractable. Full source-rendering
coverage was then rerun and rendered private packets for 194/194 target studies
covering all 2,043 target rows. This authorizes neither a full-corpus model run
nor result claims by itself.

Full-coverage source-rendered smoke follow-up: the balanced 30-row source smoke
completed with no CLI errors and no committed source quotes. It produced
nonblank answers for 13 rows and abstained on 17 rows; smoke diagnostics show
the prompt path works best for the latent/construct correlation family in this
small sample. Treat this as prompt/path evidence only, not as a full-corpus
performance estimate.

Prompt/path review follow-up: the 30-row smoke was reviewed at row level and
against the full Step 5 task shell. The next executable condition is
`M1-R-SOURCE-SMOKE-REVISED`, planned but not authorized, after direct-r packet
selection and beta-family non-path routing are corrected or isolated. A 40-row
revised smoke task bundle has been prepared with 10 rows each for latent positive
controls, S003 direct-r packet retrieval, non-path secondary route review, and
true beta/path controls. Full-corpus model execution remains blocked.
