# Phase 2 Source-Value Decision Log

Date: 2026-06-08

Boundary: These entries document Step 3 source-document adjudication only. They
do not freeze the Step 4 source-anchored adjudicated human reference standard
and do not authorize Step 5 LLM comparison or MASEM substitution.

## S195/S206 - duplicate source and no usable target construct matrix

- Phase/pair: `S195` = Phase 2 Pair C, R1 + R4; `S206` = Phase 2 Pair D, R2 + R3.
- Field or construct pair: duplicate-source status and all one-coder-only target rows carried by `S195`.
- Raw values:
  - `S195`: R1/R4 normalized to excluded, but the disagreement queue still carries R1 one-coder-only values for `BI-PE`, `BI-UB`, `EE-UB`, `PE-UB`, and `SI-UB`.
  - `S206`: R2/R3 excluded with metadata-only disagreement and no coder correlation rows.
- Source location: local `S195.pdf` and `S206.pdf`; Figure 3, Table 3, and Table 4.
- Evidence type: duplicate PDF/source plus PLSR loading/variance evidence; no usable construct-level target correlation or standardized SEM/path table.
- Priority: P0.
- Decision: Use `S195` as the canonical duplicate audit row, mark `S206` as duplicate of `S195`, and exclude the `S195` one-coder-only target rows from the reference matrix.
- Rule applied: duplicate sources are not counted twice; item/image-only correlations and PLSR component loadings do not populate target construct-pair evidence.
- Rationale: The local audit recorded identical SHA-256 for `S195.pdf` and `S206.pdf`, and the source evidence does not provide a usable construct-level target matrix for Paper B.
- Adjudicator: Codex source check for researcher review.
- Follow-up: In Step 4, preserve one canonical duplicate/exclusion audit note and do not count `S206` as a second study/source record.

## S202 - AI-driven LMS administrative automation

- Phase/pair: Phase 2 Pair D, R2 + R3.
- Field or construct pair: study-level target-matrix eligibility.
- Raw values:
  - R2: `review_source`; no retained target rows.
  - R3: `review_source`; no retained target rows.
- Source location: local `S202.pdf`, research model, Table 4, and Table 5.
- Evidence type: SEM path coefficients and Fornell-Larcker-style off-diagonal construct correlations.
- Priority: P0.
- Decision: `exclude_study` from the Paper B target MASEM matrix.
- Rule applied: focal-technology boundary supersedes numeric availability.
- Rationale: Although the source contains numeric SEM evidence, the focal technology is AI-driven LMS administrative automation/student readiness rather than the current Paper B AI-adoption target universe.
- Adjudicator: Codex source check for researcher review.
- Follow-up: In Step 4, preserve the exclusion rationale and do not use the numeric source evidence for target rows.

## S014 - AI-based data-analysis tool adoption among academic researchers

- Phase/pair: Phase 2 Pair C, R1 + R4.
- Field or construct pair: `PE-UB`; `SI-UB`.
- Raw values:
  - R1: `PE-UB = 0.31`, `SI-UB = 0.30`, both beta-converted from Table 4 and noted as indirect effects through perceived risk.
  - R4: no retained values; `review_source`.
- Source location: `source_pdfs/S014.pdf`, Results 4.3 and Table 4; Table 3 HTMT checked as disallowed evidence.
- Evidence type: indirect mediated PLS-SEM effects and HTMT discriminant-validity ratios; no direct standardized mapped target-pair coefficient found.
- Priority: P1.
- Decision: `exclude_row` for the two R1 indirect-effect rows. `S014` remains population-eligible, but it contributes no extractable target-matrix values from this source check.
- Rule applied: HTMT values are not usable target correlations; indirect perceived-risk effects are not admissible as direct target-pair reference values; beta-to-r applies only to direct standardized path coefficients for mapped target constructs.
- Rationale: Table 4 reports `PU PR ADPT` and `SI PR ADPT` indirect effects plus interaction effects via perceived risk. Those paths do not supply direct `PE-UB` or `SI-UB` coefficients after the perceived-risk exclusion rule is applied.
- Adjudicator: Codex source check for researcher review.
- Follow-up: In Step 4, remove the two R1 candidate rows from the target reference matrix unless the researcher later supplies a separate direct-path source not found in this PDF check.

## S021 - GenAI acceptance among higher-education staff pre/post training

- Phase/pair: Phase 2 Pair D, R2 + R3.
- Field or construct pair: limited main-PDF primary-model row set for `ATT-BI`, `BI-UB`, `EE-BI`, `FC-BI`, `PE-BI`, and `SI-BI`, with T1 and T2 as separate strata.
- Raw values:
  - R2: `review_source`; metadata/source review only.
  - R3: `review_source`; metadata/source review only.
- Source location: `source_pdfs/S021.pdf`, Results 4.2-4.3, Figures 1-2; online Springer supplementary files copied to `source_pdfs/S021_supplementary_file1.pdf` and `source_pdfs/S021_supplementary_file2.docx`.
- Evidence type: PLS-SEM standardized path coefficients in main text/Figure 1; Supplementary Table S4 reports `f Squared` effect sizes, not path coefficients or a correlation matrix.
- Priority: P1.
- Decision: `include_limited_main_pdf_primary_model`. Include S021 in the Step 4 draft using the source-transcribed primary Model 1 row set recorded in `s021_primary_model_row_set_20260608.md`.
- Rule applied: preserve T1/T2 strata if retained; do not pool pre/post coefficients.
- Rationale: The main PDF confirms separate T1/T2 PLS-SEM models and reports standardized path coefficients in Figure 1 and prose. The recovered Supplementary Table S4 is auditable, but it only reports `f Squared` effect sizes for paths, so it is not used as coefficient evidence. The researcher decided to include S021 using the limited main-PDF primary Model 1 row set. `Habit` and `Hedonic motivation` are excluded from the target row set, AIAS-4 is retained as `ATT` with medium mapping confidence, and cross-time paths are excluded because T1/T2 are retained as separate strata.
- Adjudicator: Codex source check for researcher review.
- Follow-up: In Step 4, apply the T1 and T2 rows separately, mark evidence type as beta-converted path evidence, record original beta values, and flag S021 for beta-converted sensitivity analysis.

## S056 - ChatGPT acceptance among CFL learners

- Phase/pair: Phase 2 Pair D, R2 + R3.
- Field or construct pair: `ATT-EE`; `ATT-PE`; `EE-PE`.
- Raw values:
  - R2: `ATT-EE = 0.437`, `ATT-PE = 0.489`, `EE-PE = 0.541`, beta-converted from Table 3 path coefficients.
  - R3: no retained values; `review_source`.
- Source location: `source_pdfs/S056.pdf`, Table 2 and Table 3.
- Evidence type: Table 2 Fornell-Larcker off-diagonal construct correlations; Table 3 standardized path coefficients.
- Priority: P1.
- Decision: `source_corrected`. Use Table 2 source-reported construct correlations as the primary source if `S056` is retained: `ATT-EE = 0.816`, `ATT-PE = 0.803`, and `EE-PE = 0.854`. Do not freeze the R2 beta-converted Table 3 values as the primary row values.
- Rule applied: source-reported target-construct correlations supersede beta-converted path coefficients when available; do not use Fornell-Larcker diagonals as correlations.
- Rationale: The PDF states that discriminant validity was established through Fornell-Larcker correlations, and Table 2 reports off-diagonal target-construct correlations for `PU`, `PEU`, and `AT`. These map to `PE`, `EE`, and `ATT`, respectively. Table 3 path coefficients remain useful audit evidence but are secondary under the current evidence-type rule.
- Adjudicator: Codex source check for researcher review.
- Follow-up: Step 4 reference construction should use the source-corrected Table 2 values or explicitly record a researcher override if path coefficients are preferred for this study.

## S092 - ChatGPT adoption among ESP/business-communication students

- Phase/pair: Phase 2 Pair D, R2 + R3.
- Field or construct pair: `BI-EE`; `BI-PE`; `EE-PE`.
- Raw values:
  - R2: `review_source`.
  - R3: `BI-EE = 0.174`, `BI-PE = 0.234`, `EE-PE = 0.354`, marked as beta-converted from standardized SEM paths in the coder return.
- Source location: `source_pdfs/S092.pdf`, Table 3.
- Evidence type: standardized SEM path coefficients.
- Priority: P1.
- Decision: `accept_R3_source_beta_corrected` for the three target rows under the beta-to-r rule. The source Table 3 standardized betas are `BI-EE beta = 0.174`, `BI-PE beta = 0.234`, and `EE-PE beta = 0.354`; Step 4 should carry Peterson-Brown converted `r` values `BI-EE = 0.224`, `BI-PE = 0.284`, and `EE-PE = 0.404`, with the source betas recorded in `original_beta`.
- Rule applied: beta-to-r may be used for direct standardized path coefficients when no usable target correlation matrix is reported.
- Rationale: Table 3 reports direct standardized path estimates from perceived ease of participation to perceived usefulness and intention to use ChatGPT, and from perceived usefulness to intention. The PDF describes squared inter-construct correlation checks but does not report target correlation coefficients. Privacy concerns, security concerns, peer behavior, and academic integrity paths are not retained as target construct rows in this decision.
- Adjudicator: Codex source check for researcher review.
- Follow-up: Carry the accepted target rows into the Step 4 reference draft with source type marked as standardized SEM path/beta-converted, original betas retained, and Peterson-Brown converted `r` values used as the draft `r_value`.

## S121 - GenAI use and intention among Austrian students and teachers

- Phase/pair: Phase 2 Pair D, R2 + R3.
- Field or construct pair: one-coder-only R2 Figure 2 direct correlation rows involving `BI`, `EE`, `FC`, `PE`, `SI`, `TRU`, `UB`, and `SE`.
- Raw values:
  - R2: 21 direct Figure 2 rows.
  - R3: no retained values; `review_source`.
- Source location: `data/02_screening/pdfs/S121.pdf`, Figure 2, page 8.
- Evidence type: Spearman correlation heatmaps for students and teachers.
- Priority: P1.
- Decision: `source_corrected_row_set_ready_for_step4_draft`. Use Figure 2 Spearman correlations as preferred source evidence, with students and teachers handled as separate samples. The source-transcribed row set is recorded in `s121_figure2_row_set_20260608.md`.
- Rule applied: source-reported direct correlations supersede SEM/PLS paths when available; do not pool student and teacher samples.
- Rationale: Figure 2 reports separate student and teacher heatmaps. The Step 3 row-set artifact transcribes all Figure 2 correlations among the mapped target constructs `BI`, `UB`, `PE`, `EE`, `SI`, `FC`, `TRU`, and `SE`. `SE` is retained as a self-efficacy/competence analogue with medium construct-mapping confidence because the source label is `genAI-related subjective competence`. The earlier R2 candidate mismatches are resolved: student `FC-UB` is `0.29` rather than `0.16`, and student `PE-SE` is `0.40` rather than `0.29`; the displaced values correspond to `FC-TRU` and `SE-SI`, respectively.
- Adjudicator: Codex source check for researcher review.
- Follow-up: In Step 4, apply the student and teacher rows separately, keep source type as direct Spearman correlation, and carry a medium-confidence construct-mapping flag for `SE`.
