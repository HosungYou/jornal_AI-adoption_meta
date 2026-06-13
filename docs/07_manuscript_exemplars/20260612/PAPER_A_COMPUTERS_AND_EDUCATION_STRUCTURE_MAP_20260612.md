# Paper A Target-Journal Structure Map

Target journal: Computers & Education

Decision state: target journal, construct scope, figure spine, and table spine are approved. The actual TSSEM/OSMASEM/sensitivity estimate insertion is approved but cannot be treated as complete from the current input because the model-ready primary file lacks source-supported numeric sample size for most rows.

## Researcher-Approved Route Recorded on 2026-06-12

| Item | Current decision |
| --- | --- |
| Primary SEM route | Full 10-construct route. |
| Sample-size policy | Source-supported PDF/workbook N override is allowed with provenance. |
| Evidence class | Direct-r is primary; expanded direct-r-form and converted effects are sensitivity evidence. |
| Construct/moderator boundary | Trust, anxiety, and self-efficacy are focal mediator/mechanism candidates inside the 10-construct SEM, not study-level moderators. |
| Moderator candidates | `ai_type` is the strongest current substantive moderator candidate. `common_method_bias` is QC/sensitivity. Year/generative-AI era was merged but is not feasible as pre/post moderator from current data because available years are all post-2023. |

Trust, anxiety, and self-efficacy can be studied as moderators only if a separate study-level variable is defined, such as construct presence, measurement role, or construct framing. That route is weaker than the current construct-level SEM and should not replace the primary model. The current researcher intent is to test them as mediator/mechanism constructs through indirect paths where coverage permits.

## Mediator/Mechanism Feasibility Update

First-pass audit file: `data/04_extraction/05_llm_masem_substitution/results/paper_a_mediator_feasibility_20260612/PAPER_A_MEDIATOR_FEASIBILITY_AUDIT_20260612.md`.

| Construct | Feasibility result | Manuscript treatment |
| --- | --- | --- |
| `ATT` | Main indirect candidate for `PE/EE/SI/FC -> ATT -> BI`. | Standard TAM mediation family. |
| `TRU` | Main indirect candidate for `PE/EE -> TRU -> BI`; sensitivity for `SI -> TRU -> BI`. | AI-specific trust mediation/mechanism. |
| `SE` | Sensitivity-level mechanism for `FC/EE/PE/SI -> SE -> BI` and selected `SE -> ATT` paths. | Sensitivity/mechanism evidence only. |
| `ANX` | Underpowered or not identified for current candidate paths. | Theory-specified construct; avoid confirmed mediation claim. |

## Moderator Feasibility Update

Initial moderator report: `data/04_extraction/05_llm_masem_substitution/results/initial_execution_validation_20260612/PAPER_A_B_INITIAL_EXECUTION_VALIDATION_20260612.md`.

Year/generative-era merge report: `data/04_extraction/05_llm_masem_substitution/results/paper_a_year_moderator_merge_20260612/PAPER_A_YEAR_GENERATIVE_ERA_MODERATOR_MERGE_20260612.md`.

| Moderator | Result | Manuscript treatment |
| --- | --- | --- |
| `ai_type` | 36 nonmissing studies, two usable levels: generative=21, general=15. | Main substantive moderator candidate. |
| `common_method_bias` | 36 nonmissing studies, two usable levels: not addressed=22, addressed=14. | Methodological/QC sensitivity moderator. |
| `year/generative-AI era` | 66 studies with year all post-2023; 8 missing; no pre/post contrast. | Not feasible as current pre/post moderator. |
| `user_role` | 36 nonmissing studies but smallest level has 2 studies. | Not feasible as current main moderator. |
| `education_level`, `country/region`, `theoretical_framework` | Sparse or unbalanced. | Not feasible from current input. |

## Current Analysis Gate

| Check | Current value | Implication |
| --- | --- | --- |
| Primary model-ready rows | 804 | Available in the OneDrive Paper1 working folder |
| Usable 10-construct rows after r checks | 796 | No r absolute value >= 1 blocker in the tiered primary file |
| Rows missing numeric N | 754 | N-weighted TSSEM/MASEM cannot be claimed until sample size is reconciled or explicit exclusion rule is applied |
| Studies represented | 74 | Correlation evidence is spread across incomplete matrices |
| Covered construct pairs | 44/45 | Coverage is broad but not complete |
| Complete 10-construct matrices | 0 | Complete-case 10-construct TSSEM is not feasible as the primary route |
| Studies with 15 or more construct pairs | 26 | FIML/TSSEM route may be possible after N reconciliation |

Least-covered pairs:

| Construct pair | Rows |
| --- | --- |
| SE-TRU | 1 |
| ANX-FC | 2 |
| ANX-SE | 2 |
| ANX-UB | 2 |
| ATT-TRU | 2 |
| ANX-BI | 3 |
| ANX-EE | 3 |
| ANX-SI | 3 |
| ANX-PE | 4 |
| FC-TRU | 4 |
| ATT-SE | 5 |
| SE-UB | 5 |

## C&E Submission Components

- Main manuscript: double-anonymized Word file with title page separated at submission.
- Abstract: no more than 250 words.
- Keywords: 1 to 7.
- Highlights: 3 to 5 bullets, no more than 85 characters each, submitted separately.
- Tables: editable text, cited in order, with captions and notes.
- Figures: conceptual model, PRISMA, coverage heatmap, and path model as editable/high-resolution files.

## Proposed Highlights

- Synthesizes AI adoption evidence in higher education with MASEM.
- Integrates TAM/UTAUT predictors with trust and AI anxiety.
- Separates direct-r inputs from converted sensitivity evidence.
- Tests structural and moderator paths across ten constructs.
- Provides reproducible extraction and QC artifacts.

## Section Spine

1. Introduction: higher-education AI adoption problem, why structural synthesis is needed, why AI trust/anxiety expand TAM/UTAUT.
2. Theory and hypotheses: TAM/UTAUT, attitude mediation, self-efficacy, trust, anxiety, use behavior.
3. Method: search, screening, source adjudication, coding, 10-construct harmonization, TSSEM/OSMASEM, sensitivity.
4. Results: PRISMA, study characteristics, input coverage, Stage 1 pooled matrix, Stage 2 model paths, indirect effects/mediator feasibility, moderators, sensitivity.
5. Discussion: theory, institutional implications, limitations, reproducibility, future AI-adoption measurement.

## Table Spine

| Table | Title | Status |
| --- | --- | --- |
| Table 1 | Construct harmonization and operational definitions | Ready to draft |
| Table 2 | PRISMA and study-characteristics profile | Needs final inclusion lock |
| Table 3 | Analysis-ready input sets and source-type rules | Ready with current caveats |
| Table 4 | Construct-pair coverage and missingness | Ready as pre-model table |
| Table 5 | Stage 1 pooled correlation matrix | Needs TSSEM run after N gate |
| Table 6 | Stage 2 structural paths and indirect effects | Needs TSSEM run |
| Table 7 | Moderator and sensitivity results | Needs OSMASEM/sensitivity run |

## Figure Spine

| Figure | Purpose | Status |
| --- | --- | --- |
| Figure 1 | PRISMA flow from 22,166 records to final included studies | Needs final inclusion lock |
| Figure 2 | Ten-construct conceptual model | Ready to draw |
| Figure 3 | Construct-pair coverage heatmap | Ready from current coverage |
| Figure 4 | Final Stage 2 path model | Needs TSSEM run |
| Figure 5 | Moderator/sensitivity comparison | Needs OSMASEM/sensitivity run |

## Manuscript Boundary

Do not insert final C&E results claims until numeric N is reconciled or an approved N-eligible subset rule is documented for Paper A. The currently defensible manuscript state is introduction, theory spine, methods, input/QC results, and analysis gate.
