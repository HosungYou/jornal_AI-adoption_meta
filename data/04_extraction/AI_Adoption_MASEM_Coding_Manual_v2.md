# AI Adoption in Education — MASEM Coding Manual

**Version 2.0**
**Author:** Hosung You
**Date:** 2026-03-09
**Study:** AI Adoption in Education — Meta-Analytic Structural Equation Modeling (MASEM)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-16 | Initial release |
| 2.0 | 2026-03-09 | Major revision: year range 2022–2026; education-only scope; independent coding workflow; AI metadata pre-coding; 3 CLI models (Claude, Gemini, Codex); Addendum integrated and replaced; unnecessary fields removed; study_id S001 format; full-text exclusion codes E-FT1–E-FT6 added |
| 2.1 | 2026-03-10 | Paper A+B integrated design; 2-pair ICR (R1+R2, R3+R4); Phase 1 100건 dual + Phase 2 150건 single; calibration 10건; cross-pair adjudication; Paper B gold standard = Paper A ICR sample |

---

## Table of Contents

1. [Introduction and Purpose](#1-introduction-and-purpose)
2. [Eligibility Criteria](#2-eligibility-criteria)
3. [Coding Workflow Overview](#3-coding-workflow-overview)
4. [Coder Training Protocol](#4-coder-training-protocol)
5. [Study-Level Coding Instructions](#5-study-level-coding-instructions)
6. [Correlation Matrix Coding Instructions](#6-correlation-matrix-coding-instructions)
7. [Construct Harmonization Instructions](#7-construct-harmonization-instructions)
8. [Moderator Variable Coding](#8-moderator-variable-coding)
9. [Reliability Data Extraction](#9-reliability-data-extraction)
10. [AI-Assisted Coding Protocol](#10-ai-assisted-coding-protocol)
11. [Inter-Coder Reliability Protocol](#11-inter-coder-reliability-protocol)
12. [Discrepancy Resolution Protocol](#12-discrepancy-resolution-protocol)
13. [Study Exclusion Protocol](#13-study-exclusion-protocol)
14. [Quality Assurance Checklist](#14-quality-assurance-checklist)
15. [References](#15-references)
16. [Appendix A: Decision Trees](#appendix-a-decision-trees)
17. [Appendix B: FAQ](#appendix-b-faq)
18. [Appendix C: Excel Template Sheet Descriptions](#appendix-c-excel-template-sheet-descriptions)

---

## 1. Introduction and Purpose

### 1.1 MASEM Study Overview

This meta-analytic structural equation modeling (MASEM) study synthesizes empirical research on AI technology adoption in **educational contexts** (K-12, higher education, and vocational) to:

1. Test the validity of traditional technology acceptance models (TAM/UTAUT) in the educational AI context
2. Evaluate whether AI-specific constructs (Trust, Anxiety, Transparency, Autonomy) provide incremental explanatory power
3. Identify moderators of AI adoption relationships (AI type, education level, culture, temporal period)
4. Compare competing theoretical models using two-stage SEM (TSSEM)

The study extracts correlation matrices from primary studies to build pooled correlation matrices, then fits structural models. This requires precise extraction of Pearson *r* values (or standardized β for conversion) and careful harmonization of construct labels across studies.

### 1.2 How to Use This Manual

1. Read the entire manual before beginning coding
2. Complete the training protocol (Chapter 4) before independent coding
3. Keep the Excel codebook (`AI_Adoption_MASEM_Coding_v2.xlsx`) open alongside this manual
4. When uncertain, consult the decision trees (Appendix A)
5. Document all ambiguous decisions in the DISCREPANCY_LOG sheet

### 1.3 Canonical Source of Truth

- This document is the **canonical coding protocol** for the project
- The Excel codebook (`AI_Adoption_MASEM_Coding_v2.xlsx`) is the data-entry implementation
- Operational mirrors (markdown/docs) must remain synchronized with this document
- AI screening decisions are **advisory only** — they do not finalize exclusions
- All raw AI outputs, human coding records, and adjudication logs must be preserved

---

## 2. Eligibility Criteria

### 2.1 PICOS Framework

| Element | Criterion | Notes |
|---------|-----------|-------|
| **Population** | Students, teachers, instructors, faculty, or administrators in educational settings | K-12, higher education, vocational training |
| **Intervention/Exposure** | AI technology adoption/acceptance | Generative AI, predictive AI, ITS, chatbots, AI-powered LMS, etc. |
| **Comparison** | Not required (correlational studies) | Most studies are single-group surveys |
| **Outcomes** | Correlation matrix or standardized path coefficients (β) | Must include ≥ 2 of 12 target constructs |
| **Study Design** | Quantitative empirical studies | Cross-sectional surveys, longitudinal, experimental |

### 2.2 Inclusion Criteria

1. Empirical quantitative study with primary data
2. AI technology adoption/acceptance as focal phenomenon
3. **Educational setting/population** (K-12, higher education, or vocational)
4. Correlation matrix OR standardized path coefficients (β) reported
5. At least 2 of 12 target constructs measured
6. **Published 2022–2026**
7. English language
8. Sample size n ≥ 50
9. Peer-reviewed journal article or full conference paper

### 2.3 Exclusion Criteria

| Code | Definition |
|------|-----------|
| E1 | Not empirical/quantitative (qualitative, conceptual, review) |
| E2 | AI not focal (general IT, e-commerce without AI) |
| E3 | **Not educational context** (healthcare, manufacturing, finance, etc.) |
| E4 | No adoption/acceptance outcome measured |
| E5 | No effect size data (no correlation or β) |
| E6 | Not English |
| E7 | Outside 2022–2026 |
| E8 | n < 50 |
| E9 | Not peer-reviewed |
| E10 | Duplicate sample |
| E11 | Qualitative/review only |
| E12 | Other |

### 2.4 Full-Text Exclusion Criteria (Phase 4)

| Code | Definition |
|------|-----------|
| E-FT1 | Reports < 2 construct-pair statistics (r or β) |
| E-FT2 | Constructs do not map to the 12-construct model |
| E-FT3 | Not educational context (upon full-text review) |
| E-FT4 | Duplicate sample (same data in multiple publications) |
| E-FT5 | Conference abstract only (no full paper available) |
| E-FT6 | Full-text inaccessible |

### 2.5 Borderline Decision Rules

- **Chatbots/virtual assistants:** INCLUDE if AI-powered and adoption is measured in educational setting
- **Recommendation systems:** INCLUDE if AI/ML-based and study frames as AI adoption in education
- **Mixed-methods studies:** INCLUDE if quantitative portion meets all criteria
- **Partial correlation reporting:** INCLUDE (use available-case principle)
- **Conference papers later published as journal articles:** Use journal version only
- **K-12 vs. Higher Ed ambiguity:** Code the education_level moderator; include both

---

## 3. Coding Workflow Overview

### 3.1 Workflow Diagram

```
Phase 0: Calibration (10 studies)
   │  All 4 coders (R1-R4) code same 10 studies
   │  ► Calculate inter-pair consistency
   │  ► Resolve disagreements, refine rules
   ↓
Phase 1: Dual Coding — 100 studies
   │  = Paper B Gold Standard + Paper A ICR sample
   │  Pair A (R1 + R2): 50 studies independently (blinded)
   │  Pair B (R3 + R4): 50 studies independently (blinded)
   │  ► Cross-pair adjudication for discrepancies
   │  ► ICR targets: κ ≥ .85, ICC ≥ .90, MAE ≤ .03
   ↓
Phase 2: Single Coding — ~150 studies
   │  = Paper A remaining studies
   │  R1: ~38 studies + ~6 spot-checks
   │  R2: ~38 studies + ~6 spot-checks
   │  R3: ~37 studies + ~6 spot-checks
   │  R4: ~37 studies + ~6 spot-checks
   │  ► 15-20% cross-checked by another coder (rotating)
   ↓
Phase 3 (parallel): AI Extraction
   │  ► 3-model consensus: Claude CLI + Gemini CLI + Codex CLI
   │  ► Results NOT shown to human coders until Phase 4
   ↓
Phase 4: ICR & AI-Human Comparison
   │  ► Pair A ICR (R1 vs R2) on 50 studies
   │  ► Pair B ICR (R3 vs R4) on 50 studies
   │  ► Inter-pair consistency (Pair A gold vs Pair B gold)
   │  ► AI-Human agreement (3-model consensus vs human gold)
   ↓
Phase 5: Discrepancy Resolution
   │  ► Cross-pair adjudication for Phase 1 discrepancies
   │  ► Return to original study for all discrepancies
   ↓
Phase 6: QA Final (6 Gates)
   │  ► Range, symmetry, diagonal, completeness, sample size, duplicate
   ↓
Final Validated Dataset
```

### 3.2 Key Workflow Rules

1. **Calibration (Phase 0):** All 4 coders code the same 10 studies to establish inter-pair consistency before Phase 1 begins.
2. **Dual coding (Phase 1):** Two independent pairs (R1+R2, R3+R4) each code 50 studies. This 100-study set serves dual purpose: Paper B gold standard AND Paper A ICR validation.
3. **Cross-pair adjudication:** Discrepancies within Pair A (R1-R2) are adjudicated by R3 or R4. Discrepancies within Pair B (R3-R4) are adjudicated by R1 or R2.
4. **Single coding (Phase 2):** Remaining ~150 studies divided equally among R1-R4 (~38 each), with 15-20% spot-checked by a different coder.
5. **AI extraction (Phase 3):** Runs in parallel with human coding. Results are NOT shown to human coders until Phase 4.
6. **Human-coded data is the gold standard.** AI output is used for comparison, validation, and Paper B analysis.

### 3.3 Estimated Timeline

| Phase | Duration | Personnel | Output |
|-------|----------|-----------|--------|
| Phase 0: Calibration | 3 days | R1, R2, R3, R4 (all) | Inter-pair consistency report |
| Phase 1: Dual coding (100 studies) | 3 weeks | Pair A (R1+R2), Pair B (R3+R4) | Paper B gold standard + Paper A ICR |
| Phase 2: Single coding (~150 studies) | 2 weeks | R1, R2, R3, R4 (equal split) | Paper A remaining data |
| Phase 3: AI extraction (parallel) | 1 week | AI pipeline | AI consensus dataset |
| Phase 4: ICR calculation | 3 days | PI | ICR metrics report |
| Phase 5: Discrepancy resolution | 1 week | All coders + PI | Resolved dataset |
| Phase 6: QA finalization | 3 days | PI | Final validated dataset |

---

## 4. Coder Training Protocol

| Phase | Duration | Activities | Success Criterion |
|-------|----------|------------|-------------------|
| Orientation | 2 hours | Read full manual; review Excel codebook; understand MASEM basics | Can explain MASEM data requirements |
| Practice — Metadata | 1 day | Code 3 practice studies independently | >90% agreement with gold standard |
| Practice — Correlations | 2 days | Extract correlations from 3 diverse studies (full matrix, partial, β-only) | >95% agreement on r values (within .02) |
| Practice — Harmonization | 1 day | Harmonize constructs from 3 studies using mapping tables | >85% agreement on construct mapping |
| Calibration session | 2 hours | Compare practice coding; discuss disagreements; refine rules | All disagreements resolved |
| Certification | — | Code 2 new studies independently; compare with gold standard | All criteria met |
| Calibration (Phase 0) | 3 days | All 4 coders code same 10 studies; calculate inter-pair κ; discuss all disagreements | Inter-pair κ ≥ .80; all disagreements resolved |

---

## 5. Study-Level Coding Instructions

All study-level variables are coded in the **STUDY_METADATA** sheet. AI pre-codes identification and demographic fields; human coders verify and complete remaining fields.

### 5.1 Identification Variables (AI Pre-Coded, Human Verified)

| Variable | Type | Definition | Example |
|----------|------|------------|---------|
| study_id | string | Unique ID in S001 format | S001 |
| first_author | string | Last name of first author | Kim |
| year | integer | Publication year (2022–2026) | 2024 |
| title | string | Full title of the paper | AI Adoption in Higher Education... |
| doi | string | Digital Object Identifier | 10.1000/xyz123 |
| source_type | categorical | journal, conference | journal |

### 5.2 Study Design Variables (AI Pre-Coded, Human Verified)

| Variable | Type | Definition | Example |
|----------|------|------------|---------|
| study_design | categorical | cross_sectional, longitudinal, experimental | cross_sectional |
| data_collection | categorical | survey, experiment, mixed | survey |
| theoretical_framework | categorical | TAM, UTAUT, UTAUT2, TAM_AI, UTAUT_AI, TPB, SCT, other | UTAUT2 |

### 5.3 Sample & Context Variables (AI Pre-Coded, Human Verified)

| Variable | Type | Definition | Example |
|----------|------|------------|---------|
| sample_size | integer | Total valid sample size (N). Use final analytic sample. | 384 |
| sample_type | categorical | students, instructors, mixed, administrators | students |
| country | string | Country where data was collected | South Korea |
| culture_cluster | categorical | individualist (IDV≥50) or collectivist (IDV<50) per Hofstede | collectivist |
| education_level | categorical | K-12, undergraduate, graduate, vocational, mixed | undergraduate |

### 5.4 AI Technology Variables (AI Pre-Coded, Human Verified)

| Variable | Type | Definition | Example |
|----------|------|------------|---------|
| ai_type | categorical | generative, predictive, decision_support, conversational, robotic, general | generative |
| ai_tool_name | string | Specific AI tool if named | ChatGPT |

### 5.5 Quality Assessment Variables (Human Coded)

| Variable | Type | Definition | Example |
|----------|------|------------|---------|
| n_constructs_measured | integer | Number of our 12 constructs measured | 6 |
| n_correlations_reported | integer | Number of pairwise correlations involving our constructs | 15 |
| matrix_completeness | float | Reported pairs / possible pairs (0–1) | 0.75 |
| common_method_bias | categorical | addressed, not_addressed, partial | addressed |

### 5.6 Source Management Variables

| Variable | Type | Definition | Example |
|----------|------|------------|---------|
| human_coder | string | Initials of the human coder | HY |
| coding_date | date | Date coding completed (YYYY-MM-DD) | 2026-04-01 |
| ai_precoded | boolean | Whether AI pre-coded metadata | TRUE |
| ai_precoded_verified | boolean | Whether human verified AI metadata | TRUE |

---

## 6. Correlation Matrix Coding Instructions

> **This is the most critical chapter.** MASEM requires pairwise Pearson correlations between constructs. All correlation data is coded in the CORRELATION_MATRIX sheet.

### 6.1 Variable Reference

| Variable | Type | Definition | Example |
|----------|------|------------|---------|
| study_id | string | Links to STUDY_METADATA | S001 |
| construct_row | categorical | Row construct (one of 12) | PE |
| construct_col | categorical | Column construct (one of 12) | BI |
| r_value | float | Pearson correlation (-1 to 1) | 0.52 |
| r_source | categorical | direct, beta_converted, author_provided | direct |
| original_beta | float | Original β if r_source=beta_converted, else NA | NA |
| r_sample_size | integer | Pairwise N if differs from study N, else NA | NA |
| p_value | float | Reported p-value if available | 0.001 |
| significance | categorical | p<.001, p<.01, p<.05, ns, NR | p<.001 |
| source_location | string | Location in paper | Table 3 |
| extraction_notes | string | Notes about extraction decisions | Lower triangle only |

### 6.2 Correlation Extraction Protocol

**Step 1:** Identify the correlation matrix table. Look for tables titled "Correlations," "Descriptive Statistics and Correlations," or "Inter-Construct Correlations." The diagonal should be 1.00 or reliability coefficients.

**Step 2:** Map study constructs to our 12 target constructs using the harmonization rules in Chapter 7. Record the mapping in the CONSTRUCT_MAPPING sheet.

**Step 3:** Extract all pairwise correlations involving our constructs. Record Pearson r values to 2 decimal places. Ignore significance asterisks (record effect size, not p-value). If only lower triangle shown, mirror values.

**Step 4:** Record sample size per correlation. Use overall study N as default. If pairwise N differs, record pairwise N.

**Step 5:** Document source location and any extraction decisions.

### 6.3 Beta-to-r Conversion (Peterson & Brown, 2005)

When a study reports only standardized path coefficients (β) without a correlation matrix:

> **r = β + 0.05 × λ**, where λ = 1 if β ≥ 0, λ = −1 if β < 0

Examples:
- β = 0.40 → r = 0.40 + 0.05(1) = **0.45**
- β = −0.30 → r = −0.30 + 0.05(−1) = **−0.35**

Always set `r_source = "beta_converted"` and record `original_beta`. Mark study for sensitivity analysis.

### 6.4 Incomplete Matrix Handling

Apply the **available-case principle**:
- Extract all reported correlations; leave unreported cells as NA
- Do NOT assume unreported or non-significant correlations are zero
- Record `matrix_completeness = reported_pairs / possible_pairs`
- Stage 1 TSSEM handles missing cells via FIML

### 6.5 Where to Find Correlation Data

| Priority | Location | Notes |
|----------|----------|-------|
| 1 | Main text tables (Results section) | Most common |
| 2 | Appendices | Often "Appendix: Correlation Matrix" |
| 3 | Supplementary materials / OSF | Online supplements |
| 4 | SEM output tables | May contain implied correlations |
| 5 | Author contact | If "available upon request" |

---

## 7. Construct Harmonization Instructions

Harmonization maps diverse construct labels onto our 12 standard constructs. **Prioritize conceptual alignment over label matching.** All mappings go in the CONSTRUCT_MAPPING sheet.

### 7.1 The 12 Target Constructs

| Abbr | Construct | Definition | Origin | Education-Specific Variants |
|------|-----------|------------|--------|----------------------------|
| PE | Performance Expectancy | Belief that AI helps attain performance gains | UTAUT / TAM (PU) | Learning Effectiveness, Academic Performance Expectancy |
| EE | Effort Expectancy | Perceived ease of using AI | UTAUT / TAM (PEOU) | AI Learning Ease, Educational AI Usability |
| SI | Social Influence | Important others believe one should use AI | UTAUT / TRA (SN) | Peer Influence, Instructor Encouragement |
| FC | Facilitating Conditions | Organizational/technical infrastructure for AI use | UTAUT / TPB (PBC) | Institutional AI Support, University AI Infrastructure |
| BI | Behavioral Intention | Strength of intention to adopt/use AI | TAM / UTAUT | Intent to Use AI for Academic Work |
| UB | Use Behavior | Actual use of AI technology | TAM / UTAUT | AI Usage for Learning/Teaching |
| ATT | Attitude | Overall evaluative judgment about using AI | TRA / TAM | Attitude Toward AI in Education |
| SE | Self-Efficacy | Belief in own capability to use AI | SCT (Bandura) | Academic AI Self-Efficacy |
| TRU | AI Trust | Willingness to be vulnerable based on positive AI expectations | Trust theory (Mayer) | Trust in Educational AI |
| ANX | AI Anxiety | Apprehension or fear about AI | Computer anxiety lit. | AI Academic Integrity Anxiety |
| TRA | AI Transparency | Perceived ability to understand AI decisions | XAI literature | AI Grading Transparency |
| AUT | Perceived AI Autonomy | Perceived degree of AI independent operation | Automation literature | AI Autonomy in Education |

### 7.2 TAM/UTAUT Cross-Reference Table

| Study Construct Label | Model Origin | Maps to | Confidence |
|-----------------------|-------------|---------|------------|
| Perceived Usefulness (PU) | TAM | PE | Exact |
| Perceived Ease of Use (PEOU) | TAM | EE | Exact |
| Attitude Toward Using | TAM | ATT | Exact |
| Behavioral Intention to Use | TAM/UTAUT | BI | Exact |
| Actual System Use | TAM/UTAUT | UB | Exact |
| Performance Expectancy | UTAUT | PE | Exact |
| Effort Expectancy | UTAUT | EE | Exact |
| Social Influence | UTAUT | SI | Exact |
| Facilitating Conditions | UTAUT | FC | Exact |
| Subjective Norm | TRA/TPB | SI | High |
| Perceived Behavioral Control | TPB | FC or SE | High (check items) |
| Relative Advantage | DOI | PE | High |
| Complexity | DOI | EE (reverse) | High |
| Compatibility | DOI | FC | High |
| Computer Self-Efficacy | SCT | SE | High |
| Anxiety (computer/technology) | Various | ANX | High |
| Hedonic Motivation | UTAUT2 | ATT | Moderate |

### 7.3 AI-Specific Construct Mappings

| Study Construct Label | Maps to | Confidence | Notes |
|-----------------------|---------|------------|-------|
| Trust in AI / AI Trust | TRU | Exact | Direct match |
| Algorithmic Trust | TRU | Exact | Trust in algorithm |
| Automation Trust | TRU | High | Trust in automated system |
| Perceived Reliability | TRU | Moderate | Competence dimension of trust |
| AI Anxiety | ANX | Exact | Direct match |
| Technology Anxiety | ANX | High | If AI context |
| Technostress | ANX | Moderate | Only anxiety component |
| Explainability / Interpretability | TRA | Exact | XAI construct |
| Algorithmic Transparency | TRA | Exact | Direct match |
| Black Box Perception | TRA (reverse) | High | Reverse-coded transparency |
| AI Autonomy / Machine Autonomy | AUT | Exact | Direct match |
| Perceived AI Agency | AUT | High | Agency implies autonomy |
| Automation Level | AUT | High | Degree of autonomy |

### 7.4 Harmonization Decision Tree

1. **Exact label match** to our 12? → Code directly (confidence = exact)
2. **TAM/UTAUT family** label? → Use cross-reference table §7.2 (confidence = high)
3. **AI-specific** label? → Use AI mapping table §7.3 (confidence = high/exact)
4. **Definition aligns?** → Compare study definition to our 12 (confidence = moderate)
5. **Items align?** → Review scale items (confidence = moderate)
6. **Expert review** → Flag for PI discussion (confidence = low)
7. **No match** → Exclude construct from coding

### 7.5 Ambiguous Cases Requiring Item Review

| Study Construct | Possible Mappings | Decision Rule |
|-----------------|-------------------|---------------|
| AI Value | PE or ATT | "valuable for tasks" → PE; "valuable overall" → ATT |
| AI Confidence | SE or TRU | "confident in my ability" → SE; "confident in AI" → TRU |
| AI Understanding | TRA or EE | "understand how AI works" → TRA; "understand how to use" → EE |
| AI Support | FC or SI | "organizational support" → FC; "peer encouragement" → SI |
| Perceived Control | SE or FC or AUT(rev) | "I can control" → SE/FC; "AI controls" → AUT |
| AI Quality | PE or TRU | "output quality" → PE; "trustworthy" → TRU |
| AI Capability | PE or AUT | "helps me" → PE; "operates independently" → AUT |

---

## 8. Moderator Variable Coding

### 8.1 Variable Reference

| Variable | Type | Definition | Levels | Example |
|----------|------|------------|--------|---------|
| study_id | string | Links to STUDY_METADATA | — | S001 |
| ai_type | categorical | AI technology type | generative, predictive, decision_support, conversational, robotic, general | generative |
| education_level | categorical | Education context | K-12, undergraduate, graduate, vocational, mixed | undergraduate |
| temporal_period | categorical | Publication era | pre_chatgpt (2022), post_chatgpt (2023–2026) | post_chatgpt |
| culture_cluster | categorical | Hofstede-based | individualist (IDV≥50), collectivist (IDV<50) | collectivist |
| sample_type | categorical | Respondent type | students, instructors, mixed, administrators | students |
| user_role | categorical | User role studied | student, instructor, both | student |

### 8.2 Moderator Coding Rules

- **AI Type:** Code based on the specific AI technology described. If multiple AI types, code as "general."
- **Education Level:** Code based on the sample's educational context. If cross-level, code as "mixed."
- **Temporal Period:** Based on publication year. 2022 = pre_chatgpt; 2023–2026 = post_chatgpt.
- **Culture:** Use Hofstede individualism score. IDV ≥ 50 = individualist; IDV < 50 = collectivist.
- **User Role:** Code primary respondent role.

---

## 9. Reliability Data Extraction

### 9.1 Variable Reference

| Variable | Type | Definition | Example |
|----------|------|------------|---------|
| study_id | string | Links to STUDY_METADATA | S001 |
| construct | categorical | One of 12 target constructs | PE |
| study_label | string | Original construct label in the study | Perceived Usefulness |
| cronbach_alpha | float | Cronbach's alpha (0–1) | 0.89 |
| composite_reliability | float | Composite reliability / CR (0–1) | 0.92 |
| ave | float | Average Variance Extracted (0–1) | 0.65 |
| n_items | integer | Number of scale items | 5 |
| scale_source | string | Original scale reference | Venkatesh et al. (2003) |
| harmonization_confidence | categorical | exact, high, moderate, low | exact |

### 9.2 Reliability Extraction Protocol

1. Check diagonal of correlation matrix for reliability values (often α or CR)
2. Check measurement model tables (CFA results) for CR and AVE
3. Check "Measures" or "Instruments" section for α values
4. If multiple estimates reported, prefer: CR > α > test-retest
5. Record **all** available reliability indicators

---

## 10. AI-Assisted Coding Protocol

### 10.1 Dual-Track Design

The AI-assisted coding protocol operates on **two separate tracks**:

**Track 1 — AI Metadata Pre-Coding** (before human coding):
- AI extracts non-critical metadata from PDFs
- Fields: author, year, title, DOI, sample_size, country, study_design, ai_type, education_level, theoretical_framework
- Humans verify and correct during their independent coding
- This saves time on clerical tasks without introducing bias

**Track 2 — AI Independent Extraction** (parallel with human coding):
- AI extracts core MASEM data (correlations, construct mappings)
- Results are **NOT shown to human coders** until human coding is complete
- Used for AI-Human comparison metrics and validation
- 3-model consensus determines AI extraction quality

### 10.2 Models

| Model | CLI Tool | Version (March 2026) | Role |
|-------|----------|---------------------|------|
| Claude | Claude CLI | claude-sonnet-4-6 | Primary AI coder |
| Gemini | Gemini CLI | gemini-2.5-flash | Secondary AI coder |
| Codex | Codex CLI | Latest available | Tertiary AI coder |

All models operate via CLI under authenticated sessions. Each processes the same study independently.

### 10.3 Execution Rules

1. Each AI model processes the same study **independently** (no communication between models)
2. **Human gold-standard coding is completed independently** — humans do NOT see AI extraction results for correlations and construct mappings
3. Humans MAY see AI-precoded metadata (Track 1) as this covers non-critical clerical fields
4. All AI raw outputs are preserved in the AI_EXTRACTION_PROVENANCE sheet
5. AI outputs are compared to human coding **after** human coding is complete (Phase D)

### 10.4 Consensus Methods

- **Full agreement** (2+ models agree exactly): Use that value. Confidence = High.
- **Close agreement** (all within .05): Use median. Confidence = Moderate. Flag for review.
- **Disagreement** (range > .05): Consensus = NULL. Must review.
- **Construct mapping:** Majority vote (2/3 agree). If no majority, flag for human review.

### 10.5 AI-Human Comparison Metrics

| Metric | Applied To | Minimum | Target |
|--------|-----------|---------|--------|
| Exact match rate | Categorical variables | 80% | 90% |
| ICC(2,1) | Continuous variables (r values) | .80 | .90 |
| Cohen's κ | Categorical variables | .70 | .80 |
| Mean absolute error | r values | <.05 | <.02 |

These metrics quantify AI extraction quality relative to human gold standard and are reported in the manuscript.

---

## 11. Inter-Coder Reliability Protocol

### 11.1 When to Calculate

Calculate ICR on the **Phase 1 dual-coded set (100 studies)**. Two independent coder pairs (Pair A: R1+R2; Pair B: R3+R4) each code 50 studies.

**ICR is calculated at three levels:**
1. **Within-pair:** R1 vs R2 (50 studies), R3 vs R4 (50 studies)
2. **Inter-pair consistency:** Compare Pair A gold standard values to Pair B gold standard values on the calibration set (10 studies coded by all 4)
3. **AI-Human:** 3-model AI consensus vs human gold standard (100 studies)

**Stratification of Phase 1 sample (100 studies):**
- Publication year (2022, 2023–2024, 2025–2026)
- AI type (generative vs. non-generative)
- Education level (K-12, undergraduate, graduate+)

### 11.2 Metrics and Thresholds

| Metric | Applied To | Minimum | Target | If Below Minimum |
|--------|-----------|---------|--------|-----------------|
| Cohen's κ | Categorical variables | .70 | .85 | Retrain; re-code |
| ICC(2,1) | Continuous variables (r) | .90 | .95 | Review procedure; re-code |
| Exact agreement % | All coded variables | 85% | 95% | Identify systematic errors |
| r value MAE | Correlation values | <.05 | <.02 | Re-extract from source tables |

### 11.3 Reporting Format

| Variable Category | Metric | Value | 95% CI | n items |
|-------------------|--------|-------|--------|---------|
| Construct harmonization | Cohen's κ | [calculated] | [CI] | [n] |
| Correlation r values | ICC(2,1) | [calculated] | [CI] | [n] |
| Moderator coding | Cohen's κ | [calculated] | [CI] | [n] |
| Quality assessment | Cohen's κ | [calculated] | [CI] | [n] |
| Beta conversion | ICC(2,1) | [calculated] | [CI] | [n] |

---

## 12. Discrepancy Resolution Protocol

### 12.1 Discrepancy Classification

| Classification | Definition | Examples | Resolution |
|---------------|------------|----------|------------|
| Clerical | Typo, data entry error | r = .45 vs .54 (transposition) | Verify against source; correct |
| Interpretive | Different but defensible readings | Mapping "AI Value" to PE vs ATT | Discuss; check items; decide with PI |
| Substantive | Fundamental disagreement | Including vs excluding a study | Full review; PI makes final decision |

### 12.2 Resolution Workflow

1. **Identify** all discrepancies by comparing coder sheets
2. **Classify** each discrepancy (clerical, interpretive, substantive)
3. **Resolve** clerical errors by re-checking source
4. **Discuss** interpretive differences; reach consensus or escalate
5. **Escalate** substantive disagreements to PI
6. **Document** all resolutions in DISCREPANCY_LOG

### 12.3 Resolution Hierarchy

1. **Original study text** (highest authority)
2. **Human consensus** (both human coders agree)
3. **AI consensus** (2+ models agree AND human review confirms)
4. **PI adjudication** (if still unclear)

---

## 13. Study Exclusion Protocol

### 13.1 Variable Reference

| Variable | Type | Definition | Example |
|----------|------|------------|---------|
| study_id | string | Original study ID | S045 |
| first_author | string | First author last name | Kim |
| year | integer | Publication year | 2023 |
| title | string | Paper title | AI Acceptance... |
| exclusion_stage | categorical | title_abstract, full_text, data_extraction | full_text |
| exclusion_code | categorical | E1–E12 or E-FT1–E-FT6 | E-FT1 |
| detailed_rationale | string | Free-text explanation | Only reports regression β without correlation table |
| final_decision | categorical | exclude | exclude |

### 13.2 When to Log

- Log every study excluded at full-text screening or later
- Title/abstract exclusions are tracked in PRISMA counts (not individually logged here)
- If initially included then excluded during data extraction, log with stage = "data_extraction"

---

## 14. Quality Assurance Checklist

- [ ] All study-level variables completed for every included study
- [ ] All correlation matrix cells extracted (or marked NA with reason)
- [ ] Construct harmonization mapping documented for every study
- [ ] Beta-to-r conversions checked with formula (r = β + 0.05 × λ)
- [ ] Matrix symmetry verified (r(PE,BI) = r(BI,PE))
- [ ] Sample sizes recorded and plausible
- [ ] Reliability data extracted where available
- [ ] Moderator variables coded consistently
- [ ] AI provenance data preserved for AI-coded studies
- [ ] Discrepancy log completed for all disagreements
- [ ] Inter-coder reliability calculated and meets thresholds
- [ ] Exclusion log completed with reasons
- [ ] No duplicate studies in dataset
- [ ] Construct labels in CORRELATION_MATRIX match CONSTRUCT_MAPPING

---

## 15. References

- Ajzen, I. (1991). The theory of planned behavior. *OBHDP*, 50(2), 179–211.
- Bandura, A. (1986). *Social foundations of thought and action*. Prentice-Hall.
- Cheung, M. W.-L. (2015). *Meta-analysis: A structural equation modeling approach*. Wiley.
- Cheung, M. W.-L., & Chan, W. (2005). Meta-analytic structural equation modeling: A two-stage approach. *Psychological Methods*, 10(1), 40–64.
- Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly*, 13(3), 319–340.
- Hofstede, G. (2001). *Culture's consequences* (2nd ed.). Sage.
- Jak, S., & Cheung, M. W.-L. (2020). Meta-analytic structural equation modeling with moderating effects. *Psychological Methods*, 25(4), 430–455.
- Mayer, R. C., Davis, J. H., & Schoorman, F. D. (1995). An integrative model of organizational trust. *AMR*, 20(3), 709–734.
- Peterson, R. A., & Brown, S. P. (2005). On the use of beta coefficients in meta-analysis. *JAP*, 90(1), 175–181.
- Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology. *MIS Quarterly*, 27(3), 425–478.
- Venkatesh, V., Thong, J. Y. L., & Xu, X. (2012). Consumer acceptance and use of information technology. *MIS Quarterly*, 36(1), 157–178.

---

## Appendix A: Decision Trees

### A.1 Inclusion/Exclusion Decision

1. Is it an empirical quantitative study? → NO → Exclude (E1)
2. Does it study AI technology? → NO → Exclude (E2)
3. Is it in an **educational setting**? → NO → Exclude (E3)
4. Does it measure adoption/acceptance? → NO → Exclude (E4)
5. Does it report correlations or betas? → NO → Exclude (E5)
6. Does it measure ≥ 2 of our 12 constructs? → NO → Exclude (E-FT1)
7. Is N ≥ 50? → NO → Exclude (E8)
8. Is it in English? → NO → Exclude (E6)
9. Is it peer-reviewed (2022–2026)? → NO → Exclude (E7/E9)
10. Is it a duplicate sample? → YES → Exclude (E10)
11. **INCLUDE**

### A.2 AI Technology Classification

- **Generative AI:** ChatGPT, GPT-4, Claude, Gemini, DALL-E, Midjourney, Copilot
- **Predictive AI:** ML-based forecasting, diagnostic AI, risk scoring
- **Decision Support:** AI-assisted decision making, recommendation systems
- **Conversational AI:** Chatbots, virtual assistants (Siri, Alexa), AI tutors
- **Robotic AI:** Physical robots, surgical robots, educational robots
- **General:** Study discusses "AI" without specifying type

### A.3 Construct Harmonization Decision

1. Exact label match to our 12? → Code directly (exact confidence)
2. TAM/UTAUT family label? → Use cross-reference table (high confidence)
3. AI-specific label? → Use AI mapping table (high/exact confidence)
4. Definition aligns? → Map to closest construct (moderate confidence)
5. Items align? → Map based on items (moderate confidence)
6. Ambiguous? → Flag for expert review (low confidence)
7. No match? → Exclude construct from coding

### A.4 Correlation Source Selection

1. Direct Pearson r available? → Use direct r (best quality)
2. Only standardized β available? → Convert using Peterson & Brown (2005)
3. Only unstandardized b? → Cannot convert; mark as missing
4. Implied correlations from SEM? → Use if no direct r; flag quality
5. No numeric data? → Contact authors or exclude

---

## Appendix B: FAQ

**Q: What if a study reports both Pearson r and SEM-implied correlations?**
A: Use Pearson r (direct correlations). SEM-implied correlations are model-dependent.

**Q: What if a study measures a construct but does not include it in the correlation matrix?**
A: Record the construct as measured but leave correlations as NA.

**Q: How do I handle reverse-coded constructs?**
A: Flip the sign. E.g., Complexity (reverse EE) with r = −.35 to BI becomes EE-BI r = .35. Document the reversal.

**Q: What if a study reports correlation but not reliability?**
A: Code the correlations. Leave reliability fields as NA.

**Q: What if sample sizes differ across correlation pairs?**
A: Record pairwise N in r_sample_size. Use the minimum N for conservative analysis.

**Q: How do I handle multiple samples in one paper?**
A: Treat each independent sample as a separate entry (e.g., S005a, S005b).

**Q: What if a study uses a construct not in our 12?**
A: Do not code it. Only code correlations involving our 12 target constructs.

**Q: What about second-order constructs?**
A: If a study measures PE as a second-order factor, use the second-order correlation. If only first-order correlations available, average and flag quality.

**Q: Can AI pre-code metadata fields?**
A: Yes. AI pre-codes non-critical fields (identification, demographics). Humans verify during their independent coding. AI does NOT pre-code correlations or construct mappings — those must be human-coded independently.

---

## Appendix C: Excel Template Sheet Descriptions

| Sheet | Purpose |
|-------|---------|
| **CODEBOOK** | Master reference for all variables across all sheets. Contains variable_name, sheet, type, valid_values, coding_rules, example, and notes. |
| **STUDY_METADATA** | One row per included study. Identification, design, sample, AI technology, quality assessment, and source management variables. |
| **CORRELATION_MATRIX** | One row per construct pair per study. study_id, construct_row, construct_col, r_value, r_source, and extraction metadata. |
| **CONSTRUCT_MAPPING** | Documents how each study construct maps to our 12 target constructs. Includes harmonization confidence level. |
| **MODERATOR_VARIABLES** | Moderator values for each study. Used in OSMASEM and subgroup analyses. |
| **AI_EXTRACTION_PROVENANCE** | Raw AI model outputs for AI-assisted coding. Preserves full provenance chain for Claude, Gemini, and Codex. |
| **DISCREPANCY_LOG** | All inter-coder disagreements with classification, resolution method, and final values. |
| **EXCLUSION_LOG** | All studies excluded at full-text or data extraction stage with reasons and codes. |
