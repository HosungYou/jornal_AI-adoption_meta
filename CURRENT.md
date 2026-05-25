# CURRENT

Project: AI Adoption Meta-Analysis Methodology Strategy

This file is regenerated from `.longtable/current-session.json` and `.longtable/state.json`.

## Focus Now
- Current goal: Phase 1+2 전체 213-study coding disagreement 산출물을 기준으로 source-anchored reference standard freeze 전까지 Paper A/B/C의 분석 가능성과 문서화 순서를 구조화한다.
- Current blocker: Combined Phase 1+2 pre-adjudication queues are generated, but the source-anchored adjudicated human reference standard is not frozen. S195/S206 duplicate-source issue와 S014/S021/S056/S092/S121/S202 review-source decisions가 남아 있고, Paper C의 최종 model set, procedure contrast, repeated-run budget도 고정해야 한다.
- Next action: Start source-document adjudication from `combined_correlation_review_queue_20260525.csv`, resolve duplicate/source-review studies, then freeze the human reference before writing final LLM or MASEM result claims.
- Perspectives: reviewer, methods_critic, measurement_auditor, ethics_reviewer, voice_keeper, venue_strategist
- Disagreement: show_on_conflict

## Open Questions
- Should S014 indirect PLS-SEM effects through perceived risk be retained, transformed, or excluded from the MASEM-ready reference?
- How should S195/S206 be resolved as duplicate source records with the same DOI/PDF before reference freeze?
- Which versioned models, procedure/harness conditions, and repeated-run stability subset should Paper C lock before final benchmark runs?

## Restart Prompt
- "I want to continue Phase 1+2 source adjudication and Paper A/B/C structuring. The unresolved blocker is that the combined 213-study disagreement queues are prepared, but the source-anchored adjudicated human reference standard is not frozen yet."

## Quick Start
- Open `codex` in this directory.
- A good first message is usually `lt explore: How should we adjudicate S014, S195/S206, and the remaining review-source studies from the combined queue before freezing the human reference?`.

## Evidence Rule
- External or current claims should carry a source link or be labeled as inference.
