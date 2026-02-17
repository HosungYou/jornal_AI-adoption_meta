# Correlation Matrix Extraction Guide for MASEM

## Overview

This guide provides detailed, step-by-step instructions for extracting correlation matrices from primary studies. Accurate correlation extraction is **critical** for MASEM, as these values form the foundation of all meta-analytic structural equation modeling analyses.

---

## 1. Finding Correlation Matrices in Studies

### 1.1 Common Locations

**Priority Search Order:**

1. **Results Section Tables**
   - Table titles: "Correlations," "Descriptive Statistics and Correlations," "Correlation Matrix"
   - Often Table 2 or Table 3 (after demographics)
   - Look for symmetric tables with 1.00 on diagonal

2. **Appendices**
   - "Appendix A: Correlation Matrix"
   - "Appendix: Descriptive Statistics"
   - Often placed in appendices when many constructs (large tables)

3. **Supplementary Materials**
   - Journal website supplementary files
   - Open Science Framework (OSF) repositories
   - Author personal websites or ResearchGate
   - Look for links like "Online Supplement" or "Additional Materials"

4. **Embedded in Text**
   - Rarely, small matrices reported in text (e.g., "PE correlated with BI (r=.52)")
   - More common in older studies or brief reports

**Search Strategy:**
- Use PDF search (Ctrl+F / Cmd+F): "correlation," "corr," "means and standard deviations"
- Scan all tables visually (some tables not titled "correlation" but contain correlation data)
- Check figure captions (sometimes correlation heatmaps presented as figures)

---

### 1.2 Identifying Correlation Tables vs. Other Tables

**Correlation Table Characteristics:**

✅ **Is a correlation table if:**
- Symmetric matrix (same rows and columns)
- Diagonal values = 1.00 (or reliability coefficients like α)
- Values in range [-1, 1]
- Variable names in rows match column names
- Lower triangle and upper triangle mirror each other (or one is blank)

❌ **Not a correlation table if:**
- Regression table (β, t, p columns; different variables in rows vs. predictors)
- Descriptive statistics only (M, SD, Min, Max but no pairwise values)
- Factor loadings (items loading on factors, not inter-factor correlations)
- Covariance matrix (values can exceed 1.00, no 1.00 on diagonal)
- Discriminant validity table (HTMT or Fornell-Larcker, may show √AVE on diagonal)

**Borderline Case: Discriminant Validity Tables**
- Fornell-Larcker criterion tables show correlations below diagonal and √AVE on diagonal
- **Decision:** Extract correlations from below diagonal; ignore diagonal (it's √AVE, not 1.00)

---

## 2. Reading and Transcribing Correlation Tables

### 2.1 Standard Lower-Triangle Format

**Example Table:**

```
Table 3. Means, Standard Deviations, and Correlations

Variable         M     SD    1     2     3     4     5
1. PE           4.2   0.8  (.89)
2. EE           3.9   0.9   .45  (.85)
3. SI           3.5   1.0   .38   .42  (.80)
4. ATT          4.0   0.9   .61   .53   .40  (.92)
5. BI           4.1   0.8   .52   .48   .40   .67  (.90)

Note: N = 312. Reliabilities (Cronbach's α) in parentheses on diagonal.
Correlations ≥ .11 are significant at p < .05.
```

**Extraction:**

| Construct 1 | Construct 2 | r    | n   |
|-------------|-------------|------|-----|
| PE          | EE          | .45  | 312 |
| PE          | SI          | .38  | 312 |
| PE          | ATT         | .61  | 312 |
| PE          | BI          | .52  | 312 |
| EE          | SI          | .42  | 312 |
| EE          | ATT         | .53  | 312 |
| EE          | BI          | .48  | 312 |
| SI          | ATT         | .40  | 312 |
| SI          | BI          | .40  | 312 |
| ATT         | BI          | .67  | 312 |

**Notes:**
- Diagonal values (.89, .85, .80, .92, .90) are **reliabilities**, not correlations
- Record reliabilities separately in reliability dataset
- Extract only off-diagonal values as correlations

---

### 2.2 Upper-Triangle Format

Some studies report correlations in upper triangle:

```
         1     2     3     4
1. PE   1.00  .45   .38   .52
2. EE         1.00  .42   .48
3. SI               1.00  .40
4. BI                     1.00
```

**Extraction:** Same as lower triangle, just read from upper triangle
- PE-EE: .45 (row 1, column 2)
- PE-SI: .38 (row 1, column 3)
- PE-BI: .52 (row 1, column 4)
- EE-SI: .42 (row 2, column 3)
- EE-BI: .48 (row 2, column 4)
- SI-BI: .40 (row 3, column 4)

**Symmetry Check:** Lower and upper should mirror. If both reported, verify they match.

---

### 2.3 Full Matrix Format (Both Triangles)

```
         PE    EE    SI    BI
PE      1.00  .45   .38   .52
EE      .45   1.00  .42   .48
SI      .38   .42   1.00  .40
BI      .52   .48   .40   1.00
```

**Extraction:** Read from either triangle (they should be identical)

**Verification:**
- Check symmetry: PE-EE (.45) should equal EE-PE (.45)
- If values differ: Data entry error in original study (flag and use average or contact authors)

---

### 2.4 Handling Significance Markers

**Common Notations:**
- `*` = p < .05
- `**` = p < .01
- `***` = p < .001
- `†` or `+` = p < .10 (marginal)

**Example:**

```
         1      2      3
1. PE   1.00
2. EE   .45**  1.00
3. BI   .52*** .48**  1.00
```

**Extraction Rule:**
- **Record the numeric value, ignore asterisks**
- Extract: PE-EE = .45, PE-BI = .52, EE-BI = .48
- Do NOT record significance levels (meta-analysis focuses on effect sizes, not p-values)
- Do NOT code "significant" as 1 and "non-significant" as 0

**Why:** Meta-analysis pools effect sizes (correlations), not significance tests. A small but significant correlation (r=.12, p<.05, n=1000) and a large non-significant correlation (r=.35, p=.08, n=50) are both valuable data.

---

### 2.5 Non-Significant Correlations

**Case A: Study reports only significant correlations**

```
         1      2      3
1. PE   1.00
2. EE   .45**  1.00
3. BI   .52*** .48**  1.00
4. SI   ns     .42**  .40**  1.00
```

**Extraction:**
- PE-EE: .45
- PE-BI: .52
- EE-SI: .42
- EE-BI: .48
- SI-BI: .40
- **PE-SI: NA (missing)** — NOT zero

**Rationale:** "Non-significant" does not mean r=.00. Could be r=-.10 (p=.08) or r=.08 (p=.12). Coding as zero biases results toward null.

**MASEM Handling:** Missing correlations handled by FIML or multiple imputation in Stage 1 TSSEM.

---

**Case B: Study states non-significant correlations set to .00**

**Example:** "Non-significant correlations (p > .05) set to .00 in table."

**Extraction:**
- If study explicitly states this: Code blank/ns cells as .00
- **Flag study for sensitivity analysis:** Note `ns_as_zero = TRUE` in study metadata
- Sensitivity analysis will compare results with/without these studies

**Rationale:** Setting ns correlations to .00 is a methodological flaw (suppressors exist, true nulls are rare), but if study did this, we code what they report.

---

### 2.6 Partial Correlation Matrices

**Scenario:** Study reports only subset of correlations

**Example:**

```
Table 4. Key Correlations (Full matrix in online supplement)

PE-BI:  .52**
EE-BI:  .48**
SI-BI:  .40**
ATT-BI: .67***
```

**Extraction:**
- Code the 4 available correlations
- Matrix completeness: 4/10 possible pairs = 40% (if 5 constructs measured)
- **Action:** Check online supplement for full matrix
- If supplement unavailable: Code available data only, mark matrix as incomplete

---

### 2.7 Correlations Reported in Text (Not Tables)

**Example from Results text:**

"Performance expectancy significantly correlated with behavioral intention (r = .52, p < .001) and effort expectancy (r = .45, p < .01). Effort expectancy also correlated with behavioral intention (r = .48, p < .001)."

**Extraction:**
- PE-BI: .52
- PE-EE: .45
- EE-BI: .48

**Challenges:**
- Time-consuming to extract from narrative
- Risk of missing some pairs
- Prefer tabular data when available

---

## 3. Special Cases and Edge Cases

### 3.1 Constructs with Subscales/Dimensions

**Example:** Study measures "Trust" with three dimensions: Competence, Benevolence, Integrity

**Case A: Overall Trust score reported**

```
         TRU_Overall  BI
TRU      1.00        .58
BI       .58         1.00
```

**Extraction:** Code TRU-BI = .58 (use overall trust)

---

**Case B: Only subscales reported, no overall**

```
         TRU_Comp  TRU_Ben  TRU_Int  BI
TRU_Comp 1.00      .72      .68      .55
TRU_Ben  .72       1.00     .75      .52
TRU_Int  .68       .75      1.00     .60
BI       .55       .52      .60      1.00
```

**Extraction Options:**

**Option 1 (Preferred):** Average subscale correlations
- TRU-BI = (.55 + .52 + .60) / 3 = .56

**Option 2:** Use composite if study provides or if items can be aggregated
- Check if study reports second-order factor loadings
- If yes, compute weighted average based on loadings

**Option 3:** Request overall score from authors
- Email: "Do you have correlation between overall Trust and BI?"

**Document choice in notes:** "TRU-BI computed as average of subscale correlations."

---

### 3.2 Multiple Informants/Sources

**Example:** Study measures PE (self-report) and UB (supervisor-report), reports cross-source correlations

```
         PE_self  EE_self  UB_supervisor
PE_self  1.00     .45      .38
EE_self  .45      1.00     .32
UB_super .38      .32      1.00
```

**Extraction:**
- PE-EE: .45 (both self-report)
- PE-UB: .38 (cross-source — **note this**)
- EE-UB: .32 (cross-source)

**Quality Consideration:**
- Cross-source correlations **reduce common method bias**
- Flag as **higher quality** in quality assessment
- Note in metadata: `same_source = FALSE`

---

### 3.3 Listwise vs. Pairwise Deletion

**Scenario:** Study has missing data, uses pairwise deletion → different n for each correlation

**Example Table:**

```
         1     2     3     n
1. PE   1.00              312
2. EE   .45   1.00        (285)
3. BI   .52   .48   1.00  (298)

Note: Pairwise deletion used. Sample sizes in parentheses for each pair.
```

**Extraction:**
- PE-EE: r=.45, n=285
- PE-BI: r=.52, n=298
- EE-BI: r=.48, n=? (not reported, use minimum: 285)

**Recording:**
- If pairwise n reported: Use pairwise n
- If not reported: Use overall n (conservative)
- Note: `pairwise_deletion = TRUE` in study metadata

---

### 3.4 Heterogeneous Samples Reported Separately

**Example:** Study reports correlations separately for Males (n=150) and Females (n=162)

**Males:**
```
PE-BI: .55
EE-BI: .50
```

**Females:**
```
PE-BI: .48
EE-BI: .46
```

**Decision:** Treat as **two separate studies** for meta-analysis
- study_id: Smith2023_Male
- study_id: Smith2023_Female
- Code moderator: gender_sample = Male / Female

**Rationale:** Separate samples, potentially different construct meanings or relationships.

**Alternative (if justified):** Pool correlations using weighted average
- PE-BI_pooled = (.55×150 + .48×162) / (150+162) = .51
- Use only if study justifies pooling (e.g., no significant gender differences tested)

---

### 3.5 Longitudinal Data: Which Timepoint?

**Example:** T1 (n=400), T2 (n=350), T3 (n=320)

**Synchronous Correlations (within time):**
- T1: PE-BI = .48
- T2: PE-BI = .52
- T3: PE-BI = .55

**Cross-Lagged Correlations (across time):**
- T1_PE with T2_BI = .45
- T2_PE with T3_BI = .50

**Decision:**
- Extract **synchronous** correlations only (within-time)
- Choose **one timepoint:** Default = T3 (most mature attitudes)
- Ignore cross-lagged correlations (different temporal structure)

**Exception:** If T3 has high attrition (n<100) but T1 has n=400, use T1.

**Document:** "Used T3 data (n=320) for most complete adoption construct measurement."

---

### 3.6 Experimental Conditions

**Example:** RCT with Control (n=100, no AI) and Treatment (n=100, AI tool provided)

**Treatment Group Correlations:**
```
PE-BI: .52
EE-BI: .48
```

**Control Group Correlations:**
```
(No AI present, so PE/EE/BI about general technology)
PE-BI: .45
EE-BI: .50
```

**Decision:**
- Use **Treatment group only** (AI context)
- Exclude control group (not AI adoption)

**Exception:** If study manipulates AI explainability (high vs. low), both are AI contexts → code separately:
- study_id: Jones2024_HighTransparency
- study_id: Jones2024_LowTransparency
- Moderator: transparency_condition = high / low

---

### 3.7 Correlation Matrix with Reliability on Diagonal

**Example:**

```
         1      2      3
1. PE   (.89)
2. EE   .45    (.85)
3. BI   .52    .48    (.90)
```

**Extraction:**

**Correlations:**
- PE-EE: .45
- PE-BI: .52
- EE-BI: .48

**Reliabilities (separate dataset):**
- PE: α=.89
- EE: α=.85
- BI: α=.90

**Do NOT code diagonal as correlations.** Diagonal = 1.00 is the true correlation of a variable with itself; α is reliability (related but distinct).

---

## 4. Verification and Quality Checks

### 4.1 Range Check

**All correlation values must be in [-1, 1]**

**Common Errors:**
- Typo: ".52" misread as "5.2" → Invalid
- Decimal missing: "52" instead of ".52" → Out of range
- Negative sign missing: ".45" should be "-.45" (check table context)

**Action if out of range:**
- Double-check original table
- If study error: Contact authors or exclude value
- If data entry error: Correct

---

### 4.2 Symmetry Check

**Lower triangle should mirror upper triangle**

**Example:**

Lower triangle: PE-EE = .45
Upper triangle: EE-PE = .45 ✓

**If asymmetric:**
- Check for typo in study table
- Use average: (.45 + .46)/2 = .455 → round to .46
- Note discrepancy in coding notes

---

### 4.3 Diagonal Check

**Diagonal should be 1.00 (or reliability coefficients)**

**Valid:**
- All diagonals = 1.00
- All diagonals = α values (e.g., .85, .89, .92)

**Invalid:**
- Mixed: Some 1.00, some α → Study error or formatting issue
- Non-1.00 values without explanation → Check if covariance matrix (wrong data type)

---

### 4.4 Construct Alignment Check

**Verify row labels match column labels**

**Example Error:**

```
         PE    EE    BI
PE      1.00  .45   .52
EE      .45   1.00  .48
SI      .38   .42   1.00    ← Should be BI, not SI
```

**Action:**
- Check table carefully
- If mismatch: Review study to determine correct labeling
- If ambiguous: Contact authors

---

### 4.5 Sample Size Consistency

**Check that n is plausible**

**Red Flags:**
- n reported in correlation table differs from n in sample description
- n per correlation pair varies wildly (unless pairwise deletion stated)

**Example Issue:**
- Study states N=500 in Method section
- Correlation table note says N=285
- **Action:** Assume N=285 (likely effective sample after exclusions), note discrepancy

---

## 5. Transcription Best Practices

### 5.1 Use Structured Templates

**CSV Template:**

```csv
study_id,construct1,construct2,r,n,r_source,notes
Smith2023,PE,EE,0.45,312,pearson,
Smith2023,PE,BI,0.52,312,pearson,
Smith2023,EE,BI,0.48,312,pearson,
```

**Excel/Google Sheets:**
- Freeze header row
- Use data validation for construct names (dropdown from 12 standard constructs)
- Conditional formatting: Highlight if |r| > 1.0 (error detection)

---

### 5.2 Precision: Two Decimal Places

**Study reports:** r = .456
**Code as:** .46 (round to 2 decimals)

**Study reports:** r = .4
**Code as:** .40 (standardize to 2 decimals)

**Study reports:** r = .5**
**Code as:** .50 (ignore significance marker)

---

### 5.3 Construct Naming Consistency

**Use standardized construct abbreviations:**

Correct:
- PE, EE, SI, FC, BI, UB, ATT, SE, TRU, ANX, TRA, AUT

Incorrect:
- PerceivedUsefulness (use PE)
- Effort (use EE)
- Trust (use TRU)

**Rationale:** Enables automated aggregation across studies. All "PE" correlations pool together.

---

### 5.4 Document Ambiguities

**Use Notes Column for:**

- "Matrix in Table 3, page 12"
- "Averaged three trust subscales"
- "Used T3 data, not T1"
- "Pairwise n=285, differs from overall n=312"
- "Non-significant correlations coded as missing"

**Purpose:** Allows future reviewers/replicators to understand decisions.

---

## 6. Common Mistakes and How to Avoid Them

### Mistake 1: Coding Non-Significant Correlations as Zero

**Wrong:** "Study shows PE-SI is ns, so I'll code it as 0.00"
**Right:** Code as missing (NA)

**Why:** Non-significant doesn't mean zero. Could be r=.08 (small but non-zero).

---

### Mistake 2: Including Diagonal Values as Correlations

**Wrong:** Coding PE-PE = .89 as a correlation
**Right:** Recognize .89 as reliability (α), code separately

**Why:** Diagonal is reliability or by definition 1.00, not a pairwise correlation.

---

### Mistake 3: Ignoring Significance Stars

**Wrong:** Coding PE-BI = .52** as r=.52 and significance=.01
**Right:** Code r=.52, ignore stars

**Why:** Meta-analysis uses effect sizes (r), not p-values.

---

### Mistake 4: Not Checking Symmetry

**Wrong:** Extracting from both triangles without verifying they match
**Right:** Extract from one triangle, verify symmetry

**Why:** Catches typos and study errors.

---

### Mistake 5: Mixing Constructs Across Studies

**Wrong:**
- Study A calls it "Perceived Usefulness" → Code as PU
- Study B calls it "Performance Expectancy" → Code as PE
- (These are the same construct but coded differently)

**Right:** Harmonize both to **PE** using construct mapping rules

**Why:** Meta-analysis pools same constructs across studies.

---

### Mistake 6: Forgetting to Extract Sample Size

**Wrong:** Only extracting r values
**Right:** Extract r AND n for every correlation (or study-level n)

**Why:** MASEM weights by sample size. No n = cannot include in analysis.

---

### Mistake 7: Averaging Non-Independent Correlations

**Wrong:** Study reports PE-BI at T1 (.48) and T2 (.52), averaging to .50
**Right:** Choose one timepoint (T1 or T2), not average

**Why:** T1 and T2 are same sample (dependent), averaging double-counts the study.

---

### Mistake 8: Including Cross-Lagged Correlations

**Wrong:** Coding T1_PE with T2_BI as PE-BI correlation
**Right:** Only code synchronous (within-time) correlations

**Why:** Cross-lagged correlations have different meaning (temporal causality), not structural relationships.

---

## 7. Workflow Example: Step-by-Step

**Study:** Johnson et al. (2024). "AI Chatbot Adoption in Higher Education." *Computers & Education*, 45(3), 210-225.

### Step 1: Locate Correlation Data
- Scan article: Find Table 4 on page 218 titled "Descriptive Statistics and Correlations"

### Step 2: Identify Constructs
- Table has: PU, PEOU, SN, ATT, INT, Trust
- Map to standard constructs:
  - PU → PE (Perceived Usefulness for Learning)
  - PEOU → EE (Perceived Ease of Use)
  - SN → SI (Subjective Norm - peer/instructor influence)
  - ATT → ATT (Attitude)
  - INT → BI (Intention to use for academic work)
  - Trust → TRU (AI Trust in educational context)

### Step 3: Extract Correlations

Table 4:
```
         M    SD    1     2     3     4     5     6
1. PU   4.1  0.9  (.91)
2. PEOU 3.8  1.0   .48  (.88)
3. SN   3.5  1.1   .35   .40  (.85)
4. ATT  4.0  0.8   .62   .55   .38  (.93)
5. INT  3.9  0.9   .56   .50   .42   .68  (.90)
6. Trust 3.7 1.0   .45   .38   .30   .52   .60  (.89)

N = 285. Reliabilities (Cronbach's α) in parentheses.
```

**Correlations Extracted:**

| Construct1 | Construct2 | r   | n   |
|------------|------------|-----|-----|
| PE         | EE         | .48 | 285 |
| PE         | SI         | .35 | 285 |
| PE         | ATT        | .62 | 285 |
| PE         | BI         | .56 | 285 |
| PE         | TRU        | .45 | 285 |
| EE         | SI         | .40 | 285 |
| EE         | ATT        | .55 | 285 |
| EE         | BI         | .50 | 285 |
| EE         | TRU        | .38 | 285 |
| SI         | ATT        | .38 | 285 |
| SI         | BI         | .42 | 285 |
| SI         | TRU        | .30 | 285 |
| ATT        | BI         | .68 | 285 |
| ATT        | TRU        | .52 | 285 |
| BI         | TRU        | .60 | 285 |

**Reliabilities Extracted:**

| Construct | α   |
|-----------|-----|
| PE        | .91 |
| EE        | .88 |
| SI        | .85 |
| ATT       | .93 |
| BI        | .90 |
| TRU       | .89 |

### Step 4: Verify
- Range check: All r ∈ [.30, .68] ✓
- Symmetry: Lower triangle only, no upper triangle to check
- Diagonal: All α values, extracted separately ✓
- Sample size: n=285 consistent ✓

### Step 5: Record in Dataset
- Add to `correlations.csv`: 15 rows (15 correlation pairs)
- Add to `reliability.csv`: 6 rows (6 constructs)
- Add to `studies.csv`: Johnson2024, n=285, ai_tool_type=Chatbot/LLM, education_level=Undergraduate, user_role=Student

### Step 6: Document
- Notes: "Correlation matrix in Table 4, page 218. All constructs harmonized to standard 12. Sample: undergraduate students using AI chatbot for coursework."

**Complete.**

---

## 8. Summary Checklist

Before finalizing correlation extraction for a study, verify:

- [ ] Correlation matrix located (table number, page documented)
- [ ] Constructs mapped to 12 standard constructs
- [ ] All off-diagonal values extracted
- [ ] Diagonal values (if α/CR) extracted to reliability dataset
- [ ] Sample size recorded (overall or pairwise)
- [ ] Range check: All |r| ≤ 1.0
- [ ] Symmetry verified (if applicable)
- [ ] Significance markers ignored (extracted r values only)
- [ ] Non-significant correlations coded as missing (not zero)
- [ ] Precision: All r values to 2 decimal places
- [ ] Notes documented for any special cases or ambiguities
- [ ] Data entered into structured template (CSV/Excel)

---

## References

Cheung, M. W. L. (2015). metaSEM: An R package for meta-analysis using structural equation modeling. *Frontiers in Psychology*, 5, 1521.

Cooper, H. M. (2017). *Research synthesis and meta-analysis: A step-by-step approach* (5th ed.). Sage Publications.

Lipsey, M. W., & Wilson, D. B. (2001). *Practical meta-analysis*. Sage Publications.
