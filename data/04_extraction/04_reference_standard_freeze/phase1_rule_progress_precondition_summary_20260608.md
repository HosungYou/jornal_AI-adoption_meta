# Phase 1 Rule/Progress Precondition Plan

Date: 2026-06-08

Status: planning/precondition artifact only. This is not a full-corpus freeze and does not start Step 5.

## Outputs

- `phase1_rule_progress_precondition_plan_20260608.csv`

## Counts

- `row_filter_source_audit`: 5
- `row_filter_source_type_audit`: 2
- `source_value_audit`: 3

## Studies

- `S005`: row_filter_source_audit - Apply logged rule: exclude JOY and do not map CON to FC; source-check retained rows before draft.
- `S011`: row_filter_source_audit - Apply logged rule: keep structural TAM paths only; exclude TTF paths from FC mapping.
- `S044`: row_filter_source_audit - Apply logged rule: map GAAIS Positive Attitudes to ATT; do not average negative attitudes into primary ATT.
- `S079`: row_filter_source_type_audit - Apply logged rule: relevant effects are path coefficients; decide retained row/status handling under source-type rules.
- `S087`: row_filter_source_audit - Apply logged rule: exclude Satisfaction from ATT after 2026-04-29 amendment.
- `S166`: row_filter_source_type_audit - HTMT/structural-path case; audit source type and beta-converted target paths before retention.
- `S187`: row_filter_source_audit - Apply logged rule: map stress/anxious wording to ANX with traceability flag; source-check affected rows.
- `S223`: source_value_audit - R1-coded value accepted in log; row set still needs source/value confirmation.
- `S086`: source_value_audit - Progress-only case; source-value audit required before any freeze-layer row creation.
- `S168`: source_value_audit - Progress-only case; source-value audit required before any freeze-layer row creation.

S074 is already drafted with an ANX/AXT caveat and is not part of this remaining ten-study queue.
