# Paper2 TSSEM Substitution Diagnostic

Date: 2026-06-11

## Scope

- Input file: `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_substitution_rerun_input_n_weighted_eligible_20260611.csv`
- Analysis subset: N-weighted eligible rows after deterministic sample-size reconciliation.
- Constructs: PE, EE, SI, FC, BI, UB.
- Complete-case TSSEM subset: studies reporting all 15 pairwise correlations among these six constructs.
- Structural model: PE, EE, and SI to BI; FC and BI to UB.
- This is a bounded diagnostic rerun, not a final all-construct Paper1 MASEM claim.

## Execution Evidence

- Stage 1 statuses: baseline_primary_human=converged(REM); expert_reviewed_llm_assisted_primary=converged(REM)
- Stage 2 statuses: baseline_primary_human=converged; expert_reviewed_llm_assisted_primary=converged
- Eligible pair rows before complete-case TSSEM filter: baseline_primary_human=506; expert_reviewed_llm_assisted_primary=506
- Pair rows entering complete-case TSSEM after aggregation: baseline_primary_human=225; expert_reviewed_llm_assisted_primary=225
- Studies: baseline_primary_human=15; expert_reviewed_llm_assisted_primary=15
- Maximum absolute delta in pooled correlations between baseline and expert-reviewed LLM-assisted input: 0.00000000

## Claim Boundary

The expert-reviewed LLM-assisted primary input is numerically unchanged relative to the human-reference primary input in this diagnostic subset when high-risk rows are retained rather than autonomously replaced. Any final structural-path or model-fit stability claim must use the final approved model specification and document excluded missing-N rows.

## Output Files

- `paper2_tssem_substitution_stage_summary_20260611.csv`
- `paper2_tssem_substitution_pair_coverage_20260611.csv`
- `paper2_tssem_substitution_pooled_correlations_20260611.csv`
- `paper2_tssem_substitution_pooled_correlation_delta_20260611.csv`
- `paper2_tssem_substitution_stage2_paths_20260611.csv`
- `paper2_tssem_substitution_stage2_fit_indices_20260611.csv`
