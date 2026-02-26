# TRIPOD-LLM Checklist

## Transparent Reporting of LLM-Based Studies

> 출처: Collins et al. (2025), Nature Medicine
> Paper B compliance status 추적용

---

| # | Category | Item | Paper B Section | Status | Notes |
|---|----------|------|-----------------|--------|-------|
| **Title & Abstract** | | | | | |
| 1 | Title | Identify as LLM-based study | Title | ⬜ | "LLM-Assisted" in title |
| 2 | Abstract | Structured summary with LLM details | Abstract | ⬜ | Model names in abstract |
| **Introduction** | | | | | |
| 3 | Background | Context for LLM use | Intro 1.1-1.2 | ⬜ | AI in evidence synthesis context |
| 4 | Objectives | Specific objectives/hypotheses | Intro 1.3 | ⬜ | 4 RQs |
| **Methods** | | | | | |
| 5 | Source of data | Data source description | Methods 3.1 | ⬜ | 100 MASEM studies from parent MA |
| 6 | Participants | Study selection criteria | Methods 3.1 | ⬜ | MASEM eligibility + stratified sampling |
| 7 | LLM specification | Model name, version, provider | Methods 3.2 | ⬜ | 3 models fully specified |
| 8 | LLM access | API version, access dates | Methods 3.2 | ⬜ | API details documented |
| 9 | Prompt design | Full prompt or structured description | Methods 3.2.1 | ⬜ | 4 module prompts |
| 10 | Prompt development | How prompts were created/refined | Methods 3.2.1 | ⬜ | Pilot-based refinement |
| 11 | Input specification | What was provided to LLM | Methods 3.2 | ⬜ | Full-text PDFs |
| 12 | Output specification | Expected output format | Methods 3.2.2 | ⬜ | JSON schema |
| 13 | Temperature & params | Model parameters (temp, tokens) | Methods 3.2 | ⬜ | Temp=0, max_tokens=4096 |
| 14 | Reference standard | Gold standard definition | Methods 3.3 | ⬜ | 2-coder independent + resolved |
| 15 | Performance measures | Metrics used for evaluation | Methods 3.4 | ⬜ | κ, ICC, MAE, accuracy, F1 |
| 16 | Statistical methods | Analysis approach | Methods 3.4 | ⬜ | Per-model + consensus + workflow |
| **Results** | | | | | |
| 17 | Participants | Flow of studies | Results 4.1 | ⬜ | PRISMA flow diagram |
| 18 | Model performance | Performance metric values | Results 4.2 | ⬜ | Tables 5-10 |
| 19 | Error analysis | Types and patterns of errors | Results 4.3 | ⬜ | Error taxonomy |
| 20 | Comparison | Comparison across models/methods | Results 4.4 | ⬜ | 3-model comparison |
| **Discussion** | | | | | |
| 21 | Limitations | Study limitations | Discussion 5.4 | ⬜ | Model drift, generalizability |
| 22 | Interpretation | Interpretation in context | Discussion 5.1 | ⬜ | Implications for SR practice |
| 23 | Generalizability | Applicability to other contexts | Discussion 5.3 | ⬜ | Beyond MASEM/education |
| **Other** | | | | | |
| 24 | Registration | Pre-registration or protocol | Methods | ⬜ | OSF pre-registration |
| 25 | Funding | Funding sources | Acknowledgments | ⬜ | Funding statement |
| 26 | Code availability | Analysis code shared | DAS | ⬜ | OSF repository |
| 27 | Data availability | Raw data shared | DAS | ⬜ | OSF repository |

---

## Status Legend

- ⬜ Not yet completed
- 🟡 In progress
- ✅ Completed and documented

## Completion Date: ___________
