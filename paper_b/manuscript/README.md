# Paper B Manuscript Artifacts

## Current Draft

The current summarized RSM-oriented manuscript is:

- `Paper_B_RSM_Summarized_Manuscript_v0.2.docx`
- `Paper_B_RSM_Summarized_Manuscript_v0.2.md`

This version removes named discussion of the previously reviewed exemplar paper and reframes Paper B as a workflow validation study rather than a three-model vendor comparison.

## 2026-06-19 Visual Upgrade

The current visual-upgrade insert package is:

- `visual_upgrade_20260619/Paper_B_Implementation_Draft_RSM_VISUAL_UPGRADE_20260619.docx`
- `visual_upgrade_20260619/Paper_B_Implementation_Draft_RSM_VISUAL_UPGRADE_20260619.md`
- `visual_upgrade_20260619/reports/Paper_B_Frontier_Visual_Upgrade_Report_20260619.pdf`

This package adds a dense denominator-family table, a source-anchored validation flow diagram, a risk-difference forest-style plot, an accuracy-versus-review-burden plot, and a MASEM claim-gate figure. No reviewer-time logs are available, so the package intentionally does not include an elapsed-time efficiency plot or time-savings claim.

## Current Positioning

Paper B evaluates whether a prespecified Codex 5.5 workflow can augment human-supervised MASEM-ready data extraction. The main validation logic is:

1. Compare structured LLM output against an adjudicated human reference standard.
2. Evaluate extraction validity by family: bibliographic, sample, construct, measurement, correlation, matrix, and moderator fields.
3. Diagnose systematic errors by reporting condition and construct ambiguity.
4. Test downstream substitution stability by comparing human-coded and LLM-assisted MASEM inputs and outputs.

Additional models may be used only as supplementary robustness or triage analyses. They should not organize the manuscript's main claim.

## Included Figure

- `figures/figure1_substitution_stability_simulation.png`

The figure is a simulated placeholder that illustrates the planned downstream substitution analysis. It is not an empirical result and must be replaced or relabeled once real estimates are available.

## Tables in v0.2

The summarized manuscript includes three manuscript-ready tables:

| Table | Purpose |
|---|---|
| Table 1 | Validation design summary |
| Table 2 | Planned analysis and reporting matrix |
| Table 3 | Primary results shell |

In the Word draft, tables are formatted single-spaced while the main manuscript text is double-spaced.

## Next Steps

1. Freeze the extraction schema and prompt version before validation.
2. Fill Table 3 after coding and extraction are complete.
3. Replace the simulated figure with empirical substitution results.
4. Add repository links for prompts, validation data, logs, and analysis scripts before submission.
