# Paper2 Pointer-Only PDF Source-Text Audit

Date: 2026-06-11

## Boundary

This is a row-level PDF text audit for P0/P1 task units that previously had
`source_pointer_present_no_evidence_text`. It does not overwrite the frozen
source-anchored adjudicated human reference standard. Automated text hits are
treated as source-text candidates and retain a final alignment-check boundary.

## Scope

- Pointer-only rows audited: 746
- Unique studies audited: 59

## PDF Text Review Status

- pdf_text_context_found_value_not_found: 163
- pdf_text_no_target_hit: 2
- pdf_text_value_and_pair_terms_found: 245
- pdf_text_value_found_pair_terms_not_on_best_page: 336

## Review Decisions

- no_pdf_text_hit_requires_manual_pdf_table_review_or_ocr: 2
- source_text_candidate_supports_pointer_value_requires_final_human_alignment_check: 245
- source_text_context_found_but_numeric_value_requires_manual_table_review: 163
- source_text_value_found_requires_manual_pair_alignment: 336

## Claim Boundary

Rows with `pdf_text_value_and_pair_terms_found` have candidate source text
support in the local PDF extraction layer, but final manuscript claims should
still cite the source-anchored human reference and preserve the audit file.
Rows without numeric value hits require manual table review or OCR before they
can be upgraded from source-risk status.
