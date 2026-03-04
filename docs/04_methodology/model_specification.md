# Model Specification for Four Competing Models

## Overview

This document specifies the four competing structural models to be tested in the educational AI adoption meta-analysis. Each model represents a different theoretical perspective on AI adoption drivers in educational settings (students and instructors).

> **Version History:**
> - v1.0 (2026-02-16): Initial 3-model specification
> - v2.0 (2026-03-04): Added Model 4 (Trust Dual-Mechanism) based on conceptual framework discussion

---

## Model Summary

| Model | Name | Theoretical Basis | Key Constructs | Paths |
|-------|------|-------------------|----------------|-------|
| Model 1 | TAM/UTAUT Core | Traditional technology acceptance | PE, EE, SI, FC, ATT, BI, UB | 8 paths |
| Model 2 | Integrated Model | TAM/UTAUT + AI-specific | All 12 constructs | 14 paths |
| Model 3 | AI-Only Model | AI-specific drivers | TRU, ANX, TRA, AUT, SE, ATT, BI, UB | 7 paths |
| Model 4 | Trust Dual-Mechanism | Model 2 + Trust mediation via ATT/ANX | All 12 constructs | 16 paths |

---

## Model 1: TAM/UTAUT Core

### Theoretical Rationale

**Purpose:** Test whether traditional technology acceptance models (TAM and UTAUT) adequately explain AI adoption without AI-specific constructs.

**Hypothesis:** Traditional TAM/UTAUT paths will be significant and explain substantial variance in AI adoption, demonstrating that AI is "just another technology" that follows established acceptance patterns.

**Theoretical Foundations:**
- Technology Acceptance Model (Davis, 1989)
- Unified Theory of Acceptance and Use of Technology (Venkatesh et al., 2003)
- Theory of Reasoned Action (Fishbein & Ajzen, 1975)

---

### Structural Paths

**Model 1 includes 8 paths:**

1. **PE → BI** (β₁): Performance expectancy → Behavioral intention
2. **EE → BI** (β₂): Effort expectancy → Behavioral intention
3. **SI → BI** (β₃): Social influence → Behavioral intention
4. **FC → UB** (β₄): Facilitating conditions → Use behavior
5. **ATT → BI** (β₅): Attitude → Behavioral intention
6. **BI → UB** (β₆): Behavioral intention → Use behavior
7. **EE → ATT** (β₇): Effort expectancy → Attitude (TAM path)
8. **PE → ATT** (β₈): Performance expectancy → Attitude (TAM path)

---

### Path Justifications

**PE → BI (Core UTAUT path):**
- **Theory:** Performance expectancy (usefulness) is the strongest predictor of intention in UTAUT
- **Expected β:** .30-.40 (based on educational technology meta-analyses)
- **Educational AI Context:** Students/instructors adopt AI if they believe it improves learning outcomes or teaching effectiveness

**EE → BI (Core UTAUT path):**
- **Theory:** Effort expectancy (ease of use) drives intention, especially for new users
- **Expected β:** .20-.30 (education context)
- **Educational AI Context:** AI ease of use influences adoption for both students learning with AI and instructors integrating AI into pedagogy

**SI → BI (Core UTAUT path):**
- **Theory:** Social influence (subjective norm) affects intention, especially in educational contexts
- **Expected β:** .25-.35 (may be stronger in education due to peer learning culture)
- **Educational AI Context:** Peer encouragement (students) and colleague/administrator support (instructors) influences AI adoption

**FC → UB (Core UTAUT path):**
- **Theory:** Facilitating conditions directly affect behavior (not intention in UTAUT)
- **Expected β:** .15-.25
- **Educational AI Context:** Institutional AI infrastructure, technical support, and access to AI tools enable actual use

**ATT → BI (TAM path):**
- **Theory:** Attitude mediates the effect of beliefs on intention (TAM, TRA)
- **Expected β:** .40-.50 (may be stronger in education per Scherer et al., 2019)
- **Educational AI Context:** Positive attitudes toward AI for learning/teaching drive adoption intention

**BI → UB (Core TAM/UTAUT path):**
- **Theory:** Intention is the proximal predictor of behavior
- **Expected β:** .35-.45 (may be weaker in voluntary educational settings)
- **Educational AI Context:** Intention to use AI translates to actual AI usage in learning or teaching

**EE → ATT (TAM path):**
- **Theory:** Ease of use creates positive attitude
- **Expected β:** .40-.50
- **Educational AI Context:** Easy-to-use AI tools are perceived more positively by students and instructors

**PE → ATT (TAM path):**
- **Theory:** Usefulness creates positive attitude
- **Expected β:** .50-.60
- **Educational AI Context:** AI tools that improve learning outcomes or teaching effectiveness are evaluated positively

---

### Exogenous Correlations

**Model 1 allows correlations among exogenous variables:**
- PE ↔ EE
- PE ↔ SI
- PE ↔ FC
- EE ↔ SI
- EE ↔ FC
- SI ↔ FC

These correlations acknowledge that predictors are intercorrelated but do not imply causal relationships among them.

---

### Model 1 Path Diagram

```
         ┌──────┐
         │  PE  │────────────────┐
         └──┬───┘                │
            │                    ▼
            │                 ┌──────┐      ┌──────┐      ┌──────┐
            └────────────────►│ ATT  │─────►│  BI  │─────►│  UB  │
                              └──▲───┘      └──▲───┘      └──▲───┘
                                 │             │             │
         ┌──────┐                │             │             │
         │  EE  │────────────────┴─────────────┤             │
         └──────┘                               │             │
                                                │             │
         ┌──────┐                               │             │
         │  SI  │───────────────────────────────┘             │
         └──────┘                                             │
                                                              │
         ┌──────┐                                             │
         │  FC  │─────────────────────────────────────────────┘
         └──────┘

Legend:
→ = Structural path
Exogenous: PE, EE, SI, FC (correlated)
Endogenous: ATT, BI, UB
```

---

### Expected Model Fit

**Based on educational technology meta-analyses (Scherer et al., 2019):**
- CFI: .92-.96
- RMSEA: .045-.070
- SRMR: .050-.075

**R² Expectations (educational context may differ from organizational):**
- R²(ATT): .55-.65 (explained by PE, EE)
- R²(BI): .55-.65 (may be lower in voluntary educational settings)
- R²(UB): .30-.40 (may be lower due to less mandatory use)

---

## Model 2: Integrated Model (TAM/UTAUT + AI-Specific)

### Theoretical Rationale

**Purpose:** Test whether AI-specific constructs (trust, anxiety, transparency, autonomy) provide incremental explanatory power beyond traditional TAM/UTAUT in educational settings.

**Hypothesis:** Model 2 will fit significantly better than Model 1, demonstrating that educational AI adoption requires additional constructs beyond general technology acceptance.

**Theoretical Foundations:**
- All of Model 1 (TAM/UTAUT)
- Trust in automation (Mayer et al., 1995; Lee & See, 2004)
- Technology anxiety (Venkatesh, 2000)
- Explainable AI (XAI) literature
- Human-AI interaction and autonomy (Parasuraman et al., 2000)

---

### Structural Paths

**Model 2 includes all 8 paths from Model 1 PLUS 6 additional paths:**

**Original Paths (Model 1):**
1. PE → BI
2. EE → BI
3. SI → BI
4. FC → UB
5. ATT → BI
6. BI → UB
7. EE → ATT
8. PE → ATT

**Additional Paths (AI-Specific):**
9. **TRU → BI** (β₉): AI Trust → Behavioral intention
10. **ANX → BI** (β₁₀): AI Anxiety → Behavioral intention (negative path)
11. **TRA → TRU** (β₁₁): AI Transparency → AI Trust
12. **AUT → ANX** (β₁₂): Perceived AI Autonomy → AI Anxiety
13. **SE → EE** (β₁₃): Self-Efficacy → Effort Expectancy
14. **SE → ANX** (β₁₄): Self-Efficacy → AI Anxiety (negative path)

**Total: 14 paths**

---

### AI-Specific Path Justifications

**TRU → BI:**
- **Theory:** Trust is critical for technology adoption when vulnerability and uncertainty are high
- **Expected β:** .30-.40 (may be stronger in education due to academic integrity concerns)
- **Educational AI Context:** Trust in AI accuracy for educational content and grading is critical; students/instructors need confidence in AI outputs
- **Evidence:** Schoorman et al. (2007) automation trust meta-analysis

**ANX → BI (negative):**
- **Theory:** Anxiety inhibits adoption intention
- **Expected β:** -.20 to -.30 (may be stronger in education due to academic integrity anxiety)
- **Educational AI Context:** Anxiety about AI-enabled cheating, over-reliance, or academic dishonesty reduces adoption intention
- **Evidence:** Venkatesh (2000) anxiety effects in technology adoption

**TRA → TRU:**
- **Theory:** Transparency (explainability) builds trust by reducing uncertainty
- **Expected β:** .40-.50
- **Educational AI Context:** Explainable AI in grading, feedback, or content generation builds trust among students and instructors
- **Evidence:** XAI literature (Ribeiro et al., 2016)

**AUT → ANX:**
- **Theory:** High autonomy (AI making independent decisions) creates apprehension
- **Expected β:** .25-.35
- **Educational AI Context:** Autonomous AI systems (e.g., auto-grading, AI tutors making pedagogical decisions) evoke concerns about academic integrity and loss of educational control
- **Evidence:** Parasuraman et al. (2000) automation levels and user acceptance

**SE → EE:**
- **Theory:** Self-efficacy influences perceived ease of use
- **Expected β:** .35-.45
- **Educational AI Context:** Students/instructors confident in their digital/AI skills perceive educational AI tools as easier to use
- **Evidence:** Compeau & Higgins (1995) computer self-efficacy

**SE → ANX (negative):**
- **Theory:** Self-efficacy reduces anxiety
- **Expected β:** -.30 to -.40
- **Educational AI Context:** Students/instructors confident in their ability to use AI appropriately are less anxious about academic integrity concerns
- **Evidence:** Social cognitive theory (Bandura, 1986)

---

### Exogenous Correlations

**Model 2 allows correlations among all exogenous variables:**
- All Model 1 correlations (PE↔EE, PE↔SI, etc.)
- Plus: TRA↔AUT, TRA↔SE, AUT↔SE, etc.

**Key Theoretical Correlations:**
- **TRA ↔ PE:** Transparency may correlate with perceived usefulness (clear systems are valued)
- **AUT ↔ TRU:** Autonomy and trust may be negatively correlated (high autonomy reduces trust)
- **SE ↔ PE:** Self-efficacy correlates with perceived performance benefits

---

### Model 2 Path Diagram

```
         ┌──────┐
         │  TRA │──────────────┐
         └──────┘              │
                               ▼
         ┌──────┐           ┌──────┐
    ┌────│  SE  │──────────►│ TRU  │─────┐
    │    └──┬───┘           └──────┘     │
    │       │                             │
    │       │  ┌──────┐                  │
    │       ├─►│  EE  │───────┐          │
    │       │  └──────┘       │          │
    │       │                 ▼          ▼
    │       │              ┌──────┐  ┌──────┐  ┌──────┐
    │       │              │ ATT  │─►│  BI  │─►│  UB  │
    │       │              └──▲───┘  └──▲───┘  └──▲───┘
    │       │                 │         │         │
    │       │  ┌──────┐       │         │         │
    │       │  │  PE  │───────┴─────────┤         │
    │       │  └──────┘                 │         │
    │       │                           │         │
    │       │  ┌──────┐                 │         │
    │       │  │  SI  │─────────────────┘         │
    │       │  └──────┘                           │
    │       │                                     │
    │       │  ┌──────┐                           │
    │       │  │  FC  │───────────────────────────┘
    │       │  └──────┘
    │       │
    │       │  ┌──────┐
    │       └─►│ ANX  │─────────────────────────────────────┐
    │          └──▲───┘                                     │
    │             │                                         │
    │          ┌──────┐                                     │
    └──────────│ AUT  │─────────────────────────────────────┘
               └──────┘

Legend:
→ = Structural path (solid arrows show positive paths)
Negative paths: ANX→BI, SE→ANX
Exogenous: TRA, AUT, SE, PE, EE, SI, FC (all correlated)
Endogenous: TRU, ANX, EE (also endogenous in this model), ATT, BI, UB
```

---

### Expected Model Fit

**Better fit than Model 1:**
- CFI: .95-.98
- RMSEA: .035-.055
- SRMR: .040-.060

**R² Expectations:**
- R²(TRU): .25-.35 (explained by TRA)
- R²(ANX): .25-.35 (may be higher in education due to academic integrity concerns)
- R²(EE): .15-.25 (explained by SE)
- R²(ATT): .60-.70 (higher than Model 1 due to additional predictors)
- R²(BI): .65-.75 (higher than Model 1 due to TRU and ANX; educational context)
- R²(UB): .35-.45 (educational settings)

---

### Incremental Contribution Test

**Comparison to Model 1:**
- **Δχ²:** Expected significant improvement (p < .001)
- **ΔCFI:** Expected > .02 (meaningful improvement)
- **ΔRMSEA:** Expected < -.015 (meaningful improvement)
- **ΔR²(BI):** Expected .10-.15 increase (10-15 percentage points more variance explained)

**Academic Contribution:** Demonstrates that educational AI adoption requires constructs beyond traditional IT acceptance models, with particular emphasis on trust and academic integrity anxiety.

---

## Model 3: AI-Only Model

### Theoretical Rationale

**Purpose:** Test whether AI-specific constructs alone can explain educational AI adoption without traditional TAM/UTAUT constructs.

**Hypothesis:** Model 3 will fit worse than Model 2 but may fit comparably to Model 1, suggesting AI-specific constructs are sufficient in education (but integration is best).

**Theoretical Foundations:**
- Trust in AI and automation
- AI anxiety and perceived threat
- Explainable AI
- Human-AI interaction
- Self-efficacy (social cognitive theory)

---

### Structural Paths

**Model 3 includes 7 paths (no PE, EE, SI, FC):**

1. **TRU → BI** (β₁): AI Trust → Behavioral intention
2. **ANX → BI** (β₂): AI Anxiety → Behavioral intention (negative)
3. **TRA → TRU** (β₃): AI Transparency → AI Trust
4. **AUT → BI** (β₄): Perceived AI Autonomy → Behavioral intention
5. **SE → BI** (β₅): Self-Efficacy → Behavioral intention
6. **ATT → BI** (β₆): Attitude → Behavioral intention
7. **BI → UB** (β₇): Behavioral intention → Use behavior

**Note:** ATT and BI retained as they are central to all acceptance models; focus is on removing traditional IT predictors (PE, EE, SI, FC).

---

### Path Justifications

**TRU → BI:**
- Same as Model 2
- **Expected β:** .30-.40 (stronger than in Model 2 due to no PE competition)

**ANX → BI:**
- Same as Model 2
- **Expected β:** -.20 to -.30

**TRA → TRU:**
- Same as Model 2
- **Expected β:** .40-.50

**AUT → BI:**
- **Theory:** Autonomy has direct effect on intention (not just through anxiety)
- **Expected β:** .10-.20 (could be positive or negative; exploratory)
- **AI Context:** Some users value autonomy (efficiency), others fear it

**SE → BI:**
- **Theory:** Self-efficacy directly predicts intention when no "ease of use" construct
- **Expected β:** .25-.35
- **AI Context:** Users confident in AI skills intend to use AI

**ATT → BI:**
- Same as Models 1 and 2
- **Expected β:** .35-.45

**BI → UB:**
- Same as Models 1 and 2
- **Expected β:** .45-.55

---

### Exogenous Correlations

**Model 3 allows correlations among:**
- TRA ↔ AUT
- TRA ↔ SE
- AUT ↔ SE
- TRA ↔ ATT
- AUT ↔ ATT
- SE ↔ ATT

---

### Model 3 Path Diagram

```
         ┌──────┐
         │  TRA │──────────────┐
         └──────┘              │
                               ▼
                            ┌──────┐
                            │ TRU  │─────────┐
                            └──────┘         │
                                             │
         ┌──────┐                            │
         │  SE  │─────────────────┐          │
         └──────┘                 │          │
                                  │          │
         ┌──────┐                 │          │
         │ AUT  │─────────────────┤          │
         └──────┘                 │          │
                                  ▼          ▼
         ┌──────┐              ┌──────┐  ┌──────┐
         │ ANX  │─────────────►│  BI  │─►│  UB  │
         └──────┘              └──▲───┘  └──────┘
                                  │
         ┌──────┐                 │
         │ ATT  │─────────────────┘
         └──────┘

Legend:
→ = Structural path
Negative path: ANX→BI
Exogenous: TRA, AUT, SE, ANX, ATT (all correlated)
Endogenous: TRU, BI, UB
```

---

### Expected Model Fit

**Comparable or slightly worse than Model 1:**
- CFI: .91-.95
- RMSEA: .050-.075
- SRMR: .055-.080

**R² Expectations:**
- R²(TRU): .25-.35 (explained by TRA)
- R²(BI): .50-.60 (lower than Model 2, possibly similar to Model 1; educational context)
- R²(UB): .35-.45

**Interpretation:**
- If Model 3 ≈ Model 1 fit: AI-specific constructs are as important as traditional constructs
- If Model 3 < Model 1 fit: Traditional constructs still matter
- Model 2 should outperform both (integration is superior)

---

## Model 4: Trust Dual-Mechanism Model

### Theoretical Rationale

**Purpose:** Test whether Trust operates through dual mediating mechanisms (positive attitude formation and anxiety reduction) rather than only through a direct effect on behavioral intention.

**Hypothesis:** Model 4 will fit better than Model 2 by revealing that Trust's effect on BI is partially mediated through ATT (positive pathway = Reliance proxy) and ANX (negative pathway = Resistance proxy), yielding a more complete picture of Trust's role in educational AI adoption.

**Theoretical Foundations:**
- All of Model 2 (TAM/UTAUT + AI-specific)
- Trust dual-mechanism: Trust enables positive evaluation (Reliance) and reduces resistance (Mayer et al., 1995)
- Trust–attitude link: High trust fosters favorable attitudes (McKnight et al., 2002)
- Trust–anxiety link: Trust reduces perceived risk and anxiety (Lee & See, 2004)
- Conceptual framework: Trust in GenAI mediates between antecedents and BI through both Reliance (≈ATT) and Resistance (≈ANX) pathways

---

### Structural Paths

**Model 4 includes all 14 paths from Model 2 PLUS 2 additional paths:**

**Original Paths (Model 2):**
1. PE → BI
2. EE → BI
3. SI → BI
4. FC → UB
5. ATT → BI
6. BI → UB
7. EE → ATT
8. PE → ATT
9. TRU → BI
10. ANX → BI (negative)
11. TRA → TRU
12. AUT → ANX
13. SE → EE
14. SE → ANX (negative)

**Additional Paths (Trust Dual-Mechanism):**
15. **TRU → ATT** (β₁₅): AI Trust → Attitude (positive pathway)
16. **TRU → ANX** (β₁₆): AI Trust → AI Anxiety (negative path — trust reduces anxiety)

**Total: 16 paths**

---

### Trust Dual-Mechanism Path Justifications

**TRU → ATT (β₁₅, positive):**
- **Theory:** Trust enables positive evaluation — users who trust AI form more favorable attitudes toward it (Reliance proxy)
- **Expected β:** .20-.30
- **Educational AI Context:** Students/instructors who trust AI accuracy for grading, feedback, or content develop positive attitudes toward educational AI
- **Evidence:** McKnight et al. (2002) — trust as enabler of positive evaluation; Mayer et al. (1995) — trust facilitates willingness to be vulnerable (positive stance)

**TRU → ANX (β₁₆, negative):**
- **Theory:** Trust reduces perceived risk and associated anxiety — users who trust AI experience less apprehension (Resistance suppression proxy)
- **Expected β:** -.25 to -.35
- **Educational AI Context:** Students/instructors who trust AI accuracy are less anxious about academic integrity issues, AI errors, or over-reliance
- **Evidence:** Lee & See (2004) — trust reduces perceived risk in automation; Choung et al. (2023) — trust in AI inversely related to AI anxiety

---

### Trust's Three Pathways to BI (Total Effect Decomposition)

```
                    ┌─── ATT ──→ BI   (Positive pathway = Reliance proxy)
                    │   β₁₅ × β₅
                    │
Trust in AI (TRU) ──┼─── (direct) ──→ BI   (Direct effect)
                    │   β₉
                    │
                    └─── ANX ──→ BI   (Negative pathway = Resistance proxy)
                        β₁₆ × β₁₀

Total effect = β₉ + (β₁₅ × β₅) + (β₁₆ × β₁₀)
Expected:    ≈ .20 + (.25 × .35) + (-.30 × -.20) = .20 + .09 + .06 = .35
             ~43% of Trust's total effect is mediated through ATT and ANX
```

---

### Model 4 Path Diagram

```
         ┌──────┐
         │  TRA │──────────────┐
         └──────┘              │
                               ▼
         ┌──────┐           ┌──────┐
    ┌────│  SE  │──────────►│ TRU  │─────┐
    │    └──┬───┘           └──┬───┘     │
    │       │                  │  │      │
    │       │                  │  │      │
    │       │  ┌──────┐       │  │      │
    │       ├─►│  EE  │───────┤  │      │
    │       │  └──────┘       │  │      │
    │       │                 │  │      │
    │       │              ┌──▼──┐     │
    │       │              │ ATT │     │          ← TRU→ATT (NEW: β₁₅)
    │       │              └──┬──┘     │
    │       │                 │        │
    │       │  ┌──────┐       ▼        ▼
    │       │  │  PE  │───►┌──────┐  ┌──────┐  ┌──────┐
    │       │  └──────┘    │ ATT  │─►│  BI  │─►│  UB  │
    │       │              └──▲───┘  └──▲───┘  └──▲───┘
    │       │                 │         │         │
    │       │                 │         │         │
    │       │  ┌──────┐       │         │         │
    │       │  │  SI  │───────┘─────────┤         │
    │       │  └──────┘                 │         │
    │       │                           │         │
    │       │  ┌──────┐                 │         │
    │       │  │  FC  │─────────────────┘─────────┘
    │       │  └──────┘
    │       │
    │       │  ┌──────┐
    │       └─►│ ANX  │──────────────────────────┐
    │          └──▲───┘                          │
    │             │  ▲                           │
    │             │  │                           ▼
    │          ┌──┘──┘─┐                      (to BI)
    │          │ AUT   │
    │          └───────┘
    │             ▲
    └─────────────┘           ← TRU→ANX (NEW: β₁₆, negative)

Legend:
→ = Structural path (solid arrows)
NEW paths: TRU→ATT (β₁₅, positive), TRU→ANX (β₁₆, negative)
Negative paths: ANX→BI, SE→ANX, TRU→ANX
Exogenous: TRA, AUT, SE, PE, SI, FC (all correlated)
Endogenous: TRU, ANX, EE, ATT, BI, UB
```

---

### Exogenous Correlations

**Same as Model 2:** All pairwise correlations among PE, SI, FC, SE, TRA, AUT

---

### Expected Model Fit

**Better fit than Model 2 (if Trust dual-mechanism holds):**
- CFI: .96-.99
- RMSEA: .030-.050
- SRMR: .035-.055

**R² Expectations:**
- R²(TRU): .25-.35 (same as Model 2 — predicted by TRA only)
- R²(ANX): .35-.45 (higher than Model 2 due to TRU→ANX addition)
- R²(EE): .15-.25 (same as Model 2)
- R²(ATT): .65-.75 (higher than Model 2 due to TRU→ATT addition)
- R²(BI): .65-.75 (similar total, but with clearer mediation structure)
- R²(UB): .35-.45 (same as Model 2)

---

### Model 4 vs. Model 2 Comparison

**Key theoretical question:** Does Trust operate through ATT and ANX, or only directly on BI?

**Test:**
- If TRU→ATT and TRU→ANX are both significant: Trust dual-mechanism confirmed
- If only TRU→ATT significant: Trust operates through positive attitudes only
- If only TRU→ANX significant: Trust operates through anxiety reduction only
- If neither significant: Direct effect model (Model 2) sufficient

**Mediation test (bootstrap 95% CI):**
- Indirect 1: TRU → ATT → BI (expected: .09, CI should exclude 0)
- Indirect 2: TRU → ANX → BI (expected: .06, CI should exclude 0)
- Direct: TRU → BI (expected: .20, may reduce from Model 2's .30)

---

### Implementation Notes

```r
# Model 4: Trust Dual-Mechanism
model4 <- '
  # Traditional TAM/UTAUT paths (same as Model 2)
  BI ~ PE + EE + SI + ATT + TRU + ANX
  UB ~ FC + BI
  ATT ~ PE + EE + TRU          # ← NEW: TRU→ATT added

  # AI-specific paths
  TRU ~ TRA
  ANX ~ AUT + SE + TRU         # ← NEW: TRU→ANX added
  EE ~ SE

  # Covariances among exogenous
  PE ~~ SI + FC + SE + TRA + AUT
  SI ~~ FC + SE + TRA + AUT
  FC ~~ SE + TRA + AUT
  SE ~~ TRA + AUT
  TRA ~~ AUT
'

stage2_model4 <- tssem2(stage1, RAM = lavaan2RAM(model4))
summary(stage2_model4)

# Mediation test: Trust dual-mechanism
library(boot)
trust_indirect_att <- coef(stage2_model4)["TRU_ATT"] * coef(stage2_model4)["ATT_BI"]
trust_indirect_anx <- coef(stage2_model4)["TRU_ANX"] * coef(stage2_model4)["ANX_BI"]
trust_total <- coef(stage2_model4)["TRU_BI"] + trust_indirect_att + trust_indirect_anx
```

---

## Model Comparison Strategy

### Hypotheses

**H1:** Model 2 (Integrated) will fit significantly better than Model 1 (TAM/UTAUT Core)
- **Test:** Δχ², ΔCFI > .01, ΔRMSEA < -.015
- **Implication:** AI-specific constructs add explanatory power

**H2:** Model 2 (Integrated) will fit significantly better than Model 3 (AI-Only)
- **Test:** Δχ², ΔCFI > .01, ΔRMSEA < -.015
- **Implication:** Traditional constructs still matter for AI

**H3:** Model 1 vs. Model 3 will show comparable fit
- **Test:** |ΔCFI| < .01, |ΔRMSEA| < .01
- **Implication:** AI-specific and traditional constructs are similarly important

**H4:** Model 4 (Trust Dual-Mechanism) will fit better than Model 2 (Integrated)
- **Test:** Δχ², ΔAIC, ΔCFI
- **Implication:** Trust operates through dual mediating mechanisms (ATT and ANX), not just directly on BI

**H4a:** TRU → ATT → BI indirect effect is significant (bootstrap 95% CI excludes 0)
- **Implication:** Trust fosters positive attitudes toward AI (Reliance mechanism)

**H4b:** TRU → ANX → BI indirect effect is significant (bootstrap 95% CI excludes 0)
- **Implication:** Trust reduces AI anxiety (Resistance suppression mechanism)

---

### Comparison Metrics

| Metric | Criterion | Interpretation |
|--------|-----------|----------------|
| Δχ² | p < .05 | Better-fitting model (for nested models) |
| ΔCFI | > .01 | Meaningful difference |
| ΔRMSEA | > .015 | Meaningful difference |
| ΔSRMR | > .01 | Meaningful difference |
| ΔAIC | > 10 | Strong preference for lower AIC |
| ΔBIC | > 10 | Strong preference for lower BIC |

---

### Expected Results Table

| Model | χ² | df | CFI | RMSEA | SRMR | AIC | R²(BI) |
|-------|----|----|-----|-------|------|-----|--------|
| Model 1 | ~85 | 42 | .93 | .065 | .068 | 12,800 | .65 |
| Model 2 | ~52 | 38 | .97 | .042 | .045 | 12,700 | .75 |
| Model 3 | ~78 | 40 | .94 | .058 | .062 | 12,780 | .60 |
| Model 4 | ~45 | 36 | .98 | .035 | .040 | 12,680 | .75 |

**Expected Best Model:** Model 4 (lowest AIC, highest CFI, lowest RMSEA, reveals Trust mediation structure)

---

## Theoretical Implications

### If Model 1 Fits Best (Unlikely)

**Implication:** AI is "just another technology" — traditional TAM/UTAUT is sufficient

**Challenge:** Does not explain AI-specific concerns (trust, anxiety, transparency)

**Academic Contribution:** Limited (replicates existing knowledge)

---

### If Model 2 Fits Best (Expected)

**Implication:** AI adoption requires integration of traditional and AI-specific constructs

**Contribution:**
- Extends TAM/UTAUT for AI context
- Identifies unique AI drivers (trust, anxiety, transparency)
- Provides comprehensive framework for AI adoption

**Practical Implications:**
- Organizations should address both traditional barriers (usefulness, ease) AND AI-specific concerns (trust, explainability)
- Training should include both skill development (SE) and trust-building

---

### If Model 3 Fits Best (Unlikely but Interesting)

**Implication:** AI adoption is fundamentally different from traditional IT adoption

**Challenge:** Ignores decades of TAM/UTAUT evidence

**Interpretation:** AI-specific factors dominate, but integration (Model 2) likely still superior

---

### If Model 4 Fits Best (Expected if Trust Dual-Mechanism Holds)

**Implication:** Trust in AI operates through dual mediating mechanisms — positive attitude formation (Reliance) and anxiety reduction (Resistance suppression) — rather than only through a direct effect on intention.

**Contribution:**
- Reveals the internal mechanism of Trust's influence on AI adoption in education
- Connects to the broader Reliance/Resistance conceptual framework (which cannot be directly measured with current 12-construct set, but is approximated via ATT and ANX)
- Provides actionable design guidance: interventions that build trust should target both attitude improvement and anxiety reduction

**Practical Implications:**
- Design educational AI systems that are both trustworthy (transparent, accurate) and that actively reduce anxiety (explainable decisions, undo options)
- Training programs should leverage trust to simultaneously improve attitudes AND reduce anxiety
- Trust-building interventions may have stronger indirect effects than direct effects

**Future Direction:**
- Direct measurement of Reliance and Resistance constructs (beyond ATT/ANX proxies)
- Testing whether Self-directed Learning mediates BI → Use Behavior (as suggested by the conceptual framework)

---

## Implementation Notes

### Software: metaSEM (R)

**Model 1 Code Template:**

```r
# Define A matrix (regression paths)
A1 <- matrix(0, nrow=7, ncol=7,
             dimnames=list(c("PE","EE","SI","FC","ATT","BI","UB"),
                          c("PE","EE","SI","FC","ATT","BI","UB")))
A1["ATT", "PE"] <- "beta_PE_ATT"
A1["ATT", "EE"] <- "beta_EE_ATT"
A1["BI", "PE"] <- "beta_PE_BI"
A1["BI", "EE"] <- "beta_EE_BI"
A1["BI", "SI"] <- "beta_SI_BI"
A1["BI", "ATT"] <- "beta_ATT_BI"
A1["UB", "BI"] <- "beta_BI_UB"
A1["UB", "FC"] <- "beta_FC_UB"

# Define S matrix (variances, covariances)
# ... (variances for exogenous, residuals for endogenous, covariances among exogenous)

# Fit model
model1 <- tssem2(stage1, Amatrix=A1, Smatrix=S1)
summary(model1)
```

---

## References

Bandura, A. (1986). *Social foundations of thought and action: A social cognitive theory*. Prentice-Hall.

Compeau, D. R., & Higgins, C. A. (1995). Computer self-efficacy: Development of a measure and initial test. *MIS Quarterly*, 19(2), 189-211.

Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly*, 13(3), 319-340.

Fishbein, M., & Ajzen, I. (1975). *Belief, attitude, intention, and behavior: An introduction to theory and research*. Addison-Wesley.

Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors*, 46(1), 50-80.

Mayer, R. C., Davis, J. H., & Schoorman, F. D. (1995). An integrative model of organizational trust. *Academy of Management Review*, 20(3), 709-734.

Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics-Part A: Systems and Humans*, 30(3), 286-297.

Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). "Why should I trust you?" Explaining the predictions of any classifier. *Proceedings of the 22nd ACM SIGKDD*, 1135-1144.

Schoorman, F. D., Mayer, R. C., & Davis, J. H. (2007). An integrative model of organizational trust: Past, present, and future. *Academy of Management Review*, 32(2), 344-354.

Venkatesh, V. (2000). Determinants of perceived ease of use: Integrating control, intrinsic motivation, and emotion into the technology acceptance model. *Information Systems Research*, 11(4), 342-365.

Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. *MIS Quarterly*, 27(3), 425-478.

Choung, H., David, P., & Ross, A. (2023). Trust in AI and its role in the acceptance of AI technologies. *International Journal of Human-Computer Interaction*, 39(9), 1727-1739.

McKnight, D. H., Choudhury, V., & Kacmar, C. (2002). Developing and validating trust measures for e-commerce: An integrative typology. *Information Systems Research*, 13(3), 334-359.
