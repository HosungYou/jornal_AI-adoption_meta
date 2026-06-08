# Paper C Model-by-Procedure Benchmark Workspace

This folder stores Paper C benchmark artifacts for the 213-study comparison of:

- `H`: frozen source-anchored adjudicated human reference standard.
- Raw model conditions, such as `M1-R` and `M2-R`.
- Procedure-mediated conditions, such as `M1-P`.

## Status

Created as a scaffold. The full-corpus human reference was frozen on
2026-06-09, so the workspace can now move to model/procedure run-condition
planning. The source-rendering policy placeholder and 120-row repeatability
subset are now prepared, but final analyses still require explicit approval of
model selectors, procedure contrast, budget caps, prompt/schema versions, and
private-output storage before any model run.

Current reference pointer:

- `01_human_reference_snapshot/full_corpus_reference_pointer_20260609.csv`

Current pre-run planning artifacts:

- `00_manifest/source_rendering_chunking_manifest_20260609.csv`
- `06_rerun_bundles/repeatability_subset_manifest_20260609.csv`

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
