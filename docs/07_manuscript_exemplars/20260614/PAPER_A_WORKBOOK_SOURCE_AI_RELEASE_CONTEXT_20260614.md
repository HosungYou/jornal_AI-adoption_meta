# Paper A Latest Workbook, Source Evidence, and AI Procedure Context

Date: 2026-06-14

## Why this note exists

This note records the correction after the researcher flagged that the earlier sparse-matrix conclusion did not match prior documentation. The correction is material: the supplied Drive folder was accessible but was not the final/latest human workbook source by itself. A later local OneDrive/SSD collection under `Meta/AI Adoption/Coding_Latest_R1_R4_20260605` contains the latest candidate R1-R4 read-only workbook set, including the R4 v2 workbook.

## Workbook state

The latest candidate R1-R4 workbooks were copied into the repo as a non-overwriting read-only snapshot:

- `data/04_extraction/01_raw_human_coder_data_freeze/phase2/latest_R1_R4_read_only_copies_20260614/`
- `data/04_extraction/01_raw_human_coder_data_freeze/phase2/latest_R1_R4_read_only_copies_20260614/LATEST_R1_R4_READ_ONLY_COPY_MANIFEST_20260614.csv`

Boundary: raw workbook snapshots are provenance inputs. Manuscript claims should use extracted, source-anchored, and adjudicated derivatives rather than treating raw coder cells as automatically final.

## Corrected Paper A matrix state

The latest-human-workbook extraction produced 3,654 numeric target-construct rows, 181 studies, and all 45/45 full10 construct-pair cells at the corpus level. This supersedes the earlier 44/45 pair-coverage statement from the reduced analytic input.

The full10 primary route remains blocked for final Stage 2 MASEM claims because no individual study has a complete 10-construct matrix. In the source-evidence audit, the highest single-study full10 coverage was 28/45 pairs and complete full10 study matrices remained 0.

The trust6 reduced complete-case diagnostic remains the currently converged route, with 8 positive-definite complete-case studies and local PDF/source support. It should be labeled diagnostic or sensitivity, not as a replacement for the full10 primary-theory route.

## PDF/source-level evidence collection

A full latest-human row-level source/PDF audit was run and written to:

- `data/04_extraction/05_llm_masem_substitution/results/paper_a_human_ai_source_evidence_audit_20260614/PAPER_A_HUMAN_AI_SOURCE_EVIDENCE_AUDIT_20260614.md`
- `data/04_extraction/05_llm_masem_substitution/results/paper_a_human_ai_source_evidence_audit_20260614/paper_a_latest_human_full_pdf_source_value_audit_20260614.csv`
- `data/04_extraction/05_llm_masem_substitution/results/paper_a_human_ai_source_evidence_audit_20260614/paper_a_latest_human_source_pdf_review_candidates_20260614.csv`
- `data/04_extraction/05_llm_masem_substitution/results/paper_a_human_ai_source_evidence_audit_20260614/paper_a_full10_high_coverage_densification_candidates_20260614.csv`

Automated evidence counts:

- Latest-human numeric rows audited: 3,654
- Studies represented: 181
- Construct pairs represented: 45
- Rows with source packet present: 3,224/3,654
- Rows with coded value found in source-packet text: 2,681/3,654
- Rows with local PDF present and readable by `pdftotext`: 3,565/3,654
- Rows with coded value found in PDF text: 3,174/3,654

Boundary: missing string hits do not prove miscoding. PDF tables can split values, drop leading zeroes, or render row/column labels poorly. Positive hits support source visibility; negative hits become manual source-review or densification candidates.

## AI coding procedure boundary

The AI coding procedure was not identical to the human coding procedure.

Human coding used independent coder workbooks, pairwise disagreement review, and source-anchored adjudication before freezing the human reference. The AI `M1-R` condition used post-freeze source packets and locked-output schemas keyed to the frozen reference task shell. This is appropriate for Paper B/Paper C validation because the AI output should be compared against, not used to create, the human reference standard.

For Paper A, the defensible primary premise is the source-anchored human/reference extraction. AI-derived or AI-assisted rows can support substitution/sensitivity diagnostics only when they remain locked, source-packet-based, denominator-family separated, and compared against the frozen human reference.

Post-freeze AI procedure evidence:

- Task-shell rows: 2,043
- Target studies: 194
- Source-packet coverage for target studies: 194/194
- Registered locked M1-R output files: 9
- Scored row-file rows: 2,043
- Exception-layer score rows: 2,043

## Recommended next work

1. Freeze the Paper A analytic input built from latest-human-workbook rows with explicit inclusion/provenance rules.
2. Use `paper_a_full10_high_coverage_densification_candidates_20260614.csv` to target source-level densification for high-coverage studies first.
3. Use `paper_a_latest_human_source_pdf_review_candidates_20260614.csv` to manually review rows where neither source-packet text nor PDF text found the coded value.
4. Keep full10 as the theory target, but do not claim final full10 Stage 2 path/fit/indirect estimates until an estimable full10 matrix route exists.
5. Report trust6 complete-case MASEM only as reduced diagnostic/sensitivity unless the researcher explicitly changes the Paper A primary route.
