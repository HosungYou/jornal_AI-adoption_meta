# Three-Tier AI-Assisted Screening Protocol

## Overview

This document describes the accelerated screening methodology used for the systematic review of AI adoption in education. The protocol employs a three-tier approach combining keyword pre-filtering with dual-AI screening (Codex CLI + Gemini CLI) to process 16,189 deduplicated records.

**Rationale:** Naive sequential dual-AI screening of all 16,189 records would require ~147 hours. The tiered approach reduces this to ~2.5-3 hours by eliminating obviously irrelevant records before invoking expensive AI models.

---

## Tier Architecture

```
16,189 deduplicated records
        │
        ▼
┌─────────────────────────────┐
│  TIER 1: Keyword Pre-Filter │  ← Instant (0.2s for 12,915 records)
│  No AI/education terms      │
│  Auto-exclude as E2         │
└──────────┬──────────────────┘
           │ 3,170 records pass
           ▼
┌─────────────────────────────┐
│  TIER 2: Single AI (Gemini) │  ← AI terms + partial match
│  AI + (education OR adopt)  │     (education OR adoption, not both)
│  613 records                │
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│  TIER 3: Dual AI            │  ← AI + education + adoption terms
│  Codex + Gemini concurrent  │     (highest relevance probability)
│  2,557 records              │
└──────────┬──────────────────┘
           │
           ▼
    Human adjudication
    (all include + conflict)
```

### Distribution (from 16,085 remaining after pilot)

| Tier | Records | % | Method | API Calls | Est. Time |
|------|---------|---|--------|-----------|-----------|
| T1 auto-exclude | 12,915 | 80.3% | Keyword filter | 0 | <1s |
| T2 single AI | 613 | 3.8% | Gemini only | 613 | ~30 min |
| T3 dual AI | 2,557 | 15.9% | Codex + Gemini | 5,114 | ~2.5 hr |
| **Total** | **16,085** | **100%** | | **5,727** | **~3 hr** |

---

## Tier 1: Keyword Pre-Filter

### Logic

A record is auto-excluded (T1) if **any** of the following is true:
1. No AI-related terms appear in title + abstract + keywords
2. AI terms appear, but **neither** education terms **nor** adoption/acceptance terms appear

### Exclude Code Assignment

| Condition | Exclude Code | Rationale |
|-----------|-------------|-----------|
| No AI terms at all | E2 | AI not focal — no AI-related terminology detected |
| AI terms but no education AND no adoption | E2 + E3 | AI study but not in educational context and no adoption constructs |

### Keyword Patterns

#### AI Terms (30+ patterns)
```regex
artificial intelligence | machine learning | deep learning |
intelligent tutoring | chatbot | ChatGPT | GPT-4 | GPT-3 |
large language model | LLM | natural language processing | NLP |
automated grading | adaptive learning | conversational AI |
AI tutor | AI agent | agentic AI | neural network |
computer vision | generative AI | Copilot | Gemini | Claude | Bard |
reinforcement learning | intelligent agent | recommendation system |
predictive model | text mining | sentiment analysis |
speech recognition | virtual assistant | robot* | \bAI\b
```

#### Education Terms (25+ patterns)
```regex
education | student | teacher | instructor | faculty | professor |
university | college | school | classroom | pedagogy | learning |
academic | K-12 | higher education | undergraduate | graduate |
curriculum | MOOC | e-learning | online learning | blended learning |
tutoring | learner | teaching | coursework | semester
```

#### Adoption/Acceptance Terms (20+ patterns)
```regex
adopt* | acceptance | intention | TAM | UTAUT |
technology acceptance | perceived usefulness | perceived ease |
self-efficacy | behavioral intention | trust | resistance |
usage | satisfaction | continuance | willingness | readiness |
attitude | motivation | engagement | barrier
```

### Validation

Validated against 104-record pilot (real Codex + Gemini screening):

| Pilot Outcome | T1 (auto-exclude) | T2 (single AI) | T3 (dual AI) |
|---------------|-------------------|----------------|--------------|
| Include (8) | **0** | 0 | **8** |
| Exclude (91) | 77 | 8 | 6 |
| Conflict (5) | 1 | 2 | 2 |

**False negative rate: 0%** — No study that both AI models agreed to include was misclassified by the keyword filter.

**Note:** The 1 conflict record in T1 (REC_10933) was codex=exclude, gemini=uncertain, and would have been excluded regardless.

---

## Tier 2: Single AI Screening (Gemini CLI)

### Selection Criteria
Records with AI-related terms AND either education OR adoption terms (but not both).

### Rationale for Gemini Only
- Gemini CLI had **0 timeouts** in pilot (vs 3 for Codex)
- Gemini mean confidence: 0.97 (vs Codex 0.94)
- Faster response time (~15s vs ~20s for Codex)

### Output
- `screen_decision_gemini`: include / exclude / uncertain
- `screen_consensus`: equals Gemini's decision (single evaluator)
- `screening_tier`: "T2_single_ai"
- `screen_decision_codex`: "N/A" (not evaluated)

### Escalation Rule
If Gemini returns `include` or `uncertain`, the record should be flagged for human review.

---

## Tier 3: Dual AI Screening (Codex + Gemini)

### Selection Criteria
Records with AI-related terms AND education terms AND adoption/acceptance terms.

### Method
- Codex CLI and Gemini CLI run **concurrently** per record (asyncio.gather)
- Up to 8 records processed in parallel (asyncio.Semaphore)
- Each provider independently evaluates against the full MASEM eligibility criteria

### Consensus Rules
| Codex | Gemini | Consensus |
|-------|--------|-----------|
| include | include | **include** |
| exclude | exclude | **exclude** |
| Any other combination | | **conflict** → human adjudication |

### Screening Prompt Criteria (aligned with Coding Manual Section 2.2)
1. Empirical quantitative study with primary data
2. AI technology is focal (not general ICT/IT)
3. Educational setting/population
4. Adoption/acceptance/intention/use is measured
5. Correlation matrix or standardized beta/path data available
6. English language
7. Published 2015-2025
8. Sample size n >= 50
9. Peer-reviewed journal article or full conference paper

### Exclude Codes
| Code | Definition |
|------|-----------|
| E1 | Not empirical/quantitative |
| E2 | AI not focal |
| E3 | Not education context |
| E4 | No adoption/acceptance outcome |
| E5 | No effect size data |
| E6 | Not English |
| E7 | Outside 2015-2025 |
| E8 | n < 50 |
| E9 | Not peer-reviewed |
| E10 | Duplicate sample |
| E11 | Qualitative/review only |
| E12 | Other |

---

## Technical Implementation

### Scripts
| Script | Purpose |
|--------|---------|
| `ai_screening_tiered.py` | Main three-tier screening orchestrator |
| `ai_screening_parallel.py` | Parallel-only screening (no keyword filter) |
| `ai_screening.py` | Original sequential screening |

### CLI Versions
- Codex CLI: codex-cli 0.101.0 (OpenAI)
- Gemini CLI: 0.25.1 (Google)
- Authentication: OAuth for both providers

### Performance
| Metric | Value |
|--------|-------|
| T1 throughput | ~65,000 records/second |
| T2 throughput (8 workers) | ~10 records/minute |
| T3 throughput (8 workers) | ~6 records/minute |
| Total for 16,189 records | ~3 hours |

### Checkpointing
- Results saved every 50 records per tier
- Resume mode (`--resume`) skips already-processed record_ids
- Output CSV grows incrementally; safe to interrupt and restart

---

## PRISMA 2020 Reporting

Per PRISMA 2020 guidelines for AI-assisted screening:

### Method Section Language (template)

> Records were screened using a three-tier approach. Tier 1 applied keyword pre-filtering to auto-exclude records without AI-related terminology (n = 12,915; 80.3%). Tier 2 screened borderline records using a single AI model (Gemini CLI v0.25.1; n = 613; 3.8%). Tier 3 applied dual independent AI screening (Codex CLI v0.101.0 + Gemini CLI v0.25.1) to high-relevance records (n = 2,557; 15.9%). All include and conflict decisions were reviewed by two independent human coders, with disagreements resolved by the PI. The keyword pre-filter was validated against a 104-record pilot with 0% false negative rate.

---

## Pilot Results Summary (104 records)

| Metric | Value |
|--------|-------|
| Total screened | 104 |
| Codex-Gemini agreement | 95.2% (99/104) |
| Include (both agree) | 8 (7.7%) |
| Exclude (both agree) | 91 (87.5%) |
| Conflict | 5 (4.8%) |
| Codex mean confidence | 0.94 |
| Gemini mean confidence | 0.97 |
| Codex timeouts | 3 (reprocessed, all exclude) |
| Gemini timeouts | 0 |

---

## Limitations

1. **Keyword filter sensitivity:** While validated on 104 records with 0% false negatives, novel AI terms not in the pattern list could be missed. Mitigated by comprehensive term list (30+ AI patterns).

2. **T2 single evaluator:** Tier 2 uses only Gemini, lacking the inter-rater reliability of dual-AI. Mitigated by human review of all T2 include/uncertain decisions.

3. **Title/abstract only:** Screening is based on title, abstract, and keywords. Full-text review is required for all included records.

4. **Language detection:** The keyword filter does not explicitly check language; non-English papers with English abstracts may pass to T2/T3 but will be caught by AI screening (criterion 6) or full-text review.
