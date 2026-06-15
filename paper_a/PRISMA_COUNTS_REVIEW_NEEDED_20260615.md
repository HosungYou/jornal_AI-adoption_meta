# Paper A PRISMA counts review needed

Updated: 2026-06-15

## Why this file exists

The current repository contains enough evidence to start a PRISMA 2020 flow diagram, but not enough aligned evidence to finalize it. A final PRISMA figure should not be generated until the team confirms the source-of-truth counts.

## Confirmed from local source files

| PRISMA item | Count | Source |
| --- | ---: | --- |
| Records identified from databases | 22,166 | `data/01_identification/dedup_report.txt`; `data/01_identification/merged_all_databases.csv` |
| Duplicate records removed | 5,977 | `data/01_identification/dedup_report.txt` |
| Unique records after deduplication | 16,189 | `data/01_identification/dedup_report.txt`; `data/01_identification/deduplicated_16189.csv` |
| Human-reviewed records | 657 | `data/02_screening/screening_summary.json`; `data/02_screening/human_screening_results_consolidated.csv` |
| Human-reviewed included records | 225 | `data/02_screening/screening_summary.json`; `data/02_screening/human_screening_results_consolidated.csv` |
| Human-reviewed excluded records | 432 | `data/02_screening/screening_summary.json`; `data/02_screening/human_screening_results_consolidated.csv` |

## Count conflict to resolve

| Location | Count/status |
| --- | ---: |
| Root `README.md` historical status | 224 included |
| `data/02_screening/screening_summary.json` | 225 included |
| `data/02_screening/human_screening_results_consolidated.csv` | 225 rows coded `I` |
| Previous `paper_a/README.md` | final included TBD |

Recommended resolution rule: use the current screening source files as provisional evidence (`225 included`) unless the team identifies one duplicate/sample exclusion that explains the earlier `224`.

## PRISMA boxes still requiring confirmation

- Records excluded before title/abstract screening.
- Records screened at title/abstract level after AI/human workflow consolidation.
- Records excluded at title/abstract screening.
- Reports sought for retrieval.
- Reports not retrieved.
- Full-text reports assessed for eligibility.
- Full-text reports excluded with reasons.
- Final studies included in qualitative/systematic review.
- Final studies included in MASEM analysis.
- Total sample size and total extracted correlation pairs.

## Current decision

Do not present a finalized PRISMA 2020 flow diagram in the manuscript yet. Generate a draft PRISMA figure only after the team confirms the boxes above.

