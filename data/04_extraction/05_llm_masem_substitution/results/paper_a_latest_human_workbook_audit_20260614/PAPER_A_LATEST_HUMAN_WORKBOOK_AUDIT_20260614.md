# Paper A Latest Human Workbook Audit

Date: 2026-06-14

## Source workbooks

- `R1`: `/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/Coding_Latest_R1_R4_20260605/AI_Adoption_MASEM_Coding_v3_R1_Phase0_1_2_20260425.xlsx`
- `R2`: `/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/Coding_Latest_R1_R4_20260605/AI_Adoption_MASEM_Coding_v3_R2_Phase0_1_2_20260425.xlsx`
- `R3`: `/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/Coding_Latest_R1_R4_20260605/AI_Adoption_MASEM_Coding_v3_R3_Phase0_1_2_20260425.xlsx`
- `R4`: `/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/Coding_Latest_R1_R4_20260605/AI_Adoption_MASEM_Coding_v3_R4_Phase0_1_2_20260425_v2.xlsx`

## Summary

| Dataset | Numeric rows | Studies | Pairs | Missing pairs | Complete full10 studies | Studies with >=15 pairs |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| latest_R1_R4_human_workbooks | 3654 | 181 | 45/45 | 0 | 0 | 64 |
| current_20260612_rerun_input | 796 | 74 | 44/45 | 1 | 0 | 26 |

## Comparison to current 20260612 rerun input

- Latest human workbook study-pair cells not represented in current input: 1236
- Current input study-pair cells not represented in latest raw human workbook rows: 57
- Exact study-pair-value rows from latest workbooks absent from current input: 1991

## Interpretation

The provided Drive folder is not sufficient as the final human-value source because Drive search and local OneDrive traces show later modified R1/R2/R3 files and an R4 v2 file. The latest local read-only copies under `Coding_Latest_R1_R4_20260605` should be treated as the first candidate final human-workbook set for this audit.
This audit does not yet prove PDF/source correctness. It only establishes whether the current analytic input appears to omit or transform rows relative to the latest human workbook set.
