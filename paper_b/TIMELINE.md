# 6주 실행 Timeline

## Paper A / Paper B 범위 표시

```
📘 = Paper B 범위 (100 studies, AI vs. Human 비교)
📗 = Paper A 범위 (전체 ~300 studies, MASEM 데이터)
📘📗 = 양쪽 모두 해당
```

## 전체 일정

```
W0 (3d) ──── Phase 0: Calibration (all 4 coders, 10 studies)    📘📗
Week 1  ──── Setup + Full-text Review + AI Extraction            📘📗
Week 2-3 ─── Phase 1: 2-Pair Independent Coding (3 weeks)       📘📗
Week 4  ──── Phase 1: IRR + Gold Standard + Paper B 분석          📘📗
Week 5-6 ─── Phase 2: Single coding ~150 studies (2 weeks)       📗
Week 7  ──── Phase 3 QA + Paper B 작성                             📘📗
Week 8  ──── Paper B 완성 📘 + Data Freeze 📗
```

---

## Phase 0: Calibration (3 days, before Week 1) 📘📗

| Day | 작업 | 담당 | 산출물 | 범위 |
|-----|------|------|--------|------|
| 1 | Orientation: 코딩 매뉴얼 리뷰, 12 construct 정의 | R1, R2, R3, R4 | — | 📘📗 |
| 1-2 | 10 pilot studies 전원 독립 코딩 | R1, R2, R3, R4 | Pilot coding sheets | 📘📗 |
| 3 | Calibration 미팅: IRR 확인 (κ ≥ 0.80), 규칙 명확화 | R1, R2, R3, R4 | Pilot IRR results | 📘📗 |

## Week 1: Setup + Full-text Review + AI Extraction 📘📗

| Day | 작업 | 담당 | 산출물 | 범위 |
|-----|------|------|--------|------|
| 1-2 | Full-text PDF 수집 (575개) | R1 | PDFs | 📘📗 |
| 1-2 | Full-text eligibility review 시작 | R1 | — | 📘📗 |
| 3-5 | Full-text eligibility review 완료 | R1 | fulltext_eligibility_decisions.csv | 📘📗 |
| 5 | MASEM-eligible ~300개 확정 | R1 | eligible list | 📘📗 |
| 5 | 100-study stratified sample 추출 | R1 | paper_b_sample_100.csv | 📘 |
| 5-7 | 3 AI models extract 100 studies | Pipeline | 02_ai_extraction/ | 📘 |
| 5-7 | 3 AI models extract 나머지 ~200 studies | Pipeline | 02_ai_extraction/ | 📗 |
| 6-7 | R2: 30% full-text IRR sample 독립 review | R2 | fulltext_irr_sample.csv | 📘📗 |

## Week 2-3: Phase 1 — 2-Pair Independent Human Coding (3 weeks) 📘📗

| Day | 작업 | 담당 | Pace | 범위 |
|-----|------|------|------|------|
| W2 1-5 | Pair A: 50 studies 독립 코딩 | R1, R2 | ~5/day each | 📘📗 |
| W2 1-5 | Pair B: 50 studies 독립 코딩 | R3, R4 | ~5/day each | 📘📗 |
| W3 1-5 | 코딩 계속 + 완료 | R1, R2, R3, R4 | ~5/day each | 📘📗 |

**Daily target**: 각자 ~5 studies/day (pair당 50 studies / ~2 weeks)
**예상 소요**: ~30-45 min/study × 5 = 2.5-3.75 hours/day (sustainable pace)
**핵심**: 전체 4 coders AI output에 blinded 상태 유지. Pair 내 상대방 코딩도 blinded.

## Week 4: Phase 1 — IRR + Gold Standard 📘📗

| Day | 작업 | 담당 | 산출물 | 범위 |
|-----|------|------|--------|------|
| 1 | 코딩 완료 + 제출 | R1, R2, R3, R4 | pair_a/, pair_b/ | 📘📗 |
| 1-2 | **Unblinding**: IRR 계산 (R1 vs R2, R3 vs R4) | R1 | irr_results.csv | 📘 |
| 2-3 | Discrepancy identification (both pairs) | R1 | discrepancy_log.csv | 📘📗 |
| 3-4 | Cross-pair adjudication (R3→Pair A, R1→Pair B) | R1, R3 | resolved values | 📘📗 |
| 5 | Gold standard finalization | R1 | gold_standard_100.csv | 📘📗 |

## Week 4 (cont.): Paper B 분석 📘

| Day | 작업 | 담당 | 산출물 | 범위 |
|-----|------|------|--------|------|
| 5 | AI consensus 계산 (100 studies) | R1 | consensus_100.csv | 📘 |
| 5 | RQ1-4 분석 실행 | R1 | model_accuracy.csv 등 | 📘 |

## Week 5-6: Phase 2 — Single Coding ~150 studies (2 weeks) 📗

| Day | 작업 | 담당 | 산출물 | 범위 |
|-----|------|------|--------|------|
| W5 1-5 | AI consensus 검증 (single coding) | R1 | ~38 studies | 📗 |
| W5 1-5 | AI consensus 검증 (single coding) | R2 | ~38 studies | 📗 |
| W5 1-5 | AI consensus 검증 (single coding) | R3 | ~37 studies | 📗 |
| W5 1-5 | AI consensus 검증 (single coding) | R4 | ~37 studies | 📗 |
| W6 1-3 | Phase 2 verification 완료 | R1, R2, R3, R4 | verified_data_phase2.csv | 📗 |

**Phase 2 pace**: 각자 ~8 studies/day (verification mode, 독립 코딩보다 빠름). R1-R4 균등 분할.

## Week 7: Phase 3 QA 📗 + Paper B 작성 📘

| Day | 작업 | 담당 | 산출물 | 범위 |
|-----|------|------|--------|------|
| 1-2 | Phase 2 cross spot-check (10%) | R1-R4 (cross) | qa_spotcheck.csv | 📗 |
| 2-3 | QA gates 확인 | R1 | qa_report.md | 📗 |
| 3-4 | Paper B Tables 5-10 채우기 | R1 | Results section | 📘 |
| 4-5 | Figures 생성 (heatmap, Bland-Altman) | R1 | figures/ | 📘 |

## Week 8: Paper B 완성 📘 + Data Freeze 📗

| Day | 작업 | 담당 | 산출물 | 범위 |
|-----|------|------|--------|------|
| 1-2 | Paper B Discussion + Conclusion | R1 | 논문 v2.0 | 📘 |
| 2-3 | PRISMA-trAIce + TRIPOD-LLM 완성 | R1 | checklists/ | 📘 |
| 3-4 | 내부 검토 | R1, R2, R3, R4 | 피드백 | 📘 |
| 5 | Data finalization (전체 ~300) | R1 | 전체 데이터 확정 | 📗 |
| 6-7 | OSF 등록 (prompts, data, code) | R1 | OSF project | 📘📗 |

---

## Milestones & Checkpoints

| Week | Milestone | 성공 기준 | 범위 |
|------|-----------|----------|------|
| W0 | Calibration 통과 | Pilot κ ≥ 0.80, ICC ≥ 0.85 (all 4 coders) | 📘📗 |
| W1 | Full-text eligibility 완료 | ~300 MASEM-eligible studies 확정 | 📘📗 |
| W1 | 100-study sample 확정 | Stratified sample 추출 완료 | 📘 |
| W1 | AI extraction 완료 (100) | 3 models × 100 studies JSON 생성 | 📘 |
| W4 | Phase 1 IRR 확인 | κ ≥ 0.85, ICC ≥ 0.90 (both pairs) | 📘 |
| W4 | Gold standard 확정 | 100 studies × 30 variables resolved | 📘📗 |
| W4 | Paper B 분석 완료 | RQ1-4 실행 | 📘 |
| W6 | Phase 2 완료 | ~150 studies verified (R1-R4 equal split) | 📗 |
| W7 | QA spot-check 통과 | Error rate < 5% | 📗 |
| W7 | Paper B draft v2.0 | Results + figures 완성 | 📘 |
| W8 | Data freeze | 전체 ~300 studies 확정 | 📗 |

---

## Risk Mitigation

| 리스크 | 확률 | 대응 | 영향 |
|--------|------|------|------|
| Full-text 접근 불가 (>10%) | 중 | ILL 조기 요청, 저자 연락 | 📘📗 |
| Calibration 실패 (κ < 0.80) | 낮 | 추가 training session, pilot 5개 추가 (all 4 coders) | 📘📗 |
| Phase 1 IRR 미달 (either pair) | 낮 | 코딩 규칙 명확화, 10개 재코딩 | 📘 |
| AI extraction pipeline 오류 | 중 | Week 1에 10개 test run 선행 | 📘 |
| Phase 2 일정 지연 | 중 | Phase 2 volume 조정, 우선순위 재배정 | 📗 |
| Paper B 작성 지연 | 낮 | Week 4-5 분석/작성 병행 | 📘 |
