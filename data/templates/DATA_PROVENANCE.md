# Data Provenance

## Dataset: AI Adoption MASEM Final Dataset

### Source
- Primary studies identified through systematic literature search
- Databases: Web of Science, Scopus, PsycINFO, IEEE Xplore, ACM Digital Library

### Processing Pipeline
1. **AI Screening (Title/Abstract):** Codex CLI + Gemini CLI (OAuth sessions)
2. **Human Screening:** Two independent human coders on 100% of records
3. **Adjudication:** PI resolves unresolved conflicts and sets final decision
4. **Extraction Pipeline:** Claude Sonnet + GPT-4o + Groq consensus (phases 1-6)
5. **Quality Assurance:** IRR thresholds + matrix/data validation gates

### Key Parameters
- Constructs: 12 (PE, EE, SI, FC, BI, UB, ATT, SE, TRU, ANX, TRA, AUT)
- Pairwise correlations: 66
- Effect size metric: Pearson r (with β→r conversion where needed)
- β→r conversion method: Peterson & Brown (2005): r ≈ β + .05λ

### Provenance Chain
```
Merged Search Results → Deduplication → Codex/Gemini Screening
→ Human Dual Coding → PI Adjudication → Full-Text Eligibility
→ AI Extraction/Mapping/Consensus → Human Verification → QA Final
→ masem_final_dataset.csv
```

### Audit Trail
- Screening run metadata: `screen_run_id`, `oauth_auth_method_codex`, `oauth_auth_method_gemini`
- Full extraction log: `data/01_extracted/extraction_log.jsonl`
- ICR results: `data/02_verified/icr_results/`
- AI provenance: Coding template Sheet 5 (AI_Extraction_Provenance)
