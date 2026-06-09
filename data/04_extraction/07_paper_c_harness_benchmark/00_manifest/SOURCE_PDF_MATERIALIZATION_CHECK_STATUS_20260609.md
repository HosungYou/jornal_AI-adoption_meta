# Source PDF Materialization Check Status

Date: 2026-06-09

Status: full materialization/readability is clean for the 191-study
materialization gap after local Downloads archive recovery for the remaining
blockers. This artifact does not authorize any model run, scoring rerun,
accuracy result, or smaller-scope claim by itself.

## What Was Checked

- Materialization gap manifest scope: 191 studies / 2,025 target rows.
- Full checker output: `source_pdf_materialization_check_full_20260609.csv`.
- Batch 01 checker output: `source_pdf_materialization_check_batch01_20260609.csv`.
- One-file CLI materialization route: attempted with `fileproviderctl materialize`; current system command surface returned usage output rather than materializing the file.
- OneDrive File Provider inspection: the provider exposes `MarkPinned` / `MarkUnpinned` as File Provider context actions, but the available `fileproviderctl evaluate` command does not execute those custom actions.

## Initial Recheck Results

| Check | Result |
|---|---:|
| Full gap studies checked | 191 |
| Full gap target rows checked | 2,025 |
| Source PDF filename matches | 191 |
| `not_materialized_or_read_timeout` | 191 |
| `materialized_text_extractable` | 0 |
| Batch 01 studies checked | 20 |
| Batch 01 `not_materialized_or_read_timeout` | 20 |

## Interpretation

The blocker is still local OneDrive materialization/readability, not archive
absence. The files are visible to the local filesystem by study-ID filename, but
the first-byte read probe times out for all 191 blocked studies. Because the
current CLI surface cannot execute the OneDrive `MarkPinned` action, the next
step has to use a OneDrive/Finder materialization action such as "Always Keep on
This Device" on the archive folder or on the materialization batch files.

Follow-up Finder/OneDrive attempt: clicking the Finder/OneDrive not-downloaded
control for the main `PDFs` archive folder produced partial progress. The latest
full snapshot after that attempt reports 16 text-extractable studies / 376
target rows and 175 still-blocked studies / 1,649 target rows. Full-corpus model
execution remains blocked.

## Latest Follow-up Snapshot

| Check | Result |
|---|---:|
| Full gap studies checked | 191 |
| Full gap target rows checked | 2,025 |
| `materialized_text_extractable` studies | 16 |
| `materialized_text_extractable` target rows | 376 |
| `not_materialized_or_read_timeout` studies | 175 |
| `not_materialized_or_read_timeout` target rows | 1,649 |
| Batch 01 materialized studies | 12 / 20 |
| Batch 01 materialized target rows | 317 / 492 |

## Later Batch Follow-up

A later batch-focused checker run found:

- Batch 01: 16/20 studies and 401/492 target rows text-extractable; remaining
  blockers are `S157`, `S036`, `S088`, and `S190`.
- Batch 02: 20/20 studies and 306/306 target rows text-extractable.
- Batch 03: 2/20 studies and 30/300 target rows text-extractable.
- Batch 04: 1/20 studies and 14/208 target rows text-extractable.

Across Batches 01-04, 39/80 studies and 751/1,306 target rows are
text-extractable, while 41 studies / 555 target rows still return
`not_materialized_or_read_timeout`. This is batch-focused evidence only; it does
not replace a full 191-study checker snapshot.

## Batch 01 Blocker Request Follow-up

The four remaining Batch 01 blockers (`S157`, `S036`, `S088`, `S190`) were
rechecked with both normal and long-timeout probes; all four remained
`not_materialized_or_read_timeout`. After restarting OneDrive and clicking each
file's Finder/OneDrive `Not downloaded` control, File Provider reported
`isDownloadRequested=1` and `isDownloading=1` for all four files. A later
post-wait checker rerun still reported 4/4
`not_materialized_or_read_timeout`.

A final probe after partial OneDrive completion found that `S157` and `S190`
became `materialized_text_extractable`, while `S036` and `S088` still returned
`not_materialized_or_read_timeout`. The full Batch 01 checker then reported
18/20 studies and 450/492 target rows text-extractable, with 2 studies / 42
target rows still blocked. A retry for `S036` and `S088` did not preserve an active
File Provider requested/downloading state.

After OneDrive was restarted again, the four-file checker reported `S157`,
`S036`, `S088`, and `S190` as `materialized_text_extractable`. The full Batch
01 checker now reports 20/20 studies and 492/492 target rows text-extractable.

## Batch 03-04 Follow-up

After the Batch 01 clearing step, Batches 03-04 were rerun while OneDrive was
active. Batch 03 remained blocked at 2/20 studies and 30/300 target rows
text-extractable. Batch 04 improved across repeated wait-based checker reruns
and ultimately cleared at 20/20 studies and 208/208 target rows
text-extractable.

Across Batches 01-04, 62/80 studies and 1,036/1,306 target rows are now
text-extractable. The remaining blocker within these four priority batches is
Batch 03: 18 studies / 270 target rows still return
`not_materialized_or_read_timeout`.

## Batch 03 Clearance Follow-up

Batch 03 was rerun while OneDrive was active and improved to 17/20 studies and
255/300 target rows text-extractable. The remaining blockers were `S126`,
`S127`, and `S128`. Local readable copies were found in the user's local
Downloads archive and copied into the ignored local source-PDF folder. The Batch
03 checker then reported 20/20 studies and 300/300 target rows
text-extractable.

Batches 01-04 are now clean: 80/80 studies and 1,306/1,306 target rows are
text-extractable across the first four priority materialization batches.

## Full Sweep and Final Clearance

After Batches 01-04 cleared, a full 191-study materialization/readability sweep
was rerun:

| Check | Result |
|---|---:|
| Full gap studies checked | 191 |
| Full gap target rows checked | 2,025 |
| `materialized_text_extractable` studies | 142 |
| `materialized_text_extractable` target rows | 1,810 |
| `not_materialized_or_read_timeout` studies | 49 |
| `not_materialized_or_read_timeout` target rows | 215 |

Wait-based follow-up checks for Batches 08-10 did not clear the remaining
blockers. A local readable-copy resolver then found readable PDFs for all 49
remaining blocker studies in the user's local Downloads archive and copied them
into the ignored local source-PDF folder:

- Resolved blockers: 49/49.
- Source location class recorded in the share-safe CSV: `downloads_archive`.
- Committed PDF paths: 0 (`pdf_path_committed=false` for every row).
- Local private PDFs: copied only into
  `data/04_extraction/03_source_document_adjudication/source_pdfs/`, which is
  ignored by Git.

The final full checker after this local copy step reports:

| Check | Result |
|---|---:|
| Full gap studies checked | 191 |
| Full gap target rows checked | 2,025 |
| `materialized_text_extractable` studies | 191 |
| `materialized_text_extractable` target rows | 2,025 |
| `not_materialized_or_read_timeout` studies | 0 |
| `not_materialized_or_read_timeout` target rows | 0 |

## Next Gate

The materialization/readability blocker is cleared for the full 191-study gap
manifest. Full source-rendering coverage has therefore been rerun separately in
`source_rendering_full_coverage_manifest_20260609.csv` and
`SOURCE_RENDERING_FULL_COVERAGE_STATUS_20260609.md`. Model execution remains a
separate authorization gate.

## Safety Boundary

- No PDF file, source text, raw model transcript, human reference value, human
  adjudication rationale, or human-adjudicated source locator is committed.
- The committed checker CSVs contain study IDs, batch IDs, filename basenames,
  materialization/readability status, and counts only.
