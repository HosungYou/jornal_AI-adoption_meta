# Paper A revised model-family MASEM strategy

Date: 2026-06-15

## Decision

Paper A remains one manuscript. The strengthened manuscript claim is not that a full 10-construct SEM has been estimated. The claim is that AI adoption theory can be reconstructed as a full10 theoretical target and then tested through empirically estimable model-family descendants.

## Accepted structure

- `full10`: theory-generating target and pairwise evidence map.
- `core7`: empirical complete-case attitude-mediation backbone.
- `trust6`: empirical complete-case AI trust/reliance mechanism.
- `anxiety/self-efficacy`: theoretically specified future mechanisms, not primary complete-case MASEM claims in the current data structure.

## PE versus EE clarification

The PE/EE issue is not the PE-EE correlation. The manuscript now treats PE and EE as distinct mechanisms:

- PE: performance/usefulness mechanism; expected value and outcome improvement.
- EE: effort/usability mechanism; operational friction and cognitive burden.

Supplemental diagnostics compare their roles across ATT, BI, TRU, and reduced model-family specifications.

## Supplemental analyses added

Location: `data/04_extraction/05_llm_masem_substitution/results/paper_a_model_family_supplemental_diagnostics_20260615/`.

Files:

- `paper_a_supplemental_model_comparison_20260615.csv/md`
- `paper_a_supplemental_structural_paths_20260615.csv/md`
- `paper_a_pe_vs_ee_role_comparison_20260615.csv/md`
- `paper_a_full10_omitted_pair_diagnostic_20260615.csv/md`
- `paper_a_anx_se_complete_case_feasibility_scan_20260615.csv/md`
- `paper_a_anx_se_targeted_model_attempts_20260615.csv/md`
- `PAPER_A_SUPPLEMENTAL_DIAGNOSTICS_SUMMARY_20260615.md`

## Key results

- Core7 baseline remained strong: CFI = 0.999, RMSEA = 0.009.
- Core7 without ATT direct-belief model also fit well but used a much larger complete-case set, so it is diagnostic rather than a replacement for the attitude-mediation model.
- Core7 pure mediation without direct belief-to-BI paths fit worse, supporting retention of direct belief-intention paths.
- Trust6 baseline remained strong: CFI = 0.996, RMSEA = 0.011.
- Trust-only mediation fit poorly, so trust should not be framed as the sole mediator of PE/EE/SI effects.
- EE -> BI was supported in trust6, while several PE paths were positive but CI-incomplete. The manuscript should not claim universal PE or EE dominance.
- ANX/SE feasibility is uneven: self-efficacy has feasible smaller subsets, but anxiety-inclusive ATT/TRU/BI/UB models remain underidentified for complete-case MASEM.

## Manuscript update

Revised files:

- `paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/PAPER_A_APA7_REVISED_MODEL_FAMILY_MANUSCRIPT_WITH_SUPPLEMENTAL_DIAGNOSTICS_20260615.md`
- `paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/PAPER_A_APA7_REVISED_MODEL_FAMILY_MANUSCRIPT_WITH_SUPPLEMENTAL_DIAGNOSTICS_20260615.docx`

## Reporting guardrail

Reduced model comparisons are sensitivity/model-family diagnostics, not definitive nested chi-square model-selection tests. Removing constructs can change the complete-case study set, degrees of freedom, and matrix structure.
