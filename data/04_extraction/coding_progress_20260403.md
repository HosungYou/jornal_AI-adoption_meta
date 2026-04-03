# Coding Progress Report
**Project**: AI Adoption MASEM  
**Date**: 2026-04-03  
**Data source**: Google Drive coder packages (downloaded 2026-04-03T17:00 KST)  
**Coding Manual**: v3.0  

---
## 1. Overall Progress

| Metric | Count |
|--------|-------|
| Total unique studies coded (any coder) | 52 |
| Studies with 4-coder overlap (calibration set) | 10 |
| Studies with R1-R2 dual coding | 34 |
| Studies with R3-R4 dual coding | 10 |
| R1-only studies | 6 |
| R4-only studies | 12 |

---
## 2. Per-Coder Summary

### R1 (40 studies done, 3 excluded)
- **STUDY_METADATA**: 37/40 studies with author filled
- **CORRELATIONS**: 327 r-values entered
- **Excluded**: S023, S211, S196
- **Coding Manual**: Updated version (244KB, differs from template)
- **Latest file**: `AI_Adoption_MASEM_Coding_v3_R1.xlsx` (292KB, updated 2026-04-03)

### R2 (34 studies done, 1 excluded)
- **STUDY_METADATA**: 0/34 with author (metadata not yet entered)
- **CORRELATIONS**: 57 r-values entered
- **Excluded**: S211
- **Additional file**: `construct_harmonization.docx` (R2's annotated copy)
- **Latest file**: `AI_Adoption_MASEM_Coding_v3_R2.xlsx` (199KB, updated 2026-04-03)

### R3 (10 studies done, 0 excluded)
- **STUDY_METADATA**: 35 studies with author (includes pre-filled calibration?)
- **CORRELATIONS**: 321 r-values entered
- **Note**: Only calibration set completed so far
- **Latest file**: `AI_Adoption_MASEM_Coding_v3_R3.xlsx` (195KB, updated 2026-04-03)

### R4 (22 studies done, 0 excluded)
- **STUDY_METADATA**: 33 studies with author
- **CORRELATIONS**: 318 r-values entered
- **Note**: 12 unique studies not coded by other raters
- **Latest file**: `AI_Adoption_MASEM_Coding_v3_R4_260402.xlsx` (262KB, updated 2026-04-02)
- **Archived versions**: `_R4.xlsx` (original), `_R4_260326.xlsx` (March 26)

---
## 3. Cross-Coder Overlap Structure

```
4-coder calibration (10 studies):
  S028, S059, S110, S145, S147, S185, S194, S208, S218, S222

R1-R2 dual coding (34 studies = calibration 10 + 24 additional):
  + S009, S015, S018, S019, S023, S030, S038, S042, S046, S053,
    S064, S071, S076, S095, S102, S104, S156, S164, S169, S177,
    S178, S190, S201, S211

R1-only (6 studies):
  S005, S079, S091, S187, S196, S223

R4-only (12 studies):
  S016, S045, S047, S052, S072, S090, S097, S111, S146, S176, S212, S219
```

---
## 4. Observations and Issues

### 4.1 R2 Metadata Gap
R2 has 34 "done" studies but STUDY_METADATA has 0 authors filled. Either R2 is coding correlations-first (valid workflow) or metadata entry was deferred. Needs follow-up.

### 4.2 R4 Multiple File Versions
R4 folder contains 3 xlsx versions. The latest (`_260402`) has the most data (262KB). The original `_R4.xlsx` (188KB) appears to be the initial template. All versions preserved in repo for audit trail.

### 4.3 R3 Low Completion
R3 has only completed the 10-study calibration set. No Phase 1/2 studies started.

### 4.4 Exclusion Discrepancies
- S211: Excluded by both R1 and R2 (consistent)
- S023: Excluded by R1 only (R2 marks as "done")
- S196: Excluded by R1 only (not in R2's assignment)

---
## 5. File Manifest (repo paths)

```
data/04_extraction/coder_packages/
  R1/
    AI_Adoption_MASEM_Coding_v3_R1.xlsx          (292,817 bytes, 2026-04-03)
    AI_Adoption_MASEM_Coding_Manual_v3.docx      (244,849 bytes, 2026-03-20)
    PDFs/  (89 files)
  R2/
    AI_Adoption_MASEM_Coding_v3_R2.xlsx          (199,471 bytes, 2026-04-03)
    AI_Adoption_MASEM_Coding_Manual_v3.docx      (60,545 bytes, 2026-03-13)
    construct_harmonization.docx                  (595,618 bytes, 2026-03-26)
    PDFs/  (88 files)
  R3/
    AI_Adoption_MASEM_Coding_v3_R3.xlsx          (195,359 bytes, 2026-04-03)
    AI_Adoption_MASEM_Coding_Manual_v3.docx      (60,545 bytes, 2026-03-13)
    PDFs/  (88 files)
  R4/
    AI_Adoption_MASEM_Coding_v3_R4.xlsx          (188,628 bytes, 2026-03-20)
    AI_Adoption_MASEM_Coding_v3_R4_260326.xlsx   (258,732 bytes, 2026-03-26)
    AI_Adoption_MASEM_Coding_v3_R4_260402.xlsx   (262,092 bytes, 2026-04-02)
    AI_Adoption_MASEM_Coding_Manual_v3.docx      (60,545 bytes, 2026-03-13)
    PDFs/  (88 files)
```
