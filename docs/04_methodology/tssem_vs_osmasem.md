# TSSEM vs. OSMASEM: Choosing the Right MASEM Approach

## Overview

This document compares Two-Stage Structural Equation Modeling (TSSEM) and One-Stage Meta-Analytic Structural Equation Modeling (OSMASEM), providing guidance on when to use each approach in the educational AI adoption meta-analysis.

---

## 1. TSSEM: Two-Stage Approach

### 1.1 Overview

**Developer:** Cheung & Chan (2005), Cheung (2015)

**Philosophy:** Separate meta-analysis from structural modeling

**Stages:**
1. **Stage 1:** Pool correlation matrices across studies → create pooled correlation matrix
2. **Stage 2:** Fit structural equation model on pooled correlation matrix

---

### 1.2 Stage 1: Pooling Correlations

**Objective:** Synthesize correlation matrices using multivariate meta-analysis

**Method:**
- Random-effects or fixed-effects model
- Estimates pooled correlation for each construct pair
- Produces pooled correlation matrix + variance-covariance matrix of sampling errors

**Handling Missing Data:**
- Full Information Maximum Likelihood (FIML)
- Uses all available data; estimates missing correlations

**Output:**
- 12×12 pooled correlation matrix (for our 12 constructs)
- Heterogeneity statistics (I², Q, τ²) for each correlation
- Between-study variance estimates

**R Implementation:**

```r
library(metaSEM)

# Stage 1: Pool correlations
stage1 <- tssem1(Cov = correlation_matrices,
                 n = sample_sizes,
                 method = "REM",      # Random-effects
                 RE.type = "Diag")    # Diagonal τ² matrix

# View pooled correlations
summary(stage1)
coef(stage1)  # Pooled correlation matrix
```

---

### 1.3 Stage 2: Structural Modeling

**Objective:** Fit SEM on pooled matrix from Stage 1

**Input:**
- Pooled correlation matrix (from Stage 1)
- Structural model specification (A and S matrices in RAM notation)
- Harmonic mean sample size

**Estimation:**
- Weighted Least Squares (WLS)
- Treats pooled matrix as data, incorporates sampling variance

**Output:**
- Path coefficients (β) with 95% confidence intervals
- Model fit indices (CFI, RMSEA, SRMR, χ²)
- R² for endogenous variables
- Indirect effects (if specified)

**R Implementation:**

```r
# Stage 2: Fit structural model
stage2 <- tssem2(stage1,
                 Amatrix = A_matrix,    # Regression paths
                 Smatrix = S_matrix,    # Variances/covariances
                 intervals.type = "LB") # Likelihood-based CI

# View results
summary(stage2)
```

---

### 1.4 TSSEM Advantages

**✅ Simplicity:**
- Two clear, interpretable stages
- Easy to explain to non-statistical audiences
- Transparent meta-analysis → SEM workflow

**✅ Flexibility:**
- Stage 1 results useful independently (pooled correlations)
- Can fit multiple models on same Stage 1 output
- Easy to compare competing models

**✅ Robustness:**
- Well-established method (20+ years of use)
- Extensively validated in meta-analytic literature
- Handles missing correlations well (FIML)

**✅ Computational Efficiency:**
- Faster than OSMASEM for complex models
- Stage 1 only run once; Stage 2 rerun for different models
- Less prone to convergence issues

**✅ Heterogeneity Examination:**
- Stage 1 provides detailed heterogeneity statistics per correlation
- Can identify which correlations are most heterogeneous
- Informs moderator analysis decisions

---

### 1.5 TSSEM Limitations

**❌ Two-Stage Uncertainty:**
- Standard errors from Stage 2 don't account for Stage 1 uncertainty
- May slightly underestimate path coefficient standard errors
- Effect is typically small in practice

**❌ Categorical Moderators Only (in standard form):**
- Moderators tested via subgroup analysis (separate Stage 1 per subgroup)
- Cannot include continuous moderators in single model
- Must run separate models for each subgroup

**❌ Assumes Homogeneity Within Stage 2:**
- Stage 2 treats pooled matrix as fixed
- Doesn't model residual heterogeneity in structural paths

---

## 2. OSMASEM: One-Stage Approach

### 2.1 Overview

**Developer:** Jak & Cheung (2020)

**Philosophy:** Simultaneous estimation of correlation pooling and structural model fitting

**Method:**
- Single-step multivariate meta-analysis
- Directly estimates structural paths while accounting for between-study heterogeneity
- Can include moderators of structural paths

---

### 2.2 How OSMASEM Works

**Model:**
- Combines Stage 1 (pooling) and Stage 2 (SEM) into one likelihood function
- Estimates:
  - Pooled correlations (or structural paths directly)
  - Between-study variance in correlations/paths
  - Moderator effects on paths (if specified)

**Estimation:**
- Maximum Likelihood via OpenMx
- Computationally intensive (many parameters estimated simultaneously)

**R Implementation:**

```r
library(metaSEM)

# Define structural model
model <- "
  BI ~ beta_PE*PE + beta_EE*EE + beta_SI*SI
  UB ~ beta_BI*BI + beta_FC*FC
  PE ~~ cov_PE_EE*EE
"

# Fit OSMASEM (no moderators)
osmasem_fit <- osmasem(model = model,
                       data = correlation_matrices,
                       n = sample_sizes)

summary(osmasem_fit)
```

---

### 2.3 OSMASEM Advantages

**✅ Continuous Moderators:**
- Can include continuous moderators (e.g., publication year, Hofstede individualism)
- Models how moderators affect structural paths
- Example: β(PE→BI) = .35 + .02×(year - 2020)

**✅ Single-Step Inference:**
- Standard errors account for all sources of uncertainty
- No two-stage uncertainty issue
- More accurate confidence intervals

**✅ Path-Specific Heterogeneity:**
- Can model different amounts of heterogeneity for different paths
- Example: PE→BI may have high τ², EE→BI may have low τ²

**✅ Complex Moderator Models:**
- Can test moderator interactions
- Multiple moderators simultaneously
- Moderator effects on specific paths (not just all paths)

---

### 2.4 OSMASEM Limitations

**❌ Computational Complexity:**
- Much slower than TSSEM (minutes vs. seconds)
- Requires more RAM for large models
- Convergence issues more common

**❌ Less Transparent:**
- Single-stage output harder to interpret
- Cannot examine Stage 1 pooled correlations separately
- Difficult to explain to non-expert audiences

**❌ Requires More Data:**
- Needs sufficient studies for moderator testing (k ≥ 30-40 per moderator)
- Underpowered with small k
- May not converge with sparse data

**❌ Model Comparison More Complex:**
- Fitting multiple models more time-consuming
- Each model requires full re-estimation (no "Stage 1 once, Stage 2 many times")

---

## 3. Comparison Table

| Feature | TSSEM | OSMASEM |
|---------|-------|---------|
| **Stages** | Two (pooling → SEM) | One (simultaneous) |
| **Speed** | Fast (seconds to minutes) | Slow (minutes to hours) |
| **Transparency** | High (clear stages) | Moderate (single model) |
| **Continuous moderators** | No (subgroup only) | Yes (directly modeled) |
| **Categorical moderators** | Yes (subgroup analysis) | Yes (dummy coding) |
| **Missing data handling** | FIML in Stage 1 | FIML throughout |
| **Standard errors** | Slight underestimation | Fully accounts for uncertainty |
| **Computational burden** | Low | High |
| **Convergence** | Rare issues | More common issues |
| **Model comparison** | Easy (reuse Stage 1) | Harder (refit each time) |
| **Heterogeneity examination** | Detailed (per correlation) | Path-specific (if modeled) |
| **Best for** | Primary analysis, model comparison | Moderator testing (continuous) |

---

## 4. When to Use Each Approach

### 4.1 Use TSSEM When:

✅ **Primary structural model testing**
- Testing 3 competing models (our Models 1, 2, 3)
- Comparing model fit indices
- Estimating main effect path coefficients

✅ **Categorical moderator analysis**
- Student vs. Instructor (subgroup TSSEM)
- K-12 vs. Higher Education (subgroup TSSEM)
- AI Tool Type (ChatGPT vs. ITS vs. LMS-AI) (subgroup TSSEM)
- Pre-ChatGPT vs. Post-ChatGPT (subgroup TSSEM)

✅ **Exploratory analysis**
- Initial examination of pooled correlations
- Understanding heterogeneity patterns
- Building intuition before complex moderator models

✅ **Limited sample size per moderator level**
- k < 30 studies total (expected: k=40-80 for education focus)
- Or unbalanced subgroups (e.g., k=50 students, k=15 instructors)

✅ **Transparency and reproducibility priorities**
- Journal reviewers may prefer clear two-stage logic
- Easier to explain to educational research audiences

---

### 4.2 Use OSMASEM When:

✅ **Continuous moderator testing**
- Publication year as continuous (2015-2025)
- Education level as ordinal (K-12=1, Undergrad=2, Grad=3)
- Sample mean age as moderator

✅ **Moderator interactions**
- Does year effect differ by user role (student vs. instructor)?
- Does education level moderate the PE→BI path differently than the TRU→BI path?

✅ **Path-specific heterogeneity modeling**
- Suspicion that some paths vary more across studies than others
- Want to model τ² separately for each path

✅ **Adequate sample size**
- k ≥ 40 studies total (achievable with education focus: expected k=40-80)
- Sufficient range on continuous moderator (not all clustered at one value)

✅ **Precision priority over speed**
- Willing to wait for computation
- Want most accurate standard errors

---

## 5. Our Approach: Hybrid Strategy

### 5.1 Primary Analysis: TSSEM

**Use TSSEM for:**

**Research Question 1:** TAM/UTAUT validity in AI context
- TSSEM Stage 1: Pool all 66 correlations
- TSSEM Stage 2: Fit Model 1, assess fit
- Compare to Sabherwal et al. (2006) benchmarks (via Bayesian MASEM)

**Research Question 2:** AI-specific constructs' incremental power
- TSSEM Stage 2: Fit Models 1, 2, 3 on same Stage 1 output
- Compare fit indices (Δχ², ΔCFI, ΔRMSEA, AIC, BIC)
- Compare R²(BI) across models

**Research Question 3a-c:** Categorical moderators
- Subgroup TSSEM:
  - Student vs. Instructor user role
  - K-12 vs. Higher Education
  - AI Tool Type: ChatGPT vs. Intelligent Tutoring Systems vs. LMS-integrated AI
  - Pre-ChatGPT (2015-2022) vs. Post-ChatGPT (2023-2025)

---

### 5.2 Moderator Analysis: OSMASEM

**Use OSMASEM for:**

**Research Question 3 (continuous moderators):**
- Publication year (continuous: 2015-2025)
- Education level (ordinal: K-12=1, Undergraduate=2, Graduate=3)
- Sample mean age (if sufficient studies report)

**Example OSMASEM Model:**

```r
# Year as continuous moderator of PE→BI path
osmasem_year <- osmasem(
  model = "
    BI ~ (beta_PE_0 + beta_PE_year*data.year)*PE + beta_EE*EE
    UB ~ beta_BI*BI
  ",
  data = correlation_matrices,
  n = sample_sizes,
  moderators = data.frame(year = publication_years - 2020)  # Center at 2020
)

summary(osmasem_year)
# Output: beta_PE_0 = average PE→BI path in 2020
#         beta_PE_year = change in PE→BI per year
```

**Interpretation:**
- If `beta_PE_year` > 0 and significant → PE→BI path strengthens over time
- If `beta_PE_year` < 0 → PE→BI path weakens over time

---

### 5.3 Decision Rules

**Start with TSSEM:**
1. Run Stage 1 on full sample
2. Examine heterogeneity (I², Q per correlation)
3. Fit Models 1, 2, 3 in Stage 2
4. Identify best-fitting model

**If high heterogeneity (I² > 75% for key paths):**
- Proceed to moderator analysis

**For categorical moderators:**
- Use subgroup TSSEM (separate Stage 1 per subgroup)
- Compare pooled correlations across subgroups
- Compare path coefficients across subgroups

**For continuous moderators:**
- Use OSMASEM
- Test one moderator at a time (avoid overfitting)
- Report TSSEM main effects + OSMASEM moderator effects

---

## 6. Technical Considerations

### 6.1 Sample Size Requirements

**TSSEM:**
- **Minimum k:** 10 studies (can work with fewer, but unstable)
- **Recommended k:** ≥20 studies for Stage 1
- **Per correlation:** ≥5 studies reporting each correlation (more is better)

**OSMASEM:**
- **Minimum k:** 30 studies (for moderator testing)
- **Per moderator:** ≥40 studies recommended for continuous moderators
- **Moderator range:** Need variance on moderator (not all clustered at one value)

---

### 6.2 Convergence Issues

**TSSEM:**
- Stage 1 rarely fails (unless severe data issues)
- Stage 2 may fail if:
  - Model is misspecified (wrong paths)
  - Pooled matrix is non-positive definite (rare with FIML)
  - Starting values are poor

**OSMASEM:**
- More prone to convergence failure
- Common causes:
  - Too many parameters (overparameterized)
  - Too few studies for complexity
  - Poor starting values
- **Solutions:**
  - Simplify model (fewer moderators)
  - Increase iterations (`mxOption`)
  - Try different optimizers

---

### 6.3 Computation Time

**TSSEM (k=150 studies, 12 constructs):**
- Stage 1: ~30 seconds
- Stage 2 (simple model): ~5 seconds
- Stage 2 (complex model): ~15 seconds
- Total for 3 models: ~1 minute

**OSMASEM (k=150 studies, 12 constructs, 1 moderator):**
- Single model: 5-30 minutes (depending on complexity)
- 3 models: 15-90 minutes
- Complex moderator models: Up to several hours

**Implication:** TSSEM allows rapid model iteration; OSMASEM requires patience

---

## 7. Reporting Standards

### 7.1 TSSEM Reporting

**Stage 1 Report:**
- Number of studies (k) and total N
- Pooled correlations (table with 95% CI)
- Heterogeneity statistics (I², Q, τ²) per correlation
- Number of studies contributing to each correlation

**Stage 2 Report:**
- Model specification (path diagram)
- Path coefficients with 95% CI (table)
- Model fit indices (χ², df, p, CFI, TLI, RMSEA, SRMR)
- R² for endogenous variables
- Indirect effects (if applicable)

**Model Comparison:**
- Fit indices for all models (table)
- Δχ², ΔCFI, ΔRMSEA, AIC, BIC
- Best-fitting model identified

---

### 7.2 OSMASEM Reporting

**Report:**
- Model specification with moderator
- Main effect path coefficients
- Moderator effect coefficients (e.g., β_year)
- Model fit indices
- Interpretation of moderator effects (substantive meaning)

**Example:**
"OSMASEM revealed that publication year moderated the PE→BI path (β_year = .02, p = .012), indicating that the relationship between performance expectancy and behavioral intention strengthened by .02 per year from 2015 to 2025."

---

## 8. Practical Example

### Scenario: Testing Culture as Moderator

**Research Question:** Does individualism (Hofstede score) moderate the SI→BI path?

**Hypothesis:** Collectivist cultures (low individualism) show stronger SI→BI path (social influence matters more).

---

**Approach 1: TSSEM (Categorical)**

**Step 1:** Dichotomize individualism
- Individualist: Hofstede score ≥ 50
- Collectivist: Hofstede score < 50

**Step 2:** Subgroup TSSEM
```r
# Stage 1 - Individualist countries
stage1_ind <- tssem1(Cov = cor_matrices_ind, n = n_ind, method = "REM")

# Stage 1 - Collectivist countries
stage1_col <- tssem1(Cov = cor_matrices_col, n = n_col, method = "REM")

# Stage 2 - Fit same model on both
model_ind <- tssem2(stage1_ind, Amatrix=A, Smatrix=S)
model_col <- tssem2(stage1_col, Amatrix=A, Smatrix=S)

# Compare SI→BI path
beta_SI_BI_ind <- coef(model_ind)["beta_SI_BI"]  # e.g., .25
beta_SI_BI_col <- coef(model_col)["beta_SI_BI"]  # e.g., .38
```

**Interpretation:** SI→BI is stronger in collectivist cultures (.38 vs. .25)

**Limitation:** Dichotomization loses information (all 0-49 treated same, all 50-100 treated same)

---

**Approach 2: OSMASEM (Continuous)**

**Step 1:** Use continuous Hofstede score
```r
# Prepare moderator data
moderator_data <- data.frame(
  study_id = study_ids,
  individualism = hofstede_scores - 50  # Center at 50
)

# OSMASEM with individualism moderating SI→BI
osmasem_culture <- osmasem(
  model = "
    BI ~ beta_PE*PE + beta_EE*EE + (beta_SI_0 + beta_SI_ind*data.individualism)*SI
    UB ~ beta_BI*BI
  ",
  data = cor_matrices,
  n = sample_sizes,
  moderators = moderator_data
)

summary(osmasem_culture)
# beta_SI_0 = SI→BI path at individualism=50 (e.g., .32)
# beta_SI_ind = change in SI→BI per 1-point increase in individualism (e.g., -.003)
```

**Interpretation:**
- At individualism=50 (moderate): SI→BI = .32
- At individualism=20 (collectivist): SI→BI = .32 + (-.003)×(20-50) = .32 + .09 = .41
- At individualism=80 (individualist): SI→BI = .32 + (-.003)×(80-50) = .32 - .09 = .23

**Conclusion:** SI→BI decreases by .003 per 1-point increase in individualism (stronger in collectivist cultures)

**Advantage:** Uses full range of individualism scores; more precise estimate

---

### Which to Use?

**Use TSSEM if:**
- Clear theoretical dichotomy (individualist vs. collectivist)
- Want simple, interpretable results
- Committee prefers clear subgroups

**Use OSMASEM if:**
- Individualism is truly continuous
- Want to model full range (not just 2 categories)
- Adequate sample size (k ≥ 40 with variance on moderator)

**Our recommendation:** Report both
1. TSSEM subgroup analysis (simple, clear)
2. OSMASEM continuous (precise, uses full information)
3. Show that both approaches converge on same conclusion

---

## 9. Summary and Recommendations

### Use TSSEM for:
✅ Primary structural model testing
✅ Comparing multiple models (Models 1, 2, 3)
✅ Categorical moderators (subgroup analysis)
✅ Transparency and simplicity
✅ Rapid model iteration

### Use OSMASEM for:
✅ Continuous moderators (year, culture scores)
✅ Moderator interactions
✅ Path-specific heterogeneity
✅ Most accurate standard errors
✅ Complex moderator models

### Hybrid Strategy (Recommended):
1. **TSSEM first** → main effects, model comparison, categorical moderators
2. **OSMASEM second** → continuous moderators, interactions
3. **Triangulate** → show convergence across methods
4. **Report both** → transparency and rigor

---

## References

Cheung, M. W. L. (2015). *Meta-analysis: A structural equation modeling approach*. Wiley.

Cheung, M. W. L., & Chan, W. (2005). Meta-analytic structural equation modeling: A two-stage approach. *Psychological Methods*, 10(1), 40-64.

Jak, S., & Cheung, M. W. L. (2020). Meta-analytic structural equation modeling with moderating effects on SEM parameters. *Psychological Methods*, 25(4), 430-455.

Yu, J., Downes, P. E., Carter, K. M., & O'Boyle, E. H. (2016). The problem of effect size heterogeneity in meta-analytic structural equation modeling. *Journal of Applied Psychology*, 101(10), 1457-1473.
