# Source PDF Materialization Batch 03-04 Follow-up Status

Date: 2026-06-09

Status: Batch 04 cleared after OneDrive restart and wait-based checker reruns;
Batch 03 remains blocked. This artifact does not authorize any additional
model run, scoring rerun, accuracy result, or smaller-scope claim.

## Action Taken

- Reran the share-safe materialization checker for Batch 03 and Batch 04 after
  OneDrive was restarted.
- Waited and reran Batch 03 and Batch 04 to capture delayed OneDrive
  completion.
- Waited again and reran Batch 04 only, because Batch 04 was still improving
  while Batch 03 remained unchanged.
- Did not commit PDF files, source text, raw model transcripts, human reference
  values, human adjudication rationales, or human-adjudicated source locators.

## Result Snapshot

| Check | Studies | Target rows | Result |
|---|---:|---:|---|
| Batch 03 after OneDrive restart | 20 | 300 | 2 `materialized_text_extractable` / 30 rows; 18 `not_materialized_or_read_timeout` / 270 rows |
| Batch 03 after wait | 20 | 300 | 2 `materialized_text_extractable` / 30 rows; 18 `not_materialized_or_read_timeout` / 270 rows |
| Batch 04 after OneDrive restart | 20 | 208 | 11 `materialized_text_extractable` / 118 rows; 9 `not_materialized_or_read_timeout` / 90 rows |
| Batch 04 after wait | 20 | 208 | 13 `materialized_text_extractable` / 138 rows; 7 `not_materialized_or_read_timeout` / 70 rows |
| Batch 04 after second wait | 20 | 208 | 20 `materialized_text_extractable` / 208 rows |

## Current Batch 03 Blockers

`S126`, `S127`, `S128`, `S133`, `S137`, `S146`, `S153`, `S162`, `S163`,
`S165`, `S171`, `S183`, `S186`, `S187`, `S193`, `S199`, `S214`, and `S221`
remain `not_materialized_or_read_timeout`, representing 270 target rows.

## Interpretation

Batches 01, 02, and 04 are now clean. Across Batches 01-04, 62/80 studies and
1,036/1,306 target rows are text-extractable. Batch 03 is the remaining blocker
within this four-batch priority set: 18/20 studies and 270/300 target rows are
still not locally readable.

Full-corpus `M1-R`, `M1-P`, `M2-R`, and optional `M3-R` remain blocked. The next
gate is targeted local materialization for the 18 remaining Batch 03 studies,
followed by Batch 03 checker rerun and then full source-rendering coverage
rerun only if the intended scope is clean.

## Evidence Files

- `source_pdf_materialization_check_batch03_after_onedrive_restart_20260609.csv`
- `source_pdf_materialization_check_batch03_after_onedrive_restart_wait_20260609.csv`
- `source_pdf_materialization_check_batch04_after_onedrive_restart_20260609.csv`
- `source_pdf_materialization_check_batch04_after_onedrive_restart_wait_20260609.csv`
- `source_pdf_materialization_check_batch04_after_onedrive_restart_wait2_20260609.csv`
