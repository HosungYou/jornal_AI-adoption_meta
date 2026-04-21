# Construct Identification: Inductive Derivation from the 224-Study Corpus

## Subsection Draft (Target: ~600 words)

---

### 2.X Construct Identification

A defining methodological commitment of this study was that construct selection would be driven by what primary researchers *actually measured*, not by what any single theoretical framework prescribes. Most MASEM studies in the technology adoption literature begin from a nominated theoretical model (typically TAM or UTAUT) and extract only the constructs that model specifies, then test whether those constructs replicate at the meta-analytic level. This approach privileges theoretical coherence over empirical coverage and carries a well-documented risk: constructs that appear prominently in primary research but fall outside the nominated framework are systematically excluded, producing a confirmatory artifact rather than a synthesis of the literature's actual structure.

To avoid this, we conducted a systematic full-text analysis of all 224 included PDFs prior to any construct selection decision. Each study was coded for (a) the theoretical frameworks cited, (b) every latent construct operationalized with validated items, (c) the construct label and its source theory, and (d) whether the construct was presented as a predictor, mediator, or outcome within the study's structural model. This coding was performed using a three-model AI-consensus protocol (Claude, GPT-4o, Llama-3) with 20% human inter-coder reliability verification (kappa >= .85), ensuring that the resulting construct frequency map reflects the actual measurement practices of the field rather than researcher-imposed categories.

The theoretical landscape of the corpus was heterogeneous. TAM was present in 194 studies (86.6%), UTAUT in 143 (63.8%), TPB in 111 (49.6%), IDT in 47 (21.0%), SCT in 37 (16.5%), TTF in 19 (8.5%), and ECM and VAM in 12 and 14 studies respectively. This pluralism immediately signals that no single framework is adequate as an a priori scaffolding: 13.4% of the corpus does not use TAM at all, and 36.2% does not use UTAUT, meaning that constructs unique to either framework would be absent from a meaningful proportion of studies.

From this mapping, a natural two-tier frequency structure emerged. Tier 1 comprises constructs appearing in 20% or more of the 224 studies: Performance Expectancy (PE, k = 186, 83.0%), Behavioral Intention (BI, k = 185, 82.6%), Effort Expectancy (EE, k = 162, 72.3%), Social Influence (SI, k = 114, 50.9%), Facilitating Conditions (FC, k = 105, 46.9%), Use Behavior (UB, k = 90, 40.2%), Attitude (ATT, k = 81, 36.2%), and Self-Efficacy (SE, k = 44, 19.6%). These eight constructs satisfy what we term the *universal coverage threshold*: they appear with sufficient frequency across sufficiently diverse theoretical contexts to yield stable Stage 1 correlation pooling.

Tier 2 comprises constructs appearing in 15–20% of studies that carry explicit theoretical significance for the AI adoption context specifically: Anxiety (ANX, k = 40, 17.9%) and Trust (TRU, k = 36, 16.1%). Although both fall just below the Tier 1 threshold, they are theoretically non-redundant with any Tier 1 construct and represent the two most consistently measured AI-specific psychological barriers in the corpus. Exclusion of ANX and TRU would constitute a systematic suppression of the literature's AI-specific signal. They were therefore retained, yielding a final 10-construct model.

Below this threshold, construct coverage became too sparse for reliable MASEM estimation. Transparency (TRA, k approximately 2) and Autonomy (AUT, k approximately 0) appeared in too few studies to produce stable pooled correlations. Three additional constructs, Hedonic Motivation (HM), Habit (HAB), and Price Value (PV), exceeded minimum frequency counts but were excluded on methodological grounds. HM and HAB showed pronounced structural inconsistency across studies: some treated them as antecedents to BI, others as antecedents to UB, and others as concurrent predictors, producing a construct equivalence problem incompatible with MASEM pooling. PV was almost exclusively measured in commercial AI tool contexts and showed near-zero variance in the higher-education subsample, making it non-informative for this population.

The result is a 10-construct model grounded entirely in observed measurement practice across 224 studies, spanning five theoretical frameworks, and partitioned into universal adoption factors (Tier 1) and AI-specific psychological factors (Tier 2). This derivation sequence, from full-text frequency mapping to tiered inclusion criteria to methodological exclusion review, is represented in Table X and constitutes a novel contribution to MASEM methodology in the educational technology literature.

---

## Table X. Construct Identification: Frequency, Theoretical Origin, AI-Specificity, and Inclusion Decision

| Construct | Abbr. | k (%) | Primary Theory | AI-Specific? | Tier | Decision |
|-----------|-------|--------|----------------|--------------|------|----------|
| Performance Expectancy | PE | 186 (83.0%) | TAM / UTAUT | No (universal) | 1 | Included |
| Behavioral Intention | BI | 185 (82.6%) | TAM / UTAUT / TPB | No (universal) | 1 | Included |
| Effort Expectancy | EE | 162 (72.3%) | TAM / UTAUT | No (universal) | 1 | Included |
| Social Influence | SI | 114 (50.9%) | UTAUT / TPB | No (universal) | 1 | Included |
| Facilitating Conditions | FC | 105 (46.9%) | UTAUT | No (universal) | 1 | Included |
| Use Behavior | UB | 90 (40.2%) | TAM / UTAUT | No (universal) | 1 | Included |
| Attitude | ATT | 81 (36.2%) | TAM / TPB | No (universal) | 1 | Included |
| Self-Efficacy | SE | 44 (19.6%) | SCT | Partial (amplified in AI) | 1 | Included |
| Anxiety | ANX | 40 (17.9%) | SCT / TAM-extensions | Yes (AI-salient) | 2 | Included |
| Trust | TRU | 36 (16.1%) | Trust theory / AI ethics | Yes (AI-specific) | 2 | Included |
| Hedonic Motivation | HM | -- | UTAUT2 | No | -- | Excluded: structural inconsistency |
| Habit | HAB | -- | UTAUT2 | No | -- | Excluded: structural inconsistency |
| Price Value | PV | -- | UTAUT2 | No | -- | Excluded: near-zero variance in HE |
| Transparency | TRA | ~2 (<1%) | XAI / AI ethics | Yes | -- | Excluded: k insufficient |
| Autonomy | AUT | ~0 (<1%) | SDT | Yes | -- | Excluded: k insufficient |

*Note.* k = number of included studies operationalizing the construct. Percentage is of N = 224 PDFs analyzed. TAM = Technology Acceptance Model; UTAUT = Unified Theory of Acceptance and Use of Technology; TPB = Theory of Planned Behavior; SCT = Social Cognitive Theory; SDT = Self-Determination Theory; XAI = Explainable AI literature. "AI-specific" indicates the construct was predominantly introduced to the adoption literature in the AI/intelligent systems context rather than general IT adoption.*

---

## Notes for Integration

- This section goes in Methods, after the search/screening section and before the data extraction/coding section.
- The table number (Table X) should be updated to match final manuscript numbering.
- Cross-reference to the PRISMA flow diagram where the 224 PDF analysis is described.
- The phrase "universal coverage threshold" can be defined in a footnote if the journal prefers.
- Word count of narrative only: approximately 620 words (within target).

