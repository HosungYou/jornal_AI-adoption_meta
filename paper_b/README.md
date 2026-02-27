# Paper B: LLM-Assisted Data Extraction for MASEM

## 논문 정보

- **제목**: LLM-Assisted Data Extraction for Meta-Analytic Structural Equation Modeling: A Three-Model Comparative Framework with Multi-Model Consensus Validation
- **저자**: Hosung You
- **소속**: College of Education, Pennsylvania State University
- **타겟 저널**: Research Synthesis Methods (1순위) / JMIR AI (2순위)
- **상태**: Draft v1.0 (2026-02-25)

## Paper A와의 관계

- **Paper A** (parent meta-analysis): AI Adoption in Education MASEM (Computers & Education 타겟)
- **Paper B** (본 논문): Paper A의 100-study subsample을 gold standard로 사용하여 AI coding 신뢰도 평가
- Paper B는 Paper A 완성 전에 독립적으로 제출 가능 (Paper A를 OSF Preprint으로 cite)

## 연구 설계 요약

```
Gold Standard Sample: 100 studies (from ~300 MASEM-eligible studies)
Human Coders: 2명 (R2 + R3), 독립 코딩 → Cohen's κ IRR
              R1(PI) = Adjudicator (불일치 중재)
AI Models: 3개 (Claude Sonnet 4.6 / GPT Codex 5.3 / Gemini CLI)
Variables: 30개/study × 100 studies ≈ 3,000 data elements
Design: Comparative accuracy (AI vs. human gold standard)
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
- R2+R3: 200건 동일 독립 코딩 (IRR: Cohen's κ)
- R1(PI): spot-check 86건 + 추가코딩 135건 + adjudicator
- Excel: `data/templates/human_review_sheet_v8.xlsx`

## 디렉토리 구조

```
paper_b/
├── README.md                          ← 현재 파일
├── DISCUSSION_LOG_KR.md               ← 연구 논의 기록 (한국어)
├── RESEARCHER_ROLES.md                ← 연구자 3명 역할 분담
├── SAMPLING_PROTOCOL.md               ← 575 → 300 → 100 선정 프로세스
├── CODING_PROTOCOL.md                 ← Phase 1-3 코딩 프로토콜
├── TIMELINE.md                        ← 6주 실행 일정
├── ANALYSIS_PLAN.md                   ← 통계 분석 계획 (RQ1-4)
├── LITERATURE_REVIEW.md               ← 선행연구 요약
├── JOURNAL_STRATEGY.md                ← 저널 타겟팅 전략
├── AUDIT_TRAIL_GUIDE.md               ← 감사 추적 가이드
│
├── manuscript/
│   └── Paper_B_LLM_MASEM_v1.0.docx   ← 논문 초안
│
├── prompts/                           ← AI extraction 프롬프트
│   ├── module_a_bibliographic.md
│   ├── module_b_correlation.md
│   ├── module_c_construct.md
│   └── module_d_moderator.md
│
├── data/
│   ├── 00_fulltext_eligibility/       ← 575 → 300 풀텍스트 심사
│   ├── 01_sample_selection/           ← 100-study 층화추출
│   ├── 02_ai_extraction/              ← AI 추출 결과 (모델별)
│   │   ├── claude/
│   │   ├── codex/
│   │   └── gemini/
│   ├── 03_human_coding/               ← 독립 인간 코딩
│   │   ├── coder1_PI/
│   │   └── coder2_phd1/
│   ├── 04_consensus/                  ← 다중모델 합의
│   ├── 05_gold_standard/              ← 최종 인간 골드 스탠다드
│   └── 06_analysis/                   ← IRR 계산, 시각화
│
├── templates/                         ← 코딩/로깅 템플릿
├── checklists/                        ← PRISMA-trAIce, TRIPOD-LLM
└── scripts/                           ← 분석 스크립트
```

## 핵심 RQ

1. **RQ1**: AI 3개 모델의 MASEM 코딩 정확도 (vs. human gold standard)
2. **RQ2**: Variable type별 AI 정확도 차이 (bibliographic > statistical > classificatory?)
3. **RQ3**: Multi-model consensus가 single model보다 나은가?
4. **RQ4**: 최적 human-AI hybrid workflow는?

## IRR 설계

- **코더**: R2 + R3 (동일 200건 독립 코딩)
- **지표**: Cohen's κ (2명 범주형), ICC(2,1) (연속형)
- **목표**: κ ≥ 0.85
- **R1(PI)**: Adjudicator — R2-R3 불일치 시 독립 검토 후 최종 판단
- **Gold Standard**: R2-R3 일치 시 채택, 불일치 시 R1 중재 후 확정

## 보고 기준

- PRISMA-trAIce 14-item checklist (2025)
- TRIPOD-LLM guideline (Collins et al., 2025)
- RAISE framework (Cochrane/Campbell/JBI/CEE, 2025)
