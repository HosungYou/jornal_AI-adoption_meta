# Source PDF Materialization Plan

Date: 2026-06-09

Status: materialization action package prepared. This artifact does not authorize any additional model run or any smaller-scope result claim.

## Scope

- Target studies in source rendering coverage manifest: 194
- Studies already source-rendered into private packets: 3
- Studies requiring local PDF materialization/readability resolution: 191
- Target rows already source-rendered: 18
- Target rows still blocked by materialization/readability: 2025
- Materialization batches prepared: 10

## Failure Mode Counts

- `onedrive_read_timeout`: 191

## Blocked Rows by Denominator Family

- `primary_direct_r_or_source_reported_correlation`: 56 studies / 697 target rows
- `primary_latent_or_construct_correlation_with_source_type_flag`: 78 studies / 931 target rows
- `secondary_beta_or_path_converted_effect_size`: 57 studies / 397 target rows

## Prepared Artifacts

- `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_pdf_materialization_gap_manifest_20260609.csv`: study-level materialization gap manifest, prioritized by target-row burden.
- `data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/source_pdf_materialization_batches_20260609.csv`: batch-level materialization worklist.
- `scripts/llm_scoring_20260606/check_source_pdf_materialization.py`: share-safe local readability checker for hydrated PDFs.

## Procedure Boundary

- The archive has study-ID filename coverage for the full 194-study target shell, but filename coverage is not enough for source-rendered model prompts.
- The current blocker is local OneDrive materialization/readability: most files time out when a PDF reader attempts to open them.
- Do not run full-corpus `M1-R`, `M1-P`, `M2-R`, or optional `M3-R` until materialization checks and source-rendering coverage are clean for the intended target scope.
- Do not use human reference values, human adjudication rationales, or human-adjudicated source locators to make model prompts.
- Keep PDFs, rendered source packets, and raw model transcripts out of Git.

## Next Gate

After the OneDrive PDFs are locally materialized, run the checker on the relevant batch or full gap manifest. Then rerun the source-rendering coverage audit. A balanced source-rendered smoke is only eligible after rendered private packets cover the intended scope.

## Integrity

- `source_pdf_materialization_gap_manifest_20260609.csv` sha256: `ed9013f3328b2f8b0c40411ce0ef575cfe5df9bcbeab35fc5006e32b0862c462`
- `source_pdf_materialization_batches_20260609.csv` sha256: `b190f0f3242c7c448aca7a276fc174a45d0ebec9746a7d5d1c783a2a281841d3`
- Generated at UTC: `2026-06-09T00:11:01Z`
