# CURRENT

Project: AI Adoption Meta-Analysis Methodology Strategy

This file is regenerated from `.longtable/current-session.json` and `.longtable/state.json`.

## Focus Now
- Current goal: Execute post-freeze Step 5 Paper B/C model/procedure validation from the frozen 213-study source-anchored reference standard while preserving leakage boundaries and caveats.
- Current blocker: M1-R-SOURCE-SMOKE-TABLE-RETRIEVAL beta/path contract review completed on 2026-06-11. Full-corpus M1-R remains blocked by beta/path contract issues rather than source materialization: v4 path-direction metadata treated construct-pair order as source direction for several S009/S010 rows; S010 raw beta recovery is being scored against Peterson-Brown converted reference values; and S009 has rows labeled beta_converted_peterson_brown that behave like raw beta plus one unresolved FC-UB directed-value mismatch. The current 25-row smoke remains diagnostic only and cannot support accuracy, model-comparison, or MASEM substitution claims.
- Next action: Prepare a leakage-safe M1-R-BETA-PATH-CONTRACT-PROBE before any larger M1-R execution: use source-directed path metadata, separate raw source beta/path coefficients from Peterson-Brown converted effect-size values, reject IPMA/importance/total/indirect-effect tables as path evidence, and keep S009 FC-UB/reference-contract caveats explicit.
- Perspectives: reviewer, methods_critic, measurement_auditor, ethics_reviewer, voice_keeper, venue_strategist
- Disagreement: show_on_conflict

## Open Questions
- What leakage-safe output schema and scoring patch should be used for the M1-R beta/path contract probe?

## Restart Prompt
- "Continue after the 2026-06-11 beta/path contract review: full-corpus M1-R is still blocked, not by source materialization but by S009/S010 beta/path contract issues. Next gate is a leakage-safe M1-R-BETA-PATH-CONTRACT-PROBE with source-directed paths and separate raw-beta versus converted-effect fields."

## Quick Start
- Open `codex` in this directory.
- A good first message is usually `lt explore: What leakage-safe output schema and scoring patch should be used for the M1-R beta/path contract probe?`.

## Evidence Rule
- External or current claims should carry a source link or be labeled as inference.