# Paper A C-tier full10 ordered review log

Date: 2026-06-14

## User-selected route

- Review all `C_open_table_for_possible_full10_densification` rows in full10 pair order.
- Full10 construct order: `PE, EE, SI, FC, ATT, SE, TRU, ANX, BI, UB`.

## Generated review work products

- A spot-check worksheet: `data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/paper_a_A_fast_confirm_study_level_spotcheck_worksheet_20260614.csv`
- C full10 ordered queue: `data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/paper_a_C_full10_pair_ordered_densification_review_queue_20260614.csv`
- C batch 01: `data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/paper_a_C_full10_pair_ordered_batch01_20260614.csv`
- C batch 01 initial evidence draft: `data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/paper_a_C_batch01_initial_source_evidence_draft_20260614.csv`

## Initial C review: pair order 03, FC-PE

`PE-EE` and `PE-SI` had no possible densification candidate rows, so the first actionable pair in full10 order is `FC-PE`.

| study_id | preliminary result | reason |
| --- | --- | --- |
| S036 | exclude_or_defer_not_promote | failed_or_unresolved_FC_not_visible_as_full10_FC |
| S138 | exclude_or_defer_not_promote | failed_or_unresolved_FC_not_visible_as_full10_FC |

## Methodological note

The first actionable full10 pair shows that the queue must pass a construct-mapping gate before value extraction. If a source packet has a visible correlation table but the target full10 construct is not present under the project construct definition, the row should not be promoted merely because nearby TAM/AI constructs are visible.

## Next review item

Continue with pair order 04 `ATT-PE` in `paper_a_C_full10_pair_ordered_batch01_20260614.csv`.


## 2026-06-14 pair 04_ATT-PE preliminary source review

- 대상 row: 13
- 예비 결론: 승격 후보 0개. 모든 row에서 PE/PU 대응 construct는 확인되지만 full10 `ATT` 측정 construct가 보이지 않아 `do_not_promote_construct_mapping_failure_no_ATT`로 분류했다.
- 산출물: `paper_a_C_pair04_ATT_PE_source_evidence_draft_20260614.csv`, `PAPER_A_C_PAIR04_ATT_PE_REVIEW_LOG_KO_20260614.md`
- 다음 pair: `05_PE-SE`


## 2026-06-14 pair 05_PE-SE preliminary source/PDF review

- 대상 row: 13
- 예비 결론: 즉시 승격 0개, 조건부 후보 2개 (`S121-1=.40`, `S121-2=.30`, Figure 2 Spearman r).
- 조건: `genAI-related subjective competence`를 full10 `SE`로 인정할지 연구자 확인 필요.
- 제외 원칙: `PBC`, `Security`, 일반 efficacy 표현, 참고문헌의 self-efficacy는 full10 `SE`로 자동 매핑하지 않는다.
- 산출물: `paper_a_C_pair05_PE_SE_source_evidence_draft_20260614.csv`, `PAPER_A_C_PAIR05_PE_SE_REVIEW_LOG_KO_20260614.md`
- 다음 pair: `06_PE-TRU`

## 2026-06-14 researcher approval - pair 05_PE-SE S121 supplement

- Researcher approved the construct mapping `genAI-related subjective competence` -> full10 `SE`.
- Promoted two S121 PE-SE rows into researcher-approved supplement staging: `S121-1=.40` and `S121-2=.30`.
- Source: `S121.pdf` p.8 Figure 2, source-reported Spearman correlation heatmap.
- Non-approved exclusions remain unchanged: PBC, Security, generic efficacy language, and reference/background self-efficacy are not full10 SE.

## 2026-06-14 pair 06_PE-TRU preliminary source/PDF review

- 대상 row: 10
- 예비 결론: 승격 후보 0개, 조건부 후보 0개.
- 핵심 제외 원칙: `insecurity`, `privacy concerns`, `psychological risk`, `perceived risk`, `habit`, `perceived competence`, `perceived enjoyment`는 full10 `TRU`로 자동 매핑하지 않는다.
- 산출물: `paper_a_C_pair06_PE_TRU_source_evidence_draft_20260614.csv`, `PAPER_A_C_PAIR06_PE_TRU_REVIEW_LOG_KO_20260614.md`
- 다음 pair: `07_ANX-PE`

## 2026-06-14 pair 07_ANX-PE preliminary source/PDF review

- 대상 row: 14
- 예비 결론: 즉시 승격 0개, 조건부 후보 2개 (`S121-1=-0.23`, `S121-2=-0.08`, Figure 2 Spearman r).
- 조건: `threat appraisal`을 full10 `ANX`로 인정할지 연구자 확인 필요.
- 제외 원칙: `perceived risk`, `innovative resistance`, `trust`, `privacy/security`, `reference-only anxiety`, `challenge appraisal`은 full10 `ANX`로 자동 매핑하지 않는다.
- 산출물: `paper_a_C_pair07_ANX_PE_source_evidence_draft_20260614.csv`, `PAPER_A_C_PAIR07_ANX_PE_REVIEW_LOG_KO_20260614.md`
- 다음 pair: `08_BI-PE`

## 2026-06-15 batch triage after S121 ANX rejection

- Researcher rejected `threat appraisal` -> full10 `ANX`; pair 07 final promoted rows remain 0.
- Remaining C-tier full10 queue rows triaged at once: 413 rows across 36 pair labels.
- Batch-safe source-visible numeric-cell candidates: 7 rows, all from `S048` Table 2.
- Rows closed/held without promotion: S004 SE-related rows closed because `PKC -> SE` is not approved; S072 rows held for construct-mapping audit; all one/no-human-supported-construct rows remain excluded unless reopened by source adjudication.
- Next action: researcher confirms or rejects the seven S048 source-visible values before any supplemental input or model-family MASEM rerun.
