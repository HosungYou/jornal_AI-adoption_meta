# Construct Harmonization Guide

## Overview

This document provides the complete framework for mapping diverse construct labels from primary studies onto the 12 standardized constructs used in this meta-analysis. Construct harmonization is critical for ensuring that we pool conceptually equivalent constructs while maintaining theoretical validity.

---

## 1. The 12 Standard Constructs

### 1.1 Complete Construct Table

| ID | Standard Name | Abbr | TAM Equivalent | UTAUT Equivalent | Key Education-Specific Variants |
|----|--------------|------|----------------|------------------|-------------------------|
| 1 | Performance Expectancy | PE | Perceived Usefulness (PU) | Performance Expectancy | Learning Effectiveness, Academic Performance Expectancy, AI Learning Value |
| 2 | Effort Expectancy | EE | Perceived Ease of Use (PEOU) | Effort Expectancy | AI Learning Ease, Educational AI Usability |
| 3 | Social Influence | SI | Subjective Norm | Social Influence | Peer Influence on AI Use in Learning, Instructor Encouragement |
| 4 | Facilitating Conditions | FC | — | Facilitating Conditions | Institutional AI Support, University AI Infrastructure |
| 5 | Behavioral Intention | BI | Intention to Use | Behavioral Intention | Intent to Use AI for Academic Work, AI Learning Intention |
| 6 | Use Behavior | UB | Actual System Use | Use Behavior | AI Usage for Learning/Teaching, Educational AI Use |
| 7 | Attitude | ATT | Attitude Toward Using | — | Attitude Toward AI in Education, Educational AI Sentiment |
| 8 | Self-Efficacy | SE | Computer Self-Efficacy | — | Academic AI Self-Efficacy, Digital Literacy Confidence |
| 9 | AI Trust | TRU | — | — | Trust in Educational AI, AI Assessment Trust |
| 10 | AI Anxiety | ANX | Computer Anxiety | — | AI Academic Integrity Anxiety, AI Plagiarism Fear |
| 11 | AI Transparency | TRA | — | — | AI Grading Transparency, Educational AI Explainability |
| 12 | Perceived AI Autonomy | AUT | — | — | AI Autonomy in Education, AI Decision-Making in Learning |

---

## 2. All 66 Pairwise Correlations

### 2.1 Complete List of Construct Pairs

For 12 constructs, there are **66 unique pairwise correlations**: C(12,2) = 12×11/2 = 66

**Traditional TAM/UTAUT Core (15 pairs):**
1. PE-EE
2. PE-SI
3. PE-FC
4. PE-BI
5. PE-UB
6. PE-ATT
7. EE-SI
8. EE-FC
9. EE-BI
10. EE-UB
11. EE-ATT
12. SI-FC
13. SI-BI
14. FC-BI
15. BI-UB

**Additional TAM/UTAUT Extensions (6 pairs):**
16. PE-SE
17. EE-SE
18. SI-ATT
19. SI-UB
20. FC-UB
21. ATT-BI

**AI-Specific Core (10 pairs):**
22. TRU-BI
23. TRU-UB
24. ANX-BI
25. ANX-UB
26. TRA-TRU
27. TRA-BI
28. AUT-ANX
29. AUT-BI
30. SE-ANX
31. SE-BI

**Cross-Domain Pairs (35 pairs):**
32. PE-SE
33. PE-TRU
34. PE-ANX
35. PE-TRA
36. PE-AUT
37. EE-SE (duplicate, see #17)
38. EE-TRU
39. EE-ANX
40. EE-TRA
41. EE-AUT
42. SI-SE
43. SI-TRU
44. SI-ANX
45. SI-TRA
46. SI-AUT
47. FC-SE
48. FC-TRU
49. FC-ANX
50. FC-TRA
51. FC-AUT
52. ATT-SE
53. ATT-TRU
54. ATT-ANX
55. ATT-TRA
56. ATT-AUT
57. SE-TRU
58. SE-TRA
59. SE-AUT
60. TRU-ANX
61. TRU-TRA
62. TRU-AUT
63. ANX-TRA
64. ANX-AUT
65. TRA-AUT
66. BI-SE (duplicate counting correction)

*(Corrected list: PE-SE appears as both 16 and 32; EE-SE as both 17 and 37; BI-SE needs to be added)*

**Corrected unique pairs = 66:**
- TAM/UTAUT family: 28 pairs (all combinations of PE, EE, SI, FC, BI, UB, ATT, SE)
- AI-specific family: 6 pairs (all combinations of TRU, ANX, TRA, AUT)
- Cross-domain: 32 pairs (traditional × AI-specific)

---

## 3. Detailed Mapping Rules by Construct

### 3.1 Performance Expectancy (PE) Mappings

**Exact Matches (Confidence: Exact):**
- Performance Expectancy
- PE (if study uses UTAUT)

**High-Confidence Mappings:**
- Perceived Usefulness (TAM)
- PU
- Usefulness
- Relative Advantage (Rogers, 2003)
- Job-Fit (Thompson et al., 1991)
- Outcome Expectations (Compeau & Higgins, 1995) — when performance-focused
- Productivity
- Performance Impact
- AI Usefulness
- AI Benefits
- AI Value — when instrumental (check items for "helps me perform" not "I value AI generally")

**Moderate-Confidence Mappings (Require Item Review):**
- Utility (check if performance-focused vs. general value)
- Effectiveness (check if task performance vs. system effectiveness)
- Output Quality (usually PE, but could be TRU if reliability-focused)
- Extrinsic Motivation (when work/performance context; exclude if hedonic context)
- Task-Technology Fit (when outcome-focused)

**Low-Confidence / Ambiguous:**
- "AI Value" without context → Could be PE (instrumental) or ATT (evaluative)
  - **Decision rule:** Check items. "Valuable for my work" → PE. "Valuable overall" → ATT
- "Benefit" alone → Too vague, check operational definition

**Do NOT Map to PE:**
- Enjoyment, Fun, Pleasure → ATT (hedonic attitude)
- Ease, Simplicity → EE
- "Usefulness of learning AI" → Context-dependent; often SE (capability building)

---

### 3.2 Effort Expectancy (EE) Mappings

**Exact Matches:**
- Effort Expectancy
- EE (if UTAUT)
- Perceived Ease of Use (TAM)
- PEOU

**High-Confidence Mappings:**
- Ease of Use
- User-Friendliness
- Ease of Learning
- Complexity (REVERSE-CODED)
- Simplicity
- Learnability
- AI Ease of Use
- Understandability — when usage-focused ("easy to understand how to use")

**Moderate-Confidence Mappings:**
- Usability (check definition: ease of use = EE; broader UX quality = ambiguous)
- Clarity (check if interaction clarity = EE; or explainability = TRA)
- Accessibility (physical/interface ease = EE; availability = FC)

**Low-Confidence / Ambiguous:**
- "Understandability" → EE if usage-focused; TRA if mechanism-focused
  - **Decision rule:** Items saying "easy to understand how to use" → EE. "Understand how AI works" → TRA
- "Difficulty" (reverse) → Usually EE, but check context

**Do NOT Map to EE:**
- "Understanding AI decisions" → TRA (explainability)
- "I can use AI" → SE (capability, not system ease)
- "Training available" → FC (resources)

---

### 3.3 Social Influence (SI) Mappings

**Exact Matches:**
- Social Influence
- SI (if UTAUT)
- Subjective Norm (TRA/TPB)

**High-Confidence Mappings:**
- Social Norm
- Social Factors (Thompson et al., 1991)
- Peer Influence
- Social Pressure
- Image (Moore & Benbasat, 1991)
- Normative Beliefs
- Referent Influence
- Colleague Influence
- Supervisor Encouragement (when normative, not resource provision)

**Moderate-Confidence Mappings:**
- Social Support (ambiguous: SI if encouragement; FC if resource provision)
  - **Decision rule:** Items about "others encourage me" → SI. "Others help me" → FC
- Organizational Culture (when normative climate; could overlap with FC)
- Peer Pressure

**Do NOT Map to SI:**
- Organizational support (resources) → FC
- Training by colleagues → FC (resource provision)
- Team collaboration → Distinct construct (not in our 12)

---

### 3.4 Facilitating Conditions (FC) Mappings

**Exact Matches:**
- Facilitating Conditions
- FC (if UTAUT)

**High-Confidence Mappings:**
- Perceived Behavioral Control (when resource-focused, not capability-focused)
- PBC (resource interpretation)
- Organizational Support
- Technical Support
- Resource Availability
- Compatibility (Rogers, 2003)
- Infrastructure
- IT Support
- Access to Resources
- Training Availability

**Moderate-Confidence Mappings:**
- Support (ambiguous: technical support = FC; social encouragement = SI)
- Organizational Readiness (when resource-focused; could overlap with cultural climate)
- Technology Infrastructure

**Ambiguous: FC vs. SE:**
- "I have the knowledge to use AI" → SE (internal capability)
- "I have access to knowledge/training" → FC (external resource)
- **Decision rule:** Internal capability = SE. External availability = FC

**Do NOT Map to FC:**
- Self-efficacy → SE
- Confidence → SE or TRU (depending on referent)
- Ease of use → EE

---

### 3.5 Behavioral Intention (BI) Mappings

**Exact Matches:**
- Behavioral Intention
- BI (if TAM/UTAUT)
- Intention to Use
- Adoption Intention

**High-Confidence Mappings:**
- Intent to Use
- Willingness to Use
- Intention to Adopt
- Continuance Intention (Bhattacherjee, 2001)
- Future Use Intention
- Intent to Recommend (when from user perspective)
- Planned Use
- Expected Use

**Moderate-Confidence Mappings:**
- Likelihood of Use (check if intention vs. expectation)
- Commitment to Use (when future-oriented)

**Do NOT Map to BI:**
- Current use, actual use → UB (behavior, not intention)
- Desire, want → Could be ATT (affective evaluation) unless explicitly future-oriented
- Interest → Often ATT unless clearly behavioral intent

---

### 3.6 Use Behavior (UB) Mappings

**Exact Matches:**
- Use Behavior
- UB (if UTAUT)
- Actual System Use
- Actual Use

**High-Confidence Mappings:**
- Usage
- System Usage
- Frequency of Use
- Usage Intensity
- Adoption Behavior
- AI Utilization
- Current Use
- Regular Use
- Continued Use (post-adoption)

**Moderate-Confidence Mappings:**
- Experience (when measured as usage history)
- Adoption (when measured as binary yes/no current use)
- Trial (borderline; include if intensity measured)

**Measurement Forms (all map to UB):**
- Binary: "Do you use AI?" (yes/no)
- Frequency: "How often?" (1=never to 5=daily)
- Duration: "Hours per week using AI"
- Breadth: "Number of AI features used"

**Do NOT Map to UB:**
- Intention to use → BI
- Awareness of AI → Not adoption (too early in process)

---

### 3.7 Attitude (ATT) Mappings

**Exact Matches:**
- Attitude
- ATT (if TAM)
- Attitude Toward Using
- Attitude Toward AI

**High-Confidence Mappings:**
- Affect (Thompson et al., 1991)
- Overall Evaluation
- Feelings Toward AI
- Liking
- Favorability
- Satisfaction (when pre-use or anticipatory; post-use satisfaction may be outcome)
- AI Sentiment

**Moderate-Confidence Mappings:**
- Preference (when evaluative, not behavioral choice)
- Acceptance (when attitudinal evaluation; not behavioral adoption)
- Hedonic Motivation (UTAUT2) — when AI-specific enjoyment
- Enjoyment (when overall evaluation, not specific performance benefit)

**Ambiguous: ATT vs. PE:**
- "AI is good" → ATT (evaluative)
- "AI is useful" → PE (instrumental)
- **Decision rule:** Evaluative = ATT. Instrumental/performance = PE

**Do NOT Map to ATT:**
- Specific beliefs (usefulness, ease) → PE, EE
- Intention → BI
- Anxiety, fear → ANX (specific negative affect)

---

### 3.8 Self-Efficacy (SE) Mappings

**Exact Matches:**
- Self-Efficacy
- SE (if using social cognitive theory)
- AI Self-Efficacy
- Computer Self-Efficacy (when AI context)

**High-Confidence Mappings:**
- Technology Self-Efficacy
- Digital Self-Efficacy
- Confidence in Using AI (when self-capability focused)
- Perceived Capability
- Self-Assessed Competence
- Skill Confidence

**Moderate-Confidence Mappings:**
- Capability Belief (check if self-belief vs. external enablers)
- Confidence (ambiguous: confidence in self = SE; confidence in AI = TRU)
  - **Decision rule:** "I am confident I can use AI" → SE. "I am confident AI will work well" → TRU

**Ambiguous: SE vs. FC:**
- "I have the knowledge to use AI" → SE (possessed knowledge)
- "I have access to knowledge resources" → FC (available resources)
- **Decision rule:** Internal = SE. External = FC

**Do NOT Map to SE:**
- Ease of use → EE (system attribute)
- Resources available → FC
- Past experience → Antecedent to SE, not SE itself (unless measured as capability)

---

### 3.9 AI Trust (TRU) Mappings

**Exact Matches:**
- Trust in AI
- AI Trust
- Algorithmic Trust
- Trust

**High-Confidence Mappings:**
- Automation Trust (when AI context)
- System Trust (when AI system)
- Machine Trust
- Perceived Reliability (competence dimension of trust)
- Perceived Competence (AI competence)
- Benevolence (affective trust dimension)
- Integrity (ethical trust dimension)
- Trustworthiness
- Dependability
- AI Reliability

**Moderate-Confidence Mappings:**
- Confidence in AI (TRU if vulnerability/dependence; SE if self-capability)
  - **Decision rule:** "Confident AI will perform well" → TRU. "Confident I can use AI" → SE
- Credibility (when AI-focused)
- Faith in AI (trust-related)
- Assurance (when AI dependability)

**Multi-Dimensional Trust:**
- If study measures trust with subscales (competence, benevolence, integrity):
  - **Use overall trust score** if available
  - **Average subscales** if only subscales reported
  - Document: "TRU computed as average of competence, benevolence, integrity subscales"

**Do NOT Map to TRU:**
- Transparency, explainability → TRA (antecedent to trust)
- Usefulness → PE
- "I trust myself to use AI" → SE

---

### 3.10 AI Anxiety (ANX) Mappings

**Exact Matches:**
- AI Anxiety
- Anxiety (when AI-specific)

**High-Confidence Mappings:**
- Technology Anxiety (when AI context)
- Computer Anxiety (when AI context)
- Fear of AI
- AI Apprehension
- AI Intimidation
- Technostress (when anxiety/fear dimension; not workload/invasion)
- Discomfort with AI (when affective, not attitudinal)
- Nervousness about AI

**Moderate-Confidence Mappings:**
- Perceived Threat (when affective fear component; not just cognitive threat)
  - **Decision rule:** Items like "AI makes me anxious" → ANX. "AI undermines my learning" → Cognitive threat (exclude unless affective component)
- Worry about AI (anxiety-related)
- AI Resistance (when affect-driven; could be reverse BI if behavioral)
- Academic Integrity Concerns (when emotionally-driven anxiety)

**Reverse-Coded:**
- Comfort with AI (reverse of ANX)
- Calmness about AI (reverse of ANX)
- **Flip sign** when coding correlations

**Ambiguous: ANX vs. ATT:**
- ANX = Specific fear/apprehension emotion
- ATT = General positive/negative evaluation
- A person can have positive ATT but moderate ANX (approach-avoidance)

**Do NOT Map to ANX:**
- General dislike → ATT (attitude, not anxiety)
- "AI is not useful for learning" → Reverse PE
- Perceived risk (cognitive) → Distinct construct unless affective component
- Academic dishonesty policy concerns (policy, not emotion) → Unless anxiety component present

---

### 3.11 AI Transparency (TRA) Mappings

**Exact Matches:**
- Transparency
- AI Transparency
- Explainability
- Interpretability
- Algorithmic Transparency

**High-Confidence Mappings:**
- Understandability (when mechanism-focused: "I understand how AI works")
- Clarity (when AI process clarity)
- Explainable AI (XAI)
- Black Box Perception (REVERSE-CODED)
- Opacity (REVERSE-CODED)
- Process Transparency
- Decision Transparency
- AI Grading Transparency
- Educational AI Explainability

**Moderate-Confidence Mappings:**
- Understanding (ambiguous: TRA if "understand AI process"; EE if "understand how to use")
  - **Decision rule:** "Understand how AI makes decisions" → TRA. "Understand how to use AI" → EE
- Comprehensibility (process understanding = TRA; usage understanding = EE)
- Visibility (AI process visibility = TRA; general awareness = other)

**Reverse-Coded:**
- Black Box Perception → TRA (reverse)
- Opacity → TRA (reverse)
- Inscrutability → TRA (reverse)

**Ambiguous: TRA vs. EE:**
- TRA = Understanding AI's internal process/reasoning
- EE = Ease of using/interacting with AI
- **Decision rule:** Check items for "how it works" (TRA) vs. "how to use it" (EE)

**Do NOT Map to TRA:**
- Ease of use → EE
- Trust → TRU (transparency is antecedent to trust)
- Information quality → Distinct construct

---

### 3.12 Perceived AI Autonomy (AUT) Mappings

**Exact Matches:**
- AI Autonomy
- Perceived AI Autonomy
- Automation Level (when perceived, not objective)

**High-Confidence Mappings:**
- Machine Autonomy
- AI Agency
- AI Independence
- Autonomous Decision-Making (AI's, not user's)
- Automation Degree (perceived)
- Level of Automation (Parasuraman et al., 2000 scale — when subjective perception)
- AI Self-Direction

**Moderate-Confidence Mappings:**
- Control (when referring to AI's control, not user's control)
  - **Decision rule:** "AI controls decisions" → AUT. "I control AI" → Reverse AUT or user agency (distinct)
- Agency (AI agency = AUT; user agency = distinct)

**Ambiguous: AUT vs. Other Constructs:**
- "AI makes decisions independently" → AUT
- "AI is intelligent" → General capability (not autonomy specifically)
- "AI requires little intervention" → AUT (low human involvement = high autonomy)

**Do NOT Map to AUT:**
- User control → Distinct (user agency, not AI autonomy)
- AI capability/intelligence → General attribute (not autonomy)
- Automation as job threat → ANX (if affective) or perceived threat (distinct)

---

## 4. Confidence Levels and Decision Tree

### 4.1 Confidence Level Definitions

**Exact (100%):**
- Study uses identical construct name and definition from our framework
- Example: Study uses "Performance Expectancy" and cites Venkatesh et al. (2003) UTAUT

**High (90-95%):**
- Study uses well-established synonym with clear conceptual match
- Example: "Perceived Usefulness" → PE (TAM equivalent)
- Example: "Subjective Norm" → SI (TRA/TPB equivalent)

**Moderate (70-85%):**
- Requires interpretation based on items or definition
- Some ambiguity, but reasonable conceptual alignment
- Example: "AI Value" → PE (if items focus on task performance)

**Low (<70%):**
- Significant ambiguity or partial overlap
- May require expert review or exclusion
- Example: "AI Perception" (too vague, could be ATT, PE, or TRU depending on items)

---

### 4.2 Decision Tree Application

**For each construct in a study:**

```
START
  ↓
Does study use exact same label as one of our 12?
  ├─ YES → Confidence = Exact, map directly
  └─ NO → Continue
       ↓
Is it a TAM/UTAUT/TRA/TPB construct with known mapping?
  ├─ YES → Use cross-reference table (Section 5.3 in coding manual)
       │    → Confidence = High
  └─ NO → Continue
       ↓
Check construct definition in study
  ├─ Aligns clearly with one of our 12 → Confidence = High
  └─ Partially aligns or ambiguous → Continue
       ↓
Review scale items (if available)
  ├─ Items clearly operationalize one construct → Confidence = Moderate
  └─ Items mix constructs or unclear → Continue
       ↓
Expert review
  ├─ Can reasonably map → Confidence = Low (flag for sensitivity)
  └─ Cannot map → EXCLUDE from coding
```

---

### 4.3 When to Exclude vs. Code with Low Confidence

**EXCLUDE if:**
- Construct mixes multiple of our 12 (e.g., "Ease and Usefulness" combined)
- Construct is outside our 12 and not mappable (e.g., "Price Value," "Habit")
- Definition/items are too vague to judge ("AI Perception")

**CODE with Low Confidence if:**
- Reasonable conceptual alignment but ambiguous operationalization
- **Always flag for sensitivity analysis:** Compare results with/without low-confidence mappings

---

## 5. Examples of Complex Harmonization Decisions

### Example 1: "AI Trust and Confidence in Education"

**Study construct:** "AI Trust and Confidence" (single composite measure)

**Issue:** Mixes TRU (trust in AI) and potentially SE (confidence in using AI)

**Resolution:**
- **Check items:** If items are "I trust AI for learning" + "I am confident AI will provide accurate educational content" → TRU (both trust-focused)
- If items are "I trust AI" + "I am confident I can use AI for coursework" → MIXED construct, exclude
- **Decision:** Review items carefully. If 80%+ of items are trust-focused, code as TRU with note

---

### Example 2: "Perceived Control"

**Study construct:** "Perceived Control" over AI

**Issue:** Could be user control (reverse AUT), PBC (FC), or self-efficacy (SE)

**Resolution:**
- **Check items:**
  - "I control what AI does" → User agency (not in our 12, or reverse AUT)
  - "I have control over resources to use AI" → FC (PBC variant)
  - "I feel in control when using AI" → SE (capability/mastery feeling)
- **Decision:** Depends entirely on items. Most likely FC (PBC interpretation) or exclude.

---

### Example 3: "AI Literacy in Education"

**Study construct:** "AI Literacy"

**Issue:** Could be knowledge (antecedent), SE (capability), or understanding (TRA)

**Resolution:**
- **Check items:**
  - "I understand AI concepts" → Knowledge (antecedent, not in our 12)
  - "I am capable of learning AI tools for my coursework" → SE (self-efficacy for learning)
  - "I understand how AI systems make educational decisions" → TRA (transparency understanding)
- **Decision:** Most likely SE if capability-focused, TRA if understanding-focused. If knowledge-only, exclude.

---

### Example 4: "AI Comfort in Learning"

**Study construct:** "Comfort with AI"

**Issue:** Could be reverse ANX or ATT

**Resolution:**
- **Check items:**
  - "I feel comfortable using AI for academic work" (no fear) → Reverse ANX
  - "I like using AI for learning" (positive evaluation) → ATT
- **Decision:** If affective comfort (not anxious), code as ANX (reverse). If evaluative (like/dislike), code as ATT.

---

## 6. Harmonization Workflow

### Step 1: Identify All Constructs in Study

List all constructs measured by the study (from measurement model, tables, or text).

**Example (Study X):**
- Perceived Usefulness
- Ease of Use
- Social Norm
- Intention to Use
- AI Trust

---

### Step 2: Map Each to Our 12

| Study Construct | Maps To | Confidence | Rationale |
|----------------|---------|------------|-----------|
| Perceived Usefulness | PE | High | TAM equivalent of PE |
| Ease of Use | EE | High | PEOU variant |
| Social Norm | SI | High | Subjective norm (TRA) |
| Intention to Use | BI | High | Behavioral intention |
| AI Trust | TRU | Exact | Direct match |

---

### Step 3: Document Unmappable Constructs

**Example (Study Y):**
- Perceived Usefulness → PE ✓
- Habit → NOT IN OUR 12, exclude
- Price Value → NOT IN OUR 12, exclude

**Note:** Study Y contributes PE correlations with other constructs, but Habit and Price Value are not coded.

---

### Step 4: Flag Low-Confidence Mappings

**Example (Study Z):**
- "AI Capability" → Mapped to PE (moderate confidence)
  - **Items:** "AI can perform complex tasks" (performance-focused)
  - **Flag:** `confidence = moderate`, `note = "AI Capability mapped to PE based on performance focus"`

---

## 7. Quality Control for Harmonization

### 7.1 Inter-Coder Agreement on Mappings

**Procedure:**
- Two coders independently map constructs for 20% sample
- Calculate Cohen's κ for construct mappings
- **Target:** κ ≥ .85

**Disagreements:**
- Discuss and resolve using decision tree
- Update harmonization rules if patterns emerge

---

### 7.2 Sensitivity Analysis for Ambiguous Mappings

**Track mapping confidence in dataset:**

```csv
study_id,original_construct,mapped_construct,confidence,notes
Smith2023,Perceived Usefulness,PE,high,TAM construct
Jones2024,AI Value,PE,moderate,Items focus on task performance
Brown2025,AI Perception,ATT,low,Vague; items suggest evaluative attitude
```

**Sensitivity Analysis:**
- Run MASEM with all mappings (including low-confidence)
- Re-run excluding low-confidence mappings
- Compare results: If conclusions unchanged, mappings are robust

---

## 8. Reference Mapping Tables

### 8.1 TAM Constructs → Our 12

| TAM Construct | Our Construct | Notes |
|--------------|---------------|-------|
| Perceived Usefulness (PU) | PE | Direct mapping |
| Perceived Ease of Use (PEOU) | EE | Direct mapping |
| Attitude Toward Using | ATT | Direct mapping |
| Behavioral Intention | BI | Direct mapping |
| Actual System Use | UB | Direct mapping |

---

### 8.2 UTAUT Constructs → Our 12

| UTAUT Construct | Our Construct | Notes |
|----------------|---------------|-------|
| Performance Expectancy (PE) | PE | Same name |
| Effort Expectancy (EE) | EE | Same name |
| Social Influence (SI) | SI | Same name |
| Facilitating Conditions (FC) | FC | Same name |
| Behavioral Intention (BI) | BI | Same name |
| Use Behavior (UB) | UB | Same name |

---

### 8.3 UTAUT2 Additional Constructs → Our 12

| UTAUT2 Construct | Our Construct | Notes |
|-----------------|---------------|-------|
| Hedonic Motivation | ATT | If AI-specific enjoyment; exclude if general entertainment |
| Price Value | — | NOT in our 12; exclude |
| Habit | — | NOT in our 12; exclude |

---

### 8.4 Theory of Planned Behavior (TPB) → Our 12

| TPB Construct | Our Construct | Notes |
|--------------|---------------|-------|
| Attitude | ATT | Direct mapping |
| Subjective Norm | SI | Normative influence |
| Perceived Behavioral Control | FC or SE | FC if resource-focused; SE if capability-focused |
| Intention | BI | Direct mapping |
| Behavior | UB | Direct mapping |

---

### 8.5 Social Cognitive Theory (SCT) → Our 12

| SCT Construct | Our Construct | Notes |
|--------------|---------------|-------|
| Self-Efficacy | SE | Direct mapping |
| Outcome Expectations | PE | Performance expectations |
| Affect | ATT | Emotional evaluation |
| Anxiety | ANX | When technology-specific |

---

### 8.6 Innovation Diffusion Theory (IDT/Rogers) → Our 12

| IDT Construct | Our Construct | Notes |
|--------------|---------------|-------|
| Relative Advantage | PE | Performance benefit |
| Complexity | EE (reverse) | Reverse-coded ease |
| Compatibility | FC | System/institutional fit |
| Trialability | — | NOT in our 12; exclude |
| Observability | — | NOT in our 12; exclude |

---

## 9. Summary Checklist for Harmonization

For each study, verify:

- [ ] All measured constructs identified
- [ ] Each construct mapped to our 12 (or marked as unmappable)
- [ ] Confidence level assigned (exact/high/moderate/low)
- [ ] Ambiguous cases reviewed using decision tree
- [ ] Items checked if confidence < high
- [ ] Reverse-coding noted (e.g., Complexity → EE reverse)
- [ ] Multi-dimensional constructs handled (overall score or average subscales)
- [ ] Unmappable constructs documented (excluded from coding)
- [ ] Low-confidence mappings flagged for sensitivity analysis
- [ ] Mapping rationale documented in notes

---

## References

Ajzen, I. (1991). The theory of planned behavior. *Organizational Behavior and Human Decision Processes*, 50(2), 179-211.

Bandura, A. (1986). *Social foundations of thought and action: A social cognitive theory*. Prentice-Hall.

Bhattacherjee, A. (2001). Understanding information systems continuance: An expectation-confirmation model. *MIS Quarterly*, 25(3), 351-370.

Compeau, D. R., & Higgins, C. A. (1995). Computer self-efficacy: Development of a measure and initial test. *MIS Quarterly*, 19(2), 189-211.

Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly*, 13(3), 319-340.

Moore, G. C., & Benbasat, I. (1991). Development of an instrument to measure the perceptions of adopting an information technology innovation. *Information Systems Research*, 2(3), 192-222.

Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics-Part A: Systems and Humans*, 30(3), 286-297.

Rogers, E. M. (2003). *Diffusion of innovations* (5th ed.). Free Press.

Thompson, R. L., Higgins, C. A., & Howell, J. M. (1991). Personal computing: Toward a conceptual model of utilization. *MIS Quarterly*, 15(1), 125-143.

Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. *MIS Quarterly*, 27(3), 425-478.

Venkatesh, V., Thong, J. Y., & Xu, X. (2012). Consumer acceptance and use of information technology: Extending the unified theory of acceptance and use of technology. *MIS Quarterly*, 36(1), 157-178.
