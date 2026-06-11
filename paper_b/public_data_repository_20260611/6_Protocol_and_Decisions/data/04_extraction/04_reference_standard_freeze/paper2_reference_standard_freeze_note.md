# Paper2 Reference Standard Freeze Note

Date: 2026-06-05

This packet freezes the current source-audited human reference layer as a tiered reference standard for downstream audit, denominator design, and scoring preparation. It does not claim that all 8,783 task units are one LLM accuracy denominator, and it does not start final LLM accuracy or MASEM substitution analysis because locked LLM outputs are not present.

## Freeze rule

- Raw returned coder workbooks remain preserved as raw returns.
- OneDrive `Paper2_Human_Final_Consensus_20260605_v2` is the canonical Paper2
  human consensus package for Step 5 analysis. This freeze packet is the
  source-audited task eligibility and denominator layer derived for scoring.
- The R1 freeze-candidate/working workbook was updated where R1-owned Phase 2 rows required source-audited freeze handling.
- Final analysis should use the frozen reference layer and decision logs, not silent raw-return overwrites.
- Rows are frozen as trace records, scorable candidates, sensitivity-only evidence, source-pointer-only records, not-derivable records, or excluded records.

## Source decisions

- S014: retained as sensitivity-only beta-converted indirect path evidence through perceived risk; excluded from primary direct-r.
- S021: retained as pre/post path-model evidence; excluded from primary direct-r.
- S056: retained as path-coefficient evidence from Table 3; excluded from primary direct-r.
- S072: ANX-EE r=1.0 excluded from primary and retained only as trace/influence diagnostic.
- S092: retained as SEM/path evidence; excluded from primary direct-r.
- S097, S146, S184: Paper1 source-blank/source-statistic review candidates excluded from primary direct-r and retained only as trace/sensitivity candidates until direct-r source locators are locked.
- S121: retained as latent SEM/path evidence with source-type separation.
- S195/S206: excluded as duplicate same DOI/PDF source with unusable PLSR/component-loading or item-level evidence for construct-level MASEM.
- S202: retained as Fornell-Larcker/path evidence with source-type separation.

## Counts

- Paper1 primary input rows: 822
- Paper1 primary model-ready rows after tiered freeze: 804
- Paper1 primary excluded rows after tiered freeze: 18
- Paper2 task units frozen: 8783

## Paper2 denominator boundary

Do not use 8,783 as a single accuracy denominator. Use `denominator_family` and `scoring_eligibility` in `paper2_llm_task_units_labeled_tiered_freeze_20260605.csv`. Not-derivable rows and source-pointer-only rows remain frozen as trace records but are not scored as final evidence-content accuracy rows.

2026-06-11 addendum: `source_blank_r` rows with a human consensus direct-r value
belong in the primary direct-r extraction family, with evidence-quality flags.
Converted beta/path/source-statistic rows belong in the numeric extraction
evaluation table as an explicit converted/source-type stratum, not silently
pooled with source-reported direct-r rows. S072 ANX-EE `r = 1.0` remains
excluded from primary scoring and retained only as trace/influence diagnostic.

## Locked LLM boundary

No final LLM accuracy, substitution, or empirical validity claim is made in this freeze. Accuracy analysis requires a locked model/run/output file and the scoring rule to be applied by task family.
