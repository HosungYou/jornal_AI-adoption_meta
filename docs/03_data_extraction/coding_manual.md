# Comprehensive Coding Manual for AI Adoption Meta-Analysis

## Table of Contents

1. [Overview & Purpose](#1-overview--purpose)
2. [Research Questions](#2-research-questions)
3. [Inclusion/Exclusion Criteria Summary](#3-inclusionexclusion-criteria-summary)
4. [Construct Definitions](#4-construct-definitions)
5. [Construct Harmonization Rules](#5-construct-harmonization-rules)
6. [Correlation Matrix Extraction (MASEM Core)](#6-correlation-matrix-extraction-masem-core)
7. [Reliability Data Extraction](#7-reliability-data-extraction)
8. [Moderator Variable Coding](#8-moderator-variable-coding)
9. [Quality Assessment](#9-quality-assessment)
10. [AI-Assisted Coding Protocol](#10-ai-assisted-coding-protocol)
11. [Inter-Coder Reliability](#11-inter-coder-reliability)
12. [Discrepancy Resolution](#12-discrepancy-resolution)

---

## 1. Overview & Purpose

### 1.1 Study Goal

This meta-analytic structural equation modeling (MASEM) study synthesizes empirical research on AI technology adoption in educational contexts to:

1. Test the validity of traditional technology acceptance models (TAM/UTAUT) in the educational AI context
2. Evaluate whether AI-specific constructs (trust, anxiety, transparency, autonomy) provide incremental explanatory power
3. Identify moderators of AI adoption relationships in educational settings
4. Compare three competing theoretical models

### 1.2 Purpose of This Coding Manual

This manual provides operational definitions, decision rules, and procedures for extracting and coding data from included studies. It ensures:

- **Consistency:** All coders apply identical standards
- **Reproducibility:** Future researchers can replicate our coding decisions
- **Transparency:** Stakeholders understand how raw studies became meta-analytic data
- **Quality:** Systematic procedures minimize errors and bias

### 1.3 Scope

This manual covers coding of:
- Correlation matrices (primary MASEM input)
- Standardized path coefficients (β) for conversion to correlations
- Construct harmonization (mapping study constructs to 12 standard constructs)
- Reliability coefficients (Cronbach's α, CR, AVE)
- Moderator variables (AI type, industry, culture, year, context)
- Study quality indicators

### 1.4 Who Should Use This Manual

- Primary coders extracting data from studies
- Secondary coders verifying data for inter-coder reliability
- AI-assisted coding validators reviewing AI-extracted data
- Dissertation committee members evaluating coding procedures
- Future researchers attempting replication

---

## 2. Research Questions

### RQ1: TAM/UTAUT Validity in Educational AI Context

**Question:** Do traditional technology acceptance paths (PE→BI, EE→BI, SI→BI, FC→UB, ATT→BI, BI→UB) hold in educational AI adoption, with comparable effect sizes to general IT adoption?

**Analysis:** Compare Model 1 (TAM/UTAUT core) fit and path coefficients to:
- Sabherwal et al. (2006) general IT meta-analysis (Bayesian priors)
- Model fit indices (CFI, RMSEA, SRMR)

**Hypothesis:** Traditional paths remain significant but may be weaker in educational AI context due to unique AI characteristics (opacity, autonomy, uncertainty) and educational-specific factors (academic integrity concerns, institutional policies).

---

### RQ2: AI-Specific Constructs' Incremental Power

**Question:** Do AI-specific constructs (Trust, Anxiety, Transparency, Autonomy) explain variance in behavioral intention beyond TAM/UTAUT constructs?

**Analysis:** Compare Model 1 (TAM/UTAUT only) vs. Model 2 (Integrated):
- ΔR² in BI prediction
- Model comparison: Δχ², ΔCFI (>.01), ΔAIC/BIC
- Incremental paths: TRU→BI, ANX→BI, TRA→TRU, AUT→ANX

**Hypothesis:** Model 2 shows superior fit and explains 10-15% additional variance in BI.

---

### RQ3: Moderators of Educational AI Adoption Relationships

**Question:** Do education level, user role, discipline, AI tool type, cultural context, and temporal period moderate key adoption paths?

**Sub-questions:**
- **RQ3a (Education Level):** Do relationships differ across K-12, undergraduate, and graduate education?
- **RQ3b (User Role):** Are paths different for students vs. instructors?
- **RQ3c (Discipline):** Do relationships vary across STEM, humanities, and social sciences?
- **RQ3d (AI Tool Type):** Are ChatGPT/LLM paths different from ITS, LMS-AI, or auto-grading tools?
- **RQ3e (Culture):** Do relationships differ by individualism/collectivism?
- **RQ3f (Temporal):** Pre-ChatGPT (2015-2022) vs. Post-ChatGPT (2023-2025)?

**Analysis:** OSMASEM with continuous moderators, subgroup TSSEM for categorical moderators

**Hypotheses:**
- K-12 students show stronger SI→BI (peer influence more salient in younger students)
- Instructors show stronger FC→UB (institutional support more critical for faculty adoption)
- STEM students show stronger PE→BI (productivity focus in technical disciplines)
- Post-2023 shows stronger overall adoption in education (ChatGPT normalization effect)
- Collectivist cultures show stronger SI→BI (consistent with general TAM/UTAUT findings)

---

## 3. Inclusion/Exclusion Criteria Summary

(See `inclusion_exclusion_criteria.md` for full details)

### Quick Reference

**INCLUDE if ALL of:**
- ✅ Empirical quantitative study
- ✅ AI technology adoption/acceptance as focal phenomenon
- ✅ Correlation matrix OR standardized β reported
- ✅ At least 2 of 12 target constructs measured
- ✅ Published 2015-2025
- ✅ English language
- ✅ n ≥ 50
- ✅ Peer-reviewed journal or full conference paper

**EXCLUDE if ANY of:**
- ❌ Qualitative only, conceptual, review
- ❌ No correlation/β data
- ❌ Non-AI technology
- ❌ Only AI perception without adoption/acceptance
- ❌ Duplicate sample
- ❌ n < 50

---

## 4. Construct Definitions

This section provides **operational definitions** for all 12 target constructs. Use these definitions to determine whether a study's construct maps to our framework.

### 4.1 Performance Expectancy (PE)

**Definition:** The degree to which an individual believes that using AI technology will help them attain gains in learning outcomes (for students) or teaching effectiveness (for instructors), productivity, or academic task performance.

**Theoretical Origin:** UTAUT (Venkatesh et al., 2003), derived from TAM's Perceived Usefulness

**Key Indicators:**
- AI helps me achieve better learning outcomes
- AI improves my teaching effectiveness
- AI helps me complete academic tasks faster
- AI increases my academic productivity
- AI enhances my performance on coursework/research
- AI is useful for my learning/teaching tasks

**Boundary Conditions:**
- Must be **outcome-focused** (not process-focused like ease of use)
- Must be **performance-related** (not hedonic enjoyment)
- Can include relative advantage, output quality, productivity gains

**Examples from Literature:**
- "Perceived Usefulness" (Davis, 1989)
- "Relative Advantage" (Rogers, 2003)
- "Job-Fit" (Thompson et al., 1991)
- "Outcome Expectations" (Compeau & Higgins, 1995)
- "Extrinsic Motivation" (when task-focused)

**Non-Examples (Do NOT code as PE):**
- "Enjoyment" → ATT (unless explicitly task-related)
- "Ease of use" → EE
- "Usefulness of learning AI" → context-dependent (could be PE if job-related)

---

### 4.2 Effort Expectancy (EE)

**Definition:** The degree of ease associated with the use of AI technology, including ease of learning, ease of interaction, and freedom from mental effort.

**Theoretical Origin:** UTAUT (Venkatesh et al., 2003), derived from TAM's Perceived Ease of Use

**Key Indicators:**
- AI is easy to use
- Learning to use AI is easy
- Interaction with AI is clear and understandable
- AI is flexible to interact with
- It is easy to become skillful at using AI
- Using AI requires little mental effort
- AI is easy to integrate into my coursework/teaching

**Boundary Conditions:**
- Must be **effort-focused** (not outcome-focused)
- Must be **perceived** ease (not objective usability metrics)
- Can include complexity (reverse-coded), ease of learning, understandability

**Examples from Literature:**
- "Perceived Ease of Use" (Davis, 1989)
- "Complexity" (reverse) (Thompson et al., 1991)
- "Ease of Use" (Moore & Benbasat, 1991)
- "User-Friendliness"

**Non-Examples:**
- "AI is transparent" → TRA (understanding how it works, not ease of using it)
- "I am confident I can use AI" → SE (self-efficacy, not system ease)
- "Resources are available to use AI" → FC (support, not ease)

---

### 4.3 Social Influence (SI)

**Definition:** The degree to which an individual perceives that important others (colleagues, supervisors, friends, family) believe they should use AI technology.

**Theoretical Origin:** UTAUT (Venkatesh et al., 2003), derived from TRA/TPB's Subjective Norm

**Key Indicators:**
- People important to me think I should use AI
- My peers/classmates encourage AI use
- My instructors/advisors encourage AI use
- My peers use AI for learning
- Using AI improves my image/status among peers
- People who influence me think AI is valuable for learning/teaching

**Boundary Conditions:**
- Must be **social/normative** (not organizational support/resources)
- Must be **others' opinions** (not personal attitude)
- Can include injunctive norms (should use) and descriptive norms (others do use)

**Examples from Literature:**
- "Subjective Norm" (Ajzen, 1991)
- "Social Factors" (Thompson et al., 1991)
- "Image" (Moore & Benbasat, 1991)
- "Peer Influence"
- "Social Pressure"

**Non-Examples:**
- "Institution provides AI training" → FC (support, not social pressure)
- "I want to use AI because others do" → could be SI, but if it's personal desire, could be ATT
- "Administration mandates AI use" → FC (institutional context) or SI (normative pressure) — coder judgment required

---

### 4.4 Facilitating Conditions (FC)

**Definition:** The degree to which an individual believes that institutional and technical infrastructure exists to support the use of AI technology in educational settings.

**Theoretical Origin:** UTAUT (Venkatesh et al., 2003), derived from TPB's Perceived Behavioral Control and innovation diffusion's compatibility

**Key Indicators:**
- Resources necessary to use AI are available
- My institution provides AI tools and training
- I have the knowledge to use AI (when resource-framed)
- AI is compatible with existing learning management systems
- Technical support is available for AI at my school/university
- My institution supports AI use for learning/teaching

**Boundary Conditions:**
- Must be **resource/infrastructure-focused** (not social influence)
- Must be **external enablers** (not internal self-efficacy)
- Can include perceived behavioral control when resource-framed

**Examples from Literature:**
- "Perceived Behavioral Control" (Ajzen, 1991) — when resource-focused
- "Facilitating Conditions" (UTAUT)
- "Compatibility" (Rogers, 2003)
- "Organizational Support"
- "Resource Availability"

**Non-Examples:**
- "I am confident I can use AI" → SE (internal), not FC (external)
- "Others think I should use AI" → SI
- "AI is easy to use" → EE (system characteristic, not organizational support)

**Disambiguation: FC vs. SE:**
- **FC:** "Resources are available for me to use AI" (external)
- **SE:** "I am capable of using AI" (internal)
- If sentence is ambiguous, check items: "knowledge" alone is often SE; "access to knowledge/training/support" is FC

---

### 4.5 Behavioral Intention (BI)

**Definition:** The strength of an individual's intention to perform a specified behavior — in this context, to adopt, use, or continue using AI technology.

**Theoretical Origin:** Theory of Reasoned Action (Fishbein & Ajzen, 1975), TAM, UTAUT

**Key Indicators:**
- I intend to use AI
- I plan to use AI in the future
- I will use AI regularly for my academic work
- I am willing to use AI for learning/teaching
- I predict I will use AI in my coursework/teaching

**Boundary Conditions:**
- Must be **future-oriented intention** (not past/current behavior)
- Must be **behavioral** (not attitudinal evaluation)
- Can include adoption intention, continuance intention, willingness

**Examples from Literature:**
- "Behavioral Intention to Use" (Davis, 1989)
- "Intention to Adopt"
- "Willingness to Use"
- "Continuance Intention" (Bhattacherjee, 2001)
- "Intent to Recommend" (if user context)

**Non-Examples:**
- "I currently use AI" → UB (behavior, not intention)
- "I like AI" → ATT (attitude, not intention)
- "I am curious about AI" → context-dependent, likely not BI unless explicitly future use

---

### 4.6 Use Behavior (UB)

**Definition:** The actual use of AI technology, including frequency, intensity, breadth of use, or duration.

**Theoretical Origin:** TAM, UTAUT — behavior as the ultimate dependent variable

**Key Indicators:**
- I use AI regularly for learning/teaching tasks
- Frequency of AI use (times per week/month)
- I have used AI for academic tasks
- Duration of AI use sessions
- Breadth of AI features used in educational contexts

**Boundary Conditions:**
- Must be **actual behavior** (not intention)
- Must be **usage** (not awareness or trial only)
- Can be self-reported or objectively measured
- Can be retrospective ("I used AI last month") or ongoing ("I use AI weekly")

**Examples from Literature:**
- "Actual System Use" (Davis, 1989)
- "Usage Frequency"
- "System Usage"
- "Adoption Behavior"
- "Continued Use"

**Non-Examples:**
- "I intend to use AI" → BI
- "I know what AI is" → awareness (not usage)
- "I tried AI once" → trial, borderline (include if intensity/frequency measured)

**Measurement Types:**
- Self-report: "How often do you use AI?" (1=never, 5=daily)
- Objective: Log data, usage analytics (rare in meta-analysis studies)
- Binary: "Have you used AI?" (yes/no)
- Continuous: "Number of times used in past month"

---

### 4.7 Attitude (ATT)

**Definition:** An individual's overall evaluative judgment (positive or negative) about using AI technology, including affective and cognitive evaluations.

**Theoretical Origin:** Theory of Reasoned Action (Fishbein & Ajzen, 1975), TAM

**Key Indicators:**
- Using AI is a good/bad idea
- Using AI is pleasant/unpleasant
- I like/dislike using AI
- Using AI is beneficial/harmful
- Using AI is wise/foolish

**Boundary Conditions:**
- Must be **evaluative** (not descriptive)
- Must be **overall attitude** (not specific beliefs like usefulness)
- Can include affective (feelings) and cognitive (beliefs) components
- Can be pre-use (anticipated attitude) or post-use (experienced attitude)

**Examples from Literature:**
- "Attitude Toward Using Technology" (Davis, 1989)
- "Affect" (Thompson et al., 1991)
- "Overall Evaluation"
- "Satisfaction" (when pre-use or anticipatory)

**Non-Examples:**
- "AI is useful" → PE (specific belief, not overall attitude)
- "I intend to use AI" → BI (intention, not evaluation)
- "AI makes me anxious" → ANX (specific negative affect, not overall attitude)

**Disambiguation: ATT vs. PE:**
- **PE:** "AI improves my performance" (instrumental belief)
- **ATT:** "Using AI is a good idea" (evaluative judgment)
- ATT can be influenced by PE, but they are distinct constructs

**Disambiguation: ATT vs. ANX:**
- **ATT:** General positive/negative evaluation
- **ANX:** Specific negative affect (fear, apprehension)
- A person can have positive ATT but high ANX (approach-avoidance conflict)

---

### 4.8 Self-Efficacy (SE)

**Definition:** An individual's judgment of their capability to use AI technology successfully, derived from Bandura's social cognitive theory.

**Theoretical Origin:** Social Cognitive Theory (Bandura, 1986), extended to computer/technology self-efficacy

**Key Indicators:**
- I am confident in my ability to use AI for academic purposes
- I believe I can use AI without help
- I have the skills to use AI for learning/teaching
- I am capable of using AI even if challenging
- I can complete academic tasks using AI if I try

**Boundary Conditions:**
- Must be **internal capability belief** (not external resources)
- Must be **confidence/capability-focused** (not difficulty of system)
- Must be **domain-specific** (AI self-efficacy, not general self-efficacy)

**Examples from Literature:**
- "Computer Self-Efficacy" (Compeau & Higgins, 1995)
- "AI Self-Efficacy"
- "Technology Confidence"
- "Digital Competence" (when self-belief focused)
- "Perceived Capability"

**Non-Examples:**
- "AI is easy to use" → EE (system characteristic, not personal capability)
- "Training is available" → FC (external support)
- "I have used AI before" → experience (antecedent to SE, not SE itself)

**Disambiguation: SE vs. EE:**
- **SE:** "I can use AI" (personal capability)
- **EE:** "AI is easy to use" (system characteristic)
- SE is about the person; EE is about the technology

**Disambiguation: SE vs. FC:**
- **SE:** "I am capable of using AI" (internal)
- **FC:** "I have access to training/support to use AI" (external)

---

### 4.9 AI Trust (TRU)

**Definition:** The willingness to be vulnerable to AI system actions based on positive expectations regarding AI's reliability, competence, benevolence, and integrity.

**Theoretical Origin:** Organizational trust theory (Mayer et al., 1995), adapted to AI/automation trust

**Key Indicators:**
- I trust AI to make correct decisions
- AI is reliable for educational purposes
- AI is competent at its tasks
- AI acts in my best interest (benevolence)
- AI provides accurate educational content
- I am willing to depend on AI for learning/teaching support

**Boundary Conditions:**
- Must include **willingness to be vulnerable** or **positive expectation** about AI's character/competence
- Must be **AI-specific** (not general technology trust)
- Can include cognitive trust (competence, reliability) and affective trust (benevolence, integrity)

**Dimensions of Trust (code as TRU if study measures any):**
1. **Competence:** AI is capable and effective
2. **Reliability:** AI performs consistently
3. **Benevolence:** AI acts in user's interest
4. **Integrity:** AI is honest and ethical

**Examples from Literature:**
- "Trust in AI" (direct)
- "Algorithmic Trust"
- "Automation Trust"
- "System Trust"
- "Perceived Reliability" (competence dimension)
- "AI Benevolence"

**Non-Examples:**
- "AI is transparent" → TRA (antecedent to trust, not trust itself)
- "AI is useful" → PE
- "I feel comfortable with AI" → could be ATT or low ANX, not TRU unless vulnerability/dependence is implied

**Disambiguation: TRU vs. TRA:**
- **TRU:** "I trust AI" (vulnerability, positive expectation)
- **TRA:** "I understand how AI works" (explainability, transparency)
- TRA is often an antecedent to TRU, but they are distinct

---

### 4.10 AI Anxiety (ANX)

**Definition:** Apprehension, fear, or emotional discomfort when using or thinking about using AI technology.

**Theoretical Origin:** Computer anxiety (Heinssen et al., 1987), technology anxiety, extended to AI

**Key Indicators:**
- AI makes me anxious
- I fear using AI for academic work
- AI intimidates me
- I feel apprehensive about AI
- AI makes me uncomfortable
- I worry about academic integrity when using AI
- I fear plagiarism concerns with AI
- I worry about over-reliance on AI for learning

**Boundary Conditions:**
- Must be **negative emotional response** (not general negative attitude)
- Must be **anxiety/fear/apprehension** (not just dislike)
- Can include both trait anxiety (general AI anxiety) and state anxiety (during use)

**Examples from Literature:**
- "AI Anxiety"
- "Technology Anxiety"
- "Computer Anxiety"
- "Technostress" (when anxiety-focused)
- "Fear of AI"
- "AI Threat Perception" (when affective)

**Non-Examples:**
- "I dislike AI" → ATT (attitude, not anxiety)
- "AI is not useful" → reverse PE
- "AI will take my job" → could be ANX if emotional component, or perceived threat (code based on items)

**Disambiguation: ANX vs. ATT:**
- **ANX:** Specific fear/apprehension emotion
- **ATT:** General positive/negative evaluation
- A person can have neutral ATT but high ANX, or positive ATT but moderate ANX (approach-avoidance)

**Measurement Note:**
- Some studies measure "AI comfort" (reverse-coded ANX) — code as ANX (reverse)
- Some studies measure "technostress" — only code as ANX if anxiety/fear component is present (not workload/invasion dimensions)

---

### 4.11 AI Transparency (TRA)

**Definition:** The perceived ability to understand how an AI system reaches its outputs, decisions, or recommendations; explainability and interpretability of AI processes.

**Theoretical Origin:** Explainable AI (XAI) literature, algorithmic transparency

**Key Indicators:**
- I understand how AI makes decisions
- AI's reasoning is transparent
- AI provides explanations for outputs
- I can interpret AI's logic
- AI's process is clear to me
- AI grading/assessment is explainable
- I understand how AI evaluates my work
- AI is a "black box" (reverse-coded)

**Boundary Conditions:**
- Must be **understanding/explainability-focused** (not trust or ease)
- Must be about **process/mechanism** (how AI works), not just output quality
- Can include perceived transparency, explainability, interpretability

**Examples from Literature:**
- "Explainability"
- "Interpretability"
- "Transparency"
- "Algorithmic Transparency"
- "Understandability" (when mechanism-focused)
- "Black Box Perception" (reverse)

**Non-Examples:**
- "AI is easy to use" → EE (usability, not explainability)
- "I trust AI" → TRU (trust, not understanding)
- "AI provides accurate outputs" → PE (performance, not transparency)

**Disambiguation: TRA vs. EE:**
- **TRA:** "I understand how AI reaches conclusions" (explainability)
- **EE:** "AI is easy to use" (usability)
- A system can be easy to use (high EE) but opaque (low TRA), or vice versa

**Disambiguation: TRA vs. TRU:**
- **TRA:** Understanding/explainability (cognitive)
- **TRU:** Willingness to depend (affective + cognitive)
- TRA is often an antecedent to TRU (transparency → trust path in Model 2)

---

### 4.12 Perceived AI Autonomy (AUT)

**Definition:** The perceived degree to which an AI system operates independently and makes decisions without human intervention or oversight.

**Theoretical Origin:** Automation literature, human-AI interaction, agency theory

**Key Indicators:**
- AI makes decisions independently
- AI operates without human oversight
- AI has autonomous decision-making capability
- AI acts on its own
- AI requires minimal human intervention
- Level of automation (Parasuraman et al., 2000)

**Boundary Conditions:**
- Must be **autonomy/independence-focused** (not just capability)
- Must be **perceived** autonomy (not objective automation level, unless study asks participants to rate)
- Can include decision autonomy, action autonomy, or operational independence

**Examples from Literature:**
- "AI Autonomy"
- "Machine Autonomy"
- "Perceived AI Agency"
- "Automation Level"
- "AI Independence"
- "Decision-Making Autonomy"

**Non-Examples:**
- "AI is intelligent" → general capability, not autonomy
- "AI is useful" → PE
- "I trust AI to make decisions" → TRU (trust in autonomy, not perception of autonomy level)

**Disambiguation: AUT vs. FC:**
- **AUT:** Degree of AI independent operation
- **FC:** Availability of support/resources for human to use AI
- AUT is an AI characteristic; FC is an environmental characteristic

**Measurement Note:**
- Some studies use "level of automation" scales (Parasuraman et al., 2000) — code as AUT
- Some studies measure "AI agency" — code as AUT if independence/autonomy is emphasized

**Context-Dependence:**
- High autonomy can increase ANX (loss of control) or increase PE (efficient)
- Theorized path in Model 2: AUT→ANX (autonomy increases anxiety)

---

## 5. Construct Harmonization Rules

### 5.1 Harmonization Philosophy

**Goal:** Map diverse construct labels from primary studies onto our 12 standard constructs while preserving theoretical validity.

**Principle:** Prioritize **conceptual alignment** over label matching. A construct named "Usefulness" maps to PE even if the study doesn't use UTAUT terminology.

**Confidence Levels:**
- **Exact:** Study uses identical label and definition (e.g., "Performance Expectancy" from UTAUT)
- **High:** Different label but clear conceptual match (e.g., "Perceived Usefulness" → PE)
- **Moderate:** Requires interpretation based on items/definition (e.g., "AI Value" → likely PE, check items)
- **Low:** Ambiguous; items mix constructs or definition unclear (flag for expert review)

---

### 5.2 Decision Tree for Harmonization

**Step 1: Check Exact Match**
- Does study use one of our 12 construct names?
- If YES → Code as that construct (confidence = exact)
- If NO → Proceed to Step 2

**Step 2: Check TAM/UTAUT Family**
- Is construct from TAM (PU, PEOU, ATT, BI, Usage)?
- Is construct from UTAUT (PE, EE, SI, FC, BI, UB)?
- Use cross-reference table (Section 5.3)
- If YES → Map to standard construct (confidence = high)
- If NO → Proceed to Step 3

**Step 3: Check Construct Definitions (Section 4)**
- Read study's definition of the construct
- Compare to our 12 definitions
- Does it align with one?
- If YES → Map to that construct (confidence = moderate to high, depending on clarity)
- If NO → Proceed to Step 4

**Step 4: Check Items**
- Review scale items if available
- Do items operationalize one of our 12 constructs?
- If YES → Map to that construct (confidence = moderate)
- If items mix constructs → Flag for expert review or exclude
- If NO → Proceed to Step 5

**Step 5: Expert Review**
- Flag for discussion with lead investigator
- Document ambiguity
- Make best-judgment call or exclude construct from coding
- Confidence = low (if included)

---

### 5.3 TAM/UTAUT Cross-Reference Table

| Study Construct Label | Model Origin | Maps to | Confidence | Notes |
|----------------------|--------------|---------|------------|-------|
| Perceived Usefulness (PU) | TAM | PE | Exact | Core TAM construct |
| Perceived Ease of Use (PEOU) | TAM | EE | Exact | Core TAM construct |
| Attitude Toward Using | TAM | ATT | Exact | Core TAM construct |
| Behavioral Intention to Use | TAM/UTAUT | BI | Exact | Core TAM/UTAUT construct |
| Actual System Use / Usage | TAM/UTAUT | UB | Exact | Core TAM/UTAUT construct |
| Performance Expectancy | UTAUT | PE | Exact | Core UTAUT construct (synthesis of PU, extrinsic motivation, job-fit, relative advantage, outcome expectations) |
| Effort Expectancy | UTAUT | EE | Exact | Core UTAUT construct (synthesis of PEOU, complexity, ease of use) |
| Social Influence | UTAUT | SI | Exact | Core UTAUT construct (synthesis of subjective norm, social factors, image) |
| Facilitating Conditions | UTAUT | FC | Exact | Core UTAUT construct (synthesis of PBC, facilitating conditions, compatibility) |
| Subjective Norm | TRA/TPB | SI | High | Social influence antecedent |
| Perceived Behavioral Control | TPB | FC | High | When resource-focused; SE if capability-focused |
| Relative Advantage | DOI | PE | High | Rogers' diffusion of innovations |
| Complexity | DOI | EE (reverse) | High | Rogers' diffusion (reverse-coded ease) |
| Compatibility | DOI | FC | High | Fit with existing systems |
| Trialability | DOI | — | — | Not in our 12; exclude |
| Observability | DOI | — | — | Not in our 12; exclude |
| Computer Self-Efficacy | SCT | SE | High | Compeau & Higgins (1995) |
| Anxiety (computer/technology) | Various | ANX | High | If AI-specific or generalizable |
| Outcome Expectations | SCT | PE | High | Performance-related expectations |
| Affect | MPCU | ATT | High | Emotional response (Thompson et al., 1991) |
| Hedonic Motivation | UTAUT2 | ATT | Moderate | If AI-specific; could be PE if work context |
| Price Value | UTAUT2 | — | — | Not in our 12; exclude |
| Habit | UTAUT2 | — | — | Not in our 12; exclude |
| Experience | Various | — | — | Moderator, not construct; record separately |
| Voluntariness | Various | — | — | Moderator, not construct; record separately |

---

### 5.4 AI-Specific Construct Mappings

| Study Construct Label | Maps to | Confidence | Notes |
|-----------------------|---------|------------|-------|
| Trust in AI | TRU | Exact | Direct match |
| AI Trust | TRU | Exact | Direct match |
| Algorithmic Trust | TRU | Exact | Trust in algorithm |
| Automation Trust | TRU | High | Trust in automated system |
| System Trust | TRU | High | If AI system |
| Perceived Reliability | TRU | Moderate | Competence dimension of trust |
| Perceived Competence | TRU | Moderate | Competence dimension of trust |
| Benevolence | TRU | Moderate | Affective dimension of trust |
| Integrity | TRU | Moderate | Ethical dimension of trust |
| AI Anxiety | ANX | Exact | Direct match |
| Technology Anxiety | ANX | High | If AI context |
| Technostress | ANX | Moderate | Only if anxiety component (not workload/invasion) |
| Fear of AI | ANX | High | Anxiety-related |
| AI Threat Perception | ANX | Moderate | If affective component present |
| Discomfort with AI | ANX | Moderate | Check items for anxiety vs. general dislike |
| Explainability | TRA | Exact | XAI construct |
| Interpretability | TRA | Exact | XAI construct |
| Transparency | TRA | Exact | XAI construct |
| Algorithmic Transparency | TRA | Exact | Direct match |
| Black Box Perception | TRA (reverse) | High | Reverse-coded transparency |
| Understandability | TRA | Moderate | If mechanism-focused; EE if usage-focused |
| AI Autonomy | AUT | Exact | Direct match |
| Perceived AI Agency | AUT | High | Agency implies autonomy |
| Machine Autonomy | AUT | Exact | Direct match |
| Automation Level | AUT | High | Degree of autonomy |
| AI Independence | AUT | High | Autonomy-related |
| Decision-Making Autonomy | AUT | Exact | AI decision autonomy |

---

### 5.5 Ambiguous Cases Requiring Items Review

| Study Construct | Possible Mappings | Decision Rule |
|----------------|-------------------|---------------|
| "AI Value" | PE or ATT | Check items: "valuable for tasks" → PE; "valuable overall" → ATT |
| "AI Confidence" | SE or TRU | Check items: "confident in my ability" → SE; "confident in AI" → TRU |
| "AI Understanding" | TRA or EE | Check items: "understand how AI works" → TRA; "understand how to use AI" → EE |
| "AI Support" | FC or SI | Check items: "organizational support" → FC; "peer support/encouragement" → SI |
| "Perceived Control" | SE or FC or AUT (reverse) | Check items: "I can control AI" → SE or FC; "AI controls decisions" → AUT |
| "AI Quality" | PE or TRU | Check items: "output quality" → PE; "trustworthy/reliable" → TRU |
| "AI Satisfaction" | ATT or UB | Check items: Pre-use → ATT; post-use experience → could be ATT or outcome |
| "AI Capability" | PE or AUT | Check items: "helps me" → PE; "operates independently" → AUT |
| "AI Knowledge" | SE or FC | Check items: "I know how to use" → SE; "training available" → FC |

---

### 5.6 Multi-Dimensional Constructs

**Issue:** Some studies measure multi-dimensional constructs (e.g., "Trust" with Competence, Benevolence, Integrity subscales).

**Decision Rules:**

**Case A: All dimensions map to same construct**
- Study measures "Trust" with subscales: Competence, Benevolence, Integrity
- **Decision:** Code overall "Trust" as TRU
- **Correlation:** Use overall trust score if available; if only subscales reported, average correlations or use composite

**Case B: Dimensions map to different constructs**
- Study measures "AI Attitudes" with subscales: Usefulness (PE), Ease (EE), Liking (ATT)
- **Decision:** Code each subscale separately
- **Correlation:** Use subscale-specific correlations if available; if only overall score reported, code as missing for individual constructs

**Case C: Dimensions partially align**
- Study measures "AI Perception" with subscales: Usefulness (PE), Transparency (TRA), Other (unclear)
- **Decision:** Code aligned subscales separately; exclude unclear subscales
- **Correlation:** Use subscale correlations when possible

---

### 5.7 Handling Reverse-Coded Constructs

**Examples:**
- "Complexity" (reverse of EE)
- "AI Resistance" (reverse of BI or ATT)
- "Black Box Perception" (reverse of TRA)
- "Distrust" (reverse of TRU)

**Protocol:**
1. Identify reverse-coded construct
2. Map to appropriate construct with "(reverse)" flag
3. When coding correlations:
   - If study reports correlations based on reverse-coded scale → flip sign
   - Example: "Complexity" negatively correlates with BI (r = -.35) → EE positively correlates with BI (r = .35)
4. Document reversal in coding notes

---

## 6. Correlation Matrix Extraction (MASEM Core)

This is the **most critical section** for MASEM data extraction.

### 6.1 Locating Correlation Data

**Priority order for finding correlation matrices:**

1. **Main text tables:** Check "Results" and "Descriptive Statistics" sections
2. **Appendices:** Often labeled "Appendix A: Correlation Matrix" or "Appendix: Descriptive Statistics"
3. **Supplementary materials:** Online supplements, OSF repositories, journal website
4. **Author contact:** If study states "correlation matrix available upon request," email authors

**Table identification:**
- Look for tables titled: "Correlations," "Descriptive Statistics and Correlations," "Means, Standard Deviations, and Correlations," "Inter-Construct Correlations"
- Diagonal should be 1.00 (if Pearson r) or reliability coefficients (α, CR)
- Values should be in range [-1, 1] or slightly above 1 (if diagonal = reliability)

---

### 6.2 Direct Pearson r Extraction Rules

**Standard Correlation Matrix Format:**

```
         PE    EE    SI    BI
PE      1.00
EE      .45   1.00
SI      .38   .42   1.00
BI      .52   .48   .40   1.00
```

**Extraction Protocol:**

1. **Identify constructs:**
   - Map table column/row headers to our 12 constructs using harmonization rules
   - If construct unclear, check study's measurement section

2. **Extract values:**
   - Record Pearson r values for all pairs involving our 12 constructs
   - Lower triangle and upper triangle should be identical (symmetry check)
   - If table shows only lower triangle, mirror values

3. **Handle significance markers:**
   - Asterisks (*) indicate p-values: * p<.05, ** p<.01, *** p<.001
   - **Record the r value, ignore significance markers** (we care about effect size, not p-value)
   - If table shows "ns" (not significant) or blank cell: See Section 6.7

4. **Precision:**
   - Record to 2 decimal places (e.g., .45, not .4 or .450)
   - If study reports 3 decimals (.456), round to 2 (.46)

5. **Sample size per correlation:**
   - Default: Use study overall n
   - If study reports pairwise n (e.g., due to missing data): Record pairwise n
   - Create separate field: `r_sample_size` if different from study n

---

### 6.3 β→r Conversion (Peterson & Brown, 2005)

**When to use:**
- Study reports standardized path coefficients (β) from regression or SEM
- Study does NOT report Pearson correlation matrix
- β values are standardized (not unstandardized b)

**Formula (Peterson & Brown, 2005):**

```
r ≈ β + .05λ

where:
  λ = 1  if β ≥ 0
  λ = -1 if β < 0
```

**Examples:**
- β = .40 → r ≈ .40 + .05(1) = .45
- β = -.30 → r ≈ -.30 + .05(-1) = -.35
- β = .00 → r ≈ .00 + .05(1) = .05 (positive direction assumed)

**Recording Requirements:**
- **r_value:** Converted r (e.g., .45)
- **r_source:** "beta_converted"
- **original_beta:** Original β value (e.g., .40)
- **beta_se:** Standard error of β (if reported, for sensitivity analysis)

**Quality flags:**
- Mark study for sensitivity analysis (beta-converted subsample)
- In Results section, report: "X studies (Y%) contributed correlation data via β→r conversion"

**Limitations to document:**
- Conversion assumes linear relationship
- Accuracy depends on predictor correlations (not reported in most studies)
- Sensitivity analysis will compare: full sample vs. r-only subsample

---

### 6.4 Incomplete Matrix Handling

**Issue:** Study measures 5 of our 12 constructs but only reports correlations for 3 pairs.

**Protocol: Available-Case Principle**

1. **Extract available cells:**
   - Code all reported correlations
   - Leave unreported cells as missing (NA)

2. **Do NOT:**
   - Assume unreported correlations are zero
   - Assume non-significant correlations are zero
   - Impute missing correlations at extraction stage

3. **Record matrix completeness:**
   - Calculate: `matrix_completeness = (reported_pairs / possible_pairs) × 100`
   - Example: 5 constructs = 10 possible pairs; 6 reported → 60% complete

4. **MASEM handling:**
   - Stage 1 TSSEM can handle missing cells via FIML or multiple imputation
   - metaSEM package has built-in missing data handling

**Example:**

Study measures PE, EE, BI (3 constructs = 3 possible pairs: PE-EE, PE-BI, EE-BI)
Study reports: PE-BI (.52), EE-BI (.48)
Study does NOT report: PE-EE

**Coding:**
```
PE-EE: NA (missing)
PE-BI: .52
EE-BI: .48
```

---

### 6.5 Multiple Samples/Timepoints

**Scenario 1: Multiple Independent Samples in One Study**

Example: Study collects data from USA (n=300) and China (n=280) separately.

**Decision:** Treat as TWO separate studies
- study_id: AuthorYear_USA, AuthorYear_China
- Extract separate correlation matrices for each
- Code moderators separately (country, culture, etc.)

---

**Scenario 2: Longitudinal Data (Same Sample, Multiple Timepoints)**

Example: Study measures T1 (n=400), T2 (n=350), T3 (n=320) with same participants.

**Decision:** Use ONE timepoint to avoid dependency
- **Default:** Use T3 (most mature adoption attitudes)
- **Alternative:** Use T1 if T3 has excessive attrition or T1 has better construct coverage
- Document choice in coding notes

**Exception:** If study reports cross-lagged correlations (T1_PE with T2_BI), extract only synchronous correlations (T1_PE with T1_BI, T2_PE with T2_BI), choose one timepoint.

---

**Scenario 3: Experimental Conditions**

Example: Study has Control (n=100) and Treatment (n=100) groups, reports separate correlations.

**Decision:**
- If AI adoption is measured in both conditions: Use data from condition most relevant to AI adoption (typically Treatment)
- If AI adoption is only in Treatment: Use Treatment group only
- Do NOT pool across conditions (different contexts)

---

### 6.6 Positive Definiteness Check

**Issue:** For SEM to work, correlation matrix must be positive definite (all eigenvalues > 0).

**Check:**
- Not required during extraction
- Conducted during data analysis (Stage 1 TSSEM preprocessing)

**If matrix fails:**
- metaSEM will flag non-positive definite matrices
- Options: Smooth matrix, exclude study, check for data entry errors

**Extraction Implications:**
- Carefully check for data entry errors (values outside [-1, 1])
- Verify symmetry (lower triangle = upper triangle)
- Check diagonal (should be 1.00)

---

### 6.7 Handling Non-Significant or Unreported Correlations

**Case A: Study states "only significant correlations reported"**

Example: Table shows PE-BI (.52**), EE-BI (.48**), but PE-EE cell is blank.

**Decision:**
- Code blank cells as **missing (NA)**, NOT zero
- Rationale: Non-significant ≠ zero; could be r=.08 (p=.06), which is still a positive effect

**Exception:**
- If study explicitly states "non-significant correlations set to .00," code as .00 and flag for sensitivity analysis

---

**Case B: Study reports "ns" (not significant)**

**Decision:**
- Code as missing (NA)
- Rationale: We don't know the actual value, could be -.10 or +.10

---

**Case C: Study reports significance levels without r values**

Example: "PE significantly correlated with BI (p<.01)"

**Decision:**
- Cannot extract (insufficient information)
- If this is only data source: Exclude study
- If study has β coefficients: Use β→r conversion

---

### 6.8 Sample Size per Correlation Pair

**Default:** Use study overall n for all correlations

**Exception:** Pairwise n differs due to missing data

Example:
- Study overall n=500
- PE-BI pair: n=485 (15 participants missing data on PE or BI)
- EE-BI pair: n=490

**Recording:**
- Create `pairwise_n` field
- If pairwise n not reported: Use study n
- If pairwise n reported: Use pairwise n (more accurate)

**MASEM implication:**
- metaSEM uses sample size for weighting
- Larger n → more weight in pooled correlation

---

## 7. Reliability Data Extraction

### 7.1 Importance for MASEM

Reliability coefficients (Cronbach's α, composite reliability, AVE) are used for:
1. **Quality assessment:** Low reliability (<.70) flags measurement concerns
2. **Artifact correction:** Optionally correct correlations for attenuation due to unreliability
3. **Sensitivity analysis:** Compare results with/without low-reliability studies

---

### 7.2 Reliability Metrics

**Extract ALL available reliability metrics:**

**Cronbach's Alpha (α):**
- Most commonly reported
- Acceptable: α ≥ .70
- Good: α ≥ .80
- Excellent: α ≥ .90

**Composite Reliability (CR):**
- From CFA/SEM studies
- Same thresholds as α

**Average Variance Extracted (AVE):**
- Acceptable: AVE ≥ .50
- Indicates convergent validity

---

### 7.3 Extraction Protocol

**Location:**
- Measurement model tables
- "Reliability and Validity" tables
- Appendices
- Diagonal of correlation matrix (sometimes)

**Recording:**
- One row per construct per study
- Columns: study_id, construct, alpha, CR, AVE, num_items

**Example:**

| study_id | construct | alpha | CR   | AVE  | num_items |
|----------|-----------|-------|------|------|-----------|
| Smith2023 | PE       | .89   | .90  | .64  | 4         |
| Smith2023 | EE       | .85   | .86  | .61  | 3         |
| Smith2023 | BI       | .92   | .93  | .82  | 3         |

---

### 7.4 Missing Reliability Data

**If study does not report reliability:**
- Code as missing (NA)
- Flag study in quality assessment
- Do NOT exclude study (common in older TAM studies)
- Do NOT assume α=.70 or any other value

---

### 7.5 Minimum Thresholds (Quality Flags, Not Exclusion)

**Flag for quality concerns if:**
- α < .70 for any construct
- AVE < .50 for any construct
- Single-item measures (no reliability calculable)

**Do NOT exclude based on reliability alone** — handle in sensitivity analysis

---

## 8. Moderator Variable Coding

### 8.1 Education Level

**Categories:**

1. **K-12:** Elementary, middle, and high school students or teachers
   - Examples: K-6, grades 7-12, secondary education

2. **Undergraduate:** College/university students pursuing bachelor's degrees
   - Examples: Community college, 4-year university undergraduates

3. **Graduate:** Students pursuing master's or doctoral degrees
   - Examples: Master's students, PhD students, professional degree students

4. **Mixed/Unspecified:** Multiple education levels or not clearly specified
   - Examples: Study combines undergrad and graduate, education level not reported

**Coding Rules:**
- Based on study sample characteristics
- If study reports multiple levels separately: Treat as separate studies (see Section 6.5)
- If study pools multiple levels: Code as "Mixed"
- Professional development programs for teachers: Code based on teacher level (K-12 vs. higher ed)

**Binary Variable (for subgroup analysis):**
- `higher_ed`: 1=undergraduate or graduate, 0=K-12

---

### 8.2 User Role

**Categories:**

1. **Student:** Learners using AI for learning tasks
   - Examples: K-12 students, undergraduates, graduate students

2. **Instructor/Faculty:** Teachers, professors, instructors using AI for teaching
   - Examples: K-12 teachers, university faculty, teaching assistants, adjuncts

3. **Educational Administrator:** Staff or administrators using AI for institutional management
   - Examples: Deans, registrars, admissions officers, IT staff

4. **Mixed:** Multiple user roles in sample
   - Examples: Study includes both students and instructors

**Coding Rules:**
- Based on study sample description
- If study reports roles separately: Treat as separate studies
- If study pools roles: Code as "Mixed"
- Student teachers/teacher candidates: Code as "Student" (graduate education context)

**Binary Variable (for subgroup analysis):**
- `student_role`: 1=student, 0=instructor/other

---

### 8.3 Discipline

**Categories:**

1. **STEM:** Science, technology, engineering, mathematics
   - Examples: Computer science, biology, physics, chemistry, engineering, mathematics

2. **Humanities:** Literature, history, philosophy, arts
   - Examples: English, history, philosophy, foreign languages, art, music

3. **Social Sciences:** Psychology, sociology, education, business
   - Examples: Psychology, sociology, political science, education, business administration, economics

4. **Health Sciences:** Nursing, medicine, public health
   - Examples: Nursing programs, medical education, health administration

5. **Mixed/Unspecified:** Multiple disciplines or discipline not reported
   - Examples: General education samples, discipline not specified

**Coding Rules:**
- Based on study sample characteristics (major, department, course context)
- If study is course-specific: Code based on course discipline
- If general student sample without discipline info: Code as "Mixed/Unspecified"
- Professional programs (MBA, nursing): Code as discipline-specific

**Binary Variable (for subgroup analysis):**
- `stem`: 1=STEM, 0=other

---

### 8.4 AI Tool Type

**Categories:**

1. **Chatbot/LLM:** ChatGPT, Claude, Gemini, other large language models
   - Examples: ChatGPT, GPT-4, Claude, Gemini, Bard, LLaMA-based tools

2. **Intelligent Tutoring System (ITS):** AI-powered adaptive tutoring
   - Examples: ALEKS, Carnegie Learning, DreamBox, Knewton

3. **LMS-Integrated AI:** AI features within learning management systems
   - Examples: Canvas AI tools, Blackboard AI, Moodle AI plugins

4. **Automated Grading/Assessment:** AI for grading essays, code, or assignments
   - Examples: Gradescope, Turnitin Feedback Studio, automated essay scoring

5. **AI Writing Assistant:** Tools specifically for writing support
   - Examples: Grammarly, Quillbot, AI writing tutors

6. **Adaptive Learning Platform:** AI-driven personalized learning paths
   - Examples: Khan Academy AI, Smart Sparrow, Realizeit

7. **General/Other:** Generic AI or multiple tool types
   - Examples: Study refers to "AI" generically, multiple tools, other categories

**Coding Rules:**
- Based on AI tool/system described in study
- If specific tool named: Code based on tool type
- If multiple tools: Code as "General/Other" unless all in same category
- Generic "AI" without specification: Code as "General/Other"

**Binary Variable (for subgroup analysis):**
- `llm_chatbot`: 1=Chatbot/LLM, 0=other

---

### 8.5 Institutional Type

**Categories:**

1. **Public University/School:** Public higher education or K-12
2. **Private University/School:** Private higher education or K-12
3. **Online/Distance Education:** Primarily online institutions
4. **Community College:** Two-year colleges
5. **Mixed/Unspecified:** Multiple institution types or not specified

**Coding Rules:**
- Based on study sample institution
- If multiple institutions: Code as "Mixed" unless all same type
- If not reported: Code as "Unspecified"

---

### 8.6 Cultural Dimension

**Operationalization:** Hofstede's Individualism-Collectivism Index

**Data Source:** Hofstede Insights (https://www.hofstede-insights.com)

**Coding:**
- Identify study country
- Look up Hofstede individualism score (0-100 scale)
- Record continuous score (0=collectivist, 100=individualist)

**Examples:**
- USA: 91 (highly individualist)
- China: 20 (collectivist)
- Japan: 46 (moderate)

**Multi-Country Studies:**
- If study pools multiple countries: Code as weighted average (if sample sizes available) or median
- If study reports separate results by country: Treat as separate studies (see Section 6.5)

**Missing Data:**
- If country not in Hofstede database: Code as NA
- If study does not report country: Code as NA

**Binary Variable (for subgroup analysis):**
- `individualist`: 1 if score ≥50, 0 if score <50

---

### 8.7 Publication Year

**Extraction:** Year of publication (from study metadata)

**Coding:**
- Continuous variable: 2015, 2016, ..., 2025
- **Binary variable (ChatGPT era):**
  - `post_chatgpt`: 1 if year ≥ 2023, 0 if year ≤ 2022
  - Rationale: ChatGPT launched November 2022; 2023 marks generative AI boom

**Online-First Articles:**
- Use year of online-first publication (not print publication)
- If both available: Use earlier date

---

### 8.8 Country Development Level

**Categories:**

1. **Developed:** High-income economies per World Bank
2. **Developing:** Low- and middle-income economies per World Bank

**Data Source:** World Bank Country Classifications
(https://datahelpdesk.worldbank.org/knowledgebase/articles/906519-world-bank-country-and-lending-groups)

**Coding:**
- Identify study country
- Look up World Bank classification
- Code as Developed/Developing

**Examples:**
- Developed: USA, Canada, UK, Germany, Japan, South Korea, Australia
- Developing: China, India, Brazil, Mexico, Indonesia, Nigeria

**Multi-Country Studies:**
- If mix of developed/developing: Code based on majority of sample
- If equal mix: Code as "Mixed" (separate category)

---

### 8.9 Additional Moderators (Opportunistic)

**Record if available (not required):**

- **AI experience:** Novice vs. Experienced users
- **Voluntariness:** Mandatory vs. Voluntary use (Note: Most educational AI adoption is voluntary for students, but may be mandatory for course-embedded tools)
- **Age:** Mean age of sample
- **Gender:** Percent female
- **Academic level:** Year in school (freshmen, sophomore, etc.)

**Use:** Exploratory moderator analysis if sufficient studies report

---

## 9. Quality Assessment

### 9.1 Study-Level Quality Checklist

**Quality Domains:**

1. **Reporting Quality:** Transparency and completeness
2. **Sample Adequacy:** Size and representativeness
3. **Construct Validity:** Measurement quality
4. **Common Method Bias (CMB) Handling:** Procedures to mitigate
5. **Matrix Completeness:** Correlation data availability
6. **Educational Context Quality:** Educational sample appropriateness

---

### 9.2 Reporting Quality (0-5 points)

**Criteria:**
- Correlation matrix reported (2 points) or β reported (1 point)
- Sample size clearly reported (1 point)
- Reliability coefficients reported for all constructs (1 point)
- Measurement items provided or referenced (1 point)
- Study design and procedure clearly described (1 point if missing: -1)

**Scoring:**
- High: 4-5 points
- Moderate: 2-3 points
- Low: 0-1 points

---

### 9.3 Sample Adequacy (0-3 points)

**Criteria:**
- Sample size: ≥200 (2 points), 100-199 (1 point), 50-99 (0 points)
- Representativeness: Probabilistic/diverse sample (1 point), convenience sample (0 points)
- Response rate: ≥60% (bonus +1 point if applicable)

**Scoring:**
- High: 3+ points
- Moderate: 2 points
- Low: 0-1 points

---

### 9.4 Construct Validity (0-4 points)

**Criteria:**
- Validated scales used (1 point) vs. self-developed (0 points)
- Reliability: All α≥.70 (1 point), any α<.70 (-1 point)
- Convergent validity: AVE≥.50 reported (1 point)
- Discriminant validity: Fornell-Larcker or HTMT reported (1 point)

**Scoring:**
- High: 3-4 points
- Moderate: 2 points
- Low: 0-1 points

---

### 9.5 Common Method Bias (CMB) Handling (0-2 points)

**Criteria:**
- Procedural remedies: Temporal separation, anonymity, different response formats (1 point)
- Statistical remedies: Harman's test, CFA marker variable, CLF (1 point)

**Scoring:**
- Addressed: 1-2 points
- Not addressed: 0 points

**Note:** CMB is a concern for cross-sectional single-source surveys (most studies). Not addressing it is common but flags study as higher bias risk.

---

### 9.6 Matrix Completeness (0-2 points)

**Criteria:**
- ≥80% of possible construct pairs reported: 2 points
- 50-79% reported: 1 point
- <50% reported: 0 points

**Calculation:**
- Number of constructs coded: k
- Possible pairs: k(k-1)/2
- Reported pairs: count non-missing correlations
- Completeness: (reported / possible) × 100%

---

### 9.7 Educational Context Quality (0-3 points)

**Criteria:**
- Representative educational sample (not convenience only): 1 point
- Single-institution bias addressed (multi-institution or acknowledged): 1 point
- Voluntary vs. course-embedded participation clearly reported: 1 point
- Academic integrity/plagiarism concerns addressed in design: Bonus +1

**Education-Specific Quality Flags:**
- Student convenience sampling (e.g., single class section)
- Single-institution bias
- Self-selection in AI tool adoption
- Course-embedded vs. voluntary participation not distinguished

**Scoring:**
- High: 2-3 points
- Moderate: 1 point
- Low: 0 points

---

### 9.8 Overall Quality Score

**Total:** Sum of all domains (0-19 points max, but typically 0-16 realistic)

**Categories:**
- High Quality: ≥12 points
- Moderate Quality: 7-11 points
- Low Quality: 0-6 points

**Use:**
- Report distribution in meta-analysis
- Sensitivity analysis: High-quality studies only
- Meta-regression: Quality as moderator

---

## 10. AI-Assisted Coding Protocol

### 10.1 Overview: 7-Phase Pipeline

**Phase 0: RAG Index Building**
- Ingest all included study PDFs
- Build vector database (ChromaDB) with all-MiniLM-L6-v2 embeddings
- Enable retrieval-augmented generation for context

**Phase 1: Correlation Extraction (AI)**
- Claude Sonnet 4.5 extracts correlation matrices
- Prompt: "Extract correlation matrix for [constructs] from this study"
- Output: Structured JSON with correlation pairs

**Phase 2: Construct Mapping (AI)**
- Claude Sonnet maps study constructs to 12 standard constructs
- Uses harmonization rules from this manual
- Output: Mapping table with confidence scores

**Phase 3: 3-Model Consensus (AI)**
- Claude Sonnet 4.5, GPT-4o, Groq (Llama) independently code
- Compare outputs, flag discrepancies
- Consensus: Agreement by 2+ models
- Output: Consensus dataset + discrepancy log

**Phase 4: Human ICR (20% Sample)**
- Stratified random sample (20% of studies)
- Human coders independently code sample
- Calculate inter-coder reliability (ICC, κ, MAE)

**Phase 5: Discrepancy Resolution**
- Human review of AI-AI and AI-human discrepancies
- Apply priority: Original text > Human > AI consensus
- Update coding based on resolution

**Phase 6: QA Final**
- 6 quality gates:
  1. Range check (r ∈ [-1, 1])
  2. Symmetry check (r_ij = r_ji)
  3. Diagonal check (r_ii = 1.00)
  4. Completeness check (≥2 constructs per study)
  5. Sample size check (n ≥ 50)
  6. Duplicate check (no duplicate study IDs)
- Output: Final validated dataset

---

### 10.2 AI Model Roles

| Model | Primary Use | Strengths | Limitations |
|-------|-------------|-----------|-------------|
| Claude Sonnet 4.5 | Correlation extraction, construct mapping | Nuanced reasoning, long context | API cost |
| GPT-4o | Consensus coding, validation | Fast, reliable, well-established | Less nuanced than Claude for ambiguous cases |
| Groq (Llama 3.3 70B) | Third-party consensus | Fast inference, open-source | Less sophisticated than Claude/GPT |

---

### 10.3 Prompting Strategy

**Correlation Extraction Prompt Template:**

```
You are extracting correlation data for a meta-analysis on AI adoption in educational contexts.

STUDY: [Study ID, Authors, Year]

TASK: Extract Pearson correlation coefficients among the following constructs:
- Performance Expectancy (PE) - learning/teaching effectiveness
- Effort Expectancy (EE) - ease of use
- Social Influence (SI) - peer/instructor influence
- Facilitating Conditions (FC) - institutional support
- Behavioral Intention (BI) - intention to use for academic work
- Use Behavior (UB) - actual use for learning/teaching
- Attitude (ATT) - overall evaluation
- Self-Efficacy (SE) - confidence in using AI
- AI Trust (TRU) - trust in AI for education
- AI Anxiety (ANX) - fear/academic integrity concerns
- AI Transparency (TRA) - explainability/grading transparency
- Perceived AI Autonomy (AUT) - AI independence

INSTRUCTIONS:
1. Locate correlation matrix in tables, appendices, or supplementary materials
2. Map study's construct labels to the 12 standard constructs above
3. Extract r values (2 decimal places)
4. If study reports β instead of r, note this
5. Record sample size (n)
6. Note educational context (student vs. instructor, education level)

OUTPUT FORMAT (JSON):
{
  "study_id": "AuthorYear",
  "sample_size": 300,
  "correlations": [
    {"construct1": "PE", "construct2": "BI", "r": 0.52, "source": "pearson"},
    {"construct1": "EE", "construct2": "BI", "r": 0.48, "source": "pearson"}
  ],
  "construct_mapping": {
    "Perceived Usefulness": "PE",
    "Ease of Use": "EE",
    "Intention to Use": "BI"
  },
  "notes": "Matrix in Table 3, page 12. Sample: undergraduate students"
}

STUDY TEXT:
[Full study text via RAG retrieval]
```

---

### 10.4 Cost Tracking

**Estimated Costs (per study):**
- Claude Sonnet API: ~$0.50-1.00 per study (long context)
- GPT-4o API: ~$0.20-0.40 per study
- Groq: Free tier or ~$0.05 per study

**Total Budget (for 40-80 studies, educational AI focus):**
- Claude: $40-80
- GPT-4o: $16-32
- Groq: $0-5
- **Total: ~$56-117**

---

### 10.5 Audit Logging

**Log Files:**
- `ai_extraction_log.jsonl`: One entry per AI coding pass (model, study_id, timestamp, prompt, response)
- `discrepancy_log.csv`: AI-AI and AI-human discrepancies
- `resolution_log.csv`: Human resolution decisions

**Fields in Audit Log:**
- timestamp
- model_id (claude-sonnet-4.5, gpt-4o, groq-llama-3.3-70b)
- study_id
- prompt_template_version
- response (full JSON)
- processing_time_sec
- api_cost_usd

---

## 11. Inter-Coder Reliability

### 11.1 Sampling Strategy

**20% Stratified Random Sample:**
- Stratify by:
  1. Publication year (2015-2019, 2020-2022, 2023-2025)
  2. AI type (generative, predictive, other)
  3. Region (North America, Europe, Asia, Other)

**Sample Size:**
- If k=150 studies total: 30 studies for ICR (20%)
- If k=100 studies total: 20 studies for ICR (20%)

**Selection:**
- Use stratified random sampling to ensure representation
- Fixed seed for reproducibility

---

### 11.2 Metrics

**Categorical Variables (Construct Mapping, Moderators):**
- **Cohen's Kappa (κ):** Agreement beyond chance
- **Target:** κ ≥ .85
- **Interpretation:**
  - κ < .40: Poor
  - .40 ≤ κ < .60: Moderate
  - .60 ≤ κ < .80: Substantial
  - κ ≥ .80: Almost perfect

**Numerical Variables (Correlations):**
- **Intraclass Correlation Coefficient (ICC):**
  - ICC(2,1): Two-way random effects, single rater
  - **Target:** ICC ≥ .95
- **Mean Absolute Error (MAE):**
  - MAE = mean(|r_coder1 - r_coder2|)
  - **Target:** MAE ≤ .03

**Reliability (α, CR):**
- **ICC(2,1):** ≥ .95
- **MAE:** ≤ .02

---

### 11.3 Calculation Procedure

**Software:** R (irr package for κ, ICC; psych package for alternative ICC calculations)

**Code Example:**

```r
library(irr)

# Cohen's Kappa for construct mapping
construct_mapping <- data.frame(
  coder1 = c("PE", "PE", "EE", "BI", ...),
  coder2 = c("PE", "ATT", "EE", "BI", ...)
)
kappa2(construct_mapping)

# ICC for correlations
correlation_data <- data.frame(
  coder1 = c(0.52, 0.48, 0.40, ...),
  coder2 = c(0.51, 0.47, 0.42, ...)
)
icc(correlation_data, model = "twoway", type = "agreement", unit = "single")
```

---

### 11.4 Training Procedure

**Pre-Coding Training (Coders):**

1. **Session 1 (3 hours):** Review coding manual
   - Read Sections 1-6 (Overview through Correlation Extraction)
   - Discuss construct definitions
   - Practice construct harmonization with examples

2. **Session 2 (2 hours):** Pilot coding
   - Independently code 5 practice studies (not in final sample)
   - Compare results
   - Discuss discrepancies
   - Calculate pilot κ and ICC

3. **Calibration:** If pilot reliability < target, additional training session

4. **Production:** Begin coding ICR sample

---

### 11.5 Discrepancy Patterns Analysis

**After ICR calculation, analyze patterns:**

**Common Discrepancies:**
- Construct X frequently miscoded as Construct Y → Clarify definitions
- Correlation pairs with MAE > .05 → Check for table misreading
- Specific studies with low agreement → Complex reporting format

**Action:**
- Document patterns in coding manual updates
- Flag problematic studies for full team review
- Adjust AI prompts based on patterns

---

## 12. Discrepancy Resolution

### 12.1 Priority Hierarchy

**Truth Source Prioritization:**

1. **Original Study Text** (highest priority)
   - If discrepancy exists, return to original study
   - Re-read relevant sections
   - Document exact quote/page number

2. **Human Coder Decision**
   - If two human coders agree, their consensus prevails over AI

3. **AI Consensus**
   - If 2+ AI models agree, consider their consensus (but verify against study)

4. **Expert Adjudication**
   - If no consensus (human-human or human-AI disagreement), escalate to lead investigator

---

### 12.2 Resolution Process

**Step 1: Identify Discrepancies**
- Compare AI-extracted data to human-coded ICR sample
- Flag discrepancies:
  - Construct mapping differs
  - Correlation value differs by > .05
  - Missing data in one but present in other

**Step 2: Return to Source**
- Pull up original study PDF
- Navigate to relevant table/section
- Re-extract data independently by senior coder

**Step 3: Document Resolution**
- `resolution_log.csv`:
  - study_id
  - variable (construct mapping, correlation pair, etc.)
  - ai_value
  - human_value
  - discrepancy_size
  - resolution (final value)
  - resolution_source (original_text, human_consensus, expert)
  - resolver_id
  - notes

**Step 4: Update Dataset**
- Replace discrepant value with resolved value
- Mark as "human_verified" in data provenance field

---

### 12.3 Escalation Protocol

**Level 1: Primary Coder Re-Review**
- Primary coder re-checks original study
- Updates if error found
- ~80% of discrepancies resolved here

**Level 2: Secondary Coder Independent Check**
- Secondary coder independently re-codes discrepant item
- If agrees with primary coder: Resolved
- If disagrees: Escalate to Level 3

**Level 3: Consensus Discussion**
- Primary and secondary coders discuss with evidence
- Review study together
- Attempt consensus
- ~15% of discrepancies resolved here

**Level 4: Expert Adjudication**
- Dissertation chair or committee member reviews
- Final decision
- ~5% of discrepancies resolved here
- Document rationale in resolution log

---

### 12.4 Acceptable Discrepancy Rates

**Targets:**
- Construct mapping: ≤10% disagreement rate after training
- Correlation extraction: ≤5% with MAE > .05
- Moderator coding: ≤5% disagreement rate

**Actions if exceeded:**
- >10% construct mapping discrepancies: Additional training, clarify manual
- >5% large correlation discrepancies: Check for systematic table misreading
- >5% moderator coding discrepancies: Clarify category definitions

---

### 12.5 Documentation Requirements

**For Each Resolved Discrepancy:**

**Required Fields:**
- study_id
- variable_name (e.g., "PE_BI_correlation", "AI_type", "construct_mapping_usefulness")
- original_value_source1 (AI or human coder 1)
- original_value_source2 (AI or human coder 2)
- final_value (resolved)
- resolution_method (return_to_text, consensus, expert)
- evidence (quote from study, page number)
- resolver (name/ID)
- date_resolved

**Example Entry:**

```csv
study_id,variable_name,ai_value,human_value,final_value,method,evidence,resolver,date
Smith2023,PE_BI_corr,0.52,0.58,0.58,return_to_text,"Table 3 page 12: r=.58**",coder_A,2026-03-15
Jones2024,construct_PU,PE,ATT,PE,consensus,"Items focus on productivity not liking",coder_B,2026-03-16
```

---

### 12.6 Post-Resolution Quality Check

**After all discrepancies resolved:**

1. **Re-run QA Gates (Phase 6):**
   - Range, symmetry, diagonal, completeness, sample size, duplicate checks
   - Should pass all gates

2. **Calculate Final Dataset Statistics:**
   - Total studies: k
   - Total correlations extracted: n_pairs
   - Average matrix completeness: %
   - % AI-extracted vs. human-verified

3. **Dataset Provenance Tagging:**
   - Each data point tagged with source:
     - `ai_consensus` (3 models agreed, no human verification)
     - `human_verified` (ICR sample or discrepancy resolution)
     - `expert_adjudicated` (required expert decision)

---

## 13. Summary and Checklist

### 13.1 Coding Completion Checklist

For each study, verify:

- [ ] Study ID assigned (AuthorYear format)
- [ ] Inclusion criteria confirmed (all criteria met)
- [ ] Correlation matrix extracted (or β-converted)
- [ ] At least 2 of 12 constructs coded
- [ ] Construct harmonization completed with confidence levels
- [ ] Reliability data extracted (α, CR, AVE if available)
- [ ] All moderators coded (AI type, industry, culture, year, context, development)
- [ ] Quality assessment completed (5 domains)
- [ ] Sample size recorded
- [ ] Data provenance tagged (AI vs. human)
- [ ] Notes documented for any ambiguities

---

### 13.2 Dataset Structure

**Final Dataset Files:**

1. **correlations.csv:** One row per correlation pair
   - study_id, construct1, construct2, r, r_source, n, pairwise_n

2. **studies.csv:** One row per study
   - study_id, authors, year, title, journal, n, ai_type, industry, culture_score, post_chatgpt, sample_context, development, quality_score

3. **reliability.csv:** One row per construct per study
   - study_id, construct, alpha, CR, AVE, num_items

4. **constructs.csv:** Construct harmonization mapping
   - study_id, original_construct_label, mapped_construct, confidence, items

5. **notes.csv:** Coding notes and edge cases
   - study_id, note_type, note_text, coder_id, date

---

### 13.3 Recommended Timeline

| Week | Activity | Deliverable |
|------|----------|-------------|
| 1 | Coder training, pilot | Trained coders, pilot ICR |
| 2-3 | AI-assisted coding (Phases 0-3) | AI-extracted dataset |
| 4 | Human ICR coding (20% sample) | Human-coded subsample |
| 5 | Calculate ICR, identify discrepancies | ICR metrics, discrepancy log |
| 6 | Discrepancy resolution | Resolved discrepancies |
| 7 | Remaining 80% human QA review | Spot-checked full dataset |
| 8 | Final QA, dataset assembly | Final validated dataset |

---

## References

Ajzen, I. (1991). The theory of planned behavior. *Organizational Behavior and Human Decision Processes*, 50(2), 179-211.

Bandura, A. (1986). *Social foundations of thought and action: A social cognitive theory*. Prentice-Hall.

Bhattacherjee, A. (2001). Understanding information systems continuance: An expectation-confirmation model. *MIS Quarterly*, 25(3), 351-370.

Cheung, M. W. L. (2015). *Meta-analysis: A structural equation modeling approach*. Wiley.

Compeau, D. R., & Higgins, C. A. (1995). Computer self-efficacy: Development of a measure and initial test. *MIS Quarterly*, 19(2), 189-211.

Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly*, 13(3), 319-340.

Fishbein, M., & Ajzen, I. (1975). *Belief, attitude, intention, and behavior: An introduction to theory and research*. Addison-Wesley.

Heinssen, R. K., Glass, C. R., & Knight, L. A. (1987). Assessing computer anxiety: Development and validation of the Computer Anxiety Rating Scale. *Computers in Human Behavior*, 3(1), 49-59.

Mayer, R. C., Davis, J. H., & Schoorman, F. D. (1995). An integrative model of organizational trust. *Academy of Management Review*, 20(3), 709-734.

Moore, G. C., & Benbasat, I. (1991). Development of an instrument to measure the perceptions of adopting an information technology innovation. *Information Systems Research*, 2(3), 192-222.

Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics-Part A: Systems and Humans*, 30(3), 286-297.

Peterson, R. A., & Brown, S. P. (2005). On the use of beta coefficients in meta-analysis. *Journal of Applied Psychology*, 90(1), 175-181.

Rogers, E. M. (2003). *Diffusion of innovations* (5th ed.). Free Press.

Sabherwal, R., Jeyaraj, A., & Chowa, C. (2006). Information system success: Individual and organizational determinants. *Management Science*, 52(12), 1849-1864.

Thompson, R. L., Higgins, C. A., & Howell, J. M. (1991). Personal computing: Toward a conceptual model of utilization. *MIS Quarterly*, 15(1), 125-143.

Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. *MIS Quarterly*, 27(3), 425-478.
