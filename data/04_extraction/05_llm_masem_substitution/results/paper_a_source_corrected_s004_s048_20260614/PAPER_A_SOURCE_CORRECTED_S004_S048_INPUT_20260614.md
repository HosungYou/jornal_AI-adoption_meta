# Paper A S004/S048 source-corrected diagnostic input

Date: 2026-06-14

## Decision encoded

- `PKC -> SE` is rejected for S004.
- S004 PKC-derived SE rows are excluded from the diagnostic corrected input.
- S048 Table 2 is accepted as Pearson correlation evidence with `INT -> BI` and `USE -> UB`.
- This is not a frozen-reference edit and not a workbook overwrite.

## Diagnostic input changes

| action | rows |
| --- | ---: |
| add_priority_candidate | 7 |
| add_source_visible_non_candidate | 1 |
| correct_existing_frozen_value | 16 |
| keep_existing_frozen_value | 25 |
| reject_priority_candidate_unapproved_mapping | 6 |
| remove_unapproved_or_source_unsupported_pair | 1 |

## Coverage before and after

| Dataset | Route | Required pairs | Observed pairs | Missing pairs | Numeric studies | Complete-case studies | Max pairs in one study | Min pair k |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| baseline | paper_a_full10_theory_target | 45 | 44 | 1 | 74 | 0 | 28 | 1 |
| baseline | paper_a_trust6_mechanism | 15 | 15 | 0 | 72 | 6 | 15 | 8 |
| baseline | paper_a_core7_att_mediation | 21 | 21 | 0 | 71 | 3 | 21 | 10 |
| corrected | paper_a_full10_theory_target | 45 | 44 | 1 | 75 | 0 | 28 | 1 |
| corrected | paper_a_trust6_mechanism | 15 | 15 | 0 | 73 | 7 | 15 | 9 |
| corrected | paper_a_core7_att_mediation | 21 | 21 | 0 | 72 | 4 | 21 | 11 |

## Boundary

Use this input for diagnostic reruns only. If the rerun materially improves Paper A feasibility, the same S004/S048 corrections still need a final human source-adjudication promotion step before they become the canonical Paper A analytic input.

## Output files

- `/Users/newhosung/Academic/2026/AI Adoption Meta Analysis/data/04_extraction/05_llm_masem_substitution/results/paper_a_source_corrected_s004_s048_20260614/paper_a_source_corrected_s004_s048_input_20260614.csv`
- `/Users/newhosung/Academic/2026/AI Adoption Meta Analysis/data/04_extraction/05_llm_masem_substitution/results/paper_a_source_corrected_s004_s048_20260614/paper_a_source_corrected_s004_s048_changelog_20260614.csv`
- `/Users/newhosung/Academic/2026/AI Adoption Meta Analysis/data/04_extraction/05_llm_masem_substitution/results/paper_a_source_corrected_s004_s048_20260614/paper_a_source_corrected_s004_s048_coverage_summary_20260614.csv`
