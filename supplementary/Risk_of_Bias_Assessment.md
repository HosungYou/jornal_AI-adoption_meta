# Risk of Bias Assessment Framework for MASEM Studies

**AI Adoption Meta-Analysis**

**Assessment Tool:** Custom framework adapted from NIH Quality Assessment Tool for Observational Cohort and Cross-Sectional Studies, with MASEM-specific criteria.

---

## Overview

This framework assesses risk of bias (RoB) in correlational studies included in meta-analytic structural equation modeling. Unlike intervention studies (Cochrane RoB tool), correlational studies require assessment of selection bias, measurement validity, reporting completeness, and common method bias.

**Key Principle:** Risk of bias assessment informs:
1. GRADE certainty ratings
2. Sensitivity analyses (exclude high-risk studies)
3. Meta-regression (RoB as moderator)
4. Interpretation of findings

---

## Risk of Bias Domains

### Domain 1: Selection Bias (Sample Representativeness)

**Question:** Is the study sample representative of the target population, or is it systematically biased?

**Criteria:**

| Rating | Criteria |
|--------|----------|
| **Low Risk** | - Probability sampling (random, stratified random, cluster random)<br>- Response rate ≥70% OR non-response analysis shows no bias<br>- Adequate sample size (N ≥ 200 for SEM, per Kline, 2016)<br>- Sample demographics match population |
| **Some Concerns** | - Convenience sampling but diverse recruitment (multiple sites, channels)<br>- Response rate 50-69% OR non-response analysis not reported<br>- Adequate sample size but limited demographic diversity<br>- Sample demographics partially match population |
| **High Risk** | - Highly selected sample (single organization, single class, homogeneous group)<br>- Response rate <50% with no non-response analysis<br>- Small sample size (N < 100) raising generalizability concerns<br>- Sample demographics substantially differ from target population (e.g., 95% one gender for general population study) |

**Assessment Prompts:**
1. How was the sample recruited? (probability vs. convenience)
2. What was the response rate? (if survey)
3. Is the sample size adequate for the analysis?
4. Are sample demographics representative of the intended population?
5. Did authors discuss limitations of sampling approach?

**Common Issues (Education Context):**
- **Single-class student samples:** High risk if claiming generalizability beyond that specific course/institution. Rate as "High Risk" for external validity.
- **Student convenience samples:** Very common in education research. Rate as "Some Concerns" if single institution but multiple courses/sections. Rate as "High Risk" if single class only.
- **Instructor samples via email lists:** "Some Concerns" due to self-selection bias (early adopters more likely to respond).
- **Course-embedded participation:** "Some Concerns" if voluntary research participation, "High Risk" if tied to course credit (coercion concerns).
- **Digital divide in K-12:** "Some Concerns" if all students had equal technology access, "High Risk" if access barriers excluded low-SES students.

**MASEM-Specific Note (Education):** Heterogeneous sampling across studies is desirable for meta-analysis (K-12 + higher ed, students + instructors, multiple disciplines). Single-institution student convenience samples are very common in education research but limit generalizability. Selection bias is study-level concern; meta-analysis can estimate population effect if most studies are low/moderate risk.

---

### Domain 2: Measurement Bias (Construct Validity)

**Question:** Are the constructs measured with valid, reliable instruments?

**Criteria:**

| Rating | Criteria |
|--------|----------|
| **Low Risk** | - Validated scales from published sources (e.g., Davis, 1989; Venkatesh et al., 2003)<br>- Cronbach's α ≥ 0.80 for all constructs<br>- Confirmatory Factor Analysis (CFA) conducted with acceptable fit (CFI ≥ 0.90, RMSEA ≤ 0.08)<br>- Discriminant validity demonstrated (AVE > squared correlations, or HTMT < 0.85)<br>- Convergent validity demonstrated (AVE ≥ 0.50) |
| **Some Concerns** | - Validated scales but adapted (items modified)<br>- Cronbach's α 0.70-0.79 for some constructs<br>- CFA not conducted OR fit marginal (CFI 0.85-0.89)<br>- Discriminant validity partially supported OR not tested<br>- Convergent validity marginal (AVE 0.40-0.49) OR not reported |
| **High Risk** | - Ad-hoc scales without validation<br>- Cronbach's α < 0.70 for multiple constructs<br>- Single-item measures for complex constructs (except for simple demographics)<br>- No reliability reported<br>- CFA shows poor fit (CFI < 0.85) with no justification<br>- Discriminant validity clearly violated (constructs correlate > 0.90) |

**Assessment Prompts:**
1. Are scales from validated sources or author-developed?
2. Are reliability coefficients (α or CR) reported for all constructs?
3. Are reliability values acceptable (α ≥ 0.70)?
4. Was CFA conducted to assess measurement model?
5. Was discriminant validity tested (AVE vs. squared correlations, HTMT)?
6. Are there any single-item measures for multi-dimensional constructs?

**Special Cases:**
- **Formative constructs:** Internal consistency (α) not applicable; assess content validity and collinearity instead.
- **Behavioral measures (Use Behavior):** Objective log data = Low Risk. Self-report with single item (frequency) = Some Concerns if validated in prior research.

**MASEM-Specific Note:** Measurement error attenuates correlations. Low-reliability constructs introduce bias in pooled correlations. If α < 0.70, consider:
- Artifact correction (disattenuate correlations for unreliability) — requires artifact distribution meta-analysis (Schmidt & Hunter, 2015)
- Sensitivity analysis excluding low-reliability studies

---

### Domain 3: Reporting Bias (Selective Reporting)

**Question:** Is the study's correlation matrix complete, or are results selectively reported (potential publication bias or p-hacking)?

**Criteria:**

| Rating | Criteria |
|--------|----------|
| **Low Risk** | - Full correlation matrix reported (100% of construct pairs)<br>- Non-significant correlations included<br>- Pre-registration or protocol available (OSF, PROSPERO, trial registry)<br>- All hypothesized paths reported in SEM (including non-significant)<br>- No evidence of selective reporting |
| **Some Concerns** | - Correlation matrix 80-99% complete (minor gaps, likely due to space constraints)<br>- Non-significant correlations mostly reported, but some omissions<br>- No pre-registration, but appears complete reporting<br>- SEM paths: most reported, but 1-2 omissions without justification |
| **High Risk** | - Correlation matrix <80% complete (substantial missing data)<br>- Only significant correlations reported (p < 0.05)<br>- "Correlation matrix available upon request" but not provided when contacted<br>- SEM paths: only significant paths reported, or modification indices used without transparency<br>- Evidence of HARKing (Hypothesizing After Results Known) or outcome switching |

**Assessment Prompts:**
1. What percentage of the correlation matrix is reported?
2. Are non-significant correlations included?
3. Is there a pre-registration or protocol?
4. If SEM model reported, are all paths in the hypothesized model included (or justified exclusions)?
5. Do results align with stated hypotheses, or evidence of post-hoc changes?

**Red Flags:**
- Correlation table with many blank cells and no explanation
- "All correlations were significant at p < 0.05" (implausibly perfect results)
- Hypotheses in introduction don't match paths tested in results
- Model fit improved by dropping paths without theoretical justification

**MASEM-Specific Note:** Missing cells in correlation matrices reduce statistical power and may bias pooled estimates if missingness is related to effect size (e.g., only reporting significant correlations). Studies with <50% matrix completeness are excluded per eligibility criteria. For 50-80% complete matrices, use available-case analysis and flag for sensitivity.

---

### Domain 4: Common Method Bias (CMB)

**Question:** Are measures taken to prevent or assess common method bias from single-source, self-report data?

**Background:** CMB inflates correlations when:
- Same respondent reports all variables (single-source)
- Same method used (e.g., all Likert scales)
- Same time point (cross-sectional)
- Same context (e.g., all questions in one survey section)

**Criteria:**

| Rating | Criteria |
|--------|----------|
| **Low Risk** | **Procedural Remedies (≥2 of the following):**<br>- Temporal separation (IV and DV measured at different time points)<br>- Methodological separation (IV from one source, DV from another; e.g., self-report + behavioral logs)<br>- Psychological separation (clear instructions that answers are anonymous, no right/wrong answers)<br>- Counterbalancing (randomize question order)<br>- Proximal separation (physically separate IV and DV sections)<br>**AND Statistical Controls (≥1):**<br>- Harman's single-factor test (variance explained <50%)<br>- Common Latent Factor (CLF) method in CFA (loadings non-significant)<br>- Marker variable technique (CFA with theoretically unrelated marker)<br>- Correlation matrix compared to method-only matrix |
| **Some Concerns** | **Procedural Remedies (1 of the above):**<br>- At least one procedural remedy used (e.g., anonymity assured)<br>**OR Statistical Controls (1 of the above):**<br>- At least one statistical test conducted (e.g., Harman's test)<br>**BUT NOT BOTH** |
| **High Risk** | - No procedural remedies mentioned<br>- No statistical controls conducted<br>- Single-source, self-report, cross-sectional with no CMB discussion<br>- Authors acknowledge CMB as limitation but took no preventive action |

**Assessment Prompts:**
1. Are all variables self-reported by the same respondent? (single-source)
2. Are all variables measured at the same time? (cross-sectional)
3. Did authors implement procedural remedies? (List which)
4. Did authors conduct statistical tests for CMB? (List which)
5. Did authors discuss CMB in limitations?

**Interpreting CMB Tests:**

| Test | Interpretation | Limitation |
|------|----------------|------------|
| **Harman's Single-Factor Test** | If first unrotated factor explains <50% variance → CMB not severe | Conservative; may miss CMB if multiple factors |
| **Common Latent Factor (CLF)** | Add CLF to CFA; if loadings non-significant or small → CMB minimal | Requires SEM; can be overly conservative |
| **Marker Variable** | Correlations between substantive constructs and theoretically unrelated marker should be near-zero; if not, adjust | Requires theoretically justified marker |
| **Correlation Matrix Comparison** | Compare to method-only matrix; if patterns similar → CMB present | Rarely done in practice |

**MASEM-Specific Note:** CMB inflates pooled correlations. If >25% of included studies are High Risk for CMB, conduct sensitivity analysis excluding them. Consider artifact correction (common method variance) if feasible.

---

### Overall Risk of Bias

**Aggregation Rule:**

| Overall Rating | Criteria |
|----------------|----------|
| **Low Risk** | All 4 domains rated Low Risk |
| **Some Concerns** | ≥1 domain rated Some Concerns, AND no domains rated High Risk |
| **High Risk** | ≥1 domain rated High Risk |

**Rationale:** A single high-risk domain compromises study validity. Conservative approach appropriate for informing GRADE certainty.

---

## Assessment Process

### Step 1: Dual Independent Assessment
- Two reviewers (HH + RA1) independently assess each study
- Use structured assessment form (see template below)
- Blind to each other's ratings

### Step 2: Calculate Inter-Rater Reliability
- Cohen's κ for each domain (4 domains) and overall rating
- Target: κ ≥ 0.75 for overall rating
- If κ < 0.75, conduct reviewer training and re-assess sample

### Step 3: Resolve Discrepancies
- Reviewers meet to discuss disagreements
- Consensus reached for each discrepancy
- If consensus impossible, senior author (SA) adjudicates

### Step 4: Document Justifications
- For each "High Risk" or "Some Concerns" rating, provide justification quote from study or explanation
- Maintain audit trail of decision-making

---

## Assessment Form Template

**Study ID:** ___________________
**Study Citation:** ___________________
**Reviewer:** ___________________
**Date:** ___________________

---

### Domain 1: Selection Bias

**1.1 Sampling method:**
- [ ] Probability sampling
- [ ] Convenience sampling (diverse)
- [ ] Convenience sampling (homogeneous/limited)

**1.2 Response rate (if applicable):** _____ %
- [ ] ≥70%
- [ ] 50-69%
- [ ] <50%
- [ ] Not reported / Not applicable

**1.3 Sample size:** N = _____
- [ ] ≥200
- [ ] 100-199
- [ ] <100

**1.4 Sample representativeness:**
- [ ] Demographics match target population
- [ ] Demographics partially match
- [ ] Demographics substantially differ / Unclear

**1.5 Education-specific bias flags:**
- [ ] Single-institution study
- [ ] Single-class convenience sample
- [ ] Course-embedded participation (tied to credit)
- [ ] Self-selection bias (only AI adopters)
- [ ] Digital divide / access barriers not addressed

**1.6 Overall Rating:**
- [ ] Low Risk
- [ ] Some Concerns
- [ ] High Risk

**Justification:** ___________________________________________

---

### Domain 2: Measurement Bias

**2.1 Scale sources:**
- [ ] All validated scales
- [ ] Mix of validated and adapted
- [ ] Mix of validated and ad-hoc
- [ ] All ad-hoc

**2.2 Reliability (Cronbach's α):**
- Minimum α across constructs: _____
- [ ] All α ≥ 0.80
- [ ] All α ≥ 0.70
- [ ] Some α < 0.70
- [ ] Not reported

**2.3 CFA conducted:**
- [ ] Yes, acceptable fit (CFI ≥ 0.90, RMSEA ≤ 0.08)
- [ ] Yes, marginal fit (CFI 0.85-0.89)
- [ ] Yes, poor fit (CFI < 0.85)
- [ ] No

**2.4 Discriminant validity:**
- [ ] Demonstrated (AVE > r² or HTMT < 0.85)
- [ ] Partially demonstrated
- [ ] Not demonstrated / Not tested

**2.5 Overall Rating:**
- [ ] Low Risk
- [ ] Some Concerns
- [ ] High Risk

**Justification:** ___________________________________________

---

### Domain 3: Reporting Bias

**3.1 Correlation matrix completeness:** _____ % of cells reported

**3.2 Non-significant correlations included:**
- [ ] Yes, appears complete
- [ ] Mostly, some omissions
- [ ] No, only significant reported
- [ ] Unclear

**3.3 Pre-registration:**
- [ ] Yes (link: _______________)
- [ ] No

**3.4 SEM paths (if applicable):**
- [ ] All hypothesized paths reported
- [ ] Most reported, minor omissions
- [ ] Only significant paths reported
- [ ] Not applicable (no SEM)

**3.5 Overall Rating:**
- [ ] Low Risk
- [ ] Some Concerns
- [ ] High Risk

**Justification:** ___________________________________________

---

### Domain 4: Common Method Bias

**4.1 Data characteristics:**
- [ ] Single-source, self-report, cross-sectional (high CMB risk)
- [ ] Mixed sources OR multi-wave OR objective measures
- [ ] Fully objective / secondary data

**4.2 Procedural remedies (check all that apply):**
- [ ] Temporal separation (multi-wave)
- [ ] Methodological separation (mixed sources)
- [ ] Psychological separation (anonymity, clear instructions)
- [ ] Counterbalancing (randomized question order)
- [ ] Proximal separation (separated survey sections)
- [ ] None mentioned

**4.3 Statistical controls (check all that apply):**
- [ ] Harman's single-factor test (result: _____ % variance)
- [ ] Common Latent Factor (CLF) in CFA
- [ ] Marker variable technique
- [ ] Correlation matrix comparison
- [ ] None conducted

**4.4 Overall Rating:**
- [ ] Low Risk
- [ ] Some Concerns
- [ ] High Risk

**Justification:** ___________________________________________

---

### Overall Risk of Bias

**Overall Rating:**
- [ ] Low Risk (all domains low)
- [ ] Some Concerns (≥1 some concerns, no high)
- [ ] High Risk (≥1 high)

**Summary Justification:** ___________________________________________

---

### Sensitivity Analysis Flag

**Exclude from sensitivity analysis (if Overall = High Risk):**
- [ ] Yes
- [ ] No (special circumstances: _______________)

---

## Use in Analysis

### 1. GRADE Certainty Assessment

**Risk of Bias Domain (GRADE):**

| Study-Level RoB Distribution | Downgrade GRADE Certainty? |
|------------------------------|----------------------------|
| <25% weight from High Risk studies | No downgrade |
| 25-50% weight from High Risk studies | Downgrade 1 level (serious RoB) |
| >50% weight from High Risk studies | Downgrade 2 levels (very serious RoB) |

**Weight calculation:** Sum sample sizes of High Risk studies / Total sample size across all studies

### 2. Sensitivity Analysis

**Primary Analysis:** Include all studies (Low Risk + Some Concerns + High Risk)

**Sensitivity Analysis 1:** Exclude High Risk studies
- Re-run TSSEM (Stage 1 + Stage 2)
- Compare pooled correlations, path coefficients, model fit
- **Decision rule:** If conclusions change (sign flip, significance change for key paths), flag as "Low Certainty" in GRADE

**Sensitivity Analysis 2:** Exclude High Risk for CMB only
- Test whether CMB-related studies inflate correlations
- Expect lower pooled r if CMB is substantive issue

### 3. Meta-Regression

**Moderator:** Overall Risk of Bias (Low vs. Some Concerns vs. High)

**Hypothesis:** High Risk studies show larger effect sizes (correlations) due to bias

**Analysis:**
- Meta-regression: r ~ RoB_category (categorical moderator)
- Report β, SE, p-value
- If significant: CMB or other biases systematically inflate effects

---

## Reporting Risk of Bias

### Summary Table (Results Section)

**Table: Risk of Bias Assessment Summary**

| Study | Selection Bias | Measurement Bias | Reporting Bias | CMB Risk | Overall |
|-------|----------------|------------------|----------------|----------|---------|
| Smith et al. (2023) | Low | Low | Low | Some Concerns | Some Concerns |
| Jones et al. (2022) | Some Concerns | Low | Low | High | High |
| ... | ... | ... | ... | ... | ... |
| **% Low Risk** | 45% | 60% | 70% | 30% | 35% |
| **% Some Concerns** | 40% | 30% | 25% | 50% | 50% |
| **% High Risk** | 15% | 10% | 5% | 20% | 15% |

### Risk of Bias Graph (Figure)

- Stacked bar chart showing % of studies in each category (Low / Some / High) for each domain
- Color-coded: Green (Low), Yellow (Some Concerns), Red (High)
- Created using R package `robvis` or manual plotting

---

## References

- Higgins, J. P. T., et al. (2019). Cochrane Handbook for Systematic Reviews of Interventions (2nd ed.). Wiley.
- Kline, R. B. (2016). *Principles and practice of structural equation modeling* (4th ed.). Guilford Press.
- National Heart, Lung, and Blood Institute (NHLBI). (2021). Quality Assessment Tool for Observational Cohort and Cross-Sectional Studies. https://www.nhlbi.nih.gov/health-topics/study-quality-assessment-tools
- Podsakoff, P. M., MacKenzie, S. B., Lee, J.-Y., & Podsakoff, N. P. (2003). Common method biases in behavioral research: A critical review of the literature and recommended remedies. *Journal of Applied Psychology*, 88(5), 879-903.
- Schmidt, F. L., & Hunter, J. E. (2015). *Methods of meta-analysis: Correcting error and bias in research findings* (3rd ed.). Sage.
- Sterne, J. A. C., et al. (2016). ROBINS-I: A tool for assessing risk of bias in non-randomised studies of interventions. *BMJ*, 355, i4919.

---

**End of Risk of Bias Assessment Framework**

**Version:** 1.0.0
**Date:** 2026-02-16
