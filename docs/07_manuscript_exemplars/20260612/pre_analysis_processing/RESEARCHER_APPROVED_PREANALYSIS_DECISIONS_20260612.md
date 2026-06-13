# Researcher-Approved Pre-Analysis Decisions

Date: 2026-06-12

## Decisions Recorded

1. Missing sample-size rows: approved default rule is to use source-supported
   PDF-recovered analytic/sample N when recoverable; exclude only rows that
   remain unresolved after source checking. Before any final primary exclusion,
   the unresolved rows, exclusion reason, attempted source check, and analytic
   consequence must be shown to the researcher. The 63 residual rows now have
   derived PDF-supported N, so the current 804-row rerun input is N-complete and
   no residual N exclusion is currently being applied.
2. Paper A model boundary: approved and essential. Keep the 10-construct theory
   target, but final claims must follow the matrix/identification evidence.
3. ANX-TRU: approved to mark not estimable only if source tracing confirms no
   defensible primary input. Because the researcher expected more rows, the
   pair was traced across current repo, OneDrive, and mounted SSD CSV/TSV
   analysis artifacts. The trace confirms that many apparent rows are
   blank/absence shell traces or repeated metadata rows; numeric candidates
   compress to S036, S066, S102, and S142 across direct-r-like, latent, and
   converted/source-statistic strata. The SSD copy adds duplicate evidence from
   `combined_coder_values_long_20260525.csv`, but does not add a new model-ready
   primary direct-r candidate beyond the current workspace.
4. Paper B source packets: approved as mandatory. Full-corpus M1-R claims require
   source packets restored or regenerated. The current source-packet gate is
   closed at 194/194 studies for the 2,043-row full-corpus shell.
5. Claude/Gemini: include in the main text. They should be framed as cross-model
   robustness, disagreement, and triage evidence within the workflow-validation
   study, not as vendor ranking.
6. Denominator families: approved. Keep separate denominator-family reporting.
7. Beta/path-converted effects: include in the same main-results space as primary
   extraction for explicit comparison, because the comparison can be a substantive
   methodological contribution for other meta-analyses. They should sit beside
   primary/direct-r results in the manuscript tables, but with source-type labels
   and separate denominators. Do not silently pool converted effects with direct-r
   rows.
8. Claim boundary: approved. Paper B is about source-anchored workflow validation
   and downstream substitution risk, not LLM replacement.

## Implementation Consequence

The claim-carrying table/figure spine must be built around panels and gates:

- Paper A: N eligibility, matrix coverage, ANX-TRU source-type/corpus boundary,
  final estimability decision.
- Paper B: direct-r, latent/source-flagged, beta/path-converted, abstention,
  source-risk, and cross-model robustness panels.
- Downstream: core-6 diagnostic first; all-row/full-10 only after source and
  matrix sufficiency are proven.

## Current Execution State

- PDF-supported N override has been applied only as a derived input; raw
  workbooks and frozen reference files were not overwritten.
- The current matrix audit supports core-6/core-7/core-8 diagnostic lanes, but
  not a complete-case full 10-construct TSSEM/OSMASEM model.
- ANX-TRU is recoverable only as a post-freeze source-type comparison panel in
  the current evidence, not as a legacy primary direct-r matrix rescue.
- Extended ANX-TRU trace output is now available at
  `data/04_extraction/05_llm_masem_substitution/results/PAPER_A_ANX_TRU_SOURCE_TRACE_EXTENDED_20260612.md`.
- The dedicated full-corpus M1-R manifest and nine-shard run script are ready;
  full-corpus accuracy remains unclaimed until those shards are locked and
  exception-aware scored.
- Claude Sonnet and Gemini belong in the main text as cross-model robustness and
  triage evidence from the clean model-explicit package; the Codex source-
  packet-required M1-R branch remains the primary claim-bearing workflow gate
  until equivalent source-packet full-corpus runs are deliberately added.
