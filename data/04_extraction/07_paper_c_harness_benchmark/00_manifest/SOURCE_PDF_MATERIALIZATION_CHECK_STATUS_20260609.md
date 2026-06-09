# Source PDF Materialization Check Status

Date: 2026-06-09

Status: local materialization/readability remains blocked. This artifact does
not authorize any additional model run, scoring rerun, accuracy result, or
smaller-scope claim.

## What Was Checked

- Materialization gap manifest scope: 191 studies / 2,025 target rows.
- Full checker output: `source_pdf_materialization_check_full_20260609.csv`.
- Batch 01 checker output: `source_pdf_materialization_check_batch01_20260609.csv`.
- One-file CLI materialization route: attempted with `fileproviderctl materialize`; current system command surface returned usage output rather than materializing the file.
- OneDrive File Provider inspection: the provider exposes `MarkPinned` / `MarkUnpinned` as File Provider context actions, but the available `fileproviderctl evaluate` command does not execute those custom actions.

## Results

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

## Next Gate

After the OneDrive files are marked to stay local and finish downloading, rerun:

```bash
python3 scripts/llm_scoring_20260606/check_source_pdf_materialization.py \
  --output data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_pdf_materialization_check_full_20260609.csv
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
