# Paper A Human/AI Source Evidence Audit

Date: 2026-06-14

## Scope

This audit documents the 2026-06-14 correction after the latest-human-workbook recheck. It is share-safe: PDFs, source packets, and raw model transcripts are not copied into the tracked output. The audit records whether local source packets/PDF text exist and whether coded numeric values are visible in extracted text.

## Human coding evidence

- Latest-human numeric target rows audited: 3654
- Studies represented: 181
- Construct pairs represented: 45
- Rows with source packet present: 3224/3654
- Rows with coded value found in source-packet text: 2681/3654
- Rows with local PDF present: 3565/3654
- Rows with `pdftotext` status `ok`: 3565/3654
- Rows with coded value found in PDF text: 3174/3654

Important boundary: a missing string hit is not proof that the coding is wrong. PDF tables split values, remove leading zeroes, or render rows/columns in ways that defeat simple text search. Positive hits are supportive evidence; negative hits become source-level review candidates.

## Full10 densification status from latest human workbooks

- Paper A full10 pair universe audited: 45 pairs
- Studies with at least one full10 pair: 181
- Complete full10 study matrices: 0
- Highest observed full10 pair count in one study: 28

## AI coding procedure evidence

- Post-freeze Step 5 task-shell rows: 2043
- Post-freeze target studies: 194
- Source-packet files available: 194
- Task-shell studies with matching source packets: 194/194
- Locked M1-R model-output files registered: 9
- Scored row file rows: 2043
- Exception-layer score rows: 2043

## Procedure-equivalence judgment

The AI coding procedure was not identical to the human coding procedure. Human coding used independent coder workbooks, pairwise disagreement review, and source-anchored adjudication before freezing the human reference. The AI M1-R condition used post-freeze source packets and locked-output schemas keyed to the frozen reference task shell. That design is appropriate for Paper B/Paper C validation because it prevents AI outputs from defining the reference standard.

For Paper A, the defensible primary premise is the source-anchored human/reference extraction, not that AI followed the same procedure as the human coders. AI-derived or AI-assisted rows can support substitution/sensitivity diagnostics only when they remain locked, source-packet-based, denominator-family separated, and compared against the frozen human reference.

## Generated artifacts

- `paper_a_latest_human_full_pdf_source_value_audit_20260614.csv`
- `paper_a_latest_human_full_pdf_source_value_audit_summary_20260614.csv`
- `paper_a_full10_latest_human_densification_gaps_20260614.csv`
- `paper_a_ai_procedure_evidence_summary_20260614.csv`
