# Decision Log: IRR Results and Auto-INCLUDE Full Verification

**Date:** 2026-03-06 (updated 2026-03-09)
**Decision Maker:** PI (R1)
**Status:** COMPLETED

---

## 1. Context

The screening pipeline (Option C: 2-Rater IRR + R1 Adjudicator) produced the following distribution from 1,457 T3 dual-AI screened records:

| Category | Count | Description |
|----------|-------|-------------|
| Auto-INCLUDE | 358 | Gemini + Claude both include |
| Auto-EXCLUDE | 15 | Gemini + Claude both exclude |
| TIER1 conflict | 95 | include vs exclude |
| TIER2 confirm | 495 | include + uncertain |
| TIER3 low | 494 | uncertain + uncertain |

Tab 1 (200 records) was coded independently by R2 and R3 for IRR establishment.
Tab 3 (135 records) was coded by R1 and completed (134/135).

---

## 2. IRR Results (Tab 1: 200 Records, R2 + R3)

### 2.1 Three-Category Agreement (I / X / U)

| Metric | Value | Interpretation |
|--------|-------|----------------|
| N (both coded) | 194 | 6 records missing one rater |
| Raw agreement | 150/194 = 77.3% | — |
| Cohen's kappa | 0.566 | Moderate (below 0.85 target) |

**Contingency table (3-category):**

|  | R3=I | R3=U | R3=X | Total |
|--|------|------|------|-------|
| R2=I | 44 | 4 | 7 | 55 |
| R2=U | 6 | 3 | 9 | 18 |
| R2=X | 10 | 8 | 103 | 121 |
| Total | 60 | 15 | 119 | 194 |

### 2.2 Binary Agreement (I vs X, U excluded)

Excluding uncertain (U) rows where neither rater committed to a clear judgment:

| Metric | Value | Interpretation |
|--------|-------|----------------|
| N | 164 | 30 rows with U excluded |
| Raw agreement | 147/164 = 89.6% | Good |
| Cohen's kappa (binary) | **0.762** | Substantial |
| PABAK | 0.793 | Prevalence-adjusted |

**Contingency table (binary):**

|  | R3=I | R3=X | Total |
|--|------|------|-------|
| R2=I | 44 | 7 | 51 |
| R2=X | 10 | 103 | 113 |
| Total | 54 | 110 | 164 |

### 2.3 Conservative Binary (U merged with X)

| Metric | Value | Interpretation |
|--------|-------|----------------|
| N | 194 | All rows, U treated as X |
| Raw agreement | 167/194 = 86.1% | Good |
| Cohen's kappa | 0.667 | Substantial |
| PABAK | 0.722 | Prevalence-adjusted |

### 2.4 Post-Adjudication Agreement (R2/R3 vs Gold Standard)

Gold standard = R2-R3 agreement where concordant; R1 adjudication where discordant.

| Metric | Value |
|--------|-------|
| Gold standard established | 192/200 rows (8 pending) |
| Gold distribution | I=52, X=137, U=3 |
| R2 vs Gold (binary I/X) | 164/175 = **93.7%**, kappa = **0.849** |
| R3 vs Gold (binary I/X) | 164/178 = **92.1%**, kappa = **0.816** |

### 2.5 Reporting Decision

**For the manuscript, report the following sequence:**

1. Initial 3-category kappa = 0.566 (moderate) — acknowledges initial calibration challenge
2. Binary kappa (U excluded) = 0.762 (substantial) — reflects raters' core discriminative ability
3. Post-adjudication individual accuracy: R2 kappa vs gold = 0.849, R3 kappa vs gold = 0.816
4. All discrepancies resolved by R1 (PI) as independent adjudicator

**Justification for kappa improvement:**
- The U (Uncertain) category introduced noise; raters were conservative when unsure
- When forced to a binary I/X decision, raters showed substantial agreement
- Base rate imbalance (X >> I) depresses raw kappa; PABAK = 0.793 adjusts for this
- Post-adjudication accuracy confirms both raters performed above the 0.80 threshold against the gold standard

---

## 3. Auto-INCLUDE Verification: Critical Finding

### 3.1 Empirical False Positive Rate

A 36-record verification sample from the 358 Auto-INCLUDE records was included in the IRR set (Tab 1, rows 86-121, marked as blue rows). Results:

| Outcome | Count | Rate |
|---------|-------|------|
| Confirmed Include (R2=R3=I) | 14 | 38.9% |
| Confirmed Include (conflict resolved as I) | 1 | 2.8% |
| Confirmed Exclude (conflict resolved as X) | 11 | 30.6% |
| Confirmed Exclude (R2=R3=X) | 10 | 27.8% |
| **Total Include** | **15** | **41.7%** |
| **Total Exclude** | **21** | **58.3%** |

**AI Auto-INCLUDE False Positive Rate = 58.3%**

Projected impact on 358 records: approximately 209 records would be excluded upon human verification, leaving ~149 actual includes.

### 3.2 Root Cause Analysis

The high false positive rate reflects the inherent limitation of title/abstract-level AI screening for MASEM-specific criteria:

- **E-FT1** (no correlation matrix/beta): Cannot be determined from abstract
- **E-FT2** (< 2 target constructs): AI may over-match construct terms
- **E-FT3** (not education context): Borderline cases misjudged
- **E-FT6** (full-text inaccessible): AI cannot detect access issues

---

## 4. Decision: Full Verification of Auto-INCLUDE (Tab 2)

### 4.1 Decision

**R1 (PI) will conduct full verification of all 358 Auto-INCLUDE records.**

This replaces the original plan of spot-checking 86 records (36 IRR + 50 R1).

### 4.2 Rationale

1. The 36-record verification sample revealed a 58.3% false positive rate — far too high to accept without full review
2. Full verification eliminates approximately 209 false positives, reducing downstream coding burden by ~60%
3. R1 verification at title/abstract level is efficient (~1-2 minutes per record, ~6-12 hours total)
4. This satisfies the PRISMA-trAIce requirement for "performance evaluation of AI tools" and "human verification of AI decisions"

### 4.3 Protocol

- **Reviewer:** R1 (PI) only — single reviewer is sufficient at this stage because:
  - Dual-AI screening already serves as the first filter
  - IRR has been established on the 200-record set (binary kappa = 0.762)
  - Cochrane guidance permits single-reviewer verification for AI-include decisions
  - Full-text data extraction (Phase 5) provides a second verification layer
- **Judgment:** I / X / U using the same coding guide (Tab 5)
- **Exclude codes:** E-FT1 through E-FT6
- **Output:** Updated Tab 2 with R1 judgment, code, and memo columns completed

### 4.4 Actual Outcome (Completed 2026-03-09)

| Metric | Predicted (36-sample) | Actual (358 full) |
|--------|----------------------|-------------------|
| Input records | 358 | 358 |
| Confirmed Include | ~150 (41.7%) | **137** (42.5%) → 135 after 2022 filter |
| Confirmed Exclude | ~208 (58.3%) | **185** (57.5%) → 187 after 2022 filter |
| False Positive Rate | 58.3% | **57.5%** |
| Prediction accuracy | — | Sample prediction within 1.2% of actual |

**Exclude code distribution (185 records, pre-filter):**

| Code | Count | Description |
|------|-------|-------------|
| E-FT3 | 106 | Not education context |
| E-FT2 | 48 | < 2 target constructs / constructs do not map |
| E-FT6 | 17 | Full-text inaccessible |
| E-FT1 | 8 | No correlation matrix/beta |
| E7 | 2 | Outside date range (pre-2022) |
| Unspecified | 6 | Excluded without specific code |

**Key finding:** The 36-record sample accurately predicted the population false positive rate (58.3% vs 57.5%), validating the sampling methodology.

### 4.5 Manuscript Reporting

The following will be reported in the Methods section:

> "Among the 358 records classified as Auto-INCLUDE by dual-AI consensus (Gemini + Claude), a 36-record verification sample revealed a 58.3% false positive rate. Based on this finding, the PI (R1) conducted full human verification of all 358 records. Of these, 137 were confirmed for inclusion and 185 were reclassified as excluded (E-FT3: 106, E-FT2: 48, E-FT6: 17, E-FT1: 8, other: 6). After applying the revised year filter (2022–2026), 135 records remained as confirmed includes. This verification step demonstrates the necessity of human oversight in AI-assisted screening, consistent with PRISMA-trAIce guidelines."

---

## 5. Auto-EXCLUDE 15 Records

### 5.1 Location

The 15 Auto-EXCLUDE records (Gemini + Claude both exclude) are **not included in the human review Excel file**. They exist only in the AI screening pipeline output (`data/03_screening/screening_ai_dual.csv`).

### 5.2 Risk Assessment

Given the 58.3% false positive rate for Auto-INCLUDE, the false negative rate for Auto-EXCLUDE should also be examined. However:

- 15 records is a very small number (1% of the 1,457 human-review pool)
- Both AI models independently agreed to exclude — higher confidence than single-AI decisions
- The base rate of include among exclude-consensus records is expected to be very low

### 5.3 Verification Result (Completed 2026-03-09)

R1 verified all 15 Auto-EXCLUDE records. **All 15 confirmed as Exclude.** AI dual-consensus exclusion false negative rate = **0/15 (0%)**.

This confirms that when both AI models agree to exclude, the decision is highly reliable.

---

## 6. Data Extraction Coding Protocol

### 6.1 Screening vs Data Extraction Standards

| Phase | Minimum Requirement | This Project |
|-------|-------------------|-------------|
| **Screening (I/X/U)** | 1 reviewer + verification | R2+R3 IRR on 200 + R1 full verification of Auto-INCLUDE |
| **Data extraction (correlations)** | 2 independent coders + ICR | See below |

### 6.2 Data Extraction Plan (Updated 2026-03-09)

For the correlation matrix / beta coefficient extraction phase, **independent human coding** is used:

1. **AI Metadata Pre-Coding:** AI pre-codes non-critical fields (author, year, DOI, sample_size, country, ai_type, education_level). Humans verify during their coding.
2. **30% ICR sample dual coding:** R2 and R3 independently code ~68-75 studies, **blinded** to AI extraction results for correlations and construct mappings
3. **ICR target:** ICC(2,1) ≥ 0.90 for numeric values; Cohen's κ ≥ 0.85 for construct mappings; MAE ≤ .03
4. **If ICR met:** Remaining 70% coded by one coder + second coder verifies 10-20%
5. **If ICR not met:** Additional calibration session, then re-code sample
6. **AI extraction** (Claude CLI + Gemini CLI + Codex CLI, 3-model consensus) runs in **parallel** with human coding. AI results are compared to human gold standard **after** human coding is complete, providing AI-Human agreement metrics.
7. **Canonical documents:** Coding Manual v2 and Codebook v2 in `data/04_extraction/`

---

## 7. Updated PRISMA Flow Numbers (Projected)

```
Identification: 16,189 records
  - T1 keyword auto-exclude: 12,915
  - T2 single-AI screened: 613
  - T3 dual-AI screened: 2,557
  - Pilot: 104

T3 Dual-AI Results (1,457 to human review):
  - Auto-INCLUDE: 358 -> R1 full verification -> 135 Include (2022+ filter)
  - Auto-EXCLUDE: 15 -> R1 verified -> 0 Include (all confirmed exclude)
  - TIER1 conflict: 95 -> IRR + R1 adjudication -> ~30 Include
  - TIER2 confirm: 495 -> R1/R2/R3 coding -> ~120 Include
  - TIER3 low: 494 -> R1 coding -> ~25 Include

Completed screening (657 records from Tabs 1-3):
  - Include: 225 (year filter: 2022-2026)
  - Exclude: 432
  - Pending: 0

Remaining screening: TIER1 (10), TIER2 (266), TIER3 (494)
Estimated total for full-text review: ~325 studies
Estimated final MASEM-eligible: ~250-300 studies
```

---

## 8. Timeline

| Week | Task | Owner |
|------|------|-------|
| Week 1 | R1 full verification of Tab 2 (358 records) | PI |
| Week 1 | R1 verify Auto-EXCLUDE 15 records | PI |
| Week 1 | Finalize Tab 1 remaining 154 records (auto-confirm R2=R3 agreements) | System |
| Week 2 | TIER2 remaining 266 records screening | R1/R2/R3 |
| Week 3 | TIER3 494 records screening | R1 |
| Week 4+ | Full-text data extraction begins | R2+R3 (dual) + AI pipeline |

---

## References

- PRISMA-trAIce: Transparent Reporting of AI in Systematic Literature Reviews (2025). JMIR AI.
- Cochrane Handbook for Systematic Reviews of Interventions, Section 4.6: Screening and selecting studies.
- Borenstein, M., Hedges, L. V., Higgins, J. P., & Rothstein, H. R. (2009). Introduction to Meta-Analysis. Wiley.
