# Screening Protocol

## Overview

This document outlines the two-phase screening protocol for study selection, including AI-assisted screening, human oversight, inter-rater reliability procedures, and conflict resolution.

---

## Two-Phase Screening Process

### Phase 1: Title/Abstract Screening

**Objective:** Rapidly exclude clearly irrelevant studies

**Screeners:** 2 independent human screeners + AI-assisted flagging

**Input:** Deduplicated records from database search (estimated 1,000-2,000 records)

**Output:** Eligible records for full-text review (estimated 100-350 records)

**Timeline:** 2 weeks

---

### Phase 2: Full-Text Review

**Objective:** Apply detailed inclusion/exclusion criteria

**Screeners:** 2 independent human screeners

**Input:** Records passing Phase 1 (estimated 100-350 records)

**Output:** Final included studies (target: 40-80 studies)

**Timeline:** 3-4 weeks

---

## Phase 1: Title/Abstract Screening

### Screening Questions (Binary Yes/No)

Screeners answer the following for each record:

1. **Is this an empirical quantitative study?**
   - Yes: Reports data collection and statistical analysis
   - No: Conceptual, review, qualitative-only, opinion piece
   - Unclear: Proceed to next question (default to Yes if ambiguous)

2. **Does it focus on AI technology?**
   - Yes: Clear mention of AI, ML, deep learning, intelligent system, ITS, etc.
   - No: Generic IT, non-AI technology, or no technology mentioned
   - Unclear: Check keywords; if "artificial intelligence" or "machine learning" present → Yes

3. **Is the study conducted in an educational setting?**
   - Yes: School, university, online learning, educational administration mentioned
   - No: Workplace, healthcare, consumer, general public context
   - Unclear: Check for student/instructor/teacher population → Yes

4. **Does it measure adoption, acceptance, intention, or use?**
   - Yes: Adoption, acceptance, intention, use, resistance mentioned
   - No: Only awareness, perception, ethical views without behavior
   - Unclear: Proceed to full-text (default to Yes)

5. **Any indication of correlation or regression analysis?**
   - Yes: Mentions correlation, regression, SEM, path analysis, or "relationships"
   - No: Only ANOVA, t-test, chi-square, frequencies
   - Unclear: Proceed to full-text (default to Yes)

**Decision Rule:**
- **INCLUDE (proceed to Phase 2):** YES to questions 1, 2, 3, 4, and YES or UNCLEAR to question 5
- **EXCLUDE:** NO to any of questions 1, 2, 3, or 4; OR definitely NO to question 5

**Philosophy:** Liberal screening at Phase 1. When in doubt, include for full-text review.

---

### AI-Assisted Flagging System

**Purpose:** Pre-screen records to flag likely excludes for human review efficiency

**Model:** Fine-tuned BERT classifier (trained on pilot coding)

**Training Set:** 200 manually coded records (100 include, 100 exclude)

**Features:**
- Title + Abstract text embeddings
- Keyword presence (AI terms, adoption terms, method terms)
- Publication venue (journal impact, CS vs. psychology)

**Output:** Binary prediction (likely include / likely exclude) + confidence score

**Protocol:**
1. AI flags records with >80% confidence as "likely exclude"
2. Human screeners review AI-flagged excludes for false negatives
3. Human screeners review all AI "likely include" records normally
4. **Critical:** AI is advisory only; all exclusions require human confirmation

**Validation:**
- Test on hold-out set of 50 records
- Target: Sensitivity ≥ 95% (minimize false negatives)
- Specificity ≥ 70% (reduce human workload)

**Rationale:** AI assists but humans decide. False negatives (missed relevant studies) are worse than false positives (wasted full-text reviews).

---

### Human Screening Workflow

**Tool:** Rayyan QCRI (web-based screening tool)

**Workflow:**
1. Upload deduplicated records to Rayyan
2. AI flagging applied and visible to screeners as "suggestion"
3. Each screener independently reviews assigned records
4. Screeners blind to each other's decisions
5. After both complete: System reveals conflicts
6. Conflicts discussed and resolved

**Screening Assignment:**
- Screener A: All records (100%)
- Screener B: 100% of records (full independent screening)
- **OR** (if workload high):
  - Screener A: 50% of records + 20% overlap
  - Screener B: 50% of records + 20% overlap
  - 20% overlap used for reliability calculation

**Training:**
- 3-hour training session on inclusion/exclusion criteria
- Pilot screening of 50 records with discussion
- Calibration: Calculate κ on pilot; if κ < .70, additional training and re-pilot

**Decision Recording:**
- Include / Exclude
- Primary exclusion reason (if exclude)
- Confidence (high / moderate / low)
- Notes for borderline cases

---

### Inter-Rater Reliability Target

**Metric:** Cohen's Kappa (κ)

**Target:** κ ≥ .80 (substantial agreement)

**Calculation Sample:** 20% random stratified sample OR full overlap if using overlapping assignment

**Actions if Below Target:**
- κ = .70-.79: Discuss disagreements, clarify criteria, continue
- κ = .60-.69: Additional training session, re-code 50 studies, recalculate
- κ < .60: Major recalibration required, potentially revise criteria

**Reporting:**
- Report κ with 95% CI
- Report percent agreement
- Report disagreement patterns (which criteria most contentious)

---

### Conflict Resolution (Phase 1)

**Level 1: Discussion**
- Two screeners discuss conflicted records
- Review abstract together
- Attempt consensus
- **Success rate target:** >90% resolved at Level 1

**Level 2: Third Screener**
- If no consensus, third screener (senior researcher) reviews
- Third screener's decision is final
- Document rationale

**Level 3: Full-Text Preview**
- If still uncertain, retrieve full text and make decision based on more info
- Effectively promotes to Phase 2

**Documentation:**
- Log all conflicts and resolutions in `screening_conflicts.csv`
- Columns: study_id, screener1_decision, screener2_decision, conflict_type, resolution, final_decision, resolver

---

## Phase 2: Full-Text Review

### Full-Text Retrieval

**Sources:**
1. Institutional library access (primary)
2. Open access repositories (PubMed Central, arXiv)
3. Author contact (email request, ResearchGate)
4. Interlibrary loan (if critical and unavailable)

**Unobtainable Full Texts:**
- Document retrieval attempts (3 attempts minimum)
- Exclude if cannot obtain after 3 attempts
- Report in PRISMA flow diagram as "full text not available"

---

### Detailed Screening Questions

Screeners apply all inclusion/exclusion criteria (see inclusion_exclusion_criteria.md):

**Data Extraction Form Fields (used during screening):**

1. **Study Design:**
   - Quantitative? (Yes/No)
   - Design type: Cross-sectional / Longitudinal / Experimental / Mixed-methods

2. **AI Technology:**
   - AI technology mentioned? (Yes/No)
   - Type: ITS / Generative_AI / LMS_AI / Auto_Grading / Writing_Assistant / Adaptive_Learning / Other
   - Specificity: Named system / General AI category / Vague

3. **Educational Context:**
   - Educational setting? (Yes/No)
   - Setting: K-12 / Undergraduate / Graduate / Mixed / Faculty/Instructor / Administrator

4. **Dependent Variable:**
   - Adoption/acceptance/use measured? (Yes/No)
   - Construct: Behavioral Intention / Actual Use / Continuance / Resistance

5. **Statistical Reporting:**
   - Correlation matrix? (Yes/No) → If Yes, location: Main text / Appendix / Supplement
   - Standardized β? (Yes/No) → If Yes, number of paths reported: ___
   - Neither? → EXCLUDE

5. **Constructs Present:**
   - Checklist of 12 target constructs (check all that apply)
   - Number checked: ___ (must be ≥2)

6. **Sample Characteristics:**
   - Sample size (n): ___
   - n ≥ 50? (Yes/No)
   - Population: K-12_Students / Undergraduate / Graduate / Instructors / Administrators / Mixed
   - Country: ___
   - Education Level: K-12 / Higher_Education / Mixed
   - Discipline (if HE): STEM / Humanities / Social_Sciences / Business / Mixed / Not_Specified

7. **Publication Information:**
   - Year: ___
   - 2015-2025? (Yes/No)
   - Type: Journal / Conference / Other
   - Peer-reviewed? (Yes/No)
   - Language: English / Other

8. **Duplicate Check:**
   - Duplicate of another study? (Yes/No)
   - If Yes, which study: ___
   - Keep this version? (Yes/No, with justification)

**Final Decision:**
- [ ] INCLUDE
- [ ] EXCLUDE → Reason code (E1-E12): ___

---

### Screening Assignment (Phase 2)

**Double-Screening:**
- Screener A: All full texts (100%)
- Screener B: All full texts (100%)
- Independent decisions, then compare

**Alternative (if workload high):**
- Screener A: 100% of full texts
- Screener B: 30% random sample for reliability
- Third screener reviews any conflicts

**Training:**
- 2-hour refresher on detailed criteria
- Pilot full-text review of 10 studies
- Discuss disagreements and edge cases
- Calculate κ on pilot; proceed if κ ≥ .85

---

### Inter-Rater Reliability Target (Phase 2)

**Metric:** Cohen's Kappa (κ)

**Target:** κ ≥ .85 (almost perfect agreement)

**Rationale:** Full-text review allows more detailed assessment; higher reliability expected than Phase 1

**Calculation Sample:** 30% random sample OR full overlap if full double-screening

**Actions if Below Target:**
- κ = .80-.84: Acceptable; discuss major disagreements
- κ = .70-.79: Additional calibration session, clarify edge cases
- κ < .70: Major issues; convene full team meeting to revise criteria or retrain

---

### Conflict Resolution (Phase 2)

**Level 1: Independent Review**
- Each screener independently completes full-text review form
- Document specific page numbers and quotes for decisions

**Level 2: Comparison**
- Compare decisions in team meeting
- For each conflict, screeners present evidence (specific passages, tables)

**Level 3: Consensus Discussion**
- Discuss rationale for each decision
- Re-read relevant sections together
- Attempt consensus
- **Success rate target:** >85% resolved at Level 3

**Level 4: Senior Arbiter**
- If no consensus, research team member or expert consultant reviews
- Arbiter's decision is final
- Document rationale

**Level 5: Contact Authors (if data ambiguous)**
- If study is likely includable but data reporting unclear, email authors
- Request: Correlation matrix, sample size, construct definitions
- Allow 2 weeks for response
- If no response: Exclude with reason "insufficient data"

**Documentation:**
- `fulltext_conflicts.csv`: study_id, conflict_type, screener1_rationale, screener2_rationale, resolution, final_decision

---

## PRISMA 2020 Flow Diagram

### Data to Populate Diagram

**Identification:**
- Records identified from databases (by database)
- Records identified from citation searching
- Records removed before screening (duplicates)
- Records screened (title/abstract)

**Screening:**
- Records excluded at title/abstract stage (with reasons)
- Full-text articles sought for retrieval
- Full-text articles not retrieved (with reasons)

**Eligibility:**
- Full-text articles assessed for eligibility
- Full-text articles excluded (with reasons breakdown)

**Included:**
- Studies included in meta-analysis
- Total participants (N)

### Exclusion Reasons Breakdown (Phase 1 - Title/Abstract)

Track counts for:
- Not empirical/quantitative
- Not AI technology
- Not educational context
- Not adoption/acceptance focus
- Clearly qualitative only
- Clearly conceptual/review
- Other language
- Duplicate record
- Other

### Exclusion Reasons Breakdown (Phase 2 - Full Text)

Track counts for:
- E1: Not empirical/quantitative
- E2: No correlation matrix or β
- E3: Not AI technology
- E4: No adoption/acceptance focus
- E5: Fewer than 2 target constructs
- E6: Outside date range (2015-2025)
- E7: Not English
- E8: Sample size < 50
- E9: Not peer-reviewed
- E10: Duplicate sample
- E11: Non-educational context
- E12: Other (specify in notes)

---

## Screening Timeline

| Week | Phase | Activity | Deliverable |
|------|-------|----------|-------------|
| 1 | Training | Screener training, pilot Phase 1 | Training complete, κ ≥ .80 on pilot |
| 2-3 | Phase 1 | Title/abstract screening | Included records for full-text |
| 4 | Retrieval | Full-text retrieval, conflict resolution Phase 1 | Full-text PDFs obtained |
| 5 | Training | Phase 2 training, pilot full-text | Training complete, κ ≥ .85 on pilot |
| 6-7 | Phase 2 | Full-text review | Final inclusion decisions |
| 8 | Resolution | Conflict resolution, author contact | Final included studies list |
| 9 | Documentation | PRISMA diagram, screening report | Screening complete |

---

## Screening Software and Tools

### Rayyan QCRI (Phase 1)

**Features:**
- Web-based, collaborative screening
- Blinded screening mode
- AI suggestions (labels, filters)
- Conflict highlighting
- Export decisions

**Setup:**
- Import RIS/BibTeX files from all databases
- Assign screeners
- Configure inclusion/exclusion reasons
- Enable blinding

---

### Covidence (Alternative)

**Features:**
- PRISMA flow diagram auto-generation
- Full-text PDF management
- Duplicate detection
- Risk of bias assessment tools

**Consideration:** Requires subscription; Rayyan is free for academics

---

### Zotero (Reference Management)

**Use:**
- Store all retrieved full texts
- Tag studies (included, excluded, needs_review)
- Export citations for included studies

---

## Quality Control Procedures

### Random Audit

**Procedure:**
- After screening complete, randomly sample 5% of excluded records
- Senior researcher reviews
- Calculate false negative rate
- Target: <3% false negatives

**Action if >3% false negatives:**
- Review screener training
- Identify patterns in missed studies
- Consider re-screening with revised criteria

---

### Included Studies Verification

**Procedure:**
- After Phase 2 complete, all included studies reviewed by lead investigator
- Verify that each truly meets all inclusion criteria
- Spot-check for construct presence, correlation data availability

**Action if issues found:**
- Discuss with screeners
- Revise decision if necessary
- Document changes

---

## Reporting in Journal Article

### Methods Section Content

**Screening Process:**
- Describe two-phase screening
- Report screener training and reliability
- Report κ with 95% CI for both phases
- Describe conflict resolution process

**PRISMA Diagram:**
- Include full PRISMA 2020 flow diagram
- Report all numbers with exclusion reasons

**Supplementary Materials:**
- List of all excluded studies with reasons (online supplement)
- List of all included studies (in main text or appendix)
- Screening forms used

---

## Screener Roles and Responsibilities

### Lead Screener (Lead Investigator)

**Responsibilities:**
- Design screening protocol
- Train screeners
- Resolve conflicts (Level 2)
- Quality control audits
- PRISMA reporting

---

### Screener A (Co-Investigator or Research Assistant)

**Responsibilities:**
- Independent screening (Phases 1 and 2)
- Document decisions and rationale
- Participate in conflict resolution discussions
- Attend calibration meetings

---

### Screener B (Co-Investigator or Research Assistant)

**Responsibilities:**
- Independent screening (Phases 1 and 2)
- Document decisions and rationale
- Participate in conflict resolution discussions
- Attend calibration meetings

---

### Senior Arbiter (Research Team Member or Expert Consultant)

**Responsibilities:**
- Final decision on unresolved conflicts (Level 4)
- Quality audit of included studies
- Advisory on edge cases

---

## Edge Case Protocols

### Case: Conference Paper + Journal Article

**Detection:** Same authors, overlapping titles, similar year

**Decision:**
1. Check if data collection period overlaps
2. If same sample: Keep journal article only
3. If different samples: Include both as separate studies
4. If journal article is extended analysis: Keep journal only

---

### Case: Correlation Matrix in Supplementary Materials Not Linked

**Action:**
1. Check journal website for supplementary files
2. Search author's personal website, ResearchGate, OSF
3. Email corresponding author
4. If unobtainable after 3 attempts: Exclude with reason "correlation matrix reported but unavailable"

---

### Case: Study Reports "Significant Correlations Only"

**Decision:** Include if table reports actual r values for significant correlations

**Handling:** Non-significant correlations coded as missing (not zero)

**Quality Flag:** Mark for sensitivity analysis

---

### Case: Multi-Level Educational Study with Pooled Data Only

**Decision:** Include pooled data

**Moderator Coding:** Code as "mixed education level" for education level moderator

**Preference:** If level-specific data available (K-12 vs. higher ed), request from authors and code separately

---

## References

Higgins, J. P., Thomas, J., Chandler, J., Cumpston, M., Li, T., Page, M. J., & Welch, V. A. (Eds.). (2019). *Cochrane handbook for systematic reviews of interventions* (2nd ed.). Wiley.

McHugh, M. L. (2012). Interrater reliability: The kappa statistic. *Biochemia Medica*, 22(3), 276-282.

Ouzzani, M., Hammady, H., Fedorowicz, Z., & Elmagarmid, A. (2016). Rayyan—a web and mobile app for systematic reviews. *Systematic Reviews*, 5(1), 210.

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., ... & Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ*, 372, n71.
