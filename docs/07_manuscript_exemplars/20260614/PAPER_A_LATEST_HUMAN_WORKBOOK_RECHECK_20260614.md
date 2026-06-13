# Paper A Latest Human Workbook Recheck

Date: 2026-06-14

## Why this recheck was needed

The first Paper A MASEM attempt used `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_substitution_rerun_input_n_weighted_all_source_supported_20260612.csv`. That file contained 796 usable target-construct rows, 74 studies, and 44/45 full10 construct pairs. The run failed at TSSEM1 and initially suggested a sparse partial-matrix blocker.

The researcher flagged that this seemed inconsistent with prior coding documentation and asked whether the final human coding values, PDFs, Git, or SSD-local source materials had been missed.

## Drive and local-source finding

The Google Drive folder supplied by the researcher is accessible, but it contains the original 2026-04-25 Phase 2 coder package folders. Drive-wide search and local OneDrive/SSD inspection show later candidate final read-only copies under:

`/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/Coding_Latest_R1_R4_20260605/`

The candidate latest human workbook set is:

| Coder | Candidate latest workbook |
| --- | --- |
| R1 | `AI_Adoption_MASEM_Coding_v3_R1_Phase0_1_2_20260425.xlsx` |
| R2 | `AI_Adoption_MASEM_Coding_v3_R2_Phase0_1_2_20260425.xlsx` |
| R3 | `AI_Adoption_MASEM_Coding_v3_R3_Phase0_1_2_20260425.xlsx` |
| R4 | `AI_Adoption_MASEM_Coding_v3_R4_Phase0_1_2_20260425_v2.xlsx` |

Therefore, the supplied Drive folder alone should not be treated as the final human-value source.

## Latest-human-workbook audit result

Audit report: `data/04_extraction/05_llm_masem_substitution/results/paper_a_latest_human_workbook_audit_20260614/PAPER_A_LATEST_HUMAN_WORKBOOK_AUDIT_20260614.md`

| Dataset | Numeric rows | Studies | Full10 pair coverage | Complete full10 studies | Studies with >=15 pairs |
| --- | ---: | ---: | ---: | ---: | ---: |
| Latest R1-R4 human workbooks | 3,654 | 181 | 45/45 | 0 | 64 |
| Prior 20260612 rerun input | 796 | 74 | 44/45 | 0 | 26 |

Interpretation: the prior analytic input omitted or transformed many latest-human-workbook study-pair cells. The earlier sparse-input result should be treated as a property of that 20260612 input, not as proof that the final human coding set lacks pair coverage.

## Re-run from latest human workbook input

Latest-human direct-r input: `data/04_extraction/05_llm_masem_substitution/results/paper_a_latest_human_workbook_audit_20260614/paper_a_latest_human_workbook_direct_r_input_20260614.csv`

Execution report: `data/04_extraction/05_llm_masem_substitution/results/paper_a_masem_latest_human_execution_20260614/PAPER_A_MASEM_EXECUTION_ATTEMPT_20260614.md`

| Route | Pair coverage | Partial studies | Complete-case studies | TSSEM1 | Stage 2 | Interpretation |
| --- | ---: | ---: | ---: | --- | --- | --- |
| Core7 ATT mediation | 21/21 | 175 | 4 | Failed under partial-matrix TSSEM | Not run | Overall pair coverage is sufficient, but partial-matrix TSSEM remains unstable. |
| Trust6 mechanism | 15/15 | 176 | 8 | Failed under partial-matrix TSSEM | Not run | Overall pair coverage is sufficient, but partial-matrix TSSEM remains unstable. |
| Full10 theory target | 45/45 | 179 | 0 | Failed under partial-matrix TSSEM | Not run | Full10 has all pairs somewhere, but no study reports a complete 10-construct matrix. |

## Complete-case reduced-route probe

Complete-case report: `data/04_extraction/05_llm_masem_substitution/results/paper_a_complete_case_latest_human_20260614/PAPER_A_LATEST_HUMAN_COMPLETE_CASE_TSSEM_PROBE_20260614.md`

| Route | Complete candidates | Positive-definite complete cases | Stage 1 | Stage 2 | Boundary |
| --- | ---: | ---: | --- | --- | --- |
| Core7 ATT complete-case | 4 | 3 | Converged | Failed: `aCov` not positive definite | Diagnostic only. |
| Trust6 complete-case | 8 | 8 | Converged | Converged | Technically estimable as a reduced diagnostic, not the full10 primary model. |

Trust6 Stage 2 diagnostic path estimates were generated at:

`data/04_extraction/05_llm_masem_substitution/results/paper_a_complete_case_latest_human_20260614/paper_a_latest_human_complete_case_stage2_paths_20260614.csv`

## PDF/source check

PDF/source audit: `data/04_extraction/05_llm_masem_substitution/results/paper_a_latest_human_workbook_audit_20260614/TRUST6_COMPLETE_CASE_PDF_SOURCE_VALUE_AUDIT_20260614.md`

The eight trust6 complete-case studies are `S004`, `S035`, `S086`, `S088`, `S138`, `S173`, `S176`, and `S223`. All have local PDFs and source packets. Automated text checks found the coded values in PDF text for all rows in all eight studies; source-packet text also found nearly all values, with misses attributable to rendering/text extraction limits rather than confirmed coding errors.

## Corrected conclusion

The current evidence does not support the claim that the human coding values are generally wrong. The stronger conclusion is:

1. The supplied Drive folder is not the final/latest human coding source by itself.
2. The prior 20260612 analytic input did not carry the full latest-human-workbook row universe.
3. Latest human workbooks restore full10 pair coverage to 45/45, but no individual study has a complete 10-construct matrix.
4. Full10 primary MASEM remains blocked by study-level matrix completeness, not by absence of pair coverage across the corpus.
5. A reduced trust6 complete-case MASEM is technically estimable and source-supported, but it is a diagnostic/sensitivity route unless the researcher changes the primary estimand.
