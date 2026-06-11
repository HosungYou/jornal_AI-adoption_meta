# PRISMA-trAIce Checklist (2025)

## Reporting AI Use in Evidence Synthesis — 14-Item Checklist

> 출처: PRISMA-trAIce Consortium (2025)
> Paper B compliance status 추적용

---

| # | Item | Description | Paper B Section | Status | Notes |
|---|------|-------------|-----------------|--------|-------|
| 1 | **AI Tool Identification** | Name, version, and provider of AI tools used | Methods 3.2 | ⬜ | Claude Sonnet 4.6, GPT Codex 5.3, Gemini CLI |
| 2 | **Access Date Range** | Date range when AI tools were accessed | Methods 3.2 | ⬜ | Week 1 extraction dates |
| 3 | **Task Description** | Specific tasks AI performed (screening, extraction, etc.) | Methods 3.2 | ⬜ | Data extraction for 30 MASEM variables |
| 4 | **Prompt Documentation** | Full prompts or structured summary | Appendix A | ⬜ | 4 module prompts in OSF: https://osf.io/mkrgd/overview |
| 5 | **Prompt Development** | How prompts were developed and refined | Methods 3.2.1 | ⬜ | Pilot testing on 10 non-sample studies |
| 6 | **Input Data Description** | What data was provided to the AI | Methods 3.1 | ⬜ | Full-text PDFs of 100 studies |
| 7 | **Output Format** | Structure and format of AI output | Methods 3.2.2 | ⬜ | JSON schema per module |
| 8 | **Human Oversight Protocol** | How human reviewers monitored AI | Methods 3.3 | ⬜ | Phase 1: independent human coding; Phase 2: rotated-pair human coding before LLM comparison |
| 9 | **Verification Method** | How AI outputs were verified | Methods 3.3 | ⬜ | Phase 1+2 comparison against source-anchored adjudicated human reference |
| 10 | **Error Handling** | Protocol for AI errors or failures | Methods 3.3.3 | ⬜ | Discrepancy resolution protocol |
| 11 | **Reproducibility Measures** | Steps to ensure reproducibility | Methods 3.4 | ⬜ | Fixed seeds, temp=0, version-locked |
| 12 | **Limitations of AI Use** | Known limitations acknowledged | Discussion | ⬜ | Model drift, prompt sensitivity |
| 13 | **Cost/Resource Reporting** | Time and cost of AI use | Results | ⬜ | API costs, human hours |
| 14 | **Data Availability** | Access to AI outputs and analysis data | DAS | ⬜ | OSF: https://osf.io/mkrgd/overview |

---

## Status Legend

- ⬜ Not yet completed
- 🟡 In progress
- ✅ Completed and documented

## Completion Date: ___________

## Notes

- 모든 항목은 Paper B 제출 전까지 ✅ 상태여야 함
- OSF에 prompts, locked model outputs, derived analysis data, and analysis code 공개: https://osf.io/mkrgd/overview
- Supplementary materials에 detailed prompt documentation 포함
