# Paper A Stage 2 Indirect-Effect Specification

Date: 2026-06-12

Source audit: `data/04_extraction/05_llm_masem_substitution/results/paper_a_mediator_feasibility_20260612/paper_a_mediator_path_feasibility_20260612.csv`

## Specification rule

- `main_indirect_effect`: include in primary Stage 2 reporting if model convergence and fit are acceptable.
- `sensitivity_indirect_effect`: estimate/report only as sensitivity or mechanism evidence.
- `theory_specified_underpowered_no_confirmed_mediation_claim`: keep in theory narrative but do not claim confirmed mediation.
- `exclude_from_indirect_effect_claim_current_input`: do not report as an indirect effect from current data.

## Indirect-effect candidates

| Role | Mediator | Path | a studies | b studies | a/b overlap | Claim boundary |
| --- | --- | --- | ---: | ---: | ---: | --- |
| main_indirect_effect | ATT | PE -> ATT -> BI | 27 | 30 | 25 | Eligible for primary Stage 2 indirect-effect reporting if the structural model converges. |
| main_indirect_effect | ATT | EE -> ATT -> BI | 26 | 30 | 24 | Eligible for primary Stage 2 indirect-effect reporting if the structural model converges. |
| main_indirect_effect | ATT | SI -> ATT -> BI | 12 | 30 | 12 | Eligible for primary Stage 2 indirect-effect reporting if the structural model converges. |
| main_indirect_effect | ATT | FC -> ATT -> BI | 10 | 30 | 9 | Eligible for primary Stage 2 indirect-effect reporting if the structural model converges. |
| main_indirect_effect | TRU | PE -> TRU -> BI | 12 | 12 | 10 | Eligible for primary Stage 2 indirect-effect reporting if the structural model converges. |
| main_indirect_effect | TRU | EE -> TRU -> BI | 10 | 12 | 10 | Eligible for primary Stage 2 indirect-effect reporting if the structural model converges. |
| sensitivity_indirect_effect | SE | PE -> SE -> BI | 15 | 9 | 7 | Report only as sensitivity/mechanism evidence; do not overstate as confirmed primary mediation. |
| sensitivity_indirect_effect | SE | FC -> SE -> BI | 6 | 9 | 6 | Report only as sensitivity/mechanism evidence; do not overstate as confirmed primary mediation. |
| sensitivity_indirect_effect | SE | EE -> SE -> BI | 7 | 9 | 6 | Report only as sensitivity/mechanism evidence; do not overstate as confirmed primary mediation. |
| sensitivity_indirect_effect | SE | SI -> SE -> BI | 6 | 9 | 5 | Report only as sensitivity/mechanism evidence; do not overstate as confirmed primary mediation. |
| sensitivity_indirect_effect | SE | PE -> SE -> ATT | 15 | 5 | 4 | Report only as sensitivity/mechanism evidence; do not overstate as confirmed primary mediation. |
| sensitivity_indirect_effect | SE | EE -> SE -> ATT | 7 | 5 | 3 | Report only as sensitivity/mechanism evidence; do not overstate as confirmed primary mediation. |
| sensitivity_indirect_effect | TRU | SI -> TRU -> BI | 9 | 12 | 9 | Report only as sensitivity/mechanism evidence; do not overstate as confirmed primary mediation. |
| theory_specified_underpowered_no_confirmed_mediation_claim | ANX | EE -> ANX -> ATT | 3 | 6 | 3 | Mention as theory-specified but underpowered; no confirmed mediation claim. |
| theory_specified_underpowered_no_confirmed_mediation_claim | ANX | PE -> ANX -> ATT | 4 | 6 | 3 | Mention as theory-specified but underpowered; no confirmed mediation claim. |
| theory_specified_underpowered_no_confirmed_mediation_claim | ANX | EE -> ANX -> BI | 3 | 3 | 2 | Mention as theory-specified but underpowered; no confirmed mediation claim. |
| theory_specified_underpowered_no_confirmed_mediation_claim | ANX | PE -> ANX -> BI | 4 | 3 | 2 | Mention as theory-specified but underpowered; no confirmed mediation claim. |
| theory_specified_underpowered_no_confirmed_mediation_claim | SE | FC -> SE -> ATT | 6 | 5 | 2 | Mention as theory-specified but underpowered; no confirmed mediation claim. |
| theory_specified_underpowered_no_confirmed_mediation_claim | TRU | FC -> TRU -> BI | 4 | 12 | 4 | Mention as theory-specified but underpowered; no confirmed mediation claim. |
| exclude_from_indirect_effect_claim_current_input | ANX | FC -> ANX -> ATT | 2 | 6 | 2 | Do not report as indirect effect from current input. |
| exclude_from_indirect_effect_claim_current_input | ANX | SE -> ANX -> BI | 2 | 3 | 1 | Do not report as indirect effect from current input. |
| exclude_from_indirect_effect_claim_current_input | ANX | FC -> ANX -> BI | 2 | 3 | 1 | Do not report as indirect effect from current input. |
| exclude_from_indirect_effect_claim_current_input | ANX | SE -> ANX -> ATT | 2 | 6 | 1 | Do not report as indirect effect from current input. |
| exclude_from_indirect_effect_claim_current_input | TRU | ATT -> TRU -> BI | 2 | 12 | 2 | Do not report as indirect effect from current input. |
| exclude_from_indirect_effect_claim_current_input | TRU | SE -> TRU -> BI | 1 | 12 | 0 | Do not report as indirect effect from current input. |

## Manuscript implication

Paper A should report attitude mediation as the strongest standard TAM mechanism. Trust mediation can be tested as an AI-specific mechanism for `PE -> TRU -> BI` and `EE -> TRU -> BI`, with `SI -> TRU -> BI` as sensitivity. Self-efficacy paths should be sensitivity-level. Anxiety paths are theory-specified but underpowered or not identified in the current input.
