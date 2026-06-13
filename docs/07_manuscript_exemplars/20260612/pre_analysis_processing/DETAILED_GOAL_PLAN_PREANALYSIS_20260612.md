# Detailed Goal Plan: Pre-Analysis Processing Before Manuscript Spine Redesign

Date: 2026-06-12

## G001: Lock Pre-Analysis Contract

Status: completed for current decisions; keep open only for later scope changes.

Deliverables:

- `PRE_ANALYSIS_PROCESSING_CONTRACT_20260612.md`
- Paper A N/matrix gate
- Paper B denominator/source-packet gate

Completion evidence:

- Contract lists accepted decisions and non-claims.
- Gate reports are generated from current authoritative files.

## G002: Paper A Source-Supported N Reconciliation

Status: completed for the derived 804-row rerun input.

Deliverables:

- Adopt and verify the existing deterministic N reconciliation table.
- Residual 7-study missing-N source/PDF check queue with row-level reasons.
- Researcher-facing confirmation packet before final primary exclusion of unresolved N rows.
- Rebuilt primary model input or subset input with `primary_n_status`.

Completion evidence:

- Rows entering the derived 804-row TSSEM/OSMASEM input have numeric N and provenance.
- The residual 63 rows were not silently excluded; PDF source checking supplied defensible study-level N in a derived override file.
- Raw workbooks and frozen reference files remain untouched.
- Any future row still lacking source-supported numeric N must be shown to the
  researcher with source-check reason and analytic consequence before final
  primary exclusion.

## G002B: Paper A ANX-TRU Rescue/Boundary Audit

Status: completed as a source-type boundary panel; not completed as a legacy-primary full-model rescue.

Deliverables:

- ANX-TRU source trace across the 2026-06-05 Paper A package, the 2026-06-09 full-corpus reference, OneDrive, and mounted SSD copies.
- Decision whether ANX-TRU is not estimable in final Paper A, or recoverable through a post-freeze full-corpus rebuild/source-type panel.

Completion evidence:

- `ANX-TRU` is no longer treated as a generic 0-row absence without source/corpus explanation.
- Recovered post-freeze rows are assigned to direct-r-like, latent/source-flagged, or converted-effect strata before modeling.
- Direct-r, latent, and converted-effect candidates are compared as a main results source-type panel and are not silently pooled into the legacy primary estimate.
- Extended repo/OneDrive/SSD CSV tracing confirms that apparent high row volume
  mostly reflects blank/absence shell rows and repeated metadata traces; numeric
  candidates compress to S036, S066, S102, and S142, with SSD evidence duplicating
  existing combined-coder rows rather than adding a new primary model-ready row.

## G003: Paper A Matrix/Identification Audit

Status: completed for the current N-complete derived input.

Deliverables:

- Construct-pair coverage heatmap data.
- Study-level matrix completeness data.
- Core-plus-extension recommendation if full 10-construct model is not estimable.

Completion evidence:

- Full 10-construct complete-case TSSEM/OSMASEM is not identified from the current legacy primary direct-r matrix because `ANX-TRU` is absent.
- Core-6, core-7, and core-8 remain the immediate bounded diagnostic lanes.

## G004: Paper B Full-Corpus Source-Packet Restoration

Status: completed for the 194-study / 2,043-row full-corpus shell.

Deliverables:

- 194-study source-packet coverage check.
- Missing-packet exception list if any packet cannot be restored.

Completion evidence:

- M1-R can run with `--require-source-packet`; the current missing-packet count is 0.
- A dedicated empty full-run manifest and nine-shard command script have been generated.

## G005: Paper B Exception-Aware M1-R Scoring

Status: ready for execution; not yet claim-complete.

Deliverables:

- Larger/full M1-R locked output shards.
- Exception-aware scoring outputs by denominator family.
- Abstention/source-risk/not-derivable reporting strata.
- Main-text cross-model comparison for Codex, Claude Sonnet, and Gemini, framed as robustness/triage rather than vendor ranking.
- Main-results comparison panel for beta/path-converted effects beside direct-r/latent rows, without pooled-denominator claims.
- Converted beta/path/source-statistic rows should remain in the same main-results
  table spine as primary numeric extraction, because the source-type comparison
  itself is a methodological result with implications for other meta-analyses.

Completion evidence:

- RQ1-RQ3 can be reported without pooled heterogeneous denominators only after the dedicated full-run manifest is locked and exception-aware scored.
- The next executable gate is the nine-shard full-corpus M1-R run, followed by `score_full_corpus_m1_r_with_exception_layer.py`.

## G006: Downstream Substitution Diagnostic Gate

Status: partially completed for core-6; full-10/all-row claims blocked.

Deliverables:

- Core-6 diagnostic update.
- Full-10/all-row eligibility decision.
- Delta tables for pooled r, paths, indirect effects, fit, and claim consequences where estimable.

Completion evidence:

- RQ4 is populated only within verified eligibility boundaries.

## G007: Claim-Carrying Table/Figure Spine Redesign

Status: not started; must consume only closed or explicitly bounded gates.

Deliverables:

- Paper A table/figure specification.
- Paper B table/figure specification.
- Source-data and script path for every table/figure.

Completion evidence:

- Every main table/figure has a named RQ, input data, script/output, and claim boundary.

## G008: Full Manuscript Rebuild

Status: not started for the revised claim-carrying version.

Deliverables:

- Paper A target-journal draft with real result tables/figures or explicit diagnostic boundary.
- Paper B target-journal draft with denominator-family results and source-governed limitations.
- Team writing briefs for Literature Review and Discussion only.

Completion evidence:

- No result placeholder is presented as a manuscript claim.
