# Paper A broader AI-candidate construct-support triage

Date: 2026-06-14

## Purpose

This gate reclassifies all possible AI/source-trace densification candidates by checking whether each candidate pair uses constructs already supported in the latest/frozen human reference for that study.

It does not add values to the matrix. It identifies which candidates deserve PDF-level numeric-cell review.

## Triage counts

- likely_false_positive_one_construct_not_human_supported: 408
- likely_false_positive_no_construct_human_supported: 41
- source_review_priority_both_constructs_human_supported: 15
- already_in_human_or_frozen_reference: 1

## Source-review priority candidates by study

- S048: 7
- S004: 6
- S072: 2

## Interpretation

Candidates in `source_review_priority_both_constructs_human_supported` are the only class that should move to detailed PDF/source numeric-cell extraction now.
Candidates with one or both constructs unsupported should not be added unless a source review explicitly reopens construct mapping.

## Outputs

- Full triage CSV: `paper_a_broader_ai_candidate_construct_support_triage_20260614.csv`
- Source-review priority CSV: `paper_a_broader_ai_candidate_source_review_priority_20260614.csv`
