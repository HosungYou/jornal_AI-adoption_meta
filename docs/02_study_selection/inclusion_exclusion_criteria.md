# Inclusion and Exclusion Criteria

## Canonical Source

- This file is an operational mirror of:
  `docs/03_data_extraction/AI_Adoption_MASEM_Coding_Manual_v1.docx`
- If this file conflicts with the coding manual, the `docx` rules are authoritative.
- Screening decisions in the dataset must use canonical exclusion codes (E1-E12) and a written rationale.

## Overview

This document specifies the eligibility criteria for study inclusion in the AI adoption meta-analytic structural equation modeling (MASEM) analysis. All criteria must be applied systematically and documented for PRISMA reporting.

Operational decision authority:
- AI (Gemini/Claude) outputs are advisory only.
- Two independent human coders apply these criteria for all records.
- PI adjudicates unresolved conflicts and issues final inclusion/exclusion decisions.

---

## Inclusion Criteria

### 1. Study Design

**Included:**
- Empirical quantitative studies
- Cross-sectional surveys
- Longitudinal surveys (each wave treated independently if independent samples)
- Experimental studies reporting correlations among acceptance constructs
- Mixed-methods studies with quantitative component meeting other criteria

**Operationalization:**
- Study must collect primary data using structured instruments
- Study must report statistical relationships among variables
- Sample must be human participants (not simulations, algorithms, or theoretical models)

---

### 2. Statistical Reporting

**Required (at least ONE of the following):**

**Option A: Correlation Matrix**
- Pearson correlation matrix among study variables
- Must include ≥2 of the 12 target constructs
- Can be partial (not all 66 pairwise correlations required)
- Acceptable locations: main text table, appendix, supplementary materials, online repository

**Option B: Standardized Path Coefficients**
- Standardized beta (β) coefficients from regression or SEM
- Must include ≥2 of the 12 target constructs
- Must report sufficient information for β→r conversion (see coding manual)
- Unstandardized coefficients alone are NOT sufficient

**Minimum Requirement:**
- At least 1 pairwise relationship among target constructs must be quantifiable

**Excluded:**
- Studies reporting only frequencies, means, standard deviations without correlations
- Studies reporting only unstandardized coefficients without conversion information
- Studies reporting only chi-square, t-tests, ANOVA without correlation data
- Studies reporting only qualitative coding, thematic analysis, case studies

---

### 3. Focal Technology

**Included AI Technologies (Education-Focused):**
- **Intelligent tutoring systems (ITS)** and adaptive learning platforms
- **Generative AI for learning** (ChatGPT, Claude, GPT-4 for academic writing, learning support)
- **AI-powered LMS features** and learning analytics
- **Automated grading and assessment systems** (essay scoring, automated feedback)
- **AI writing assistants** for academic writing (Grammarly AI, Quillbot, etc.)
- **AI-based adaptive learning platforms** (personalized learning paths)
- Machine learning systems in educational contexts
- Natural language processing (NLP) systems for education
- Computer vision for education (automated attendance, gesture recognition)
- Educational chatbots and virtual teaching assistants
- AI-powered recommendation systems for learning resources
- Educational robotics with AI capabilities

**Context Requirement:**
- AI must be used in **educational settings** (schools, universities, online learning platforms, educational administration)
- Generic workplace AI adoption: EXCLUDED
- Healthcare AI adoption: EXCLUDED
- Consumer AI adoption: EXCLUDED

**Technology Specificity Required:**
- Study must clearly identify the AI system or technology being adopted
- Generic "technology adoption" without AI specification: EXCLUDED
- "Educational technology" without AI component: EXCLUDED

**Boundary Cases:**
- Expert systems (legacy AI) in education: INCLUDED if post-2015
- Rule-based automation without learning: EXCLUDED
- Basic LMS features without AI/ML: EXCLUDED
- AI-augmented educational tools: INCLUDED if AI is focal

---

### 4. Dependent Variable

**Included:**
- AI adoption intention
- AI acceptance
- AI use behavior (actual or self-reported)
- AI continuance intention
- AI resistance (reverse-coded acceptance)
- Willingness to use AI

**Focal Requirement:**
- AI adoption, acceptance, or use must be a key dependent variable or mediating variable in the model
- Studies where AI is only a moderator or control variable: EXCLUDED

---

### 5. Constructs Measured

**Minimum Requirement:**
- Study must measure at least 2 of the 12 target constructs:
  1. Performance Expectancy (PE)
  2. Effort Expectancy (EE)
  3. Social Influence (SI)
  4. Facilitating Conditions (FC)
  5. Behavioral Intention (BI)
  6. Use Behavior (UB)
  7. Attitude (ATT)
  8. Self-Efficacy (SE)
  9. AI Trust (TRU)
  10. AI Anxiety (ANX)
  11. AI Transparency (TRA)
  12. Perceived AI Autonomy (AUT)

**Construct Identification:**
- Constructs may use different labels (see construct harmonization document)
- Construct definitions must align with our operational definitions
- Mixed constructs (e.g., "trust and confidence") require theoretical alignment check

---

### 6. Publication Timeframe

**Included:**
- Published or in-press between January 1, 2015 and December 31, 2025

**Justification:**
- 2015: Modern deep learning era, widespread commercial AI systems
- Sufficient time window for meta-analytic synthesis
- Captures both early AI (predictive) and generative AI eras

**Exception:**
- Online-first articles without year: use date of first online appearance
- Preprints with publication year 2026: EXCLUDED (search closed end of 2025)

---

### 7. Language

**Included:**
- English language only

**Justification:**
- Construct harmonization requires semantic precision
- Translation quality varies; semantic drift threatens validity
- Resource constraints prevent validated translation of 100+ instruments

**Exception:**
- If English abstract and tables/figures are sufficient to extract all data: INCLUDED (rare)

---

### 8. Sample Characteristics

**Minimum Sample Size:**
- n ≥ 50 participants

**Justification:**
- Correlation stability requires adequate sample size
- k studies with n < 50 contribute excessive sampling error to meta-analysis
- Aligns with SEM rule-of-thumb (n ≥ 50 for correlation estimates)

**Population:**
- **Included:**
  - Students (K-12, undergraduate, graduate)
  - Instructors and faculty
  - Educational administrators
  - Age ≥ 13 years (ethical considerations for child samples)
  - No geographic restrictions

- **Excluded:**
  - Employees in non-educational sectors (business, healthcare, manufacturing, etc.)
  - General consumers
  - Healthcare workers (unless in educational role)
  - Non-educational organizational contexts

**Exception:**
- If same study reports multiple independent samples, each must meet n ≥ 50

---

### 9. Publication Type

**Included:**
- Peer-reviewed journal articles
- Peer-reviewed conference proceedings with full papers (≥6 pages)
- Early view/online-first peer-reviewed articles

**Excluded:**
- Dissertations and theses (to avoid overlap with published versions)
- Book chapters (unless reporting original data not published elsewhere)
- White papers, technical reports, working papers
- Conference abstracts, posters, and extended abstracts (<6 pages)
- Editorials, commentaries, letters to the editor
- Systematic reviews and meta-analyses (may use for citation chasing)

**Justification:**
- Peer review ensures minimum methodological quality
- Reduces publication bias from non-peer-reviewed sources
- Conference full papers undergo rigorous review in top-tier venues (e.g., CHI, ICIS)

---

## Exclusion Criteria

### Explicit Exclusions

1. **Qualitative-Only Studies**
   - Interviews, focus groups, case studies without quantitative component
   - Thematic analysis, grounded theory, ethnography
   - Content analysis without numerical coding

2. **No Usable Correlation Data**
   - Studies reporting only descriptive statistics (M, SD, frequencies)
   - Studies reporting only unstandardized coefficients
   - Studies reporting only significance levels (p-values) without effect sizes
   - Studies with correlation data but none involving target constructs

3. **Non-AI Technology Focus**
   - General IT adoption without AI specification
   - Social media, mobile apps, e-commerce (unless AI-powered and in education)
   - Cloud computing, blockchain, IoT (unless AI component)
   - Traditional information systems
   - Basic LMS/educational technology without AI features

4. **AI Perception Without Adoption**
   - Studies measuring only AI awareness, knowledge, or attitudes without adoption/acceptance
   - Public opinion surveys about AI without behavioral intention
   - AI literacy assessments without adoption outcomes

5. **Duplicate Samples**
   - Same data reported in multiple publications
   - Longitudinal studies using same sample across waves (keep most complete wave)
   - Conference paper later published as journal article (keep journal version)

6. **Insufficient Sample Size**
   - n < 50 participants
   - Correlation matrix reported but sample size not reported and cannot be obtained

7. **Non-English Publications**
   - Full text not available in English
   - Abstract-only English with results in other language

8. **Out of Scope**
   - Adoption by organizations (unit of analysis = organization, not individual)
   - Algorithm performance studies without human acceptance component
   - Technical feasibility studies
   - AI ethics discussions without empirical acceptance data

9. **Non-Educational Context**
   - Workplace AI adoption (corporate, business, manufacturing)
   - Healthcare AI adoption (unless for medical education/training)
   - Consumer AI adoption (general public, non-educational use)
   - Government/public sector AI adoption (unless in education departments)

---

## Decision Rules for Borderline Cases

### Case 1: Mixed Methods with Limited Quantitative Data

**Scenario:** Study is primarily qualitative but reports correlation matrix in appendix.

**Decision:** INCLUDE if correlation matrix meets minimum criteria (≥2 constructs, n ≥ 50).

**Rationale:** Data source is irrelevant if data quality is adequate.

---

### Case 2: Longitudinal Study with Same Sample

**Scenario:** Study measures same participants at T1, T2, T3.

**Decision:**
- If analyzing stability: Use T3 data only (most mature adoption)
- If analyzing change: Use T1 data only (most independent)
- **Default:** Use T3 unless T1 has more complete construct coverage

**Rationale:** Avoid dependency in correlation pooling. Same participants = same sample, not independent observations.

---

### Case 3: Conference Paper and Journal Article from Same Study

**Scenario:** Same authors, same data, published in both conference and journal.

**Decision:** INCLUDE journal version only.

**Exception:** If conference version reports constructs not in journal version, code both and merge into single study entry.

**Rationale:** Avoid duplicate sample. Journal version typically has more complete reporting.

---

### Case 4: AI as Moderator Only

**Scenario:** Study compares adoption of AI vs. non-AI technology, but adoption is measured for both.

**Decision:** INCLUDE only the AI condition data.

**Rationale:** We need within-AI-context correlations, not AI vs. non-AI comparisons.

---

### Case 5: Very High Sample Size (n > 10,000)

**Scenario:** Study with n = 50,000 participants reports correlations.

**Decision:** INCLUDE but flag for sensitivity analysis.

**Consideration:** Single study should not dominate meta-analysis. Weight-sensitivity analysis required.

**Rationale:** Exclusion would discard valuable data. Sensitivity analysis addresses influence.

---

### Case 6: Self-Developed vs. Validated Measures

**Scenario:** Study uses self-developed scales not validated in prior research.

**Decision:** INCLUDE if:
- Construct definition aligns with our operational definition
- Reliability reported (α ≥ .60 minimum)
- Items are face-valid for the construct

**Decision:** EXCLUDE if:
- Construct definition is unclear or inconsistent
- Reliability not reported
- Items mix multiple distinct constructs (e.g., "trust and ease of use")

**Rationale:** Construct harmonization can accommodate varied operationalizations if theoretically aligned.

---

### Case 7: Beta Coefficients Without Correlation Matrix

**Scenario:** SEM study reports only standardized path coefficients (β), no correlation matrix.

**Decision:** INCLUDE and convert β→r using Peterson & Brown (2005) formula.

**Requirement:**
- β must be standardized
- Sufficient paths reported to populate ≥2 construct pairs
- Mark as "beta-converted" for sensitivity analysis

**Rationale:** Excluding these studies would lose substantial data. Conversion method is validated. Sensitivity analysis addresses any bias.

---

### Case 8: Partial Correlation Matrix

**Scenario:** Study reports only significant correlations or only lower triangle.

**Decision:** INCLUDE and code available cells.

**Handling:**
- Non-significant correlations: If p > .05 and r not reported, code as missing (NOT as zero)
- Symmetry: If lower triangle only, mirror to upper triangle
- Diagonal: Always 1.00 for construct with itself

**Rationale:** Missing-data methods in MASEM can handle incomplete matrices. Available data still valuable.

---

### Case 9: Multi-Group Study (e.g., Education Level Comparison)

**Scenario:** Study reports separate correlation matrices for K-12 students (n=300) and undergraduate students (n=280).

**Decision:** Treat as TWO independent studies for meta-analysis.

**Coding:**
- study_id: AuthorYear_K12, AuthorYear_Undergrad
- Moderator: code education level for each

**Rationale:** Independent samples, potentially different construct meanings (developmental differences). Pooling would mask heterogeneity.

---

### Case 10: Constructs with Similar but Not Identical Names

**Scenario:** Study measures "Perceived AI Reliability" – is this Trust (TRU) or something else?

**Decision:** Apply construct harmonization decision tree (see construct_harmonization.md).

**Process:**
1. Review items if available
2. Check definition in study
3. Consult expert if unclear
4. Assign to closest construct with confidence rating (exact/high/moderate/low)
5. If confidence = low, consider excluding that construct pair from coding

**Rationale:** Construct validity is paramount. Forced misclassification introduces error.

---

## Quality Flags (Not Exclusion Criteria)

The following are recorded but do not exclude studies:

1. **Common Method Bias Risk:** Single-source, cross-sectional survey
2. **Low Reliability:** Any construct with α < .70
3. **Small Sample:** 50 ≤ n < 100
4. **Incomplete Matrix:** <50% of possible construct pairs reported
5. **Self-Developed Measures:** Non-validated scales
6. **Student Convenience Sample:** Convenience sample from single institution (very common in education research)
7. **Single-Item Measures:** Constructs measured with 1 item
8. **Single-Institution Bias:** Data from only one school/university
9. **Self-Selection Bias:** Voluntary participation in AI adoption studies

**Use:** Quality flags used in sensitivity analysis and moderator testing, not for exclusion.

---

## Inclusion Decision Flowchart

```
┌─────────────────────────────────────┐
│ Study identified in search          │
└──────────────┬──────────────────────┘
               │
               ▼
        ┌──────────────┐
        │ Empirical &  │───No──→ EXCLUDE
        │ Quantitative?│
        └──────┬───────┘
               │ Yes
               ▼
        ┌──────────────┐
        │ AI technology│───No──→ EXCLUDE
        │ focal?       │
        └──────┬───────┘
               │ Yes
               ▼
        ┌──────────────┐
        │ Educational  │───No──→ EXCLUDE
        │ context?     │
        └──────┬───────┘
               │ Yes
               ▼
        ┌──────────────┐
        │ Adoption/    │───No──→ EXCLUDE
        │ acceptance   │
        │ measured?    │
        └──────┬───────┘
               │ Yes
               ▼
        ┌──────────────┐
        │ Correlation  │───No──→ EXCLUDE
        │ matrix OR β? │
        └──────┬───────┘
               │ Yes
               ▼
        ┌──────────────┐
        │ ≥2 target    │───No──→ EXCLUDE
        │ constructs?  │
        └──────┬───────┘
               │ Yes
               ▼
        ┌──────────────┐
        │ 2015-2025?   │───No──→ EXCLUDE
        └──────┬───────┘
               │ Yes
               ▼
        ┌──────────────┐
        │ English?     │───No──→ EXCLUDE
        └──────┬───────┘
               │ Yes
               ▼
        ┌──────────────┐
        │ n ≥ 50?      │───No──→ EXCLUDE
        └──────┬───────┘
               │ Yes
               ▼
        ┌──────────────┐
        │ Peer-reviewed│───No──→ EXCLUDE
        │ article?     │
        └──────┬───────┘
               │ Yes
               ▼
        ┌──────────────┐
        │ Duplicate    │───Yes─→ EXCLUDE (keep best version)
        │ sample?      │
        └──────┬───────┘
               │ No
               ▼
        ┌──────────────┐
        │  INCLUDE     │
        └──────────────┘
```

---

## Inter-Rater Reliability for Inclusion Decisions

### Screening Phase

**Title/Abstract Screening:**
- Two independent screeners
- Training on 20 pilot studies
- Kappa target: κ ≥ .80
- Conflict resolution: Third screener or consensus discussion

**Full-Text Screening:**
- Two independent screeners
- More detailed decision justification required
- Kappa target: κ ≥ .85
- Complex cases: Full team discussion

### Sample Size for Reliability

- **Pilot:** 20 studies coded by both screeners
- **Reliability check:** 20% random sample of all screened studies
- **Ongoing calibration:** Monthly meetings to discuss borderline cases

### Disagreement Resolution Protocol

1. **Level 1:** Two screeners discuss and attempt consensus
2. **Level 2:** If unresolved, third screener reviews and votes
3. **Level 3:** If still unresolved, full team discussion with lead investigator final decision
4. **Documentation:** All disagreements and resolutions logged

---

## Documentation Requirements

For each included study, record:
- Inclusion decision (yes/no)
- Reason for exclusion (if applicable, coded)
- Screener ID
- Date of decision
- Any quality flags
- Notes on borderline decisions

For each excluded study, record:
- Primary exclusion reason (from standardized list)
- Secondary reasons (if applicable)
- Full-text reviewed? (yes/no)

**Exclusion Reason Codes:**
- E1: Not empirical/quantitative
- E2: No correlation matrix or β
- E3: Not AI technology
- E4: No adoption/acceptance focus
- E5: Fewer than 2 target constructs
- E6: Outside date range
- E7: Not English
- E8: Sample size < 50
- E9: Not peer-reviewed
- E10: Duplicate sample
- E11: Non-educational context
- E12: Other (specify)

---

## References

Cooper, H. M. (2017). *Research synthesis and meta-analysis: A step-by-step approach* (5th ed.). Sage.

Lipsey, M. W., & Wilson, D. B. (2001). *Practical meta-analysis*. Sage.

Peterson, R. A., & Brown, S. P. (2005). On the use of beta coefficients in meta-analysis. *Journal of Applied Psychology*, 90(1), 175-181.

Pigott, T. D. (2012). *Advances in meta-analysis*. Springer Science & Business Media.
