# Paper2 MASEM Sample-Size PDF Override

Date: 2026-06-12

## Boundary

This is a derived post-reconciliation input. It does not overwrite raw
coder workbooks, frozen reference files, or the 2026-06-11 deterministic
sample-size reconciliation. It applies the researcher-approved default
recommendation: use PDF source-supported study-level analytic/sample N
for residual rows when the source check supplies defensible N.

## Result

- Input rows: 804
- Rows with `sample_size_numeric` after PDF override: 804
- Rows missing `sample_size_numeric` after PDF override: 0
- N-weighted eligible rows written: 804

## PDF Override Status Counts

- applied_pdf_recovered_study_level_n: 63
- not_needed_existing_source_supported_n: 741

## Study-Level PDF Overrides Applied

- S028: 10 rows
- S100: 2 rows
- S145: 6 rows
- S185: 14 rows
- S194: 15 rows
- S208: 10 rows
- S218: 6 rows

## Claim Boundary

The N-coverage blocker is closed for this derived input: every row now
has a numeric sample-size candidate. This does not by itself authorize
final all-construct TSSEM/OSMASEM claims. Those claims still require the
separate matrix sparsity, identification, model-specification, and
source-type boundary gates.

## Inputs

- `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_substitution_rerun_input_n_reconciled_20260611.csv`
- `docs/07_manuscript_exemplars/20260612/pre_analysis_processing/paper_a_residual_n_source_check_20260612.csv`

## Outputs

- `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_substitution_rerun_input_n_pdf_override_20260612.csv`
- `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_substitution_rerun_input_n_weighted_all_source_supported_20260612.csv`
- `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_sample_size_pdf_override_20260612.csv`
- `data/04_extraction/05_llm_masem_substitution/results/paper2_masem_sample_size_pdf_override_summary_20260612.csv`
