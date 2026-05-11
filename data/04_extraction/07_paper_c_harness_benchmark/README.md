# Paper C Harness Benchmark Workspace

This folder stores Paper C benchmark artifacts for the 213-study comparison of:

- `H`: frozen source-anchored adjudicated human reference standard.
- `C`: raw Codex extraction.
- `L`: Codex + LongTable harness extraction.

## Status

Created as a scaffold. Final analyses must wait until the human reference
standard is frozen in `data/04_extraction/04_reference_standard_freeze/`.

## Structure

| Folder | Purpose |
|---|---|
| `00_manifest/` | Corpus manifest and source-document identifiers |
| `01_human_reference_snapshot/` | Share-safe frozen-reference snapshot or pointer |
| `02_codex_raw/` | Raw Codex outputs and validation summaries |
| `03_codex_longtable/` | LongTable-mediated outputs and validation summaries |
| `04_three_way_comparison/` | `H-C-L` comparison tables and pattern summaries |
| `05_auditability_metrics/` | Source-span, schema, correction, and triage metrics |
| `06_rerun_bundles/` | Share-safe rerun manifests and reproducibility summaries |
| `private/` | Local-only private inputs, raw transcripts, PDFs, or sensitive artifacts |

## Git Policy

Commit share-safe manifests, schemas, summaries, and aggregate tables only. Do
not commit raw PDFs, private human workbooks, raw model transcripts, raw
LongTable state, or non-redacted rerun bundles.
