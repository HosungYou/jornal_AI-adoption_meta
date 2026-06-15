# Paper A PRISMA counts lock

Updated: 2026-06-15

## Current lock

The previous `224` versus `225` discrepancy is explained by one duplicate DOI among the 225 included screening rows. The current working lock is therefore:

- 225 included screening rows.
- 1 duplicate included DOI row merged.
- 224 unique included reports/studies for PRISMA reporting, pending final team review.

## Locked counts

| PRISMA item | Count | Source/logic |
| --- | --- | --- |
| Records identified from databases | 22166 | `data/01_identification/dedup_report.txt` |
| Duplicate records removed | 5977 | `data/01_identification/dedup_report.txt` |
| Records after deduplication | 16189 | `data/01_identification/dedup_report.txt` |
| Records screened | 16189 | deduplicated records entering AI-assisted screening |
| Records excluded before human review | 15532 | 16,189 unique records minus 657 human-reviewed records |
| Human-reviewed records | 657 | `data/02_screening/human_screening_results_consolidated.csv` |
| Human-reviewed excluded rows | 432 | screening_decision = X |
| Human-reviewed included rows | 225 | screening_decision = I |
| Duplicate included DOI rows merged | 1 | included DOI duplicate audit |
| Unique included reports/studies | 224 | 225 included rows - 1 duplicate DOI row |

## Duplicate included DOI audit

- DOI `10.48009/3_iis_2024_119` has 2 included rows: REC_14749 (Tab3_R1, 2024) Examining generative artificial intelligence adoption in academia: a UTAUT perspective; REC_12567 (Tab3_R1, 2024) Impact and Perspectives of Generative Artificial Intelligence in Higher Education: A Study on Lecturers' Perception and Adoption using the AETGE/GATE Model; Impacto y Perspectivas de la Inteligencia Artificial Generativa en la Educación Superior: Un Estudio sobre la Percepción y Adopción Docente usando el modelo AETGE/GATE

## Human exclusion-code counts

| Exclude code | Count |
| --- | --- |
| E-FT1 | 12 |
| E-FT2 | 96 |
| E-FT3 | 136 |
| E-FT6 | 30 |
| E12 | 3 |
| E7 | 3 |
| not_coded | 152 |

## Included rows by source

| Source | Included rows |
| --- | --- |
| Tab1_IRR | 37 |
| Tab2_AutoINC_R1 | 135 |
| Tab2_Blue | 14 |
| Tab3_R1 | 39 |

## Included rows by year

| Year | Included rows |
| --- | --- |
| 2022 | 4 |
| 2023 | 9 |
| 2024 | 60 |
| 2025 | 151 |
| 2026 | 1 |

## Boundary

This lock is sufficient for a draft PRISMA 2020-style flow diagram. Before journal submission, the team should confirm whether the two duplicate-DOI rows represent the same report, a metadata error, or two distinct reports sharing a DOI.
