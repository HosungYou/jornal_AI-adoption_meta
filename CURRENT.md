# CURRENT

Project: AI Adoption Meta-Analysis Methodology Strategy

This file is regenerated from `.longtable/current-session.json` and `.longtable/state.json`.

## Focus Now
- Current goal: Execute post-freeze Step 5 Paper B/C model/procedure validation from the frozen 213-study source-anchored reference standard while preserving leakage boundaries and caveats.
- Current blocker: Source PDF materialization remains blocked after CLI route inspection and full checker rerun: the current local command surface did not execute OneDrive MarkPinned/pin materialization, and all 191 gap studies / 2,025 target rows still return not_materialized_or_read_timeout. Full-corpus M1-R/M1-P/M2-R remains blocked.
- Next action: Use OneDrive/Finder local materialization such as Always Keep on This Device for the archive folder or the materialization batches, then rerun check_source_pdf_materialization.py and the full source-rendering coverage audit. Only after clean intended-scope coverage should a balanced source-rendered smoke be run.
- Perspectives: reviewer, methods_critic, measurement_auditor, ethics_reviewer, voice_keeper, venue_strategist
- Disagreement: show_on_conflict

## Open Questions
- Can the OneDrive archive folder or materialization batches be marked Always Keep on This Device and downloaded locally, so the checker can be rerun to confirm intended-scope source coverage?

## Restart Prompt
- "Continue after the full source PDF materialization recheck. The checker output source_pdf_materialization_check_full_20260609.csv has 191/191 not_materialized_or_read_timeout; do not run full-corpus M1-R/M1-P/M2-R until OneDrive/Finder local materialization is completed and checker/source-rendering coverage are clean."

## Quick Start
- Open `codex` in this directory.
- A good first message is usually `lt explore: Can the OneDrive archive folder or materialization batches be marked Always Keep on This Device and downloaded locally, so the checker can be rerun to confirm intended-scope source coverage?`.

## Evidence Rule
- External or current claims should carry a source link or be labeled as inference.