# R1-R4 Pairwise Comparison Playbook

## Purpose

This playbook documents the practical workflow for comparing R1-R4 human coder
values without repeatedly opening every PDF. It applies to Phase 1 pairwise
review and Phase 2 rotated-pair review before the source-anchored adjudicated
human reference standard is frozen.

The goal is not to force immediate consensus inside raw coder workbooks. The
goal is to identify meaningful disagreements, decide which items need
source-document adjudication, and preserve a transparent audit trail.

## Current Pair Structure

| Phase | Pair | Coders | Purpose |
|---|---|---|---|
| Phase 1 | Pair A | R1 + R2 | Completed Wave 1 comparison |
| Phase 1 | Pair B | R3 + R4 | Completed Wave 1 comparison |
| Phase 2 | Pair C | R1 + R4 | Rotated Wave 2 comparison |
| Phase 2 | Pair D | R2 + R3 | Rotated Wave 2 comparison |

Phase 1 and Phase 2 together form the Paper B validation corpus. Treat Phase 2
as a second wave in the same validation design, not as a supplementary afterthought.

## Non-Negotiable Rules

1. Preserve raw independent coder workbooks. Do not overwrite raw coder cells
   during comparison meetings.
2. Use the comparison workbook and decision logs as working artifacts.
3. Keep PDF hyperlinks out of shareable workbooks because local PDF paths differ
   by machine and can corrupt Excel files.
4. Use `source-anchored adjudicated human reference standard`, not `gold standard`,
   except when preserving historical wording.
5. Do not begin LLM accuracy or MASEM substitution analysis until the adjudicated
   human reference file is frozen in `04_reference_standard_freeze/`.

## Artifact Flow

1. Freeze returned raw coder workbooks in `01_raw_human_coder_data_freeze/`.
2. Generate or update the pairwise comparison workbook in
   `02_pre_adjudication_disagreement/`.
3. Triage differences by study, field family, source type, and numeric magnitude.
4. Discuss only meaningful differences in the comparison meeting.
5. Record each source-checked decision in
   `03_source_document_adjudication/phase*/decision_log_*.md`.
6. Apply decisions only to the adjudicated reference dataset, not to the raw
   coder workbook.
7. Freeze the final source-anchored adjudicated human reference after all
   discrepancies have a source-backed decision.

## Comparison Meeting Workflow

### Before The Meeting

Prepare a filtered agenda from the comparison workbook:

- Sort by `review`, `flag`, `mismatch`, blank status, or unresolved resolution.
- Group rows by Study ID so metadata, exclusion, construct mapping, and
  correlations are reviewed together.
- Start with studies that affect inclusion/exclusion, sample definition, or
  many construct-pair rows.
- Keep source PDFs local, but do not embed links into the workbook.

For each study, review in this order:

1. Inclusion/exclusion and study status.
2. Target sample and sample size.
3. Educational AI focal technology and user group.
4. Evidence type: zero-order r, latent correlation, Fornell-Larcker table, HTMT,
   or standardized path coefficient.
5. Construct mapping.
6. Numeric value differences.
7. Notes and unresolved flags.

### During The Meeting

Use one decision unit at a time: one study-field, one construct mapping, or one
construct-pair statistic. Avoid broad "R1 is right" or "R2 is right" decisions
unless the same source table and rule clearly apply to the whole study.

For each decision, record:

- Study ID.
- Field or construct pair.
- R1/R2/R3/R4 raw values as applicable.
- Source table/page/section.
- Evidence type.
- Final source-anchored adjudicated value.
- Rule applied.
- Rationale.
- Adjudicator and date.

### After The Meeting

Update the comparison workbook's resolution/status fields and the Markdown
decision log. Do not edit the raw coder workbook to look "clean"; unresolved raw
disagreement is itself an analyzable pre-adjudication result.

## What Counts As A Meaningful Difference

Use this triage rule to keep meetings focused.

| Difference type | Count as discussion item? | Handling |
|---|---:|---|
| Same value, different rounding only | No | Preserve source-reported precision up to three decimals. |
| r coded by one coder, beta/path by another | Not as numeric difference | Classify as source-type mismatch and adjudicate which evidence type is usable. |
| HTMT used by one coder as a correlation | Yes | HTMT-only evidence is not a usable MASEM correlation matrix. |
| Fornell-Larcker diagonal used as a correlation | Yes | Diagonal values are usually sqrt AVE or 1.00; do not code as pairwise r. |
| Fornell-Larcker off-diagonal latent correlations | Maybe | Usable if clearly latent correlations and no better zero-order matrix is available; note source type. |
| Sign difference | Yes | Always source-check. |
| r/beta absolute difference <= .005 from rounding | No | Treat as rounding unless source table shows otherwise. |
| r/beta absolute difference > .01 | Yes | Source-check and log. |
| r/beta absolute difference >= .05 | High priority | Review source row/column alignment and construct mapping first. |
| Sample N differs by 1 from table note/article text | Maybe | Log if it changes weighting or reflects a different sample. |
| Different subgroup/sample selected | Yes | Decide target sample before resolving correlations. |
| Different construct family mapping | Yes | Resolve against coding manual and item wording. |
| One coder excluded, one coder included | Yes | Resolve before correlation-level discussion. |

## Evidence-Type Rules

### Zero-Order Correlations

Use source-reported Pearson or zero-order correlations when available. Preserve
three decimals when the source reports three decimals.

### Standardized Path Coefficients

PLS-SEM tables often label standardized paths as `Original Value`, `Original
Sample`, or similar. Treat these as beta/path coefficients, not zero-order
correlations. Do not compare them numerically against r values as if they were
the same statistic.

Use beta-converted path coefficients only when the protocol permits path
coefficient recovery and no usable correlation matrix is available.

### Fornell-Larcker Tables

Fornell-Larcker criterion tables can contain off-diagonal latent correlations,
but the diagonal is usually sqrt AVE. Use off-diagonal values only when the table
structure is clear and no better zero-order matrix is reported. Record the source
type as latent/Fornell-Larcker so downstream sensitivity checks can separate it
from observed Pearson r.

### HTMT Tables

HTMT is a discriminant-validity ratio, not a correlation matrix. Do not use
HTMT-only values as MASEM correlations. HTMT can be noted as measurement-validity
evidence, but it should not populate target construct-pair r cells.

## Common Traps From Phase 1

- PDF hyperlinks and machine-specific paths can trigger Excel repair warnings.
- Three-decimal source values should not be reduced to two decimals during
  adjudication.
- `Original Value` in SmartPLS path tables is usually a standardized path
  coefficient.
- Satisfaction is not automatically `ATT`.
- Perceived Risk is not automatically `ANX`; require anxiety, fear,
  apprehension, or threat-affect wording.
- Task-Technology Fit should not be mapped to `FC` unless the manual explicitly
  supports the case.
- Perceived Playfulness should not be mapped to `ATT`.
- GAAIS Positive Attitudes can be primary `ATT`; do not average GAAIS Negative
  Attitudes into primary `ATT` unless a sensitivity analysis is explicitly
  planned.
- Multiple samples should not be pooled unless the study design and coding manual
  justify pooling.
- If the selected sample changes, all dependent correlation rows may need review.

## Resolution Labels

Use consistent labels in comparison workbooks and decision logs:

| Label | Meaning |
|---|---|
| `accept_R1` / `accept_R2` / `accept_R3` / `accept_R4` | One coder's value matches the source and rule. |
| `source_corrected` | Neither raw coder value is fully correct; source-check supplies corrected value. |
| `exclude_row` | Row should not enter target MASEM matrix. |
| `exclude_study` | Study is outside scope or lacks usable target evidence. |
| `construct_remap` | Statistic is retained but mapped to a different target construct family. |
| `source_type_mismatch` | Difference is driven by r vs beta/path/HTMT/Fornell-Larcker source type. |
| `rounding_only` | Difference is due only to precision or rounding. |
| `flag_sensitivity` | Retain for potential sensitivity or separate construct analysis, not primary matrix. |
| `escalate` | Source evidence remains ambiguous after first adjudication. |

## Cross-Pair Adjudication

When pair members cannot resolve a meaningful difference from the source
document, use a cross-pair adjudicator:

- Phase 1 Pair A differences can be reviewed by an available Pair B coder.
- Phase 1 Pair B differences can be reviewed by an available Pair A coder.
- Phase 2 Pair C (R1+R4) differences should be reviewed by R2 first, with R3 as
  secondary if needed.
- Phase 2 Pair D (R2+R3) differences should be reviewed by R1 first, with R4 as
  secondary if needed.

If a PI decision supersedes this routing, record that in the decision log with
date and rationale.

## Minimum Decision Log Template

```markdown
### S### - short study label

- Pair: R# + R#
- Field or construct pair:
- Raw values:
  - R#:
  - R#:
- Source location:
- Evidence type:
- Decision:
- Rule applied:
- Rationale:
- Adjudicator:
- Date:
- Follow-up:
```

## Ready-To-Freeze Checklist

Before creating the source-anchored adjudicated human reference standard, confirm:

- Every included study has one final status.
- Every exclusion has an exclusion code and source-backed rationale.
- Every correlation/path row has one evidence type.
- HTMT-only values have been excluded from target correlations.
- Fornell-Larcker diagonal values have not been used as correlations.
- Construct mappings are consistent with the current coding manual.
- Subgroup/sample decisions are documented before numeric rows are finalized.
- Rounding-only differences are marked as such rather than escalated.
- Decision logs cover all meaningful discrepancies.
- Raw coder files remain preserved as pre-adjudication evidence.
