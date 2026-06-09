# Source PDF Materialization Batch Follow-up Status

Date: 2026-06-09

Status: Batch 02 is locally text-extractable, Batch 01 is mostly
text-extractable, and Batches 03-04 remain mostly blocked. This artifact does
not authorize any additional model run, scoring rerun, accuracy result, or
smaller-scope claim.

## Action Taken

- Confirmed OneDrive was running.
- Reran the share-safe materialization checker for Batches 01-04.
- Attempted to execute OneDrive `MarkPinned` through `fileproviderctl evaluate`
  for the remaining Batch 01 blockers. The local command surface rejected that
  custom action as invalid and did not pin or download those files.
- Did not commit PDF files, source text, raw model transcripts, human reference
  values, human adjudication rationales, or human-adjudicated source locators.

## Result Snapshot

| Batch | Studies checked | Text-extractable studies | Text-extractable rows | Still blocked studies | Still blocked rows |
|---|---:|---:|---:|---:|---:|
| Batch 01 | 20 | 16 | 401 | 4 | 91 |
| Batch 02 | 20 | 20 | 306 | 0 | 0 |
| Batch 03 | 20 | 2 | 30 | 18 | 270 |
| Batch 04 | 20 | 1 | 14 | 19 | 194 |
| Batches 01-04 combined | 80 | 39 | 751 | 41 | 555 |

Remaining Batch 01 blockers:
`S157`, `S036`, `S088`, `S190`.

Batch 03 and Batch 04 still have broad materialization/read-timeout blockers.
This is batch-focused evidence only; the full 191-study gap checker was not
rerun in this follow-up.

## Interpretation

The OneDrive background/Finder materialization state improved after the prior
folder-level attempt. Batch 02 is now clean, and Batch 01 improved from 12/20 to
16/20 studies. However, four high-yield Batch 01 studies still block 91 target
rows, and the next two batches remain mostly unavailable as local prompt inputs.

Full-corpus `M1-R`, `M1-P`, `M2-R`, and optional `M3-R` remain blocked. The next
defensible unit is targeted local materialization of the four remaining Batch 01
PDFs, followed by Batch 03 and Batch 04 materialization.

## Evidence Files

- `source_pdf_materialization_check_batch01_followup_20260609.csv`
- `source_pdf_materialization_check_batch02_followup_20260609.csv`
- `source_pdf_materialization_check_batch03_followup_20260609.csv`
- `source_pdf_materialization_check_batch04_followup_20260609.csv`
