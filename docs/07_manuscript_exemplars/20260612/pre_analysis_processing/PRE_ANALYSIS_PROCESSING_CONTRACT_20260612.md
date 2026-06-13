# Pre-Analysis Processing Contract

Date: 2026-06-12

## Purpose

This contract locks the pre-analysis processing decisions that must be completed before claim-carrying table and figure spine redesign. It converts the researcher's accepted recommendations into executable gates.

## Paper A Decisions

1. Primary N rule: use pairwise source-supported N when available; otherwise use source-supported analytic sample N.
2. Rows without recoverable N: report the row-level source-check reason,
   attempted recovery path, and expected analytic consequence to the researcher
   before final primary exclusion; if still unresolved, exclude from primary
   N-weighted TSSEM/OSMASEM and retain in sensitivity/readiness ledgers only.
3. Construct scope: keep the 10 constructs as the theory target.
4. Model strategy: run matrix sparsity/identification audit before deciding whether final analysis can support the full 10-construct model or needs a staged core-plus-extension structure.
5. Converted beta/path/source-statistic rows: keep in the main results space as a source-type comparison panel beside primary direct-r evidence, but do not silently pool them into the direct-r primary estimate.
6. ANX-TRU: do not treat the current 0-row primary result as simple absence until corpus-version and source-type rescue checks are reported. Extended repo/OneDrive/SSD CSV tracing shows many apparent rows are blank/absence shell traces or repeated metadata; numeric candidates compress to S036, S066, S102, and S142 across direct-r-like, latent, and converted/source-statistic strata. Current trace shows post-freeze full-corpus candidates that are outside the 2026-06-05 primary direct-r freeze.

## Paper B Decisions

1. Corpus: use the post-freeze 213-study full-corpus Step 5 universe.
2. Denominators: keep direct-r, latent/source-flagged, beta/path-converted, source-absence/not-derivable, duplicate-source, and status-only strata separate.
3. Source packets: restore/regenerate full private source-packet coverage before full-corpus M1-R accuracy claims.
4. Main-text model comparison: Codex M1-R remains the primary workflow condition, while Claude Sonnet and Gemini must appear in the main text as cross-model robustness/triage evidence. The framing is workflow validation, not vendor ranking.
5. Exception layer: S009/S010 exception logic must be consumed in the scoring pass.
6. Abstention: count abstention on scorable rows as incorrect and report separately as workflow behavior.
7. Converted-effect comparison: beta/path-converted rows belong in the main results space alongside primary numeric extraction as a separate comparison panel. They must not be silently pooled with direct-r rows, but the comparison itself is a substantive finding because it shows how source-type recovery choices can affect downstream meta-analytic evidence.
8. Downstream substitution: run core-6 diagnostic first; full-10/all-row substitution claims require matrix/N/coverage sufficiency.
9. Claim boundary: Paper B is a source-anchored workflow validation and downstream substitution-risk study, not an LLM replacement paper.

## Current Gate Snapshot

| gate | current_state | status |
| --- | --- | --- |
| Paper A N/matrix | 804/804 rows in the derived MASEM rerun input now carry numeric N after approved PDF source-supported override; 0 complete 10-construct studies | pdf_n_override_applied_derived_input_full10_not_identified |
| Paper A ANX-TRU | 2,255 CSV/TSV files scanned across repo/OneDrive/SSD; 2,490 blank/absence traces separated; numeric candidates compress to 4 studies: S036 direct-r-like, S102 latent, S066/S142 converted/source-statistic | source_type_panel_ready_do_not_pool_with_legacy_primary |
| Paper B source packets | 194/194 private packets present | source_packet_gate_closed_full_run_ready |
| Paper B denominator shell | 2043 full-corpus task rows split into 697 direct/source-r, 931 latent/source-flagged, and 415 beta/path-converted rows | dedicated_manifest_and_9_shard_plan_ready |
| Paper B exception layer | 15 exception-layer rows | must_be_consumed_by_larger_scoring_pass |

## Non-Claims Until Gates Close

- Do not claim Paper A final path estimates, indirect effects, or fit.
- Do not claim Paper B full-corpus M1-R accuracy.
- Do not claim all-row or full-10 downstream substitution stability.
- Do not pool Paper B heterogeneous task units into one accuracy denominator.

## Next Execution Order

1. Execute the dedicated Paper B full-corpus M1-R shards only with source packets required and source quotes suppressed.
2. Apply exception-aware scoring to the dedicated full-corpus M1-R manifest.
3. Produce Paper B denominator-family and source-type comparison tables; do not use one pooled denominator.
4. Use Paper A core-6/core-7/core-8 as the immediate SEM diagnostic lane unless a source-type-approved full model rebuild is specified.
5. Produce claim-carrying table/figure specifications from closed gates only.
