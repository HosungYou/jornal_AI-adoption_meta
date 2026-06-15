# Paper A researcher README

Updated: 2026-06-15

## Current interpretation

Paper A should be read as a model-family MASEM study, not as a single full10 SEM.

- `full10`: theoretical target and evidence map across 10 constructs.
- `core7`: empirical attitude-mediation MASEM route.
- `trust6`: empirical AI-reliance/trust mechanism MASEM route.
- `ANX` and `SE`: theory-relevant future mechanisms; currently underidentified for primary complete-case MASEM.

## Current manuscript status

The current Word manuscript is a structured scaffold with real model-family results, but it is not yet submission-ready.

- Tables are inserted in the body, but their current grid styling is not APA 7th professional table style.
- Figures are inserted in the body, but Figure 0 and the path diagrams need publication-grade redesign.
- A true PRISMA 2020 flow diagram has not yet been generated.
- External articles should be used as reporting exemplars only; do not directly reuse their tables or figures.

Current draft:

- `paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/PAPER_A_APA7_SUBMISSION_STRENGTHENED_INLINE_MANUSCRIPT_20260615.docx`

## PRISMA count lock needed

Current source files do not fully agree.

| Source | Current count/status |
| --- | ---: |
| `data/01_identification/dedup_report.txt` | 22,166 identified; 5,977 duplicates removed; 16,189 unique records |
| `data/02_screening/screening_summary.json` | 657 human-reviewed; 225 included; 432 excluded |
| root `README.md` before audit | 224 included |
| previous `paper_a/README.md` before audit | final included TBD |

Until the team resolves `224` vs `225` and confirms the full-text eligibility boxes, PRISMA should be reported as `review needed`, not final.

Review file:

- `paper_a/PRISMA_COUNTS_REVIEW_NEEDED_20260615.md`

## Tables needed for a submission-ready manuscript

Main text:

1. Construct genealogy and model-family role.
2. Search, screening, and eligibility summary.
3. Study and effect-size characteristics.
4. Primary model-family fit.
5. Primary structural path estimates with 95% CIs.
6. Supplemental model-family diagnostics.
7. PE versus EE role comparison.
8. Anxiety/self-efficacy feasibility diagnostics.

Supplement:

1. Full search strategy.
2. Coding and adjudication rules.
3. Source-anchored construct mapping examples.
4. Full10 pairwise evidence coverage.
5. Full path estimates and CI diagnostics.
6. Source/reference manifest.

## Figures needed for a submission-ready manuscript

Main text:

1. PRISMA 2020 flow diagram.
2. Theoretical genealogy of AI adoption constructs.
3. Paper A analytic workflow.
4. Full10 evidence coverage heatmap.
5. Core7 MASEM path model.
6. Trust6 MASEM path model.
7. Path estimate coefficient/forest plot.
8. Model feasibility or complete-case availability plot.

## Next work order

1. Lock PRISMA counts from the screening and eligibility source files.
2. Regenerate APA 7th tables without internal grid lines.
3. Generate a true PRISMA 2020 flow diagram.
4. Redesign path figures and evidence-map figures using Paper A data.
5. Rebuild the Word manuscript with corrected tables and figures.
6. Refresh the OSF-ready package after the manuscript rebuild.

