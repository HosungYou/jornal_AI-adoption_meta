# 6주 실행 Timeline

## Paper A / Paper B 범위 표시

```
📘 = Paper B 범위 (100 studies, AI vs. Human 비교)
📗 = Paper A 범위 (전체 ~300 studies, MASEM 데이터)
📘📗 = 양쪽 모두 해당
```

## 전체 일정

```
Week 1 ──── Setup + Full-text Review + AI Extraction     📘📗
Week 2 ──── Phase 1: Independent Human Coding (시작)      📘📗
Week 3 ──── Phase 1: Coding 완료 + IRR + Gold Standard   📘📗
Week 4 ──── Phase 1 분석 📘 + Phase 2 시작 📗
Week 5 ──── Phase 2 완료 + Phase 3 QA 📗 + Paper B 작성 📘
Week 6 ──── Paper B 완성 📘 + Data Freeze 📗
```

---

## Week 1: Setup + Full-text Review + AI Extraction 📘📗

| Day | 작업 | 담당 | 산출물 | 범위 |
|-----|------|------|--------|------|
| 1-2 | Full-text PDF 수집 (575개) | H1 | PDFs | 📘📗 |
| 1-2 | Full-text eligibility review 시작 | H1 | — | 📘📗 |
| 3 | Calibration session (H1+H2, pilot 10개) | H1, H2 | Pilot IRR | 📘📗 |
| 3-5 | Full-text eligibility review 완료 | H1 | fulltext_eligibility_decisions.csv | 📘📗 |
| 5 | MASEM-eligible ~300개 확정 | H1 | eligible list | 📘📗 |
| 5 | 100-study stratified sample 추출 | H1 | paper_b_sample_100.csv | 📘 |
| 5-7 | 3 AI models extract 100 studies | Pipeline | 02_ai_extraction/ | 📘 |
| 5-7 | 3 AI models extract 나머지 ~200 studies | Pipeline | 02_ai_extraction/ | 📗 |
| 6-7 | H2: 30% full-text IRR sample 독립 review | H2 | fulltext_irr_sample.csv | 📘📗 |

## Week 2: Phase 1 — Independent Human Coding 📘📗

| Day | 작업 | 담당 | Pace | 범위 |
|-----|------|------|------|------|
| 1-5 | 100 studies 독립 코딩 | H1 | 20/day | 📘📗 |
| 1-5 | 100 studies 독립 코딩 | H2 | 20/day | 📘📗 |

**Daily target**: 각자 20 studies/day × 5 days = 100 studies
**예상 소요**: ~30-45 min/study × 20 = 10-15 hours/day (intensive)
**핵심**: H1, H2 모두 AI output에 blinded 상태 유지

## Week 3: Phase 1 — IRR + Gold Standard 📘📗

| Day | 작업 | 담당 | 산출물 | 범위 |
|-----|------|------|--------|------|
| 1-2 | 코딩 완료 + 제출 | H1, H2 | coder1_PI/, coder2_phd1/ | 📘📗 |
| 2-3 | **Unblinding**: IRR 계산 | H1 | irr_results.csv | 📘 |
| 3-4 | Discrepancy identification | H1 | discrepancy_log.csv | 📘📗 |
| 4-5 | Discrepancy resolution meeting | H1, H2 | resolved values | 📘📗 |
| 5 | Gold standard finalization | H1 | gold_standard_100.csv | 📘📗 |

## Week 4: Paper B 분석 📘 + Phase 2 시작 📗

| Day | 작업 | 담당 | 산출물 | 범위 |
|-----|------|------|--------|------|
| 1 | AI consensus 계산 (100 studies) | H1 | consensus_100.csv | 📘 |
| 1-2 | RQ1-4 분석 실행 | H1 | model_accuracy.csv 등 | 📘 |
| 3-5 | AI consensus 검증 (~200 studies) | H1 | ~100 studies | 📗 |
| 3-5 | AI consensus 검증 (~200 studies) | H2 | ~100 studies | 📗 |

**Phase 2 pace**: 각자 20 studies/day (verification mode, 독립 코딩보다 빠름)

## Week 5: Phase 2 완료 📗 + Paper B 작성 📘

| Day | 작업 | 담당 | 산출물 | 범위 |
|-----|------|------|--------|------|
| 1-2 | Phase 2 verification 완료 | H1, H2 | verified_data_phase2.csv | 📗 |
| 1-2 | Paper B Tables 5-10 채우기 | H1 | Results section | 📘 |
| 2-3 | Figures 생성 (heatmap, Bland-Altman) | H1 | figures/ | 📘 |
| 3-4 | H3: 10% spot-check (~20 studies) | H3 | qa_spotcheck.csv | 📗 |
| 4-5 | QA gates 확인 | H1 | qa_report.md | 📗 |

## Week 6: Paper B 완성 📘 + Data Freeze 📗

| Day | 작업 | 담당 | 산출물 | 범위 |
|-----|------|------|--------|------|
| 1-2 | Paper B Discussion + Conclusion | H1 | 논문 v2.0 | 📘 |
| 2-3 | PRISMA-trAIce + TRIPOD-LLM 완성 | H1 | checklists/ | 📘 |
| 3-4 | 내부 검토 | H1, H2 | 피드백 | 📘 |
| 5 | Data finalization (전체 ~300) | H1 | 전체 데이터 확정 | 📗 |
| 6-7 | OSF 등록 (prompts, data, code) | H1 | OSF project | 📘📗 |

---

## Milestones & Checkpoints

| Week | Milestone | 성공 기준 | 범위 |
|------|-----------|----------|------|
| W1 | Full-text eligibility 완료 | ~300 MASEM-eligible studies 확정 | 📘📗 |
| W1 | 100-study sample 확정 | Stratified sample 추출 완료 | 📘 |
| W1 | AI extraction 완료 (100) | 3 models × 100 studies JSON 생성 | 📘 |
| W1 | Calibration 통과 | Pilot κ ≥ 0.80, ICC ≥ 0.85 | 📘📗 |
| W3 | Phase 1 IRR 확인 | κ ≥ 0.85, ICC ≥ 0.90 | 📘 |
| W3 | Gold standard 확정 | 100 studies × 30 variables resolved | 📘📗 |
| W4 | Paper B 분석 완료 | RQ1-4 실행 | 📘 |
| W5 | Phase 2 완료 | ~200 studies verified | 📗 |
| W5 | QA spot-check 통과 | Error rate < 5% | 📗 |
| W6 | Paper B draft v2.0 | Results + figures 완성 | 📘 |
| W6 | Data freeze | 전체 ~300 studies 확정 | 📗 |

---

## Risk Mitigation

| 리스크 | 확률 | 대응 | 영향 |
|--------|------|------|------|
| Full-text 접근 불가 (>10%) | 중 | ILL 조기 요청, 저자 연락 | 📘📗 |
| Calibration 실패 (κ < 0.80) | 낮 | 추가 training session, pilot 5개 추가 | 📘📗 |
| Phase 1 IRR 미달 | 낮 | 코딩 규칙 명확화, 10개 재코딩 | 📘 |
| AI extraction pipeline 오류 | 중 | Week 1에 10개 test run 선행 | 📘 |
| Phase 2 일정 지연 | 중 | Phase 2 volume 조정, 우선순위 재배정 | 📗 |
| Paper B 작성 지연 | 낮 | Week 4-5 분석/작성 병행 | 📘 |
