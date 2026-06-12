# Paper2/Paper A MASEM Matrix Identification Audit

Date: 2026-06-12

## Boundary

This audit is run after PDF-recovered N completion. It checks matrix
coverage and complete-case identification only; it does not estimate final
TSSEM/OSMASEM paths or authorize substantive SEM claims.

## Result

- Input rows audited: 796
- Studies represented: 74
- Target construct-pair coverage: 44/45
- Rows with numeric N: 796/796
- Core-6 complete-case studies: 16
- Full 10-construct complete-case studies: 0
- Full 10 missing pairs: ANX-TRU

## Construct-Set Identification Gates

| construct_set | construct_count | required_pairs | covered_pairs | missing_pairs | complete_case_studies | identification_gate |
| --- | --- | --- | --- | --- | --- | --- |
| core6_legacy_tssem_diagnostic | 6 | 15 | 15 |  | 16 | eligible_for_bounded_tssem_diagnostic |
| core7_add_att | 7 | 21 | 21 |  | 3 | eligible_for_bounded_tssem_diagnostic |
| core8_add_tru | 8 | 28 | 28 |  | 1 | eligible_for_bounded_tssem_diagnostic |
| core9_add_anx | 9 | 36 | 35 | ANX-TRU | 0 | not_identified_as_complete_case_model |
| theory_target_10 | 10 | 45 | 44 | ANX-TRU | 0 | not_identified_as_complete_case_model |

## Weakest Pair Coverage

| construct_pair | rows | studies | studies_with_numeric_n | gate_status |
| --- | --- | --- | --- | --- |
| ANX-TRU | 0 | 0 | 0 | no_effect_rows |
| SE-TRU | 1 | 1 | 1 | n_ready_pairwise |
| ANX-FC | 2 | 2 | 2 | n_ready_pairwise |
| ANX-SE | 2 | 2 | 2 | n_ready_pairwise |
| ANX-UB | 2 | 2 | 2 | n_ready_pairwise |
| ATT-TRU | 2 | 2 | 2 | n_ready_pairwise |
| ANX-BI | 3 | 3 | 3 | n_ready_pairwise |
| ANX-EE | 3 | 3 | 3 | n_ready_pairwise |
| ANX-SI | 3 | 3 | 3 | n_ready_pairwise |
| ANX-PE | 4 | 4 | 4 | n_ready_pairwise |
| FC-TRU | 4 | 4 | 4 | n_ready_pairwise |
| ATT-SE | 5 | 5 | 5 | n_ready_pairwise |

## Gate Interpretation

- N coverage is complete in this derived input.
- The theory target still lacks `ANX-TRU` in the legacy primary direct-r matrix.
- The bounded core-6 set remains the defensible immediate TSSEM diagnostic lane.
- Full 10-construct claims require resolving the ANX-TRU corpus/source-type boundary or explicitly reducing the model.

## Outputs

- `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_matrix_pair_coverage_after_n_override_20260612.csv`
- `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_matrix_construct_set_completeness_20260612.csv`
- `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_matrix_study_pair_coverage_20260612.csv`
