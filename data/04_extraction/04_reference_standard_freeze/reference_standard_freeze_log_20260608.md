# Source-Anchored Adjudicated Reference Freeze Log

Freeze date: 2026-06-08

Freeze scope: Paper B Phase 2 source-adjudicated high-priority package for
`S014`, `S021`, `S056`, `S092`, `S121`, `S195`, `S202`, and `S206`.

Status: frozen for this scoped 74-row package. This log does not claim that the
entire 213-study Paper B reference standard is complete.

Final reviewer: Hosung / researcher, approval recorded in the Codex thread on
2026-06-08.

Frozen artifact commit hash:
`2c40c37a66229b6f0acac333048aa2b7e3a32679`

## Frozen Files

- `paper_b_phase2_source_adjudicated_reference_frozen_20260608.csv`
- `paper_b_phase2_step4_decision_application_audit_20260608.csv`
- `qa/freeze_audit_20260608.md`
- `post_freeze_corrections_20260608.md`

## Supporting Draft Files

- `paper_b_phase2_source_adjudicated_reference_draft_20260608.csv`
- `reference_standard_freeze_audit_draft_20260608.md`

## Source-Adjudication Files Used

- `data/04_extraction/03_source_document_adjudication/phase2/decision_log_20260608.md`
- `data/04_extraction/03_source_document_adjudication/phase2/s021_primary_model_row_set_20260608.md`
- `data/04_extraction/03_source_document_adjudication/phase2/s121_figure2_row_set_20260608.md`
- `data/04_extraction/03_source_document_adjudication/phase2/phase2_source_adjudication_evidence_split_20260529.md`
- `data/04_extraction/03_source_document_adjudication/meeting_packets/Paper_B_P0_P3_Adjudication_Meeting_Packet_20260529.md`
- `docs/06_decisions/2026-06-08_Paper_B_Source_Adjudication_Decisions.md`

## Excluded Private Or Raw Files

The following files or folders were used only as local evidence sources or
preserved raw inputs and are not part of the committed frozen reference package:

- `data/04_extraction/03_source_document_adjudication/source_pdfs/`
- `data/04_extraction/01_raw_human_coder_data_freeze/phase1/coder_packages/`
- `data/04_extraction/01_raw_human_coder_data_freeze/phase2/coder_packages/`
- `data/04_extraction/01_raw_human_coder_data_freeze/phase2/returned_raw/`
- `data/04_extraction/01_raw_human_coder_data_freeze/phase2/freeze_candidates/`
- `data/04_extraction/05_llm_masem_substitution/`

No raw human coder workbook was edited for this freeze package, and no Step 5
LLM comparison or MASEM substitution artifact was created.

## Discrepancy Resolution Summary

| Study | Frozen action | Target rows |
|---|---|---:|
| `S014` | Eligible population but no usable direct mapped target-pair coefficient; indirect perceived-risk rows excluded | 0 |
| `S021` | Included as limited main-PDF primary Model 1 row set with T1/T2 kept separate | 12 |
| `S056` | Source-corrected to Table 2 off-diagonal construct correlations | 3 |
| `S092` | Source betas reconstructed from Table 3 and Peterson-Brown converted | 3 |
| `S121` | Figure 2 Spearman correlations frozen separately for student and teacher samples | 56 |
| `S195` | Preserved as canonical duplicate audit record; one-coder-only target rows excluded | 0 |
| `S202` | Excluded from target matrix by focal-technology boundary | 0 |
| `S206` | Preserved as duplicate of `S195`; not counted as second source record | 0 |

Total frozen target rows in this scoped package: 74.

## Field-Level Rules Applied

- Use `source-anchored adjudicated human reference standard`, not `gold
  standard`.
- Keep raw human coder workbooks unchanged.
- Store excluded/no-value/duplicate decisions in the decision-application audit
  rather than the target-row CSV.
- Prefer source-reported construct correlations over beta-converted path
  coefficients when both are usable for the same target construct pair.
- Use standardized path coefficients only under the Peterson-Brown beta-to-r rule
  when no usable target correlation matrix is reported.
- Preserve source-defined strata and samples; do not pool `S021` T1/T2 or `S121`
  student/teacher rows.
- Record original beta values for beta-converted rows when available.
- Mark `S021` AIAS-4 to `ATT` mapping and `S121` subjective competence to `SE`
  mapping as medium confidence.
- Do not use HTMT, diagonal square-root AVE entries, indirect mediated effects,
  `f Squared` values, interaction terms, cross-time paths, or out-of-scope focal
  technologies as target construct-pair evidence.

## QA Evidence

The freeze audit passed after correcting `S092`:

- target-row count: 74;
- decision-audit row count: 8;
- `r_value` range check: pass;
- required field completeness: pass;
- S021 T1/T2 not pooled: pass;
- S121 student/teacher not pooled: pass;
- excluded/no-value studies absent from target rows: pass;
- Step 5 folder unchanged: pass.

## Post-Freeze Corrections

Post-freeze corrections, if any, must be recorded in
`post_freeze_corrections_20260608.md` with date, reason, affected rows, and
reviewer.
