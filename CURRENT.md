# CURRENT

Project: AI Adoption Meta-Analysis Methodology Strategy

This file is regenerated from `.longtable/current-session.json` and `.longtable/state.json`.

## Focus Now
- Current goal: Execute post-freeze Step 5 Paper B/C model/procedure validation from the frozen 213-study source-anchored reference standard while preserving leakage boundaries and caveats.
- Current blocker: A post-freeze 15-row S009/S010 beta/path exception-correction layer was created on 2026-06-11 without editing frozen reference files, but full-corpus M1-R remains blocked until the Step 5 scoring workflow explicitly consumes the layer. The layer excludes S009 raw-beta-confirmed contract caveats from the generic full-accuracy denominator, holds S009 FC-UB for manual source/reference adjudication, allows two S010 rows only under contract-aware converted-effect scoring, and excludes four S010 rows pending explicit structural path evidence or reference correction.
- Next action: Wire the beta/path exception-correction layer into the Step 5 scoring workflow or scorer wrapper, then verify that affected S009/S010 rows are excluded or contract-aware-scored before any larger M1-R shard is run or interpreted.
- Perspectives: reviewer, methods_critic, measurement_auditor, ethics_reviewer, voice_keeper, venue_strategist
- Disagreement: show_on_conflict

## Open Questions
- Should the next scorer-wrapper implementation only annotate/exclude affected beta/path rows, or should it also compute contract-aware converted-effect scoring for eligible S010 rows in the same pass?

## Restart Prompt
- "Continue after the 2026-06-11 beta/path exception-correction layer: full-corpus M1-R is still blocked. Next gate is wiring the layer into the Step 5 scoring workflow or scorer wrapper before any larger shard."

## Quick Start
- Open `codex` in this directory.
- A good first message is usually `lt explore: Should the next scorer-wrapper implementation only annotate/exclude affected beta/path rows, or should it also compute contract-aware converted-effect scoring for eligible S010 rows in the same pass?`.

## Evidence Rule
- External or current claims should carry a source link or be labeled as inference.