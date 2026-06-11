# Data Availability Statement

The public repository contains prompts, schemas, scoring rules,
manifest-registered locked model output CSVs, derived scoring outputs,
redacted source-text audit summaries, R/metaSEM readiness and bounded TSSEM
diagnostic outputs, analysis scripts, reporting checklists, and decision records
sufficient to inspect and reproduce the Paper 2 LLM evaluation and
substitution-stability pipeline.

Repository URL: https://osf.io/mkrgd/overview

Raw article PDFs, raw human coder workbooks, row-level PDF text snippets, and
local PDF paths are not redistributed because they are copyrighted or private
project materials. Text artifacts in this archive use placeholder paths rather
than local machine or OneDrive locations. The analysis uses a source-anchored
adjudicated human reference standard derived from human review; public release
of any row-level human reference file must preserve source boundaries and
exclude copyrighted source text.

Downstream MASEM claims require explicit sample-size handling. As of this
archive, the deterministic reconciliation fills numeric `sample_size_numeric`
for 741 of 804 substitution rerun rows. The remaining 63 rows are excluded from
N-weighted TSSEM/MASEM weighting unless a later source check supplies numeric
N. R/metaSEM readiness, eligible-subset inputs, and a bounded core-6
complete-case TSSEM diagnostic are included, but final all-construct/all-row
structural-path or model-fit claims still require the final approved model
specification and documented handling of excluded missing-N rows.
