# OneDrive Root Flatten Release

Date: 2026-06-17

## Decision

The AI Adoption OneDrive library now uses the library root as the human-facing
canonical workspace. The previous `Meta/AI Adoption` wrapper was removed from
the active tree.

Canonical OneDrive root:

`/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents`

Canonical local Git root:

`/Users/newhosung/Academic/2026/AI Adoption Meta Analysis`

## Active OneDrive Folders

- `00_INDEX`
- `01_workbooks`
- `02_source_packages`
- `03_source_adjudication`
- `04_analysis_outputs`
- `05_manuscripts`
- `90_repository_mirror`
- `99_archive`

`AGENTS.md` and `CLAUDE.md` remain at the OneDrive root because they are
workspace-level agent instructions, not research-stage folders.

## Paper A/B Work Allocation Package

The active task-management package is now:

`00_INDEX/2026-06-17_Paper_A_B_work_allocation/`

It contains:

- `00_shared/`
- `R1/`
- `R2/`
- `R3/`
- `R4/`
- `99_archive/`

## Release Evidence

- Root flatten inventory: `00_INDEX/ROOT_FLATTEN_INVENTORY_20260617.csv`
- Root flatten move log: `00_INDEX/ROOT_FLATTEN_MOVED_FROM_20260617.csv`
- Root flatten inventory rows: 13,102
- Root flatten moved files: 13,101
- Work-allocation DOCX checksum matched across local repo, OneDrive shared
  package, and OneDrive repository mirror.
- DOCX integrity check passed with `unzip -t`.
- OneDrive repository mirror dry-run reported 0 files remaining to transfer.

## Boundary

Private PDFs, source packages, raw coder workbooks, raw LLM outputs, `.omx`,
and `.longtable` runtime state remain outside Git/public release unless a
future explicit release decision approves share-safe derivatives.
