# Paper A Mediator/Mechanism Feasibility Audit

Date: 2026-06-12

Input: `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_substitution_rerun_input_n_weighted_all_source_supported_20260612.csv`

Researcher correction: Trust, anxiety, and self-efficacy are not moderators. They are candidate mediator/mechanism constructs inside the MASEM path model.

## Feasibility rule

- `main_indirect_candidate`: a, b, and c paths each have at least 10 studies, and at least 5 studies contain both a and b paths.
- `sensitivity_indirect_candidate`: a and b paths each have at least 5 studies, and at least 3 studies contain both a and b paths.
- `theory_only_underpowered`: a and b paths each have at least 3 studies but overlap is too sparse for strong indirect-effect reporting.
- `not_identified_current_input`: current input does not support the proposed mechanism path.

## Path-level results

| Mediator | Path | a studies | b studies | c studies | a/b overlap | Status |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| ATT | PE -> ATT -> BI | 27 | 30 | 57 | 25 | main_indirect_candidate |
| ATT | EE -> ATT -> BI | 26 | 30 | 54 | 24 | main_indirect_candidate |
| ATT | SI -> ATT -> BI | 12 | 30 | 39 | 12 | main_indirect_candidate |
| ATT | FC -> ATT -> BI | 10 | 30 | 36 | 9 | main_indirect_candidate |
| SE | FC -> SE -> BI | 6 | 9 | 36 | 6 | sensitivity_indirect_candidate |
| SE | EE -> SE -> BI | 7 | 9 | 54 | 6 | sensitivity_indirect_candidate |
| SE | PE -> SE -> BI | 15 | 9 | 57 | 7 | sensitivity_indirect_candidate |
| SE | SI -> SE -> BI | 6 | 9 | 39 | 5 | sensitivity_indirect_candidate |
| SE | FC -> SE -> ATT | 6 | 5 | 10 | 2 | theory_only_underpowered |
| SE | EE -> SE -> ATT | 7 | 5 | 26 | 3 | sensitivity_indirect_candidate |
| SE | PE -> SE -> ATT | 15 | 5 | 27 | 4 | sensitivity_indirect_candidate |
| TRU | PE -> TRU -> BI | 12 | 12 | 57 | 10 | main_indirect_candidate |
| TRU | EE -> TRU -> BI | 10 | 12 | 54 | 10 | main_indirect_candidate |
| TRU | SI -> TRU -> BI | 9 | 12 | 39 | 9 | sensitivity_indirect_candidate |
| TRU | FC -> TRU -> BI | 4 | 12 | 36 | 4 | theory_only_underpowered |
| TRU | ATT -> TRU -> BI | 2 | 12 | 30 | 2 | not_identified_current_input |
| TRU | SE -> TRU -> BI | 1 | 12 | 9 | 0 | not_identified_current_input |
| ANX | SE -> ANX -> BI | 2 | 3 | 9 | 1 | not_identified_current_input |
| ANX | FC -> ANX -> BI | 2 | 3 | 36 | 1 | not_identified_current_input |
| ANX | EE -> ANX -> BI | 3 | 3 | 54 | 2 | theory_only_underpowered |
| ANX | PE -> ANX -> BI | 4 | 3 | 57 | 2 | theory_only_underpowered |
| ANX | SE -> ANX -> ATT | 2 | 6 | 5 | 1 | not_identified_current_input |
| ANX | FC -> ANX -> ATT | 2 | 6 | 10 | 2 | not_identified_current_input |
| ANX | EE -> ANX -> ATT | 3 | 6 | 26 | 3 | theory_only_underpowered |
| ANX | PE -> ANX -> ATT | 4 | 6 | 27 | 3 | theory_only_underpowered |

## Interpretation

Attitude remains the strongest standard mediator in the current Paper A MASEM logic if its a/b paths clear coverage in the table above.

Self-efficacy, trust, and anxiety should be tested as theory-specified mechanism constructs only where the path-level audit supports both the upstream a path and downstream b path. If the full indirect path is sparse, the manuscript should describe the construct as a theoretically motivated antecedent/mechanism candidate rather than claim a confirmed mediation effect.

The next analytic step is not another moderator table. It is a Stage 2 path-model specification that includes candidate indirect effects for feasible mechanism paths and labels underpowered mechanisms as sensitivity or theory-only.

## Output files

- `paper_a_pair_coverage_for_mediation_20260612.csv`
- `paper_a_mediator_path_feasibility_20260612.csv`
- `paper_a_mediator_feasibility_summary_20260612.csv`
