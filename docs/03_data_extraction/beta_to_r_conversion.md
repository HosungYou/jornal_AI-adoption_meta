# Beta to Pearson r Conversion Protocol

## Overview

Many studies report only standardized path coefficients (β) from regression or structural equation modeling without reporting bivariate correlations. To include these studies in meta-analytic structural equation modeling (MASEM), we convert β to Pearson r using the Peterson & Brown (2005) method.

---

## 1. Rationale for β→r Conversion

### 1.1 Why Convert?

**Problem:** MASEM requires correlation matrices, but many SEM studies only report path coefficients (β).

**Solution:** Convert β to r using validated approximation formula.

**Benefit:** Include more studies, increasing meta-analytic power and reducing publication bias.

**Trade-off:** Conversion introduces approximation error, addressed via sensitivity analysis.

---

### 1.2 When to Use Conversion

**Use β→r conversion when:**
- ✅ Study reports standardized path coefficients (β)
- ✅ Study does NOT report correlation matrix
- ✅ β values are between constructs of interest
- ✅ β is standardized (not unstandardized b)

**Do NOT use conversion when:**
- ❌ Study reports correlation matrix (use direct r values)
- ❌ Only unstandardized coefficients (b) available
- ❌ β is from complex models with multiple mediators (indirect effects confound relationship)
- ❌ β is from interaction terms or non-linear relationships

---

## 2. Peterson & Brown (2005) Method

### 2.1 Formula

**Basic Formula:**

```
r ≈ β + .05λ

where:
  λ = 1  if β ≥ 0
  λ = -1 if β < 0
```

**In plain language:**
- If β is positive: add 0.05
- If β is negative: subtract 0.05

---

### 2.2 Theoretical Basis

**Why this works:**

The relationship between β (standardized regression coefficient) and r (bivariate correlation) depends on the correlation between predictors in the regression model.

**Simplified case:** In bivariate regression (one predictor), β = r exactly.

**Multiple regression:** β ≠ r because β controls for other predictors.

Peterson & Brown (2005) meta-analyzed the β-r relationship across thousands of studies and found:
- Average r ≈ β + .05 for positive relationships
- Average r ≈ β - .05 for negative relationships

**Intuition:** β is partial (controlling for others); r is bivariate (not controlling). Bivariate r is typically slightly larger in magnitude than β.

---

### 2.3 Assumptions

**The conversion assumes:**

1. **Linear relationships:** No interactions or curvilinear effects
2. **Moderate predictor intercorrelations:** Not extremely high multicollinearity
3. **Comparable model structures:** Most studies use similar TAM/UTAUT structures
4. **No suppression effects:** Rare in technology acceptance models

**When assumptions may be violated:**
- Complex mediation models with many paths
- Models with interaction terms
- Suppressor variables present

**Action if violated:** Flag for sensitivity analysis or exclude.

---

## 3. Conversion Procedure

### 3.1 Step-by-Step Guide

**Step 1: Verify β is standardized**

Look for:
- Table column labeled "β" or "Standardized Coefficient"
- Values in range roughly [-1, 1] (usually [-.80, .80])
- Study states "standardized coefficients reported"

**Red flags for unstandardized b:**
- Values > 1.0 or < -1.0 (unless odd scaling)
- Table labeled "B" or "Unstandardized"
- Standard errors are very different from coefficients

**If unsure:** Check study methods section or exclude.

---

**Step 2: Extract β value**

Example SEM path results table:

```
Path              β      SE    t      p
PE → BI          .40    .05   8.00   <.001
EE → BI          .35    .06   5.83   <.001
SI → BI          .25    .05   5.00   <.001
```

Extract:
- PE→BI: β = .40
- EE→BI: β = .35
- SI→BI: β = .25

---

**Step 3: Apply conversion formula**

**Example 1:** β = .40 (positive)
- λ = 1 (because β ≥ 0)
- r ≈ .40 + .05(1) = .40 + .05 = **.45**

**Example 2:** β = -.30 (negative, e.g., ANX→BI)
- λ = -1 (because β < 0)
- r ≈ -.30 + .05(-1) = -.30 - .05 = **-.35**

**Example 3:** β = .00 (null relationship)
- λ = 1 (assume positive direction)
- r ≈ .00 + .05(1) = **.05**
- (Conservative: assumes small positive rather than exact zero)

---

**Step 4: Record conversion metadata**

For each converted correlation, record:

| Field | Value | Example |
|-------|-------|---------|
| `r` | Converted r value | .45 |
| `r_source` | "beta_converted" | beta_converted |
| `original_beta` | Original β value | .40 |
| `beta_se` | SE of β (if available) | .05 |
| `beta_model` | Model type | SEM, regression |
| `study_id` | Study identifier | Smith2023 |

---

**Step 5: Flag for sensitivity analysis**

Mark study with:
- `beta_converted = TRUE` in study-level metadata
- Include in sensitivity analysis comparing:
  - Full sample (r + converted β)
  - r-only subsample (excluding converted β studies)

---

## 4. Special Cases

### 4.1 Multiple Paths to Same Outcome

**Scenario:** Study reports β for PE→BI, EE→BI, SI→BI in same regression model.

**Action:** Convert each β separately.

**Example:**

```
PE → BI: β=.40 → r≈.45
EE → BI: β=.35 → r≈.40
SI → BI: β=.25 → r≈.30
```

**Note:** These are all paths TO BI. We still need correlations AMONG predictors (PE-EE, PE-SI, EE-SI).

**If predictor intercorrelations not reported:** Code as missing (NA). MASEM will handle missing cells.

---

### 4.2 Mediation Models

**Scenario:** Study reports PE→ATT (β=.50), ATT→BI (β=.60), PE→BI (β=.20, direct effect).

**Action:**
- Convert PE→ATT: β=.50 → r≈.55
- Convert ATT→BI: β=.60 → r≈.65
- **Do NOT convert PE→BI direct effect** (it's partial, controlling for mediator; not comparable to bivariate r)

**Alternative:**
- Check if study reports total effect of PE→BI (direct + indirect)
- If total effect available: Convert total effect
- If not: Use only PE→ATT and ATT→BI paths

**Rationale:** Direct effects in mediation models are heavily controlled, not comparable to bivariate correlations.

---

### 4.3 Structural vs. Measurement Model Coefficients

**ONLY convert structural paths** (between latent constructs).

**Do NOT convert:**
- Factor loadings (measurement model: items → latent construct)
- Item-level correlations
- Cross-loadings

**Example (Correct):**

Structural model:
```
PE → BI: β=.40 → Convert to r≈.45 ✓
```

Measurement model:
```
Item1 → PE: λ=.85 → Do NOT convert ✗
```

---

### 4.4 Interaction Effects

**Scenario:** Study reports β for PE×EE → BI (interaction term).

**Action:** Do NOT convert interaction terms.

**Rationale:** Interaction β is not a bivariate correlation; it's a moderation effect.

**Alternative:** If study reports simple slopes or conditional effects, consider coding as moderator data.

---

### 4.5 Negative Beta Values

**Example:** ANX→BI, β = -.35 (anxiety reduces intention)

**Conversion:**
- λ = -1 (because β < 0)
- r ≈ -.35 + .05(-1) = -.35 - .05 = **-.40**

**Interpretation:** Negative β becomes more negative when converted to r (in absolute magnitude).

---

### 4.6 Very Small Beta Values

**Example:** β = .05

**Conversion:**
- λ = 1 (positive)
- r ≈ .05 + .05(1) = **.10**

**Note:** Conversion doubles a small positive β. This is expected (partial vs. bivariate).

**Quality consideration:** Very small β may indicate weak relationship. No special handling needed; include in analysis.

---

## 5. Accuracy and Limitations

### 5.1 Conversion Accuracy

**Peterson & Brown (2005) Findings:**

- **Mean absolute error:** .03 (3 percentage points)
- **95% of conversions:** Within .06 of true r
- **Best accuracy when:** Moderate predictor intercorrelations (.30-.50)

**Our context (AI adoption):**
- TAM/UTAUT predictors typically correlate .30-.60
- Model structures are consistent across studies
- Expected conversion accuracy: Good (MAE ≈ .03-.04)

---

### 5.2 When Conversion is Less Accurate

**Lower accuracy when:**

1. **High multicollinearity:** Predictors correlate > .70
   - Example: PE and ATT often correlate highly
   - β may be unstable, conversion less reliable

2. **Suppression effects:** One predictor suppresses another
   - Rare in TAM/UTAUT models
   - Sign of β may differ from sign of r

3. **Small sample sizes:** β estimates are unstable when n < 100
   - Conversion compounds sampling error

4. **Complex models:** Many predictors, mediation chains
   - β is highly partial, less similar to bivariate r

**Action:** Flag studies with these characteristics for sensitivity analysis.

---

### 5.3 Systematic Bias

**Peterson & Brown (2005) tested for bias:**

- **No systematic overestimation or underestimation** across typical regression models
- Formula is unbiased estimator of r on average

**Our approach:**
- Accept small random error (MAE ≈ .03) as trade-off for including more studies
- Sensitivity analysis quantifies impact on conclusions

---

## 6. Sensitivity Analysis Plan

### 6.1 Rationale

**Question:** Do β-converted correlations bias meta-analytic results?

**Approach:** Compare results with and without converted studies.

---

### 6.2 Analysis Steps

**Step 1: Full Sample Analysis**
- Include all studies (r + converted β)
- Run TSSEM Stage 1 pooling
- Estimate all three structural models

**Step 2: r-Only Subsample Analysis**
- Exclude studies with beta_converted = TRUE
- Re-run TSSEM Stage 1 and model fitting
- Compare pooled correlations and path coefficients

**Step 3: Comparison**

| Metric | Full Sample | r-Only | Difference | Conclusion |
|--------|-------------|--------|------------|------------|
| Pooled r (PE-BI) | .52 | .50 | .02 | Negligible |
| Path β (PE→BI) | .35 | .34 | .01 | Negligible |
| Model fit CFI | .96 | .95 | .01 | Negligible |
| k studies | 150 | 105 | -45 | 30% loss |

**Decision Rule:**
- If differences < .05 for correlations and < .03 for paths: Conversion has minimal impact, use full sample
- If differences ≥ .05: Report both analyses, discuss implications

---

### 6.3 Reporting

**In Results section:**

"Of k=150 included studies, 45 (30%) contributed correlation data via β→r conversion using the Peterson & Brown (2005) method. Sensitivity analysis compared meta-analytic results for the full sample versus the r-only subsample (k=105). Pooled correlations differed by a mean of .02 (range: .00-.04), and structural path coefficients differed by a mean of .01 (range: .00-.03). Model fit indices were virtually identical (ΔCFI < .01, ΔRMSEA < .005). Given negligible differences, we report results for the full sample to maximize statistical power and reduce sampling error."

---

## 7. Implementation in R

### 7.1 Conversion Function

```r
# Function to convert beta to r using Peterson & Brown (2005)
beta_to_r <- function(beta) {
  lambda <- ifelse(beta >= 0, 1, -1)
  r <- beta + 0.05 * lambda
  return(r)
}

# Example usage
betas <- c(0.40, -0.30, 0.52, -0.15, 0.00)
rs <- beta_to_r(betas)

data.frame(
  beta = betas,
  r = rs,
  difference = rs - betas
)
#   beta    r difference
# 1  0.40 0.45       0.05
# 2 -0.30 -0.35     -0.05
# 3  0.52 0.57       0.05
# 4 -0.15 -0.20     -0.05
# 5  0.00 0.05       0.05
```

---

### 7.2 Batch Conversion with Metadata

```r
library(dplyr)

# Load beta coefficients from studies
beta_data <- read.csv("data/beta_paths.csv")
# Columns: study_id, construct1, construct2, beta, beta_se

# Convert to r
correlations <- beta_data %>%
  mutate(
    r = beta_to_r(beta),
    r_source = "beta_converted",
    original_beta = beta,
    conversion_date = Sys.Date()
  ) %>%
  select(study_id, construct1, construct2, r, r_source,
         original_beta, beta_se, conversion_date)

# Save converted correlations
write.csv(correlations, "data/converted_correlations.csv", row.names = FALSE)
```

---

### 7.3 Sensitivity Analysis Code

```r
library(metaSEM)

# Load all correlation data
all_corrs <- read.csv("data/all_correlations.csv")

# Subset: r-only (exclude beta-converted)
r_only_corrs <- all_corrs %>% filter(r_source != "beta_converted")

# Run TSSEM Stage 1 on both datasets
stage1_full <- tssem1(Cov = cor_matrices_full, n = sample_sizes_full)
stage1_ronly <- tssem1(Cov = cor_matrices_ronly, n = sample_sizes_ronly)

# Compare pooled correlations
pooled_full <- coef(stage1_full)
pooled_ronly <- coef(stage1_ronly)

comparison <- data.frame(
  correlation_pair = names(pooled_full),
  full_sample = pooled_full,
  r_only = pooled_ronly,
  difference = pooled_full - pooled_ronly
)

# Calculate mean absolute difference
mean(abs(comparison$difference))
```

---

## 8. Recording and Documentation

### 8.1 Data Entry Template

**CSV Structure:**

```csv
study_id,construct1,construct2,r,n,r_source,original_beta,beta_se,notes
Smith2023,PE,BI,0.45,285,beta_converted,0.40,0.05,Converted from SEM path
Smith2023,EE,BI,0.40,285,beta_converted,0.35,0.06,Converted from SEM path
Jones2024,PE,BI,0.52,400,pearson,NA,NA,Direct correlation from Table 3
```

**Key Fields:**
- `r_source`: "pearson" or "beta_converted"
- `original_beta`: Original β value (NA if r_source = pearson)
- `beta_se`: Standard error of β (for meta-regression if needed)

---

### 8.2 Study-Level Metadata

**studies.csv:**

```csv
study_id,beta_converted,pct_beta_converted,n_correlations,n_beta_converted
Smith2023,TRUE,100,15,15
Jones2024,FALSE,0,10,0
Brown2025,TRUE,40,10,4
```

**Fields:**
- `beta_converted`: TRUE if ANY correlations are beta-converted
- `pct_beta_converted`: Percentage of study's correlations from β conversion
- `n_correlations`: Total correlations extracted
- `n_beta_converted`: Number of correlations from β conversion

---

### 8.3 Conversion Log

**conversion_log.csv:**

Track all conversions for audit trail:

```csv
study_id,path,beta,r,conversion_date,coder_id
Smith2023,PE→BI,0.40,0.45,2026-03-15,coder_A
Smith2023,EE→BI,0.35,0.40,2026-03-15,coder_A
```

---

## 9. Quality Control

### 9.1 Verification Checks

**Post-Conversion Checks:**

1. **Range check:** All converted r values in [-1, 1]
   - If |r| > 1.0: Error in conversion or data entry

2. **Direction check:** Sign of r matches sign of β
   - Positive β → positive r
   - Negative β → negative r

3. **Magnitude check:** |r| > |β| for positive β; |r| > |β| for negative β
   - If violated: Conversion error

4. **Plausibility check:** Converted r aligns with theoretical expectations
   - Example: PE→BI should be positive and moderate-to-large (.40-.70)

---

### 9.2 Example Checks

**Check 1: Range**
```r
converted <- read.csv("data/converted_correlations.csv")
any(abs(converted$r) > 1.0)  # Should be FALSE
```

**Check 2: Direction**
```r
converted %>%
  mutate(same_sign = sign(r) == sign(original_beta)) %>%
  summarize(all_same = all(same_sign))  # Should be TRUE
```

**Check 3: Magnitude**
```r
converted %>%
  mutate(
    expected_increase = ifelse(original_beta >= 0,
                                abs(r) >= abs(original_beta),
                                abs(r) >= abs(original_beta))
  ) %>%
  summarize(all_correct = all(expected_increase))  # Should be TRUE
```

---

## 10. Limitations and Caveats

### 10.1 Known Limitations

1. **Approximation, not exact:** Formula provides average relationship, not study-specific

2. **Model structure matters:** Accuracy depends on predictor intercorrelations

3. **Cannot recover lost information:** Bivariate r contains information that β (partial) does not

4. **Assumes comparability:** Assumes β from different studies are comparable

---

### 10.2 Mitigation Strategies

**Strategy 1: Sensitivity Analysis**
- Always compare full sample vs. r-only subsample
- Report both if differences are meaningful (>.05)

**Strategy 2: Quality Weighting**
- Consider weighting r-only studies more heavily in sensitivity analysis
- Or: Code beta-converted studies as lower quality

**Strategy 3: Subgroup Analysis**
- Examine if beta-converted studies differ systematically (year, region, quality)
- If clustered (e.g., all from China), address in moderator analysis

**Strategy 4: Transparent Reporting**
- Clearly report number and percentage of beta-converted studies
- Provide conversion formula and reference
- Acknowledge limitation in Discussion

---

## 11. Alternatives Considered

### 11.1 Alternative Methods

**Method 1: Exclude β-only studies**
- **Pro:** No approximation error
- **Con:** Lose 30-40% of potential studies, reduce power, increase publication bias risk

**Method 2: Contact authors for correlation matrices**
- **Pro:** Get exact r values
- **Con:** Low response rate (typically <30%), time-consuming, still lose most studies

**Method 3: Use other conversion formulas**
- Alwin & Hauser (1975): More complex, requires predictor correlations (rarely reported)
- **Con:** Peterson & Brown (2005) is most practical and validated

**Method 4: Compute r from other statistics (t, F, χ²)**
- **Pro:** Can extract from studies reporting only significance tests
- **Con:** Less accurate, requires exact sample sizes per test, limited applicability

**Decision:** Peterson & Brown (2005) balances accuracy, practicality, and inclusiveness.

---

## 12. Summary and Best Practices

### 12.1 When to Convert

✅ **Convert when:**
- Study reports standardized β
- No correlation matrix available
- β is for structural paths (not measurement model)
- Sample size adequate (n ≥ 100 preferred)

❌ **Do NOT convert when:**
- Correlation matrix is available (use direct r)
- Only unstandardized b reported
- β is from interaction terms or complex mediation models

---

### 12.2 Conversion Checklist

- [ ] Verify β is standardized (not b)
- [ ] Extract β value to 2 decimal places
- [ ] Apply formula: r ≈ β + .05λ (λ=1 if β≥0, λ=-1 if β<0)
- [ ] Record converted r
- [ ] Document r_source = "beta_converted"
- [ ] Record original_beta and beta_se
- [ ] Verify: |r| in [-1, 1]
- [ ] Verify: sign(r) = sign(β)
- [ ] Flag study for sensitivity analysis
- [ ] Add to conversion log

---

### 12.3 Reporting Template

**Methods Section:**

"Studies that reported only standardized path coefficients (β) without bivariate correlations were included by converting β to Pearson r using the Peterson & Brown (2005) approximation formula: r ≈ β + .05λ, where λ = 1 for positive β and λ = -1 for negative β. This method has been validated with mean absolute error of .03 across diverse regression models (Peterson & Brown, 2005). All converted correlations were flagged and sensitivity analyses compared results for the full sample versus the subsample with only directly reported correlations."

---

## References

Alwin, D. F., & Hauser, R. M. (1975). The decomposition of effects in path analysis. *American Sociological Review*, 40(1), 37-47.

Peterson, R. A., & Brown, S. P. (2005). On the use of beta coefficients in meta-analysis. *Journal of Applied Psychology*, 90(1), 175-181.
