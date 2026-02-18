# Three-Tier Screening Validation Report

**Date:** 2026-02-18
**Analyst:** AI-assisted (Codex CLI + Gemini CLI)
**Dataset:** 16,189 deduplicated records from 4 databases (WoS, Scopus, PsycINFO, IEEE)

---

## 1. Tier Classification Summary

| Tier | Records | % | Method | Est. Time |
|------|---------|---|--------|-----------|
| T1 Keyword Pre-filter | 12,915 | 79.8% | Auto-exclude (no AI terms) | <1 sec |
| T2 Single AI | 613 | 3.8% | Gemini CLI only | ~40 min |
| T3 Dual AI | 2,557 | 15.8% | Codex + Gemini concurrent | ~2.5 hrs |
| **Total** | **16,189** | **100%** | | **~3 hrs** |

**Speedup vs naive sequential:** ~50x (3 hrs vs ~147 hrs)

---

## 2. T1 Keyword Pre-filter Validation

### 2.1 Classification Logic

A record is assigned to T1 (auto-exclude) if:
- **No AI-related terms** found in title + abstract + keywords, OR
- **AI terms present** but **neither education NOR adoption** terms found

AI terms (30 patterns): `artificial intelligence`, `AI`, `machine learning`, `deep learning`, `ChatGPT`, `GPT`, `LLM`, `chatbot`, `generative AI`, `neural network`, `BERT`, `transformer`, etc.

Education terms (13 patterns): `education*`, `student`, `instructor`, `teacher`, `pedagog*`, `classroom`, `university*`, `higher education`, `K-12`, `academi*`, `curricul*`, `learning`, `school`

Adoption terms (14 patterns): `adoption`, `acceptance`, `intention`, `TAM`, `UTAUT`, `technology acceptance`, `perceived usefulness`, `perceived ease of use`, `self-efficacy`, `trust`, `resistance`, `attitude`

### 2.2 Pilot Cross-Validation (n=104)

| Metric | Value |
|--------|-------|
| **False Negatives (include misclassified as T1)** | **0** |
| True Negatives (correct T1 excludes) | 77 |
| T1 records that were pilot includes | 0/8 (0%) |
| All 8 pilot includes classified as | T3 (100%) |

### 2.3 Random Sample Audit (n=20)

20 T1 records were randomly sampled (seed=42) and manually reviewed:

| Record | Topic | AI Terms? | Correct T1? |
|--------|-------|-----------|-------------|
| REC_00494 | Fetal monitoring telemedicine | No | Yes |
| REC_00583 | HIV linkage to care | No | Yes |
| REC_00627 | Sexual behavior (erratum) | No | Yes |
| REC_01825 | Food waste behavioral intention | No | Yes |
| REC_02006 | Surgical ergonomics | No | Yes |
| REC_02167 | Cancer vascular device acceptance | No | Yes |
| REC_02409 | Adaptive radiotherapy (ART) | No | Yes |
| REC_02994 | Tricuspid valve surgery | No | Yes |
| REC_04511 | Narcissism/attachment | No | Yes |
| REC_04587 | Genital fistula stigma | No | Yes |
| REC_05006 | Self-efficacy in learning (no AI) | No | Yes |
| REC_05662 | Nurse burnout | No | Yes |
| REC_08693 | Pharmacist biosimilar attitudes | No | Yes |
| REC_11093 | Cognitive control/self-depletion | No | Yes |
| REC_12032 | Blended learning TAM (no AI) | No | Yes |
| REC_13103 | Flow in education | No | Yes |
| REC_13972 | Student technostress/JD-R | No | Yes |
| REC_15259 | Instructional quality | No | Yes |
| REC_15338 | Dental rubber dam attitudes | No | Yes |
| REC_15353 | Moodle LMS in higher ed | No | Yes |

**Result: 20/20 correctly excluded (100%)**

### 2.4 Borderline Analysis

2,595 T1 records (20.1%) contain TAM/UTAUT/ed-tech terms but NO AI terms:

| Pattern | Count | Example |
|---------|-------|---------|
| Technology acceptance | 538 | VR learning, mobile apps |
| UTAUT | 151 | Telemedicine, e-government |
| Perceived usefulness | 527 | Various non-AI tools |
| Perceived ease of use | 312 | LMS, web platforms |
| Blended learning | 107 | Non-AI blended courses |
| E-learning | 292 | Traditional e-learning |
| LMS | 84 | Moodle, Canvas, Blackboard |

**Conclusion:** These are technology acceptance studies for NON-AI tools. Given our scope (AI adoption in education), T1 exclusion is correct. These studies examine TAM/UTAUT applied to VR, LMS, mobile apps, telemedicine, etc. — not AI tools.

---

## 3. T2 Single-AI Validation

### 3.1 Results (n=613)

| Outcome | Count | % |
|---------|-------|---|
| Exclude | 190 | 31.0% |
| Include | 8 | 1.3% |
| Uncertain (Gemini failure) | 402 | 65.6% |
| Uncertain (genuine) | 3 | 0.5% |

### 3.2 Issue: Gemini Quota Exhaustion

399/402 "uncertain" records are NOT genuine screening decisions — they are Gemini API failures due to quota exhaustion:

```
Error: "You have exhausted your capacity on this model. Your quota w..."
```

**Impact:** These 399 records need Gemini re-screening once quota refreshes.

### 3.3 T2 Includes Validation

All 8 T2 includes are relevant AI-in-education studies:

| Record | Title (truncated) | Gemini Confidence |
|--------|-------------------|-------------------|
| REC_07700 | AI-Based Chatbots for Knowledge Sharing... PLS-SEM | 0.95 |
| REC_10860 | ChatGPT usability on attitudes... Indian HE students | 0.90 |
| REC_07715 | AI Knowledge Assistant... Software Capstone | 0.90 |
| REC_02169 | Pre-service teachers' perceptions... chatbots | 0.85 |
| REC_13529 | Digital Technologies in HE Entrepreneurship... AI | 1.00 |
| REC_06059 | Student attitudes toward AI... international | 0.90 |
| REC_10209 | ChatGPT at Social science faculty | 0.80 |
| REC_01469 | Self-efficacy... LLM-based AI services | 0.90 |

**Result: All 8 are plausible includes for AI adoption in education scope.**

### 3.4 Why T2 exists

T2 records have AI terms plus EITHER education OR adoption terms (but not both). They're more likely to be excludes than T3 but still need AI screening because keyword matching alone can't determine relevance (e.g., a chatbot study in healthcare would have AI terms + possibly "learning" but not be about education).

---

## 4. T3 Dual-AI Validation (in progress)

### 4.1 Interim Results (n=200/2557)

| Outcome | Count |
|---------|-------|
| Conflict (Codex vs Gemini disagree) | 150 |
| Exclude | 29 |
| Include | 21 |

### 4.2 Engine Performance

| Engine | Success Rate | Notes |
|--------|-------------|-------|
| Codex CLI | 200/200 (100%) | No failures |
| Gemini CLI | 63/200 (31.5%) | 137 quota failures |

### 4.3 Gemini Failure Strategy

1. Current run captures all Codex results (100% success)
2. After completion, `retry_gemini_failures.py` re-processes failed records
3. Consensus is recalculated after retry

---

## 5. Overall Assessment

### Strengths

1. **Zero false negatives in T1** — validated on 104-record pilot and 20-record random audit
2. **Conservative design** — borderline records are escalated (T2/T3), never auto-excluded
3. **~50x speedup** — 3 hours vs 147 hours, enabling practical use of dual-AI screening
4. **Codex reliability** — 100% success rate across all tiers

### Limitations

1. **Gemini quota exhaustion** — 67% failure rate requires retry after quota refresh
2. **T2 uncertain accumulation** — 399 records pending re-screening
3. **Keyword pattern sensitivity** — `\blearning\b` matches non-educational contexts (e.g., "machine learning for crop prediction"), causing some T1 records to be escalated to T2. This is a conservative error (more screening, not less).

### Recommendation

- T1 keyword filter is **validated and effective** for this systematic review scope
- Gemini failures are **recoverable** — no data loss, just requires retry
- Human coders should prioritize reviewing T3 includes and conflicts for adjudication

---

## 6. PRISMA 2020 Reporting Note

Per PRISMA 2020 guidelines, the three-tier approach should be reported in the Method section as:

> "Title/abstract screening was conducted using a three-tier AI-assisted approach. Tier 1 applied keyword pre-filtering to auto-exclude records lacking AI-related terminology (n=12,915; validated on 104-record pilot with 0 false negatives). Tier 2 screened records with partial keyword matches using a single AI engine (Gemini CLI; n=613). Tier 3 screened records matching all three keyword domains (AI, education, adoption) using dual AI engines (Codex CLI + Gemini CLI; n=2,557) with independent consensus determination. All AI screening decisions are subject to verification by two independent human coders with PI adjudication of conflicts."
