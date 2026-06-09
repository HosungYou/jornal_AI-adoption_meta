# Source PDF Materialization Batch 03 Clearance Status

Date: 2026-06-09

Status: Batch 03 is now clean at 20/20 studies and 300/300 target rows
text-extractable. This artifact does not authorize any additional model run,
scoring rerun, accuracy result, or smaller-scope claim.

## Action Taken

- Reran Batch 03 while OneDrive was active.
- Batch 03 improved from 2/20 studies and 30/300 target rows text-extractable
  to 17/20 studies and 255/300 target rows text-extractable.
- Identified the remaining blockers as `S126`, `S127`, and `S128`.
- Confirmed local readable PDF copies for `S126`, `S127`, and `S128` under the
  user's local Downloads archive.
- Copied those three PDFs into the ignored local source-PDF folder:
  `data/04_extraction/03_source_document_adjudication/source_pdfs/`.
- Confirmed `.gitignore` excludes the copied PDFs.
- Reran the Batch 03 checker and confirmed 20/20 studies and 300/300 target
  rows are `materialized_text_extractable`.

## Result Snapshot

| Check | Studies | Target rows | Result |
|---|---:|---:|---|
| Batch 03 current recheck | 20 | 300 | 17 `materialized_text_extractable` / 255 rows; 3 `not_materialized_or_read_timeout` / 45 rows |
| Remaining-three wait recheck | 3 | 45 | 3 `not_materialized_or_read_timeout` / 45 rows |
| Batch 03 after local Downloads copy | 20 | 300 | 20 `materialized_text_extractable` / 300 rows |

## Interpretation

Batches 01-04 are now clean: 80/80 studies and 1,306/1,306 target rows are
text-extractable across the first four priority materialization batches.

Full-corpus `M1-R`, `M1-P`, `M2-R`, and optional `M3-R` remain blocked until the
intended full source-rendering scope is clean. The next gate is a full
materialization/readability sweep or continuation into Batches 05-10 before
rerunning full source-rendering coverage.

## Evidence Files

- `source_pdf_materialization_check_batch03_current_recheck_20260609.csv`
- `source_pdf_materialization_check_batch03_remaining3_after_wait_20260609.csv`
- `source_pdf_materialization_check_batch03_after_local_downloads_copy_20260609.csv`
