# Source-Anchored Adjudicated Human Reference

This folder documents the frozen adjudicated human reference standard used for
Paper B LLM evaluation and Paper A MASEM-ready extraction.

## Current Status

The 2026-06-05 Paper1/Paper2 source-anchored tiered reference freeze packet is
prepared. It freezes source-adjudicated decision logs, checksum evidence, and
task-unit denominator boundaries for downstream Paper2 LLM scoring.

Step 5 LLM comparison may use this packet only through locked model outputs and
denominator-family scoring. Do not treat the 8,783 Paper2 task units as one
overall accuracy denominator, and do not describe the reference as perfect
ground truth.

## Terminology

Use `source-anchored adjudicated human reference standard`, not `gold standard`,
for current protocol documents.

## Required Contents Before Analysis

- Freeze date and commit hash: freeze date is 2026-06-05; Git commit is filled
  by the commit that publishes this packet.
- Source file list and excluded private/raw files: see
  `CHECKSUMS_TIERED_FREEZE_20260605.csv` and
  `workbook_mutation_manifest_20260605.csv`.
- Discrepancy resolution log: see `source_adjudication_decisions_20260605.csv`.
- Field-level decision rules applied during adjudication: see
  `paper2_reference_standard_freeze_note.md`.
- Post-freeze corrections must be added as dated entries with reason and
  reviewer before any affected scoring rerun.

The reference standard is the best available expert interpretation of the source
documents after independent coding and adjudication. It is not described as
perfect ground truth.
