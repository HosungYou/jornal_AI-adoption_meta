# Paper A ANX-TRU Extended Source Trace

Date: 2026-06-12

## Purpose

This trace answers why `ANX-TRU` could have appeared to have available rows
while still being absent from the legacy 2026-06-05 Paper A primary direct-r
matrix. The search is restricted to CSV/TSV artifacts that the analysis
pipeline can actually consume. Raw XLSX workbooks are preserved as raw coder
records and are not used directly as final model inputs.

## Search Scope

- Current repo: `/Users/newhosung/Academic/2026/AI Adoption Meta Analysis/Git/jornal_AI-adoption_meta`
- OneDrive Paper1/Paper2 working and consensus folders under `/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents`
- Mounted SSD candidate folders: `/Volumes/External SSD/Projects/Meta-Analysis/jornal_AI-adoption_meta; /Volumes/External SSD/Projects/Meta-Analysis/dissertation_AI-adoption_meta; /Volumes/External SSD/Projects/Research/AI-Adoption; /Volumes/External SSD/Projects/GoogleDrive/Academic`

Scanned CSV/TSV files: 2255
Files skipped or unreadable: 0
Raw trace rows including blank/absence traces: 2741
Blank/absence trace rows separated from candidates: 2490
Numeric source-type candidate trace rows: 110
Deduplicated numeric source-type candidates: 10

## Trace Hits by Collection

| collection | rows |
| --- | --- |
| current_repo | 1881 |
| onedrive_documents | 851 |
| ssd:jornal_AI-adoption_meta | 9 |

## Numeric Candidate Hits by Collection

| collection | rows |
| --- | --- |
| current_repo | 87 |
| onedrive_documents | 17 |
| ssd:jornal_AI-adoption_meta | 6 |

## Unique Candidate Classes

| classification | unique_candidates |
| --- | --- |
| beta_path_or_source_statistic_converted_candidate | 3 |
| candidate_review_required | 5 |
| direct_r_like_candidate | 1 |
| latent_source_flagged_candidate | 1 |

## Unique Studies

| study_id | unique_candidates |
| --- | --- |
| S036 | 2 |
| S066 | 3 |
| S102 | 2 |
| S142 | 3 |

## Interpretation

The trace distinguishes evidence presence from primary-model eligibility. A row
can be present in a post-freeze shell, public metadata copy, latent-correlation
stratum, or converted beta/path stratum and still be absent from the 2026-06-05
legacy primary direct-r model-ready file. Therefore `ANX-TRU` should be reported
as a corpus-version and source-type boundary rather than as a simple literature
absence.

For the manuscript spine, the defensible action is to keep `ANX-TRU` in the
main results space as a source-type comparison panel, while not pooling direct-r,
latent, and converted-effect candidates into one primary TSSEM/OSMASEM estimate.

## Outputs

- `data/04_extraction/05_llm_masem_substitution/results/paper_a_anx_tru_source_trace_extended_20260612.csv`
- `data/04_extraction/05_llm_masem_substitution/results/paper_a_anx_tru_unique_candidate_trace_extended_20260612.csv`
