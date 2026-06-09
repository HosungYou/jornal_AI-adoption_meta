# Source PDF Materialization Batch 01 Blocker Request Status

Date: 2026-06-09

Status: download requests were submitted for the four remaining Batch 01
blockers. `S157` and `S190` first became locally text-extractable; after
OneDrive was restarted again, `S036` and `S088` also became locally
text-extractable. Batch 01 is now clean at 20/20 studies and 492/492 target
rows. This artifact does not authorize any additional model run, scoring rerun,
accuracy result, or smaller-scope claim.

## Action Taken

- Rechecked the four remaining Batch 01 blockers: `S157`, `S036`, `S088`, and
  `S190`.
- Reran the checker with the normal 8-second probe and a longer 60-second probe.
- Restarted OneDrive after confirming File Provider was temporarily
  disconnected.
- Used Finder reveal plus the OneDrive/Finder `Not downloaded` button for each
  blocker.
- Confirmed File Provider state initially changed to `isDownloadRequested=1`
  and `isDownloading=1` for all four files.
- Waited and reran the share-safe checker. The immediate post-wait check still
  reported all four as `not_materialized_or_read_timeout`.
- Reran a final four-file probe and a full Batch 01 checker after OneDrive
  finished part of the request. `S157` and `S190` became
  `materialized_text_extractable`; `S036` and `S088` still returned
  `not_materialized_or_read_timeout`.
- Retried the Finder/OneDrive request for `S036` and `S088`; File Provider did
  not preserve an active requested/downloading state for those two files.
- Restarted OneDrive again after Finder reported the provider was not running.
- Reran the four-file checker and full Batch 01 checker. All four blocker files
  and all 20 Batch 01 studies were `materialized_text_extractable`.
- Did not commit PDF files, source text, raw model transcripts, human reference
  values, human adjudication rationales, or human-adjudicated source locators.

## Result Snapshot

| Check | Studies | Target rows | Result |
|---|---:|---:|---|
| Pre-request normal probe | 4 | 91 | 4 `not_materialized_or_read_timeout` |
| Pre-request long-timeout probe | 4 | 91 | 4 `not_materialized_or_read_timeout` |
| Post-request normal probe | 4 | 91 | 4 `not_materialized_or_read_timeout` |
| Post-wait normal probe | 4 | 91 | 4 `not_materialized_or_read_timeout` |
| Final four-file probe | 4 | 91 | 2 `materialized_text_extractable` / 49 rows; 2 `not_materialized_or_read_timeout` / 42 rows |
| Full Batch 01 checker after blocker requests | 20 | 492 | 18 `materialized_text_extractable` / 450 rows; 2 `not_materialized_or_read_timeout` / 42 rows |
| Four-file checker after OneDrive restart | 4 | 91 | 4 `materialized_text_extractable` / 91 rows |
| Full Batch 01 checker after OneDrive restart | 20 | 492 | 20 `materialized_text_extractable` / 492 rows |

Final blocker state:

| Study | Final checker status | Target rows | Notes |
|---|---|---:|---|
| `S157` | `materialized_text_extractable` | 28 | Request completed; PDF text extractable |
| `S036` | `materialized_text_extractable` | 21 | Cleared after OneDrive restart |
| `S088` | `materialized_text_extractable` | 21 | Cleared after OneDrive restart |
| `S190` | `materialized_text_extractable` | 21 | Request completed; PDF text extractable |

## Interpretation

The Batch 01 blocker has cleared. Batch 01 improved from 16/20 studies and
401/492 target rows text-extractable to 20/20 studies and 492/492 target rows
text-extractable.

Full-corpus `M1-R`, `M1-P`, `M2-R`, and optional `M3-R` remain blocked. The next
gate is to continue targeted materialization for Batches 03-04, then rerun the
relevant checker(s). No full-corpus model/procedure run is authorized before
intended-scope source rendering coverage is clean.

## Evidence Files

- `source_pdf_materialization_check_batch01_blockers_recheck_20260609.csv`
- `source_pdf_materialization_check_batch01_blockers_longtimeout_20260609.csv`
- `source_pdf_materialization_check_batch01_blockers_after_request_20260609.csv`
- `source_pdf_materialization_check_batch01_blockers_after_wait_20260609.csv`
- `source_pdf_materialization_check_batch01_blockers_final_probe_20260609.csv`
- `source_pdf_materialization_check_batch01_after_blocker_requests_20260609.csv`
- `source_pdf_materialization_check_batch01_blockers_after_onedrive_restart_20260609.csv`
- `source_pdf_materialization_check_batch01_after_onedrive_restart_20260609.csv`
