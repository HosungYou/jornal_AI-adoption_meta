# Paper2 MASEM Sample-Size Reconciliation

Date: 2026-06-11

## Boundary

This reconciliation does not overwrite raw coder workbooks or the frozen
human reference standard. It creates a derived MASEM rerun input that
copies source-supported `n` values from the 2026-06-09 frozen full-corpus
reference where the mapping is deterministic.

## Result

- Input rows: 804
- Rows with `sample_size_numeric` after reconciliation: 741
- Rows missing `sample_size_numeric` after reconciliation: 63
- N-weighted eligible rows written: 741

## Reconciliation Status Counts

- filled_from_full_corpus_reference_pair: 626
- filled_from_full_corpus_reference_study_unique: 24
- filled_from_s121_stratum_reference: 42
- missing_n_excluded_from_n_weighted_masem: 63
- retained_existing_input_n: 49

## Missing-N Exclusion Rule

The approved missing-N rule excludes rows that still lack source-supported `sample_size_numeric` after this deterministic merge from N-weighted TSSEM/MASEM weighting until a later PDF-level source check supplies N. They remain available for extraction/scoring audit, unweighted descriptive summaries, or explicitly labeled sensitivity diagnostics.

Do not describe analyses using this eligible file as all-row SEM.
Use `N-eligible subset` or `source-supported N-weighted subset` unless
source-supported numeric N has been completed for every SEM input row.

## Remaining Missing-N Studies

- S028: 10 rows
- S100: 2 rows
- S145: 6 rows
- S185: 14 rows
- S194: 15 rows
- S208: 10 rows
- S218: 6 rows

## Outputs

- `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_substitution_rerun_input_n_reconciled_20260611.csv`
- `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_substitution_rerun_input_n_weighted_eligible_20260611.csv`
- `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_sample_size_reconciliation_20260611.csv`
- `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_sample_size_reconciliation_summary_20260611.csv`
