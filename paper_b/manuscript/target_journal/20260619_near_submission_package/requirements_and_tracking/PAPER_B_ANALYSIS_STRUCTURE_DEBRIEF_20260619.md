# Paper B Analysis Structure Debrief

Date: 2026-06-19

## One-sentence Answer

The 2,043-row M1-R result is not a replacement claim. It is the completed source-packet-required Step 5 evidence showing how the prespecified Codex GPT-5.5 workflow performs across denominator families, abstentions, and exception gates after the 213-study source-anchored reference was frozen.

## Analysis Structure

1. Raw human coder workbooks are preserved as read-only trace evidence.
2. Human-human disagreements are summarized before any model comparison.
3. Source-document adjudication creates the source-anchored human reference layer.
4. The reference layer is frozen and documented before Step 5.
5. Locked LLM outputs are evaluated against the reference by task family, not as one pooled corpus-wide denominator.
6. Cross-model disagreement, source-risk flags, human-disagreement traces, abstentions, and missing model rows are interpreted as review-triage evidence.
7. Downstream MASEM/TSSEM is reported only as a bounded diagnostic. Current defensible lane is core-6; broader core7/core8/full-10 probes do not support stronger all-construct or all-row SEM substitution claims.

## What the 2,043-row Full-corpus M1-R Result Brings

- It resolves the previous Step 5 coverage blocker: the full source-rendered corpus was run across nine locked shards.
- It provides denominator-family evidence for three task strata: direct/source-reported correlations, latent/source-flagged correlations, and converted beta/path effects.
- It exposes abstention behavior rather than hiding it inside a pooled score.
- It supplies a defensible RSM-style validation result when paired with explicit exception handling, model provenance, and public-code/public-data boundaries.
- It does not authorize model-vendor ranking, autonomous replacement, or all-row SEM stability claims.

## Full-corpus M1-R Results by Denominator Family

| family | rows_total | scored_rows | correct_rows | incorrect_scored_rows | abstention_rows | accuracy_scored_only | accuracy_all_scorable |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Latent/source-flagged r | 931 | 715 | 672 | 43 | 216 | 94.0% | 72.2% |
| Direct/source-reported r | 697 | 572 | 517 | 55 | 125 | 90.4% | 74.2% |
| Converted beta/path | 415 | 338 | 153 | 185 | 77 | 45.3% | 36.9% |

Interpretation: scored-only accuracy describes numeric agreement among rows where the model emitted a scorable value. All-scorable accuracy treats abstentions as incorrect workflow outcomes, which is the more conservative validation view for high-consequence extraction.

## RQ3 Triage Signal Summary

| signal | scope_n | flagged_n | review_needed_n | precision_review_needed | recall_review_needed | review_burden_share | baseline_review_needed_rate | precision_lift_vs_baseline |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| blank_behavior_family | 7859 | 6412 | 7809 | 1.000 | 0.821 | 0.816 | 0.994 | 1.006 |
| primary_not_scored | 7859 | 4335 | 7809 | 1.000 | 0.555 | 0.552 | 0.994 | 1.006 |
| primary_incorrect | 7859 | 3474 | 7809 | 1.000 | 0.445 | 0.442 | 0.994 | 1.006 |
| primary_abstention | 7859 | 979 | 7809 | 1.000 | 0.125 | 0.125 | 0.994 | 1.006 |
| all_available_models_abstained | 7859 | 832 | 7809 | 1.000 | 0.107 | 0.106 | 0.994 | 1.006 |
| source_or_trace_risk | 7859 | 601 | 7809 | 1.000 | 0.077 | 0.076 | 0.994 | 1.006 |
| human_disagreement_trace | 7859 | 467 | 7809 | 1.000 | 0.060 | 0.059 | 0.994 | 1.006 |
| cross_model_behavior_disagreement | 7859 | 6592 | 7809 | 0.999 | 0.843 | 0.839 | 0.994 | 1.005 |
| high_consequence_numeric | 7859 | 454 | 7809 | 0.993 | 0.058 | 0.058 | 0.994 | 1.000 |

Cross-model disagreement has high precision because the review-needed base rate is already extremely high. Its value is therefore not vendor ranking, but surfacing where the workflow should route attention together with source-risk and human-disagreement traces.

## MASEM/TSSEM Gate Summary

| construct_set | construct_count | required_pairs | covered_pairs | missing_pairs | complete_case_studies | identification_gate |
| --- | --- | --- | --- | --- | --- | --- |
| Core 6 legacy TSSEM | 6 | 15 | 15 |  | 16 | Bounded |
| Core 7 plus ATT | 7 | 21 | 21 |  | 3 | Bounded |
| Core 8 plus TRU | 8 | 28 | 28 |  | 1 | Bounded |
| Core 9 plus ANX | 9 | 36 | 35 | ANX-TRU | 0 | Not identified |
| Theory target 10 | 10 | 45 | 44 | ANX-TRU | 0 | Not identified |

## Figure Package

- Figure 1: `figure_1_paper_b_source_anchored_workflow_20260619.png`
- Figure 2: `figure_2_m1r_denominator_family_outcomes_20260619.png`
- Figure 3: `figure_3_rq3_review_triage_signals_20260619.png`
- Figure 4: `figure_4_masem_identification_gate_20260619.png`
