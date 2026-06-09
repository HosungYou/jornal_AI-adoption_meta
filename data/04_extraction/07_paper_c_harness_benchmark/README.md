# Paper C Model-by-Procedure Benchmark Workspace

This folder stores Paper C benchmark artifacts for the 213-study comparison of:

- `H`: frozen source-anchored adjudicated human reference standard.
- Raw model conditions, such as `M1-R` and `M2-R`.
- Procedure-mediated conditions, such as `M1-P`.

## Status

Created as a scaffold. The full-corpus human reference was frozen on
2026-06-09, so the workspace can now move to model/procedure run-condition
planning. The source-rendering policy placeholder and 120-row repeatability
subset are prepared. A partial PDF-available source-rendering preflight has also
been completed for `S021`, `S056`, and `S092`, with private source packets kept
out of Git and a 6-row source-rendered smoke registered as a locked output.

Full source-rendering coverage is now clean for the post-freeze target shell:
194/194 target studies and 2,043/2,043 target rows have private source packets
stored outside Git. This clears the source materialization/readability blocker.
Full-corpus `M1-R`, `M1-P`, `M2-R`, and optional `M3-R` remain pending exact
model selector, budget, and run-condition authorization.

A follow-up archive coverage audit found study-ID PDF filename coverage for all
194 post-freeze target studies, but local text rendering is still blocked:
private source packets were produced for only 3 studies / 18 target rows. The
remaining 191 studies / 2,025 target rows failed local PDF read/materialization
with `Operation timed out`. Treat this as a local OneDrive materialization
blocker, not as evidence that source PDFs are absent from the archive.

A materialization action package now groups the 191 blocked studies into 10
share-safe batches prioritized by target-row burden. The accompanying checker
records only study-level readability status and does not commit PDF paths,
source text, human values, or human-adjudicated source locators. A 3-study
checker smoke confirmed that the first high-priority files still return
`not_materialized_or_read_timeout`.

The full 191-study checker has also been rerun after checking for an available
CLI materialization route. All 191 blocked studies still return
`not_materialized_or_read_timeout`. The local OneDrive File Provider exposes
pinning as a context action, but the current CLI surface did not execute that
action, so the next gate is a OneDrive/Finder "Always Keep on This Device"
materialization step followed by checker and source-rendering reruns.

A follow-up Finder/OneDrive attempt produced partial progress: 16 of the 191
blocked studies, covering 376 of the 2,025 blocked target rows, became
`materialized_text_extractable`. Full-corpus source rendering remains blocked
because 175 studies / 1,649 target rows still return
`not_materialized_or_read_timeout`.

A later batch-focused follow-up found that Batch 02 is now fully
text-extractable and Batch 01 improved to 16/20 studies. Across Batches 01-04,
39/80 studies and 751/1,306 target rows are text-extractable; 41 studies / 555
target rows still return `not_materialized_or_read_timeout`. Full-corpus source
rendering remains blocked.

A targeted Batch 01 blocker follow-up submitted Finder/OneDrive download
requests for `S157`, `S036`, `S088`, and `S190`. `S157` and `S190`
subsequently became `materialized_text_extractable`; at that intermediate
probe, `S036` and `S088` still returned `not_materialized_or_read_timeout`.
Batch 01 was then 18/20 studies and 450/492 target rows text-extractable, with
42 target rows still blocked.

After OneDrive was restarted again, `S036` and `S088` also became
`materialized_text_extractable`. Batch 01 is now clean at 20/20 studies and
492/492 target rows. Full-corpus source rendering remained blocked because
Batches 03-04 still needed follow-up.

Batch 04 subsequently cleared after repeated wait-based checker reruns while
OneDrive was active. Across Batches 01-04, 62/80 studies and 1,036/1,306 target
rows are text-extractable. Batch 03 remains the only blocker within these four
priority batches at 18 studies / 270 target rows.

Batch 03 subsequently cleared after `S126`, `S127`, and `S128` were resolved
from readable local Downloads archive copies placed in the ignored local
source-PDF folder. Batches 01-04 are now clean at 80/80 studies and 1,306/1,306
target rows.

The subsequent full 191-study materialization/readability sweep initially left
49 blockers, all of which were resolved from readable local Downloads archive
copies placed in the ignored local source-PDF folder. The final checker reports
191/191 gap studies and 2,025/2,025 gap rows text-extractable. Full
source-rendering coverage was then rerun and is clean.

A balanced full-coverage source-rendered smoke has now been executed for 30 rows
across `S002`, `S003`, and `S007` with 10 rows in each denominator family. It
completed with no CLI errors, no source quote policy violations, 13 nonblank
answers, 17 abstentions, and no committed source quotes. This is a Paper C
prompt/export/locking/scoring diagnostic only; it is not a full-corpus model
comparison or substitution result.

Current reference pointer:

- `01_human_reference_snapshot/full_corpus_reference_pointer_20260609.csv`

Current pre-run planning artifacts:

- `00_manifest/source_rendering_chunking_manifest_20260609.csv`
- `00_manifest/source_rendering_available_pdf_manifest_20260609.csv`
- `00_manifest/SOURCE_RENDERING_PREFLIGHT_STATUS_20260609.md`
- `00_manifest/source_rendering_full_coverage_manifest_20260609.csv`
- `00_manifest/SOURCE_RENDERING_FULL_COVERAGE_STATUS_20260609.md`
- `00_manifest/source_pdf_materialization_gap_manifest_20260609.csv`
- `00_manifest/SOURCE_PDF_MATERIALIZATION_PLAN_20260609.md`
- `00_manifest/source_pdf_materialization_check_smoke_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch01_20260609.csv`
- `00_manifest/source_pdf_materialization_check_full_20260609.csv`
- `00_manifest/SOURCE_PDF_MATERIALIZATION_CHECK_STATUS_20260609.md`
- `00_manifest/source_pdf_materialization_check_batch01_after_finder_click_20260609.csv`
- `00_manifest/source_pdf_materialization_check_full_after_finder_click_20260609.csv`
- `00_manifest/SOURCE_PDF_MATERIALIZATION_FINDER_ATTEMPT_STATUS_20260609.md`
- `00_manifest/source_pdf_materialization_check_batch01_followup_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch02_followup_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch03_followup_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch04_followup_20260609.csv`
- `00_manifest/SOURCE_PDF_MATERIALIZATION_BATCH_FOLLOWUP_STATUS_20260609.md`
- `00_manifest/source_pdf_materialization_check_batch01_blockers_recheck_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch01_blockers_longtimeout_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch01_blockers_after_request_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch01_blockers_after_wait_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch01_blockers_final_probe_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch01_after_blocker_requests_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch01_blockers_after_onedrive_restart_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch01_after_onedrive_restart_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch03_after_onedrive_restart_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch03_after_onedrive_restart_wait_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch04_after_onedrive_restart_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch04_after_onedrive_restart_wait_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch04_after_onedrive_restart_wait2_20260609.csv`
- `00_manifest/SOURCE_PDF_MATERIALIZATION_BATCH03_04_FOLLOWUP_STATUS_20260609.md`
- `00_manifest/source_pdf_materialization_check_batch03_current_recheck_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch03_remaining3_after_wait_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch03_after_local_downloads_copy_20260609.csv`
- `00_manifest/source_pdf_materialization_check_full_after_batches01_04_clean_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch08_after_full_sweep_wait_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch09_after_full_sweep_wait_20260609.csv`
- `00_manifest/source_pdf_materialization_check_batch10_after_full_sweep_wait_20260609.csv`
- `00_manifest/source_pdf_materialization_blocked_local_copy_resolution_20260609.csv`
- `00_manifest/source_pdf_materialization_check_full_after_local_downloads_copy_20260609.csv`
- `00_manifest/SOURCE_PDF_MATERIALIZATION_BATCH03_CLEARANCE_STATUS_20260609.md`
- `00_manifest/SOURCE_PDF_MATERIALIZATION_BATCH01_BLOCKER_REQUEST_STATUS_20260609.md`
- `06_rerun_bundles/repeatability_subset_manifest_20260609.csv`
- `06_rerun_bundles/source_rendered_smoke_task_ids_20260609.csv`
- `06_rerun_bundles/source_rendered_full_coverage_smoke_task_ids_20260609.csv`
- `00_manifest/source_rendering_table_retrieval_targets_manifest_20260609.csv`
- `06_rerun_bundles/source_rendered_table_retrieval_smoke_task_ids_20260609.csv`
- `06_rerun_bundles/source_pdf_materialization_batches_20260609.csv`

## Structure

| Folder | Purpose |
|---|---|
| `00_manifest/` | Corpus manifest and source-document identifiers |
| `01_human_reference_snapshot/` | Share-safe frozen-reference snapshot or pointer |
| `02_raw_model_conditions/` | Raw model outputs and validation summaries |
| `03_procedure_conditions/` | Procedure-mediated outputs and validation summaries |
| `04_model_procedure_comparison/` | `H` versus model/procedure comparison tables and pattern summaries |
| `05_auditability_metrics/` | Source-span, schema, correction, and triage metrics |
| `06_rerun_bundles/` | Share-safe rerun manifests and reproducibility summaries |
| `private/` | Local-only private inputs, raw transcripts, PDFs, or sensitive artifacts |

## Git Policy

Commit share-safe manifests, schemas, summaries, and aggregate tables only. Do
not commit raw PDFs, private human workbooks, raw model transcripts, raw
LongTable state, or non-redacted rerun bundles.
