# AI-Assisted Coding Pipeline

## Overview

This document describes the 7-phase AI-assisted coding pipeline for extracting correlation matrices and study metadata from included studies on AI adoption in educational contexts. The pipeline combines automated AI extraction with human validation to achieve high accuracy while reducing manual coding burden.

---

## Pipeline Architecture

### 7-Phase Pipeline Overview

```
Phase 0: RAG Index Building
   ↓
Phase 1: Correlation Extraction (AI)
   ↓
Phase 2: Construct Mapping (AI)
   ↓
Phase 3: 3-Model Consensus (AI)
   ↓
Phase 4: Human ICR (20% Sample)
   ↓
Phase 5: Discrepancy Resolution
   ↓
Phase 6: QA Final (6 Gates)
   ↓
Final Validated Dataset
```

---

## Phase 0: RAG Index Building

### Purpose
Build a retrieval-augmented generation (RAG) index to enable efficient context retrieval from study PDFs during AI coding.

### Process

**Step 1: PDF Ingestion**
- Input: All included study PDFs (k=40-80 studies, educational AI focus)
- Parse PDFs to extract text, tables, figures
- Preserve document structure (sections, pages, table IDs)

**Step 2: Chunking**
- Split each study into semantic chunks:
  - Title + Abstract (1 chunk)
  - Introduction (1-2 chunks)
  - Methods (2-3 chunks)
  - Results (3-5 chunks, including tables)
  - Discussion (1-2 chunks)
- Chunk size: 500-1000 tokens with 100-token overlap

**Step 3: Embedding**
- Model: `sentence-transformers/all-MiniLM-L6-v2` (384 dimensions)
- Generate embeddings for each chunk
- Embeddings capture semantic meaning for retrieval

**Step 4: Vector Database**
- Store in ChromaDB (local vector database)
- Index: `{study_id}_{chunk_id}`
- Metadata: study_id, section, page_number, chunk_text

**Step 5: Retrieval Testing**
- Query: "correlation matrix for PE, EE, BI"
- Verify: Returns relevant tables from results sections
- Tune: Adjust chunk size/overlap if needed

### Output
- ChromaDB index with ~600-1,600 chunks (15-20 chunks per study × 40-80 studies)
- Average retrieval latency: <100ms per query

---

## Phase 1: Correlation Extraction (AI)

### Purpose
Extract correlation matrices from studies using Claude Sonnet 4.5 with RAG context.

### Process

**Step 1: Context Retrieval**
- Query RAG index: "correlation matrix table for [study_id]"
- Retrieve top 5 most relevant chunks
- Typically returns: correlation table, sample size, construct definitions

**Step 2: AI Extraction Prompt**

```markdown
You are extracting correlation data for meta-analysis on AI adoption in educational contexts.

STUDY: {study_id} - {authors} ({year})

CONTEXT:
{retrieved_chunks}

TASK: Extract the following from this study:
1. Sample size (N)
2. Correlation matrix: Pearson r values among constructs
3. Construct names as labeled in the study
4. Table location (table number, page if available)
5. Note if standardized β reported instead of r
6. Educational context (students/instructors, education level)

OUTPUT FORMAT (JSON):
{
  "study_id": "AuthorYear",
  "sample_size": 300,
  "correlation_data": [
    {"var1": "PE", "var2": "BI", "r": 0.52},
    {"var1": "EE", "var2": "BI", "r": 0.48}
  ],
  "construct_labels": {
    "PE": "Perceived Usefulness",
    "EE": "Ease of Use",
    "BI": "Intention to Use"
  },
  "table_location": "Table 3, page 12",
  "has_beta_only": false,
  "educational_context": "undergraduate students",
  "notes": ""
}

RULES:
- Extract only off-diagonal correlation values (not diagonal reliabilities)
- If only standardized β reported, set has_beta_only=true and extract β values
- Record construct names exactly as in study
- Note educational context (student vs. instructor, K-12 vs. higher ed)
- If correlation matrix not found, return empty correlation_data with note
```

**Step 3: API Call**
- Model: `claude-sonnet-4-20250514` (Claude Sonnet 4.5)
- Temperature: 0.0 (deterministic)
- Max tokens: 4,000
- Timeout: 60 seconds per study

**Step 4: Parse Response**
- Validate JSON structure
- Check for required fields
- Store raw response in audit log

### Output
- `phase1_extractions.jsonl`: One JSON object per study
- `phase1_log.csv`: API call metadata (study_id, timestamp, tokens_used, cost)

### Estimated Cost
- ~$0.50-1.00 per study × 40-80 studies = **$20-80 total**

---

## Phase 2: Construct Mapping (AI)

### Purpose
Map study-specific construct labels to the 12 standard constructs using harmonization rules.

### Process

**Step 1: Load Harmonization Rules**
- Input: Coding manual construct definitions (Section 4)
- Input: Mapping tables (Section 5)
- Embed rules into prompt context

**Step 2: Mapping Prompt**

```markdown
You are mapping study constructs to standardized constructs for meta-analysis.

STANDARDIZED CONSTRUCTS:
1. PE (Performance Expectancy) - Perceived usefulness, performance benefits
2. EE (Effort Expectancy) - Ease of use, simplicity
3. SI (Social Influence) - Subjective norm, peer influence
4. FC (Facilitating Conditions) - Resources, institutional support
5. BI (Behavioral Intention) - Intention to use, willingness
6. UB (Use Behavior) - Actual use, usage frequency
7. ATT (Attitude) - Overall evaluation, liking
8. SE (Self-Efficacy) - Confidence in ability to use
9. TRU (AI Trust) - Trust in AI, reliability perception
10. ANX (AI Anxiety) - Fear, apprehension about AI
11. TRA (AI Transparency) - Explainability, understandability
12. AUT (Perceived AI Autonomy) - AI independence, autonomy

STUDY CONSTRUCTS (from {study_id}):
{construct_labels from Phase 1}

TASK: Map each study construct to one of the 12 standard constructs.

MAPPING RULES:
- "Perceived Usefulness" → PE (TAM equivalent)
- "PEOU" → EE (TAM equivalent)
- "Subjective Norm" → SI (TRA/TPB equivalent)
- Check full harmonization table in context

OUTPUT FORMAT (JSON):
{
  "mappings": [
    {"study_label": "Perceived Usefulness", "standard": "PE", "confidence": "high", "rationale": "TAM Perceived Usefulness = Performance Expectancy"},
    {"study_label": "Ease of Use", "standard": "EE", "confidence": "high", "rationale": "Direct PEOU equivalent"},
    {"study_label": "AI Value", "standard": "PE", "confidence": "moderate", "rationale": "Likely performance-focused but ambiguous without items"}
  ],
  "unmappable": ["Habit", "Price Value"]
}

CONFIDENCE LEVELS:
- exact: Study uses identical label
- high: Well-established equivalent (TAM/UTAUT)
- moderate: Reasonable alignment, some interpretation
- low: Ambiguous, needs item review
```

**Step 3: Execute Mapping**
- Model: Claude Sonnet 4.5
- Temperature: 0.0
- Include harmonization rules from coding manual in system prompt

**Step 4: Validation**
- Check all study constructs mapped or marked unmappable
- Verify confidence levels assigned
- Flag low-confidence mappings for human review

### Output
- `phase2_mappings.jsonl`: Construct mappings per study
- `phase2_low_confidence.csv`: Flagged mappings for human review

---

## Phase 3: 3-Model Consensus (AI)

### Purpose
Improve extraction accuracy by using three independent AI models and taking consensus.

### Models

| Model | Provider | Strengths | Cost per Study |
|-------|----------|-----------|----------------|
| Claude Sonnet 4.5 | Anthropic | Nuanced reasoning, long context | $0.50-1.00 |
| GPT-4o | OpenAI | Fast, reliable, well-validated | $0.20-0.40 |
| Llama 3.3 70B | Groq (via API) | Open-source, fast inference | $0.05 |

### Process

**Step 1: Parallel Extraction**
- Run Phase 1 + Phase 2 independently on ALL three models
- Same prompts, same RAG context
- No communication between models

**Step 2: Alignment**
- For each correlation pair in each study, collect three estimates:
  - Claude: r = 0.52
  - GPT-4o: r = 0.52
  - Llama: r = 0.51

**Step 3: Consensus Rules**

**Rule 1: Full Agreement (2+ models agree exactly)**
```
Claude: PE-BI = 0.52
GPT-4o: PE-BI = 0.52
Llama: PE-BI = 0.51

→ Consensus: 0.52 (2/3 agree)
→ Confidence: High
```

**Rule 2: Close Agreement (all within .05)**
```
Claude: PE-BI = 0.52
GPT-4o: PE-BI = 0.50
Llama: PE-BI = 0.51

→ Consensus: 0.51 (median)
→ Confidence: Moderate
→ Flag for human review
```

**Rule 3: Disagreement (range > .05)**
```
Claude: PE-BI = 0.52
GPT-4o: PE-BI = 0.45
Llama: PE-BI = 0.60

→ Consensus: NULL
→ Flag: MUST review (discrepancy > .05)
```

**Step 4: Construct Mapping Consensus**

**Agreement:**
```
Claude: "Perceived Usefulness" → PE
GPT-4o: "Perceived Usefulness" → PE
Llama: "Perceived Usefulness" → PE

→ Consensus: PE
```

**Disagreement:**
```
Claude: "AI Value" → PE (performance-focused)
GPT-4o: "AI Value" → ATT (evaluative)
Llama: "AI Value" → PE (usefulness)

→ Consensus: PE (2/3 agree)
→ Flag for human review (construct ambiguity)
```

### Output
- `phase3_consensus.jsonl`: Consensus correlations and mappings
- `phase3_discrepancies.csv`: Flagged disagreements (range > .05 or mapping conflicts)
- `phase3_confidence.csv`: Confidence scores per data point

### Estimated Cost
- Claude: $75-150
- GPT-4o: $30-60
- Llama (Groq): $5-10
- **Total: $110-220** for 150 studies

---

## Phase 4: Human ICR (20% Sample)

### Purpose
Validate AI extraction accuracy through inter-coder reliability on a representative subsample.

### Sampling

**Stratified Random Sample:**
- 20% of total studies (e.g., 16 studies if k=80, 12 studies if k=60)
- Stratify by:
  - Publication year (2015-2019, 2020-2022, 2023-2025)
  - Education level (K-12, undergraduate, graduate)
  - Region (North America, Europe, Asia, Other)

**Random Seed:** Set seed for reproducibility

### Process

**Step 1: Assign to Coders**
- Two independent human coders
- Each codes the same 30 studies
- Blinded to AI extractions and each other's work

**Step 2: Human Coding**
- Use coding manual (docs/03_data_extraction/coding_manual.md)
- Extract correlations, map constructs, code moderators
- Record in same data structure as AI output

**Step 3: Calculate ICR Metrics**

**Correlation Extraction:**
- **ICC(2,1):** Intraclass correlation for r values
  - Target: ICC ≥ .95
- **MAE:** Mean absolute error between coders
  - Target: MAE ≤ .03

**Construct Mapping:**
- **Cohen's κ:** Agreement on categorical mappings
  - Target: κ ≥ .85

**Moderators:**
- **Percent Agreement:** For categorical moderators (AI type, industry)
  - Target: ≥90%

**Step 4: Compare AI vs. Human**

**AI-Human Agreement:**
- Compare AI consensus to each human coder
- Calculate same metrics (ICC, MAE, κ)
- Identify systematic biases (e.g., AI consistently higher/lower)

### Output
- `phase4_human_coding.csv`: Human-coded data for ICR sample
- `phase4_icr_metrics.csv`: ICC, κ, MAE for human-human and AI-human
- `phase4_discrepancies.csv`: Items where human coders disagree or AI differs from humans

### ICR Benchmarks

| Metric | Target | Interpretation |
|--------|--------|----------------|
| ICC (correlations) | ≥.95 | Almost perfect reliability |
| MAE (correlations) | ≤.03 | Average error within 3 percentage points |
| Cohen's κ (mappings) | ≥.85 | Almost perfect agreement |
| % Agreement (moderators) | ≥90% | Excellent agreement |

---

## Phase 5: Discrepancy Resolution

### Purpose
Resolve disagreements between AI models, between human coders, and between AI and humans.

### Input Sources
- Phase 3 discrepancies: AI model disagreements
- Phase 4 discrepancies: Human-human and AI-human disagreements

### Resolution Process

**Step 1: Prioritize Discrepancies**

High Priority (resolve first):
1. Correlation value differences > .10
2. Construct mapping conflicts (PE vs. ATT vs. other)
3. Missing data (AI extracted, human says not available, or vice versa)

Medium Priority:
1. Correlation value differences .05-.10
2. Moderator coding differences

Low Priority:
1. Correlation value differences < .05 (may accept consensus/median)

**Step 2: Return to Original Study**

For each discrepancy:
1. Retrieve original PDF
2. Navigate to relevant section (table, page noted in extraction)
3. Senior coder re-reads and extracts independently
4. Document: exact quote, table number, page number

**Step 3: Resolution Decision**

**Hierarchy:**
1. **Original study text** (highest authority)
2. **Human consensus** (if both human coders agree)
3. **AI consensus** (if 2+ models agree and human review confirms)
4. **Expert adjudication** (if still unclear, escalate to lead investigator)

**Example Resolution Log Entry:**

```csv
study_id,variable,ai_value,human1_value,human2_value,discrepancy_size,resolution,source,evidence,resolver
Smith2023,PE_BI_r,0.52,0.58,0.58,0.06,0.58,original_text,"Table 3 p.12 shows r=.58**",coder_A
Jones2024,construct_PU,PE,PE,ATT,mapping_conflict,PE,human_consensus,"Both coders agree items are performance-focused",coder_B
```

**Step 4: Update Dataset**
- Replace discrepant values with resolved values
- Tag as `human_verified = TRUE` in provenance field
- Document resolution rationale

### Output
- `phase5_resolutions.csv`: All resolved discrepancies with evidence
- `phase5_updated_dataset.csv`: Dataset with corrections applied

---

## Phase 6: QA Final (6 Gates)

### Purpose
Perform final quality checks before data analysis to ensure dataset integrity.

### The 6 Quality Gates

**Gate 1: Range Check**
- **Rule:** All r ∈ [-1, 1]
- **Check:** `any(abs(r) > 1.0)`
- **Action if fail:** Identify out-of-range values, check data entry errors, correct

**Gate 2: Symmetry Check**
- **Rule:** r(A,B) = r(B,A)
- **Check:** For each study, verify lower triangle mirrors upper triangle
- **Action if fail:** Identify asymmetric pairs, return to original study, correct

**Gate 3: Diagonal Check**
- **Rule:** r(X,X) = 1.00 (or reported as reliability α)
- **Check:** All diagonal values are 1.00 or missing (if reliabilities extracted separately)
- **Action if fail:** Check if diagonal values are reliabilities (should be in separate table), correct

**Gate 4: Completeness Check**
- **Rule:** Each study has ≥2 of the 12 target constructs
- **Check:** Count constructs per study
- **Action if fail:** Verify study meets inclusion criteria; exclude if <2 constructs

**Gate 5: Sample Size Check**
- **Rule:** All studies have n ≥ 50
- **Check:** `any(n < 50)`
- **Action if fail:** Re-check original study for sample size; exclude if confirmed n<50

**Gate 6: Duplicate Check**
- **Rule:** No duplicate study_id entries
- **Check:** `anyDuplicated(study_id)`
- **Action if fail:** Check for duplicate samples (same data in multiple publications); keep one version

### Implementation (R Code)

```r
# Load final dataset
dataset <- read.csv("data/phase5_updated_dataset.csv")

# Gate 1: Range Check
gate1_pass <- all(abs(dataset$r) <= 1.0, na.rm = TRUE)
if (!gate1_pass) {
  out_of_range <- dataset[abs(dataset$r) > 1.0, ]
  print(paste("GATE 1 FAIL:", nrow(out_of_range), "values out of range"))
  print(out_of_range)
}

# Gate 2: Symmetry Check (requires matrix reconstruction per study)
check_symmetry <- function(study_data) {
  # Reconstruct correlation matrix
  # Check if Cor[i,j] == Cor[j,i] for all pairs
  # Return TRUE if symmetric
}
# Apply to each study...

# Gate 3: Diagonal Check
# (Assumes diagonals extracted separately as reliabilities)
# No action needed if reliabilities in separate table

# Gate 4: Completeness Check
constructs_per_study <- dataset %>%
  group_by(study_id) %>%
  summarize(
    n_constructs = length(unique(c(construct1, construct2)))
  )
gate4_pass <- all(constructs_per_study$n_constructs >= 2)

# Gate 5: Sample Size Check
gate5_pass <- all(dataset$n >= 50, na.rm = TRUE)

# Gate 6: Duplicate Check
gate6_pass <- !anyDuplicated(unique(dataset$study_id))

# Report
gates <- c(gate1_pass, gate4_pass, gate5_pass, gate6_pass)
if (all(gates)) {
  print("✓ All QA gates PASSED")
} else {
  print("✗ QA gates FAILED - review required")
}
```

### Output
- `phase6_qa_report.txt`: Pass/fail status for each gate
- `phase6_qa_issues.csv`: Any flagged issues (if gates fail)
- `final_validated_dataset.csv`: Clean dataset ready for analysis

---

## Audit Logging

### Log Files Generated

**1. API Call Log (`api_log.csv`)**

```csv
timestamp,phase,model,study_id,prompt_tokens,completion_tokens,total_cost,latency_ms
2026-03-15 10:30:22,phase1,claude-sonnet-4,Smith2023,2450,890,0.85,3200
2026-03-15 10:31:05,phase1,gpt-4o,Smith2023,2380,720,0.32,1800
```

**2. Extraction Log (`extraction_log.jsonl`)**

One JSON object per extraction attempt:

```json
{
  "timestamp": "2026-03-15T10:30:22Z",
  "phase": "phase1",
  "model": "claude-sonnet-4",
  "study_id": "Smith2023",
  "prompt": "...",
  "response": "{...}",
  "success": true,
  "error": null
}
```

**3. Discrepancy Log (`discrepancy_log.csv`)**

```csv
study_id,variable,source1,value1,source2,value2,discrepancy_size,flagged_phase
Smith2023,PE_BI_r,claude,0.52,gpt4o,0.50,0.02,phase3
Jones2024,construct_PU,claude,PE,human1,ATT,mapping_conflict,phase4
```

**4. Resolution Log (`resolution_log.csv`)**

```csv
study_id,variable,original_value,resolved_value,resolution_method,evidence,resolver,date
Smith2023,PE_BI_r,0.52,0.58,original_text,"Table 3 p.12: r=.58",coder_A,2026-03-20
```

---

## Cost Analysis

### Per-Study Costs

| Phase | Model | Cost per Study |
|-------|-------|----------------|
| Phase 1 | Claude Sonnet 4.5 | $0.60 |
| Phase 1 | GPT-4o | $0.25 |
| Phase 1 | Llama 3.3 (Groq) | $0.03 |
| Phase 2 | Claude Sonnet 4.5 | $0.30 |
| Phase 2 | GPT-4o | $0.15 |
| Phase 2 | Llama 3.3 (Groq) | $0.02 |
| **Total per study** | | **$1.35** |

### Total Project Costs (k=40-80 studies, educational AI focus)

| Component | Cost |
|-----------|------|
| AI extraction (all 3 models × 40-80 studies) | $54-108 |
| RAG infrastructure (ChromaDB hosting, embeddings) | $10-15 |
| Human coding (20% ICR sample) | $0 (study labor) |
| **Total AI pipeline cost** | **~$64-123** |

### Cost-Benefit Analysis

**Traditional Manual Coding:**
- 60 studies × 2 coders × 45 min/study = 90 hours
- At $30/hour RA rate: $2,700

**AI-Assisted Pipeline:**
- AI costs: $93 (average for 60 studies)
- Human verification (20% ICR + discrepancy resolution): ~18 hours
- At $30/hour: $540
- **Total: $633**

**Savings: $2,067 (77% reduction)**

---

## Quality Metrics and Benchmarks

### Expected Performance

Based on pilot testing and literature:

| Metric | Expected | Source |
|--------|----------|--------|
| AI extraction accuracy (correlations) | 92-96% within .05 of true value | Pilot testing |
| Construct mapping agreement (AI-human) | κ = .80-.90 | Expected based on rule clarity |
| 3-model consensus rate | 85-90% (2+ models agree) | Pilot testing |
| Discrepancy rate requiring human review | 10-15% of total extractions | Expected |
| Final dataset accuracy post-QA | >99% error-free | After human verification |

---

## Failure Modes and Mitigation

### Potential Failure Modes

**1. RAG retrieval failure (wrong chunks retrieved)**
- **Symptom:** AI cannot find correlation table
- **Mitigation:** Manual specification of table location for problematic studies
- **Fallback:** Human coding for that study

**2. AI hallucination (fabricates data)**
- **Symptom:** AI reports correlations not in study
- **Mitigation:** 3-model consensus detects outliers; human ICR catches systematic errors
- **Fallback:** Flag and human verify all data points from that study

**3. Construct mapping ambiguity**
- **Symptom:** Low consensus on mappings (<2 models agree)
- **Mitigation:** Flag for human expert review; use item-level analysis
- **Fallback:** Conservative exclusion if cannot confidently map

**4. API failures or timeouts**
- **Symptom:** API returns error or times out
- **Mitigation:** Retry logic (3 attempts with exponential backoff)
- **Fallback:** Switch to different model or manual coding

**5. Inter-coder reliability below threshold**
- **Symptom:** Human-human κ < .85 or ICC < .95
- **Mitigation:** Additional training, re-code problematic studies
- **Fallback:** Increase ICR sample to 30% for more robust estimates

---

## Timeline

| Week | Phase | Activities | Deliverable |
|------|-------|------------|-------------|
| 1 | Phase 0 | Ingest PDFs, build RAG index, test retrieval | ChromaDB index |
| 2 | Phase 1 | Run AI extractions (all 3 models in parallel) | Raw extractions |
| 3 | Phase 2 | Construct mapping (all 3 models) | Mapped constructs |
| 3 | Phase 3 | Compute consensus, flag discrepancies | Consensus dataset |
| 4 | Phase 4 | Human ICR coding (2 coders × 30 studies) | ICR metrics |
| 5 | Phase 5 | Resolve discrepancies (return to studies) | Resolved dataset |
| 6 | Phase 6 | QA checks, final validation | Final dataset |
| **Total** | **6 weeks** | | **Ready for analysis** |

---

## References

Choi, J. H., Hickman, K. E., Monahan, A., & Schwarcz, D. (2023). ChatGPT goes to law school. *Journal of Legal Education*, 71(3), 387-435.

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., ... & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *Advances in Neural Information Processing Systems*, 33, 9459-9474.

Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., & Yang, D. (2024). Can large language models transform computational social science? *Computational Linguistics*, 50(1), 237-291.
