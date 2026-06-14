# Paper A AI-Candidate-Only Source Trace Protocol

Date: 2026-06-14

## Researcher decision

The researcher selected the candidate-only route: AI may generate source-trace results for review, but the researcher decides whether any row can enter a supplemental Paper A input.

## Paper B boundary

This protocol does not modify the Paper B `source-anchored adjudicated human reference standard`. It also does not treat AI output as equal to independent human coding. AI output is a source-trace/review aid only.

Allowed AI output statuses:

- `ai_candidate_only_existing_human_value_under_review`
- `ai_candidate_only_missing_pair_no_value_added`

Not allowed without human confirmation:

- adding an AI-only row to Paper A analytic input
- changing the frozen human reference
- treating a missing-pair trace as a source-confirmed value
- reporting AI-only full10 densification as final MASEM evidence

## Generated source-trace packet

The candidate-only packet is stored under:

`data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/`

Main files:

- `PAPER_A_AI_CANDIDATE_SOURCE_TRACE_PACKET_20260614.md`
- `paper_a_ai_candidate_source_trace_existing_human_values_20260614.csv`
- `paper_a_ai_candidate_full10_densification_trace_20260614.csv`
- `paper_a_human_confirmation_template_from_ai_trace_20260614.csv`
- `paper_a_ai_candidate_source_trace_summary_20260614.csv`

## Required human decision fields

Before a row can be promoted, the researcher or designated human reviewer should fill:

- `human_decision`
- `human_decision_date`
- `human_reviewer`
- `final_value_if_confirmed`
- `evidence_type`
- `source_location_confirmed`
- `decision_rationale`
- `promote_to_supplemental_input`

## Next valid step

Review the candidate-only source-trace packet. Only after human confirmation should a separate script build `paper_a_human_confirmed_supplemental_densification_*.csv`.
