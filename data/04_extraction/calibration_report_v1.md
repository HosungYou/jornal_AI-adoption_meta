# Calibration Analysis Report
**Project**: AI Adoption MASEM  
**Date**: 2026-03-24  
**Coding Manual**: v3.0  
**Release ref**: v0.3.0 (BI/UB + Fornell-Larcker)  
**Calibration studies**: S028, S059, S110, S145, S147, S185, S194, S208, S218, S222 (n=10)  
**Raters**: R1, R2, R3, R4  

---
## Executive Summary

- **STUDY_METADATA**: 6/12 categorical variables at Excellent (κ ≥ 0.80); 5 variables below Substantial (κ < 0.60) → require consensus discussion
- **sample_size ICC**: 1.0000 (Excellent)
- **Correlation coverage (presence/absence) κ**: 0.819 (Excellent) — 94.2% exact pair agreement
- **r_value ICC(2,1)** (n=45 shared 4-rater pairs): 0.9325 (Excellent)
- **Critical r discrepancies** (Δ > 0.01): 14 pairs across 4 studies
- **Minor r discrepancies** (0.001 < Δ ≤ 0.01, rounding): 17 pairs
- **BI vs UB disagreements**: 5 studies (S059, S147, S208, S218, S222)
- **r_source not filled (R4)**: 23 entries

---
## 1. STUDY_METADATA — Inter-Rater Reliability

### 1.1 Categorical Variables (Fleiss' κ)

| Variable | Fleiss κ | Interpretation | % Agreement | Notes |
|----------|----------|----------------|-------------|-------|
| source_type | +1.000 | Excellent | 100% |  |
| study_design | +1.000 | Excellent | 100% |  |
| data_collection ⚠️ | +0.314 | Fair/Poor | 70% | R3 codes "mixed" more liberally |
| theoretical_framework | +0.880 | Excellent | 90% |  |
| sample_type | +1.000 | Excellent | 100% |  |
| country | +0.750 | Substantial | 70% | Adjectival vs nominal forms (Malaysian vs Malaysia) |
| education_level ⚠️ | +0.568 | Moderate | 60% | R3/R4 split "undergraduate" vs "mixed" |
| ai_type | +1.000 | Excellent | 100% |  |
| ai_tool_name ⚠️ | +0.398 | Fair/Poor | 40% | Free-text field; naming conventions vary |
| temporal_period | +1.000 | Excellent | 100% |  |
| user_role ⚠️ | -0.026 | Fair/Poor | 90% | R3 uses "both" vs others "student" |
| common_method_bias ⚠️ | +0.506 | Moderate | 70% | Threshold for "addressed" differs |

**Threshold**: κ ≥ 0.80 = Excellent, 0.60–0.79 = Substantial, 0.40–0.59 = Moderate, < 0.40 = Fair/Poor

### 1.2 Continuous Variable — sample_size

| Variable | ICC(2,1) | Interpretation |
|----------|----------|----------------|
| sample_size | 1.0000 | Excellent |

### 1.3 Detailed Disagreements by Variable

#### user_role (κ = -0.026)

| Study | R1 | R2 | R3 | R4 |
|-------|----|----|----|----|
| S028 | student | student | student | student |
| S059 | student | student | student | student |
| S110 | student | student | student | student |
| S145 | student | student | student | student |
| S147 | student | student | student | student |
| S185 | student | student | student | student |
| S194 | student | student | student | student |
| S208 | student | student | student | student |
| S218 | student | student | student | student |
| S222 ⚠️ | student | student | both | student |

#### data_collection (κ = +0.314)

| Study | R1 | R2 | R3 | R4 |
|-------|----|----|----|----|
| S028 | survey | survey | survey | survey |
| S059 | survey | survey | survey | survey |
| S110 | survey | survey | survey | survey |
| S145 | survey | survey | survey | survey |
| S147 ⚠️ | mixed | survey | mixed | mixed |
| S185 ⚠️ | survey | survey | mixed | survey |
| S194 | survey | survey | survey | survey |
| S208 | survey | survey | survey | survey |
| S218 | survey | survey | survey | survey |
| S222 ⚠️ | survey | survey | mixed | survey |

#### ai_tool_name (κ = +0.398)

| Study | R1 | R2 | R3 | R4 |
|-------|----|----|----|----|
| S028 ⚠️ | Humanoid robots | AI-based humanoid robots | Humanoid robots | Humanoid robots |
| S059 | ChatGPT | ChatGPT | ChatGPT | ChatGPT |
| S110 | ChatGPT | ChatGPT | ChatGPT | ChatGPT |
| S145 ⚠️ | GenAI tools (Gemini mentioned) | ChatGPT | GenAI | ChatGPT |
| S147 ⚠️ | ChatGPT, Gemini | ChatGPT, Gemini | ChatGPT and Gemini | ChatGPT, Gemini |
| S185 | ChatGPT | ChatGPT | ChatGPT | ChatGPT |
| S194 ⚠️ | e-CloudAC (AI Cloud-based applications) | AI and Cloud-Based E-Learning Tools | AI and Cloud-Based Applications and Tools | AI and Cloud-based applications |
| S208 ⚠️ |  | NA | AI | N/A |
| S218 | ChatGPT | ChatGPT | ChatGPT | ChatGPT |
| S222 ⚠️ | AI-supported Smart Learning Environment | AI-supported SLE system | AI-supported smart learning environment (SLE) | AI-supported smart learning environment (SLE) |

#### common_method_bias (κ = +0.506)

| Study | R1 | R2 | R3 | R4 |
|-------|----|----|----|----|
| S028 | not_addressed | not_addressed | not_addressed | not_addressed |
| S059 ⚠️ | not_addressed | partial | not_addressed | not_addressed |
| S110 | not_addressed | not_addressed | not_addressed | not_addressed |
| S145 | not_addressed | not_addressed | not_addressed | not_addressed |
| S147 | not_addressed | not_addressed | not_addressed | not_addressed |
| S185 | addressed | addressed | addressed | addressed |
| S194 ⚠️ | not_addressed | partial | not_addressed | not_addressed |
| S208 | not_addressed | not_addressed | not_addressed | not_addressed |
| S218 ⚠️ | partial | addressed | addressed | not_addressed |
| S222 | not_addressed | not_addressed | not_addressed | not_addressed |

#### education_level (κ = +0.568)

| Study | R1 | R2 | R3 | R4 |
|-------|----|----|----|----|
| S028 | undergraduate | undergraduate | undergraduate | undergraduate |
| S059 ⚠️ | mixed | mixed | undergraduate | undergraduate |
| S110 ⚠️ | mixed | mixed | undergraduate | mixed |
| S145 ⚠️ | mixed | mixed | undergraduate | undergraduate |
| S147 | graduate | graduate | graduate | graduate |
| S185 | undergraduate | undergraduate | undergraduate | undergraduate |
| S194 | undergraduate | undergraduate | undergraduate | undergraduate |
| S208 ⚠️ | mixed | mixed | undergraduate | undergraduate |
| S218 | graduate | graduate | graduate | graduate |
| S222 | undergraduate | undergraduate | undergraduate | undergraduate |

#### country (κ = +0.750)

| Study | R1 | R2 | R3 | R4 |
|-------|----|----|----|----|
| S028 | China | China | China | China |
| S059 | China | China | China | China |
| S110 ⚠️ | Malaysia | Malaysian | Malaysia | Malaysia |
| S145 | Jordan | Jordan | Jordan | Jordan |
| S147 ⚠️ | Egypt | Egyptian | Egypt | Egypt |
| S185 | China | China | China | China |
| S194 | Oman | Oman | Oman | Oman |
| S208 | Jordan | Jordan | Jordan | Jordan |
| S218 | China | China | China | China |
| S222 ⚠️ | Taiwan | China |  | China |

---
## 2. CORRELATIONS — Inter-Rater Reliability

### 2.1 Coverage Summary (pairs with r_value filled)

| Study | R1 | R2 | R3 | R4 | Notes |
|-------|----|----|----|----|-------|
| S028 | 10 | 10 | 10 | 10 |  |
| S059 | 4 | 0 | 6 | 0 | R1/R3: beta-converted; R2/R4: no values extracted |
| S110 | 3 | 3 | 3 | 3 |  |
| S145 | 3 | 3 | 6 | 3 |  |
| S147 | 0 | 0 | 9 | 0 | R1/R2/R4: no values; R3 has 9 pairs |
| S185 | 10 | 10 | 14 | 11 |  |
| S194 | 15 | 15 | 15 | 11 |  |
| S208 | 10 | 10 | 10 | 6 |  |
| S218 | 6 | 6 | 6 | 7 |  |
| S222 | 2 | 0 | 2 | 0 | R1/R3: beta-converted; R2/R4: no values |

**Coverage κ (presence/absence across all 660 slots)**: 0.819 (Excellent), 94.2% pair-level agreement

### 2.2 r_value Agreement (ICC)

| Metric | Value | Interpretation |
|--------|-------|----------------|
| ICC(2,1) for r_values (n=45 4-rater pairs) | 0.9325 | Excellent |
| Critical discrepancies (Δ > 0.01) | 14 pairs | — |
| Minor discrepancies (rounding, 0.001–0.01) | 17 pairs | — |

### 2.3 Critical r_value Discrepancies (Δ > 0.01)

#### S028
| Pair | R1 | R2 | R3 | R4 | Δ | Priority |
|------|----|----|----|----|---|----------|
| ATT–BI | 0.880 | 0.877 | 0.870 | 0.877 | 0.0100 | 🟡 MED |
| ATT–PE | 0.810 | 0.809 | 0.800 | 0.809 | 0.0100 | 🟡 MED |
| BI–EE | 0.630 | 0.627 | 0.620 | 0.627 | 0.0100 | 🟡 MED |
| EE–PE | 0.670 | 0.667 | 0.660 | 0.884 | 0.2240 | 🔴 HIGH |
| EE–SE | 0.790 | 0.792 | 0.790 | 0.702 | 0.0900 | 🟡 MED |
| PE–SE | 0.690 | 0.744 | 0.740 | 0.744 | 0.0540 | 🟡 MED |

#### S110
| Pair | R1 | R2 | R3 | R4 | Δ | Priority |
|------|----|----|----|----|---|----------|
| BI–EE | 0.620 | 0.623 | 0.170 | 0.623 | 0.4530 | 🔴 HIGH |
| BI–PE | 0.680 | 0.681 | 0.190 | 0.681 | 0.4910 | 🔴 HIGH |
| BI–SI | 0.520 | 0.520 | 0.050 | 0.520 | 0.4700 | 🔴 HIGH |

#### S145
| Pair | R1 | R2 | R3 | R4 | Δ | Priority |
|------|----|----|----|----|---|----------|
| BI–UB | 0.340 | 0.338 | 0.330 | 0.338 | 0.0100 | 🟡 MED |

#### S208
| Pair | R1 | R2 | R3 | R4 | Δ | Priority |
|------|----|----|----|----|---|----------|
| EE–SI | 0.360 | 0.632 | 0.360 | 0.362 | 0.2720 | 🔴 HIGH |
| EE–TRU | 0.400 | 0.395 | 0.390 | 0.395 | 0.0100 | 🟡 MED |
| PE–SI | 0.300 | 0.296 | 0.290 | 0.296 | 0.0100 | 🟡 MED |
| PE–TRU | 0.300 | 0.295 | 0.290 | 0.295 | 0.0100 | 🟡 MED |

---
## 3. BI vs. UB Construct Disambiguation (v0.3.0 Focus)

### 3.1 Outcome Construct Assignment by Study

| Study | R1 | R2 | R3 | R4 | Agreement |
|-------|----|----|----|----|-----------|
| S028 | BI | BI | BI | BI | ✓ |
| S059 | BI | — | BI | — | ⚠️ DISAGREE |
| S110 | BI | BI | BI | BI | ✓ |
| S145 | BI+UB | BI+UB | BI+UB | BI+UB | ✓ |
| S147 | — | — | BI+UB | — | ⚠️ DISAGREE |
| S185 | BI | BI | BI | BI | ✓ |
| S194 | BI+UB | BI+UB | BI+UB | BI+UB | ✓ |
| S208 | BI | BI | BI | — | ⚠️ DISAGREE |
| S218 | BI | BI | BI | BI+UB | ⚠️ DISAGREE |
| S222 | BI | — | BI | — | ⚠️ DISAGREE |

### 3.2 Studies Requiring BI/UB Consensus Review

- **S059**: {'R1': ('BI',), 'R2': ('none',), 'R3': ('BI',), 'R4': ('none',)} — requires item-level disambiguation per v0.3.0 framework
- **S147**: {'R1': ('none',), 'R2': ('none',), 'R3': ('BI', 'UB'), 'R4': ('none',)} — requires item-level disambiguation per v0.3.0 framework
- **S208**: {'R1': ('BI',), 'R2': ('BI',), 'R3': ('BI',), 'R4': ('none',)} — requires item-level disambiguation per v0.3.0 framework
- **S218**: {'R1': ('BI',), 'R2': ('BI',), 'R3': ('BI',), 'R4': ('BI', 'UB')} — requires item-level disambiguation per v0.3.0 framework
- **S222**: {'R1': ('BI',), 'R2': ('none',), 'R3': ('BI',), 'R4': ('none',)} — requires item-level disambiguation per v0.3.0 framework

---
## 4. Fornell-Larcker Extraction (v0.3.0 Focus)

**Finding**: No rater used `fornell_larcker_cbsem` or `fornell_larcker_plssem` r_source flags in calibration coding.

### r_source Usage Summary

| Rater | direct | beta_converted | blank/None | FL-sourced |
|-------|--------|----------------|------------|------------|
| R1 | 57 | 6 | 0 | 0 |
| R2 | 57 | 0 | 0 | 0 |
| R3 | 59 | 20 | 2 | 0 |
| R4 | 28 | 0 | 23 | 0 |

> **Action item**: R4 missing r_source for all entries. All raters should review studies using PLS-SEM and apply `fornell_larcker_plssem` or `fornell_larcker_cbsem` as appropriate per v0.3.0 guidance.

---
## 5. Priority Action Items for Consensus Meeting

### 🔴 HIGH PRIORITY (requires group discussion)

| # | Issue | Studies | Raters |
|---|-------|---------|--------|
| 1 | **S110 r_values completely diverge** (R3: BI–EE=0.17 vs others: 0.62) | S110 | R3 vs R1/R2/R4 |
| 2 | **S028 EE–PE outlier** (R4=0.884 vs others≈0.667) | S028 | R4 vs R1/R2/R3 |
| 3 | **S185 BI–SI diverge** (R2=0.216 vs R3/R4=0.433) | S185 | R2 vs R3/R4 |
| 4 | **S208 EE–SI diverge** (R2=0.632 vs others≈0.36) | S208 | R2 vs R1/R3/R4 |
| 5 | **S147 coverage** (R3 has 9 pairs; R1/R2/R4 have 0) | S147 | R1/R2/R4 |
| 6 | **S059/S222 coverage** (R2/R4 have no r_values; R1/R3 beta-converted) | S059, S222 | R2/R4 |

### 🟡 MEDIUM PRIORITY (codebook clarification needed)

| # | Issue | Studies | Recommendation |
|---|-------|---------|----------------|
| 7 | **data_collection** κ=0.314 (R3 over-applies "mixed") | S147, S185, S222 | Clarify threshold for mixed vs survey |
| 8 | **education_level** κ=0.568 (R3/R4 use "undergraduate" vs R1/R2 "mixed") | S059, S110, S145, S208 | Clarify when to use mixed vs specific level |
| 9 | **ai_tool_name** κ=0.398 (free-text normalization) | S028, S145, S147, S194, S208, S222 | Define preferred naming convention |
| 10 | **BI/UB disambiguation** (5 studies disagree on outcome construct) | S059, S147, S208, S218, S222 | Apply v0.3.0 item-level decision framework |
| 11 | **common_method_bias** κ=0.506 | S059, S194, S218 | Clarify threshold for partial vs addressed |

### 🟢 LOW PRIORITY (cosmetic/format)

| # | Issue | Recommendation |
|---|-------|----------------|
| 12 | **country** adjectival forms (Malaysian vs Malaysia) | Standardize to noun form (country name) |
| 13 | **R4 r_source blank** (23 entries) | R4 to backfill r_source for all coded pairs |
| 14 | **Minor r rounding** (0.001–0.01, e.g., 0.88 vs 0.877) | Use 3 decimal places; majority rule on 3rd decimal |
| 15 | **S222 country** (R1: Taiwan, R2/R4: China, R3: blank) | Check paper for clarification |

---
## 6. Overall IRR Summary

| Domain | Metric | Value | Interpretation |
|--------|--------|-------|----------------|
| STUDY_METADATA | Mean Fleiss κ | 0.699 | — |
| STUDY_METADATA | % columns Excellent (κ≥0.80) | 6/12 | — |
| STUDY_METADATA | sample_size ICC(2,1) | 1.0000 | Excellent |
| CORRELATIONS | Coverage κ | 0.819 | Excellent |
| CORRELATIONS | r_value ICC(2,1) | 0.9325 | Excellent |

> **Recommendation**: Overall r_value ICC is Good–Excellent. STUDY_METADATA categorical agreement is adequate for most variables but **3 variables** (data_collection, ai_tool_name, user_role) require codebook revision before Phase 1 proceeds. **6 HIGH priority discrepancies** require immediate consensus resolution.
