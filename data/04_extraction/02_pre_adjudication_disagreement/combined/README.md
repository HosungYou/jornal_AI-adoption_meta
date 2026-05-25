# Combined Phase 1+2 Pre-Adjudication Disagreement

Generated: 2026-05-25

These outputs combine Phase 1 Pair A/B and Phase 2 Pair C/D human-coder values for the full 213-study Paper B validation corpus.

- Phase 1: Pair A (R1+R2) and Pair B (R3+R4), 100 studies.
- Phase 2: Pair C (R1+R4) and Pair D (R2+R3), 113 studies.
- Phase 0 calibration rows and historical `Phase 2: Single` rows in the Phase 1 workbooks are excluded.

## Derived Files

- `derived/combined_coding_manifest_20260525.csv`: coder workbook coverage by phase and pair.
- `derived/combined_coder_values_long_20260525.csv`: all nonempty metadata and correlation coding values used for pre-adjudication review.
- `derived/combined_pairwise_disagreement_long_20260525.csv`: metadata and correlation disagreement rows.
- `derived/combined_pairwise_disagreement_summary_20260525.csv`: counts by phase, pair, field family, and mismatch type.
- `derived/combined_study_review_queue_20260525.csv`: all study-level review rows for meetings, including metadata-only differences.
- `derived/combined_correlation_review_queue_20260525.csv`: meeting-first queue for correlation/status/source-review issues, excluding metadata-only differences.

These are pre-adjudication artifacts. They identify where human coders differ before source-document adjudication. They are not the source-anchored adjudicated human reference standard.