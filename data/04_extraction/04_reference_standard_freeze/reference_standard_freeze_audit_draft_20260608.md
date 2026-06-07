# Reference Standard Freeze Audit Draft

Date: 2026-06-08

Status: Step 4 draft started. This is not the frozen
source-anchored adjudicated human reference standard.

Step 5 LLM comparison and MASEM substitution remain inactive until a final
freeze file and freeze log are committed.

## Scope

This draft applies the logged Phase 2 source-document adjudication decisions for
`S014`, `S021`, `S056`, `S092`, `S121`, `S195`, `S202`, and `S206`.

The draft target-row file is:

- `paper_b_phase2_source_adjudicated_reference_draft_20260608.csv`

The decision-application audit file is:

- `paper_b_phase2_step4_decision_application_audit_20260608.csv`

## Draft Row Counts

| Study | Step 4 draft action | Included target rows |
|---|---|---:|
| `S021` | Include limited main-PDF primary Model 1 rows with T1/T2 retained as separate strata | 12 |
| `S056` | Include source-corrected Table 2 construct correlations | 3 |
| `S092` | Include source-beta-corrected Peterson-Brown converted SEM path rows | 3 |
| `S121` | Include source-transcribed Figure 2 Spearman rows for student and teacher samples | 56 |
| `S014` | Preserve population eligibility but exclude indirect-effect candidate rows | 0 |
| `S195` | Preserve canonical duplicate audit record and exclude candidate rows | 0 |
| `S202` | Exclude from target matrix by focal-technology boundary | 0 |
| `S206` | Preserve as duplicate of `S195`; do not count as a second source record | 0 |

Total included target rows in this draft: 74.

## Source Files Used

- `data/04_extraction/03_source_document_adjudication/phase2/decision_log_20260608.md`
- `data/04_extraction/03_source_document_adjudication/phase2/s021_primary_model_row_set_20260608.md`
- `data/04_extraction/03_source_document_adjudication/phase2/s121_figure2_row_set_20260608.md`
- `data/04_extraction/03_source_document_adjudication/phase2/phase2_source_adjudication_evidence_split_20260529.md`
- `docs/06_decisions/2026-06-08_Paper_B_Source_Adjudication_Decisions.md`

The local source PDFs in
`data/04_extraction/03_source_document_adjudication/source_pdfs/` remain ignored
by Git and are not part of the committed reference artifact.

## Draft Field Rules Applied

- Use `source-anchored adjudicated human reference standard`, not `gold
  standard`.
- Keep raw human coder workbooks unchanged.
- Keep excluded/no-value/duplicate decisions in an audit file rather than in the
  target-row CSV.
- Preserve separate strata or samples when the source decision requires it.
- Mark beta-converted rows through `r_source` and retain `original_beta` when
  the Step 3 row artifact carries it.
- Mark `SE` in `S121` as medium-confidence construct mapping because the source
  label is subjective competence.
- Mark `AIAS-4` to `ATT` in `S021` as medium-confidence construct mapping.

## Not Yet Frozen

Freeze date: not set.

Commit hash: not set.

Final reviewer: not set.

Post-freeze correction log: not opened because the reference is not frozen.

## Required Freeze Audit Before Step 5

- Parse the draft target-row CSV and confirm 74 rows.
- Confirm all `r_value` values are within `[-1, 1]`.
- Confirm no draft row has missing study ID, construct pair, sample/stratum, or
  sample size.
- Confirm `S021` and `S121` strata are not pooled.
- Confirm `S014`, `S195`, `S202`, and `S206` have audit entries but no target
  rows.
- Confirm the `S092` original-beta reconstruction and Peterson-Brown converted
  values documented in the freeze audit.
- Record freeze date, commit hash, source file list, excluded private/raw files,
  discrepancy resolution log, field-level rules, and reviewer before Step 5.
