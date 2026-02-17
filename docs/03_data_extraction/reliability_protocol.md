# Inter-Coder Reliability Protocol

## Overview

This protocol ensures that data extraction is consistent, accurate, and reproducible across coders. High inter-coder reliability (ICR) demonstrates that our coding procedures are objective and replicable.

---

## 1. Reliability Strategy

### 1.1 Why Measure ICR?

**Scientific Rigor:**
- Demonstrates coding decisions are systematic, not arbitrary
- Shows findings are replicable by independent coders
- Identifies ambiguous coding rules that need clarification

**Meta-Analysis Standards:**
- PRISMA guidelines recommend reporting ICR for systematic reviews
- Cochrane Handbook requires ICR for risk of bias assessments
- Establishes trust in data quality

---

### 1.2 ICR Approach

**20% Stratified Sample:**
- Representative subset of all included studies
- Two independent human coders
- Compare AI extractions to human coding
- Calculate reliability metrics

**Dual Comparison:**
1. **Human-Human Reliability:** Do two human coders agree?
2. **AI-Human Reliability:** Does AI consensus match human coding?

---

## 2. Sampling Strategy

### 2.1 Sample Size

**Target:** 20% of total included studies

**Rationale:**
- PRISMA recommends 10-20% for ICR
- 20% provides robust estimates with 95% confidence intervals
- Balances thoroughness with feasibility

**Examples:**
- If k=100 studies → ICR sample = 20 studies
- If k=150 studies → ICR sample = 30 studies
- If k=200 studies → ICR sample = 40 studies

---

### 2.2 Stratified Random Sampling

**Stratification Dimensions:**

**1. Publication Year (3 strata):**
- Early period: 2015-2019 (early AI adoption research)
- Middle period: 2020-2022 (pre-ChatGPT)
- Recent period: 2023-2025 (generative AI era)

**Rationale:** Construct operationalizations may evolve over time; ensure representation across periods.

**2. AI Tool Type (4 strata):**
- Chatbot/LLM (ChatGPT, Copilot, etc.)
- Intelligent Tutoring System / Adaptive Learning
- LMS-AI / Auto-grading / Writing Assistant
- Other/Mixed

**Rationale:** Different educational AI tools may have different reporting conventions and adoption dynamics.

**3. Education Level (3 strata):**
- K-12
- Undergraduate
- Graduate / Mixed

**Rationale:** Adoption patterns and construct operationalizations differ by educational level.

**4. Geographic Region (4 strata):**
- North America
- Europe
- Asia
- Other (South America, Africa, Oceania, Multi-region)

**Rationale:** Cultural differences may affect construct labeling and measurement in educational contexts.

---

### 2.3 Sampling Procedure

**Step 1: Create Sampling Frame**

```r
library(dplyr)

# Load all included studies
studies <- read.csv("data/included_studies.csv")

# Assign strata
studies <- studies %>%
  mutate(
    year_stratum = case_when(
      year <= 2019 ~ "early",
      year <= 2022 ~ "middle",
      year >= 2023 ~ "recent"
    ),
    ai_tool_stratum = ai_tool_type,    # Already coded
    edu_level_stratum = education_level, # Already coded
    region_stratum = region              # Already coded
  )
```

**Step 2: Proportional Allocation**

```r
# Calculate strata proportions
strata_props <- studies %>%
  group_by(year_stratum, ai_tool_stratum, edu_level_stratum, region_stratum) %>%
  summarize(n = n()) %>%
  mutate(proportion = n / sum(n))

# Allocate ICR sample proportionally
target_icr_n <- ceiling(nrow(studies) * 0.20)  # 20%

icr_allocation <- strata_props %>%
  mutate(icr_n = ceiling(proportion * target_icr_n))
```

**Step 3: Random Selection**

```r
set.seed(20260315)  # Fixed seed for reproducibility

icr_sample <- studies %>%
  group_by(year_stratum, ai_tool_stratum, edu_level_stratum, region_stratum) %>%
  sample_n(size = min(n(), icr_n_for_this_stratum), replace = FALSE) %>%
  ungroup()

# Save ICR sample list
write.csv(icr_sample, "data/icr_sample.csv", row.names = FALSE)
```

---

## 3. Coder Training

### 3.1 Training Timeline

**Session 1: Orientation (3 hours)**
- Review coding manual (all sections)
- Discuss construct definitions
- Review harmonization rules
- Practice construct mapping with examples

**Session 2: Pilot Coding (4 hours)**
- Independently code 5 pilot studies (not in final ICR sample)
- Code correlations, construct mappings, moderators
- Compare results in group session
- Discuss discrepancies and clarify rules

**Session 3: Calibration (2 hours)**
- Calculate pilot ICR metrics (κ, ICC)
- If ICR below threshold: Additional training and re-pilot
- If ICR meets threshold: Proceed to production coding
- Finalize coding procedures and decision rules

**Total Training Time:** ~9 hours per coder

---

### 3.2 Training Materials

**Required Reading:**
1. Coding Manual (docs/03_data_extraction/coding_manual.md)
2. Correlation Extraction Guide (docs/03_data_extraction/correlation_extraction_guide.md)
3. Construct Harmonization Guide (docs/03_data_extraction/construct_harmonization.md)
4. Inclusion/Exclusion Criteria (docs/02_study_selection/inclusion_exclusion_criteria.md)

**Practice Studies:**
- 5 pilot studies with diverse characteristics:
  - 1 TAM study of student ChatGPT adoption with clear labeling
  - 1 UTAUT study of instructor AI tool adoption with standard constructs
  - 1 AI-specific study measuring trust/anxiety in educational AI
  - 1 study with only β coefficients (SEM-based, no correlation matrix)
  - 1 study with ambiguous construct labels (e.g., "AI Value", "System Quality")

---

### 3.3 Coder Qualifications

**Minimum Requirements:**
- Graduate student in educational technology, information systems, psychology, or related field
- Familiarity with TAM/UTAUT literature and educational technology adoption
- Experience reading empirical research articles in education or IT
- Basic statistical knowledge (understand correlation, regression)

**Preferred:**
- Prior meta-analysis experience
- Knowledge of structural equation modeling
- Familiarity with AI in education research (ChatGPT, ITS, adaptive learning)

---

## 4. Reliability Metrics

### 4.1 Categorical Variables (Construct Mappings, Moderators)

**Metric: Cohen's Kappa (κ)**

**Formula:**
```
κ = (P_o - P_e) / (1 - P_e)

where:
  P_o = Observed agreement proportion
  P_e = Expected agreement by chance
```

**Interpretation (Landis & Koch, 1977):**
- κ < 0.00: Poor agreement
- 0.00-0.20: Slight agreement
- 0.21-0.40: Fair agreement
- 0.41-0.60: Moderate agreement
- 0.61-0.80: Substantial agreement
- 0.81-1.00: Almost perfect agreement

**Target:** κ ≥ .85 (almost perfect)

---

**Calculation (R):**

```r
library(irr)

# Example: Construct mapping agreement
mappings <- data.frame(
  coder1 = c("PE", "EE", "SI", "BI", "ATT", "TRU", ...),
  coder2 = c("PE", "EE", "SI", "BI", "ATT", "TRU", ...)
)

kappa_result <- kappa2(mappings)
print(kappa_result)
#   Cohen's Kappa for 2 Raters
#   Kappa = 0.92
#   z = 15.3
#   p-value < 0.001
```

---

### 4.2 Numerical Variables (Correlations, Reliabilities)

**Metric 1: Intraclass Correlation Coefficient (ICC)**

**Model:** ICC(2,1) - Two-way random effects, single rater, absolute agreement

**Formula:** Ratio of between-target variance to total variance

**Interpretation (Cicchetti, 1994):**
- ICC < 0.40: Poor reliability
- 0.40-0.59: Fair reliability
- 0.60-0.74: Good reliability
- 0.75-1.00: Excellent reliability

**Target:** ICC ≥ .95 (excellent)

**Calculation (R):**

```r
library(irr)

# Example: Correlation extraction agreement
correlations <- data.frame(
  coder1 = c(0.52, 0.48, 0.40, 0.35, ...),
  coder2 = c(0.51, 0.47, 0.42, 0.36, ...)
)

icc_result <- icc(correlations,
                  model = "twoway",
                  type = "agreement",
                  unit = "single")
print(icc_result)
#   Intraclass Correlation Coefficient
#   Model: twoway
#   Type: agreement
#   Subjects = 100
#   Raters = 2
#   ICC(2,1) = 0.97
#   95% CI: 0.95 - 0.98
#   F-test: F(99,99) = 65.3, p < 0.001
```

---

**Metric 2: Mean Absolute Error (MAE)**

**Formula:**
```
MAE = (1/n) × Σ|coder1_i - coder2_i|
```

**Interpretation:**
- MAE < 0.03: Excellent agreement (within 3 percentage points)
- MAE 0.03-0.05: Good agreement
- MAE 0.05-0.10: Moderate agreement
- MAE > 0.10: Poor agreement

**Target:** MAE ≤ .03 for correlations, ≤ .02 for reliabilities

**Calculation (R):**

```r
mae <- mean(abs(correlations$coder1 - correlations$coder2))
print(paste("MAE =", round(mae, 3)))
# "MAE = 0.018"
```

---

### 4.3 Percent Agreement (Simple Metric)

**Use:** Supplement to κ for transparency

**Formula:**
```
% Agreement = (Number of agreements / Total comparisons) × 100
```

**Interpretation:**
- ≥90%: Excellent
- 80-89%: Good
- 70-79%: Acceptable
- <70%: Poor

**Not Recommended as Primary Metric:**
- Does not account for chance agreement
- Inflated for unbalanced categories
- Use κ instead for categorical data

---

## 5. Coding Procedure

### 5.1 Independent Coding

**Coder A:**
- Receives ICR sample list (30 studies)
- Codes all studies independently
- No access to Coder B's work
- No access to AI extractions (blinded)

**Coder B:**
- Receives same ICR sample list
- Codes all studies independently
- No access to Coder A's work
- No access to AI extractions (blinded)

**Timeline:** 2 weeks (30 studies × 45 min/study = 22.5 hours per coder)

---

### 5.2 Coding Form

**Data Entry Template (CSV):**

```csv
study_id,construct1,construct2,r,n,r_source,original_beta,mapping_confidence,coder_id,date
Smith2023,PE,BI,0.52,285,pearson,NA,high,coder_A,2026-03-20
Smith2023,EE,BI,0.48,285,pearson,NA,high,coder_A,2026-03-20
Smith2023,PE,BI,0.51,285,pearson,NA,high,coder_B,2026-03-21
Smith2023,EE,BI,0.47,285,pearson,NA,high,coder_B,2026-03-21
```

**Separate Tables:**
- `icr_correlations.csv`: Correlation data
- `icr_mappings.csv`: Construct mappings
- `icr_moderators.csv`: Moderator coding
- `icr_reliability.csv`: Alpha, CR, AVE

---

### 5.3 Blinding

**Purpose:** Prevent bias from AI extractions or other coder's work

**Procedure:**
- Coders work on separate computers
- No access to AI extraction files during coding
- AI extractions revealed only AFTER both coders complete all 30 studies

**Exception:** Coders CAN access:
- Original study PDFs (required for coding)
- Coding manual and guidelines
- Lead investigator for clarification questions (logged)

---

## 6. ICR Calculation

### 6.1 Calculation Timeline

**Week 1-2:** Independent coding by Coder A and Coder B

**Week 3, Day 1:** Submit completed coding

**Week 3, Day 2:** Lead investigator calculates ICR metrics

**Week 3, Day 3:** Review ICR results with coders, discuss discrepancies

---

### 6.2 Calculation Steps

**Step 1: Merge Data**

```r
library(dplyr)

coder_a <- read.csv("data/icr_coder_a.csv")
coder_b <- read.csv("data/icr_coder_b.csv")

# Merge on study_id, construct1, construct2
merged <- full_join(coder_a, coder_b,
                    by = c("study_id", "construct1", "construct2"),
                    suffix = c("_a", "_b"))
```

**Step 2: Calculate Metrics**

**Correlations (ICC and MAE):**

```r
# Remove missing pairs (where one coder didn't extract)
corr_data <- merged %>%
  filter(!is.na(r_a) & !is.na(r_b)) %>%
  select(r_a, r_b)

# ICC
icc_corr <- icc(corr_data, model = "twoway", type = "agreement", unit = "single")

# MAE
mae_corr <- mean(abs(corr_data$r_a - corr_data$r_b))

print(paste("Correlation ICC:", round(icc_corr$value, 3)))
print(paste("Correlation MAE:", round(mae_corr, 3)))
```

**Construct Mappings (κ):**

```r
library(irr)

mappings <- merged %>%
  filter(!is.na(mapped_construct_a) & !is.na(mapped_construct_b)) %>%
  select(mapped_construct_a, mapped_construct_b)

kappa_mappings <- kappa2(mappings)
print(paste("Construct Mapping κ:", round(kappa_mappings$value, 3)))
```

**Moderators (κ or % agreement):**

```r
# AI Tool Type
ai_tool_kappa <- kappa2(merged[, c("ai_tool_type_a", "ai_tool_type_b")])

# Education Level
edu_level_kappa <- kappa2(merged[, c("education_level_a", "education_level_b")])

# User Role
user_role_kappa <- kappa2(merged[, c("user_role_a", "user_role_b")])

# Discipline
discipline_kappa <- kappa2(merged[, c("discipline_a", "discipline_b")])

print(paste("AI Tool Type κ:", round(ai_tool_kappa$value, 3)))
print(paste("Education Level κ:", round(edu_level_kappa$value, 3)))
print(paste("User Role κ:", round(user_role_kappa$value, 3)))
print(paste("Discipline κ:", round(discipline_kappa$value, 3)))
```

---

### 6.3 Reporting Template

**ICR Results Table:**

| Variable Type | Metric | Value | 95% CI | Interpretation |
|---------------|--------|-------|--------|----------------|
| Correlations (r) | ICC(2,1) | [value] | [CI] | [interp] |
| Correlations (r) | MAE | [value] | — | [interp] |
| Construct Mapping | κ | [value] | [CI] | [interp] |
| AI Tool Type | κ | [value] | [CI] | [interp] |
| Education Level | κ | [value] | [CI] | [interp] |
| User Role | κ | [value] | [CI] | [interp] |
| Discipline | κ | [value] | [CI] | [interp] |
| Reliabilities (α) | ICC(2,1) | [value] | [CI] | [interp] |

---

## 7. Discrepancy Analysis

### 7.1 Identifying Discrepancies

**Discrepancy Criteria:**

**Correlations:**
- Absolute difference ≥ .05 (e.g., r_a=.52, r_b=.47 → diff=.05)

**Construct Mappings:**
- Different construct assigned (e.g., coder_a=PE, coder_b=ATT)

**Moderators:**
- Different category assigned (e.g., coder_a=Generative, coder_b=Predictive)

---

### 7.2 Discrepancy Patterns

**Common Discrepancy Types:**

1. **Table Misreading:**
   - Coder reads from wrong row/column
   - Example: r_a=.52 (correct), r_b=.45 (read from different pair)
   - **Solution:** Return to original table, verify correct cell

2. **Construct Ambiguity:**
   - Study label is unclear (e.g., "AI Value")
   - Coder A maps to PE, Coder B maps to ATT
   - **Solution:** Review items together, apply harmonization rules

3. **Missing Data Interpretation:**
   - Study reports "ns" for non-significant correlation
   - Coder A codes as missing, Coder B codes as .00
   - **Solution:** Clarify protocol (code as missing, not .00)

4. **Rounding Differences:**
   - Study reports r=.456
   - Coder A codes .46, Coder B codes .45 (different rounding)
   - **Solution:** Standardize to 2 decimals, round .456 → .46

---

### 7.3 Discrepancy Log

**Template:**

```csv
study_id,variable,coder_a_value,coder_b_value,discrepancy_type,discrepancy_size,pattern_identified
Smith2023,PE_BI_r,0.52,0.47,table_misread,0.05,Coder B read from PE-EE cell
Jones2024,construct_PU,PE,ATT,ambiguous_label,mapping_conflict,"AI Value" label unclear
Brown2025,SI_BI_r,NA,0.00,missing_interpretation,coding_rule,"ns" coded differently
```

---

## 8. Actions Based on ICR Results

### 8.1 If ICR Meets Thresholds

**κ ≥ .85, ICC ≥ .95, MAE ≤ .03:**

✅ **Action:**
- Accept coding procedures as reliable
- Proceed to code remaining studies
- Document ICR results in dissertation Methods section

**Next Steps:**
1. Resolve discrepancies for the 20% ICR sample (see Phase 5: Discrepancy Resolution)
2. Code remaining 80% of studies (or use AI extractions with spot-checks)
3. Final QA checks on full dataset

---

### 8.2 If ICR Below Threshold

**κ < .85 OR ICC < .95 OR MAE > .03:**

⚠️ **Action:**
- Analyze discrepancy patterns
- Identify problematic coding rules
- Additional training and calibration

**Decision Tree:**

**κ = .80-.84 (close to threshold):**
- Acceptable but not ideal
- Review major discrepancies
- Clarify ambiguous rules
- Proceed with caution, document limitations

**κ = .70-.79 (moderate agreement):**
- Additional training session required
- Identify and clarify problematic constructs/rules
- Re-code 10 studies from ICR sample
- Recalculate κ on re-coded subset
- If improved, proceed; if not, revise coding manual

**κ < .70 (substantial disagreement):**
- Major issues with coding protocol
- Convene full team meeting
- Revise coding manual
- Consider simplifying coding scheme
- Complete re-training
- Re-code entire ICR sample
- Recalculate all metrics

---

### 8.3 Recalibration Protocol

**Step 1: Diagnostic Session (2 hours)**
- Review all discrepancies
- Categorize discrepancy types
- Identify patterns (e.g., one construct always problematic)

**Step 2: Rule Clarification**
- Update coding manual with clearer rules
- Add examples for ambiguous cases
- Create decision flowcharts for complex mappings

**Step 3: Targeted Re-training (2 hours)**
- Focus on problematic constructs/rules
- Practice coding with new clarifications
- Discuss edge cases

**Step 4: Re-code Subset**
- Both coders re-code 10 studies (subset of original ICR sample)
- Calculate ICR metrics on re-coded subset
- **Target:** κ ≥ .85, ICC ≥ .95

**Step 5: Decision**
- If improved to threshold: Proceed
- If still below: Consider major protocol revision or expert consultation

---

## 9. AI-Human Agreement

### 9.1 Comparing AI to Human Coding

**Purpose:** Assess whether AI extractions are reliable enough to use for non-ICR studies

**Procedure:**
- Compare AI consensus (Phase 3) to each human coder
- Calculate same metrics: ICC, MAE, κ

**AI vs. Coder A:**
```r
ai_human_a <- merged %>%
  filter(!is.na(r_ai) & !is.na(r_a)) %>%
  select(r_ai, r_a)

icc_ai_a <- icc(ai_human_a, model = "twoway", type = "agreement", unit = "single")
mae_ai_a <- mean(abs(ai_human_a$r_ai - ai_human_a$r_a))
```

**AI vs. Coder B:**
```r
ai_human_b <- merged %>%
  filter(!is.na(r_ai) & !is.na(r_b)) %>%
  select(r_ai, r_b)

icc_ai_b <- icc(ai_human_b, model = "twoway", type = "agreement", unit = "single")
mae_ai_b <- mean(abs(ai_human_b$r_ai - ai_human_b$r_b))
```

---

### 9.2 AI Reliability Benchmarks

**Acceptable AI Performance:**
- ICC(AI, Human) ≥ .90
- MAE ≤ .05
- κ (construct mappings) ≥ .80

**Decision:**
- If AI meets benchmarks: Use AI extractions for remaining 80% with spot-checks (10% random verification)
- If AI below benchmarks: Human code all studies OR increase ICR sample to 50% with AI-assisted pre-population

---

## 10. Reporting ICR in Manuscript

### 10.1 Methods Section (Computers & Education Format)

**Template:**

"To ensure coding reliability, two independent coders extracted data from a stratified random sample of [N] studies (20% of total included studies). Stratification was based on publication year, AI tool type, education level, and geographic region to ensure representativeness. Coders underwent 9 hours of training including orientation, pilot coding, and calibration. Inter-coder reliability was assessed using Cohen's kappa for categorical variables (construct mappings, education-specific moderators) and intraclass correlation coefficients (ICC) for continuous variables (correlation coefficients). Reliability was excellent: ICC(2,1) = [value] [95% CI] for correlations with mean absolute error (MAE) = [value]; κ = [value] [95% CI] for construct mappings. All metrics exceeded pre-specified thresholds (ICC ≥ .95, κ ≥ .85, MAE ≤ .03). Discrepancies were resolved through consensus discussion and reference to original study texts. The remaining studies were coded by a single trained coder with 10% random spot-checks."

---

### 10.2 Supplementary Materials (Online Appendix)

**Include:**
- Table: ICR metrics for all variable types (correlations, construct mappings, education-level moderators)
- ICR sample characteristics (compared to full sample)
- Discrepancy patterns and resolutions
- Coding manual (as online appendix per C&E guidelines)

---

## References

Cicchetti, D. V. (1994). Guidelines, criteria, and rules of thumb for evaluating normed and standardized assessment instruments in psychology. *Psychological Assessment*, 6(4), 284-290.

Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37-46.

Hallgren, K. A. (2012). Computing inter-rater reliability for observational data: An overview and tutorial. *Tutorials in Quantitative Methods for Psychology*, 8(1), 23-34.

Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159-174.

McHugh, M. L. (2012). Interrater reliability: The kappa statistic. *Biochemia Medica*, 22(3), 276-282.

McGraw, K. O., & Wong, S. P. (1996). Forming inferences about some intraclass correlation coefficients. *Psychological Methods*, 1(1), 30-46.

Shrout, P. E., & Fleiss, J. L. (1979). Intraclass correlations: Uses in assessing rater reliability. *Psychological Bulletin*, 86(2), 420-428.
