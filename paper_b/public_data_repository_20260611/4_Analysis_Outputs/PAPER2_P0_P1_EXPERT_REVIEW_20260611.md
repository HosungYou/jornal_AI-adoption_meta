# Paper2 P0/P1 Expert Review Layer

Date: 2026-06-11

## Boundary

This artifact reviews the P0/P1 numeric and source-risk task-unit queue
against the frozen source-anchored reference packet and task-family rules.
It does not overwrite the frozen human reference standard or raw coder
workbooks. Pointer-only rows are retained with source-risk flags rather
than upgraded to fully source-text-verified rows.

## Scope

- P0/P1 reviewed task units: 1845
- P0_expert_review_numeric_or_masem: 1196
- P1_source_or_human_disagreement_review: 649

## Source Evidence Status

- no_source_required_blank_consensus: 66
- source_evidence_and_locator_present: 1033
- source_pointer_present_no_evidence_text: 746

## PDF Source-Text Audit

All 746 pointer-only source rows were audited against local PDFs. No source PDF
was missing and no PDF text extraction failed. The audit found:

- pdf_text_value_and_pair_terms_found: 245
- pdf_text_value_found_pair_terms_not_on_best_page: 336
- pdf_text_context_found_value_not_found: 163
- pdf_text_no_target_hit: 2

## Review Decisions

- exclude_duplicate_source_trace: 75
- retain_human_reference_model_absent_or_abstained: 363
- retain_human_reference_source_pointer_risk: 375
- retain_human_reference_trace_reviewed: 80
- retain_sensitivity_only_converted_input: 458
- trace_influence_only: 1
- trace_only_no_primary_substitution: 493

## Rerun Roles

- excluded_or_blank_trace: 75
- primary_retained: 363
- primary_retained_source_risk: 375
- primary_retained_trace_risk: 80
- sensitivity_only: 458
- trace_only: 494

## Interpretation

- P0/P1 review did not authorize autonomous numeric replacement for
  high-consequence rows where the primary model abstained, was missing,
  or where the source evidence was pointer-only.
- Converted beta/path/source-statistic rows remain sensitivity inputs.
- Trace-only and duplicate-source rows remain outside primary substitution.
- The PDF source-text audit supports a stronger source-risk triage layer, but
  rows without numeric value hits or pair-term alignment remain manual
  table-review/OCR or final alignment-check candidates before final
  substitution-stability claims.
