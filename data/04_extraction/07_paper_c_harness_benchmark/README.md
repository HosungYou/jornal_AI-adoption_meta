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

This preflight does not authorize full-corpus model execution or accuracy
claims. Full-corpus `M1-R`, `M1-P`, `M2-R`, and optional `M3-R` remain blocked
until source rendering coverage is complete for the intended target scope, or a
smaller PDF-available subset is explicitly authorized.

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
492/492 target rows. Full-corpus source rendering remains blocked because
Batches 03-04 remain mostly blocked.

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
- `00_manifest/SOURCE_PDF_MATERIALIZATION_BATCH01_BLOCKER_REQUEST_STATUS_20260609.md`
- `06_rerun_bundles/repeatability_subset_manifest_20260609.csv`
- `06_rerun_bundles/source_rendered_smoke_task_ids_20260609.csv`
- `06_rerun_bundles/source_rendered_full_coverage_smoke_task_ids_20260609.csv`
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
