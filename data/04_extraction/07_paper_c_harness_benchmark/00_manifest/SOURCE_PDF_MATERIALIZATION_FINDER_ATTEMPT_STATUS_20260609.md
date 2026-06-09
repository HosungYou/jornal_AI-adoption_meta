# Source PDF Materialization Finder Attempt Status

Date: 2026-06-09

Status: partial local materialization achieved, but full-corpus source rendering
remains blocked. This artifact does not authorize any additional model run,
scoring rerun, accuracy result, or smaller-scope claim.

## Action Taken

- Started the local OneDrive application and confirmed OneDrive/File Provider
  processes were available.
- Used Finder on the main `Meta/AI Adoption/PDFs` archive folder and clicked
  the OneDrive/Finder "Not downloaded" control for the selected `PDFs` folder.
- Reran source PDF materialization checks with source-text-safe outputs only.
- Did not commit PDF files, source text, raw model transcripts, human reference
  values, human adjudication rationales, or human-adjudicated source locators.

## Result Snapshot

Current share-safe full snapshot:
`source_pdf_materialization_check_full_after_finder_click_20260609.csv`.

| Check | Result |
|---|---:|
| Gap-manifest studies checked | 191 |
| Gap-manifest target rows checked | 2,025 |
| `materialized_text_extractable` studies | 16 |
| `materialized_text_extractable` target rows | 376 |
| `not_materialized_or_read_timeout` studies | 175 |
| `not_materialized_or_read_timeout` target rows | 1,649 |
| Batch 01 materialized studies | 12 / 20 |
| Batch 01 materialized target rows | 317 / 492 |

Materialized studies in the full snapshot:
`S121`, `S015`, `S057`, `S138`, `S176`, `S016`, `S025`, `S035`,
`S048`, `S055`, `S086`, `S164`, `S006`, `S198`, `S200`, `S114`.

Batch 01 studies still blocked after the Finder attempt:
`S157`, `S004`, `S030`, `S036`, `S088`, `S173`, `S190`, `S191`.

## Interpretation

The Finder/OneDrive action produced real progress: 16 previously blocked
studies now have text-extractable local PDFs. However, the main archive folder
did not remain in a stable keep-local state (`isKeepDownloaded` remained off and
the later folder state no longer reported recursive download), so the full
191-study materialization blocker is not resolved.

Full-corpus `M1-R`, `M1-P`, `M2-R`, and optional `M3-R` remain blocked. The
current partial materialization is sufficient for additional source-packet
pipeline testing only if a smaller-scope smoke is explicitly authorized; it is
not sufficient for full-corpus model/procedure execution or accuracy claims.

## Next Gate

Continue OneDrive/Finder materialization until the full checker reports
text-extractable PDFs for the intended target scope. The highest-yield next unit
is the remaining Batch 01 set listed above, followed by Batch 02.
