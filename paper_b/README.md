# Paper B: LLM-Assisted MASEM-Ready Data Extraction

## 논문 정보

- **현재 제목**: Can a Prespecified Large Language Model Workflow Augment MASEM-Ready Data Extraction?
- **저자**: Hosung You
- **소속**: College of Education, Pennsylvania State University
- **타겟 저널**: Research Synthesis Methods (1순위) / JMIR AI (2순위)
- **상태**: RSM summarized manuscript v0.2 (2026-04-24)

## 2026-04-24 포지셔닝 업데이트

Paper B는 더 이상 3개 상용 LLM의 순위 비교를 핵심 기여로 두지 않는다. 현재 포지셔닝은 **하나의 사전 지정된 LLM workflow가 인간 감독하에서 MASEM-ready data extraction을 보조할 수 있는지 검증하는 방법론 논문**이다.

Claude/Gemini 등 추가 모델은 필요한 경우 supplementary robustness 또는 triage 분석으로만 사용한다. 본문 핵심은 model ranking이 아니라 다음 세 가지다.

1. Adjudicated human reference standard 대비 extraction validity
2. Construct harmonization 및 correlation matrix recovery의 systematic error
3. Human-coded input을 LLM-assisted input으로 대체했을 때 MASEM 결론이 유지되는지에 대한 downstream substitution analysis

## 2026-04-25 Phase 1+2 검증 코퍼스 결정

Phase 1 pairwise coding is complete. Phase 2 remains the rotated-pair human
coding design adopted on 2026-04-24, but it is no longer framed as optional
external validation. Phase 1 and Phase 2 are now one combined Paper B validation
corpus.

- Phase 1 completed pairs: R1+R2 and R3+R4
- Phase 2 rotated pairs: R1+R4 and R2+R3
- LLM outputs remain blinded until independent human coding and adjudication are complete
- Raw human-human disagreement is analyzed before adjudication
- LLM evaluation and MASEM substitution use the frozen source-anchored adjudicated human reference standard

Current workload from the package generator:

| Pair | Coders | Phase 2 studies | Extra per coder vs Phase 1 |
|---|---|---:|---:|
| Pair C | R1 + R4 | 57 | +7 |
| Pair D | R2 + R3 | 56 | +6 |

## Paper A와의 관계

- **Paper A** (parent meta-analysis): AI Adoption in Education MASEM (Computers & Education 타겟)
- **Paper B** (본 논문): Paper A의 validation subset을 사용하여 LLM-assisted MASEM extraction workflow를 평가
- Paper B는 Paper A 완성 전에 독립적으로 제출 가능 (Paper A를 OSF Preprint으로 cite)

## 연구 설계 요약

```
Validation subset: stratified subset from Paper A MASEM corpus
Human standard: Phase 1 + Phase 2 independent human coding, raw disagreement analysis, and source-anchored adjudication
Primary LLM workflow: prespecified Codex 5.5 workflow
Optional robustness: additional LLMs only as supplementary sensitivity/triage checks
Extraction families: bibliographic, sample, construct, measurement, correlation, moderator
Core design: human-reference validation + matrix-level diagnostics + substitution analysis
```

## 스크리닝 파이프라인 (2026-02-26 확정)

**AI Screening**: Gemini + Claude 2-model consensus (Codex 제외 — 85% uncertain)

| Category | Count | Description |
|----------|-------|-------------|
| Auto-INCLUDE | 367 | 둘 다 include → 자동 포함 |
| Auto-EXCLUDE | 15 | 둘 다 exclude → 자동 제외 |
| TIER1 Conflict | 95 | include ↔ exclude |
| TIER2 High | 480 | include + uncertain |
| TIER3 Low | 500 | uncertain 등 |

**Human Review (Option C)**:
- Pair A (R1+R2) + Pair B (R3+R4): 200건 독립 코딩 (IRR: Cohen's κ)
- Cross-pair adjudication for discrepancies
- Excel: `data/templates/human_review_sheet_v8.xlsx`

## 디렉토리 구조

```
paper_b/
├── README.md                          ← 현재 파일
├── DISCUSSION_LOG_KR.md               ← 연구 논의 기록 (한국어)
├── RESEARCHER_ROLES.md                ← 연구자 4명 역할 분담
├── SAMPLING_PROTOCOL.md               ← 575 → MASEM corpus → Phase 1/2 선정 프로세스
├── CODING_PROTOCOL.md                 ← Phase 1-3 코딩 프로토콜
├── TIMELINE.md                        ← 6주 실행 일정
├── ANALYSIS_PLAN.md                   ← 통계 분석 계획 (RQ1-4)
├── LITERATURE_REVIEW.md               ← 선행연구 요약
├── JOURNAL_STRATEGY.md                ← 저널 타겟팅 전략
├── AUDIT_TRAIL_GUIDE.md               ← 감사 추적 가이드
│
├── manuscript/
│   ├── Paper_B_LLM_MASEM_Methodology_Draft_v1.0.docx
│   ├── Paper_B_RSM_Summarized_Manuscript_v0.2.md
│   ├── Paper_B_RSM_Summarized_Manuscript_v0.2.docx
│   ├── README.md
│   └── figures/
│       └── figure1_substitution_stability_simulation.png
│
├── prompts/                           ← AI extraction 프롬프트
│   ├── module_a_bibliographic.md
│   ├── module_b_correlation.md
│   ├── module_c_construct.md
│   └── module_d_moderator.md
│
├── data/
│   ├── 00_fulltext_eligibility/       ← 575 → 300 풀텍스트 심사
│   ├── 01_sample_selection/           ← Phase 1 층화추출 및 Phase 2 배정 로그
│   ├── 02_ai_extraction/              ← AI 추출 결과 (모델별)
│   │   ├── claude/
│   │   ├── codex/
│   │   └── gemini/
│   ├── 03_human_coding/               ← 독립 인간 코딩
│   │   ├── pair_a/
│   │   │   ├── coder_r1/
│   │   │   └── coder_r2/
│   │   └── pair_b/
│   │       ├── coder_r3/
│   │       └── coder_r4/
│   ├── 04_consensus/                  ← 다중모델 합의
│   ├── 05_reference/                  ← source-anchored adjudicated human reference
│   └── 06_analysis/                   ← IRR 계산, 시각화
│
├── templates/                         ← 코딩/로깅 템플릿
├── checklists/                        ← PRISMA-trAIce, TRIPOD-LLM
└── scripts/                           ← 분석 스크립트
```

## 핵심 RQ

1. **RQ1**: Prespecified LLM workflow는 adjudicated human reference standard 대비 MASEM-ready extraction을 얼마나 정확하게 수행하는가?
2. **RQ2**: Extraction family, construct ambiguity, reporting quality에 따라 systematic error가 어떻게 달라지는가?
3. **RQ3**: LLM-assisted inputs로 대체했을 때 pooled correlations, structural paths, indirect effects의 substantive interpretation이 유지되는가?

## IRR 설계

- **코더**: 4명 (R1-R4), 2 independent pairs
  - Phase 1 Pair A: R1+R2 (50 studies 독립 코딩; completed)
  - Phase 1 Pair B: R3+R4 (50 studies 독립 코딩; completed)
  - Phase 2 Pair C: R1+R4 (remaining eligible studies)
  - Phase 2 Pair D: R2+R3 (remaining eligible studies)
- **지표**: Cohen's κ (pair 내 범주형), ICC(2,1) (연속형)
- **목표**: κ ≥ 0.85
- **Adjudication**: Cross-pair. Phase 1은 R3→Pair A, R1→Pair B. Phase 2는 R2→Pair C, R1→Pair D를 primary adjudicator로 둔다.
- **Reference Standard**: Pair 내 일치 시 채택, 불일치 시 source-document adjudication 후 확정

## 보고 기준

- PRISMA-trAIce 14-item checklist (2025)
- TRIPOD-LLM guideline (Collins et al., 2025)
- RAISE framework (Cochrane/Campbell/JBI/CEE, 2025)
- Research Synthesis Methods GenAI evaluation guidance: model version, prompts, preprocessing, validation, QA, code/data availability, randomization, and computational environment reporting
