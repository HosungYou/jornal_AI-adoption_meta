# Paper B Visual Table/Figure/PDF Generation Logic

Date: 20260619

## Inputs

- `m1r_denominator_summary.csv`
- `rq3_triage_summary.csv`
- `masem_gate_summary.csv`
- Newly downloaded frontier PDFs: Huang et al. 2025 JMIR and Jansen et al. 2026 Educational Psychology Review.

## Output Logic

1. Recompute denominator-family accuracy, abstention/unresolved share, and Wilson 95% confidence intervals from frozen CSV counts.
2. Generate a dense table image for manuscript insertion and a CSV/Markdown source table for audit.
3. Generate a forest-style risk-difference plot comparing primary r strata with the converted beta/path sensitivity stratum.
4. Generate an accuracy-versus-review-burden plot instead of a time-savings plot because no reviewer-time or per-study duration logs are available.
5. Generate a source-anchored validation flow diagram to prevent reviewers from misreading the workflow as autonomous model replacement.
6. Extract reference PDFs into page images, text files, caption inventories, and machine-detected tables.
7. Build a visual-upgrade DOCX and PDF report from the same generated image/table artifacts.

## Claim Boundary

Do not report elapsed-time efficiency. The current evidence supports review-burden and triage framing, not a direct time-spent comparison.
