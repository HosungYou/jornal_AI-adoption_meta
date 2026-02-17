# Data Provenance

## Dataset: AI Adoption MASEM Final Dataset

### Source
- Primary studies identified through systematic literature search
- Databases: Web of Science, Scopus, PsycINFO, IEEE Xplore, ACM Digital Library

### Processing Pipeline
1. **AI Extraction** (Phase 1-2): Claude Sonnet + GPT-4o + Groq consensus
2. **Human Verification** (Phase 4-5): 20% stratified sample, κ ≥ .85
3. **Quality Assurance** (Phase 6): 6-gate validation

### Key Parameters
- Constructs: 12 (PE, EE, SI, FC, BI, UB, ATT, SE, TRU, ANX, TRA, AUT)
- Pairwise correlations: 66
- Effect size metric: Pearson r (with β→r conversion where needed)
- β→r conversion method: Peterson & Brown (2005): r ≈ β + .05λ

### Provenance Chain
```
Raw PDFs → AI Extraction → Construct Mapping → 3-Model Consensus
→ Human ICR Verification → Discrepancy Resolution → QA Final
→ masem_final_dataset.csv
```

### Audit Trail
- Full extraction log: `data/01_extracted/extraction_log.jsonl`
- ICR results: `data/02_verified/icr_results/`
- AI provenance: Coding template Sheet 5 (AI_Extraction_Provenance)
