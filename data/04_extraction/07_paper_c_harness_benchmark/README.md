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
