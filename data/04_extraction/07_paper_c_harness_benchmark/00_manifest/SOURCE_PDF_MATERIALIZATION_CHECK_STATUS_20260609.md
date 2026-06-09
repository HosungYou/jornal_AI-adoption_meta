# Source PDF Materialization Check Status

Date: 2026-06-09

Status: partial local materialization achieved after a Finder/OneDrive
follow-up, but full-scope local materialization/readability remains blocked.
This artifact does not authorize any additional model run, scoring rerun,
accuracy result, or smaller-scope claim.

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

## Next Gate

Continue targeted materialization for Batches 03-04, then rerun the relevant
batch checker. For example:

```bash
python3 scripts/llm_scoring_20260606/check_source_pdf_materialization.py \
  --batch-id PDFMAT-20260609-03 \
  --output data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_pdf_materialization_check_batch03_after_targeted_materialization_20260609.csv
```

Only if the checker reports local text-extractable PDFs for the intended scope
should the full source-rendering coverage audit be rerun. A balanced
source-rendered smoke remains ineligible until source rendering coverage is
clean for the intended target scope.

## Safety Boundary

- No PDF file, source text, raw model transcript, human reference value, human
  adjudication rationale, or human-adjudicated source locator is committed.
- The committed checker CSVs contain study IDs, batch IDs, filename basenames,
  materialization/readability status, and counts only.
