# Paper A AI-Candidate Source Trace Packet

Date: 2026-06-14

## LongTable decision boundary

Decision selected by researcher: `candidate_only_now`.

AI traces are review evidence only. They do not modify the Paper A analytic input, the Paper B frozen human reference, or any source-anchored adjudicated value. A row can be promoted only after human confirmation in the confirmation template.

## Existing human-coded values under source review

Rows traced: 727

| AI trace status | Rows |
| --- | ---: |
| `ai_trace_auto_value_visible_exact` | 609 |
| `ai_trace_possible_value_visible_broad_match` | 118 |

## Full10 missing-pair densification trace

Missing-pair rows traced: 574
Studies traced: 25

| AI trace status | Rows |
| --- | ---: |
| `likely_not_densifiable_construct_pair_not_visible` | 2 |
| `likely_not_densifiable_one_construct_not_visible` | 107 |
| `possible_densification_source_review_candidate` | 465 |

## Files for researcher review

- `paper_a_ai_candidate_source_trace_existing_human_values_20260614.csv`
- `paper_a_ai_candidate_full10_densification_trace_20260614.csv`
- `paper_a_human_confirmation_template_from_ai_trace_20260614.csv`
- `paper_a_ai_candidate_source_trace_summary_20260614.csv`

## How to use this packet

1. Use the existing-values trace to decide whether a currently coded value is source-confirmed, source-corrected, excluded, or still ambiguous.
2. Use the densification trace to decide whether a missing full10 pair has enough source evidence to justify manual table review.
3. Record human decisions in the confirmation template. Keep `promote_to_supplemental_input=no` unless you personally confirm the source value and evidence type.
4. Only human-confirmed rows may be used to build a supplemental densification input or rerun Paper A MASEM.
