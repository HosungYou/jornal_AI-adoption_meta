# Phase 2 Source-Adjudication Evidence Split

Date: 2026-05-29
Scope: S195/S206 duplicate-source exclusion plus S014/S021/S056/S092/S121/S202 source-review decisions before the Paper B reference-standard freeze.
Boundary: This note uses existing local repository evidence and locally available PDFs only. It does not edit raw coder workbooks and does not write Step 5/LLM comparison outputs.

## Decision Rules Applied

- Inclusion requires an educational population or setting and either a correlation matrix or standardized path coefficients with at least two target constructs (`data/04_extraction/00_protocol/AI_Adoption_MASEM_Coding_Manual_v2.md`).
- For correlation extraction, use source-reported target-construct correlations where available. Do not use HTMT, CR, AVE, or diagonal square-root AVE values as construct correlations.
- Use standardized path coefficients only under the beta-to-r rule when no usable correlation matrix is reported and the coefficient is a direct path for mapped target constructs.
- Perceived risk or risk concern is excluded by default unless the source definition explicitly measures anxiety, fear, apprehension, or threat affect.
- E-FT1 applies when fewer than two usable construct-pair statistics are available.
- Duplicate sources or duplicate samples should not be counted twice in the reference standard.

## Evidence Inventory

- Primary pre-adjudication queue: `data/04_extraction/02_pre_adjudication_disagreement/combined/derived/combined_correlation_review_queue_20260525.csv`.
- Source-check ledger: `data/04_extraction/03_source_document_adjudication/phase2/phase2_exclusion_source_check_20260525.md`.
- Source-check candidate table: `data/04_extraction/03_source_document_adjudication/phase2/phase2_source_check_candidates_20260525.csv`.
- Assignment evidence: `data/04_extraction/02_pre_adjudication_disagreement/combined/derived/combined_study_review_queue_20260525.csv`.
- Long coder-value file used read-only: `data/04_extraction/02_pre_adjudication_disagreement/combined/derived/combined_coder_values_long_20260525.csv`.
- Pairwise disagreement file used read-only: `data/04_extraction/02_pre_adjudication_disagreement/phase2/derived/phase2_pairwise_disagreement_long_20260525.csv`.
- Local PDFs already present and text-checked: `data/02_screening/pdfs/S121.pdf`, `data/02_screening/pdfs/S195.pdf`, `data/02_screening/pdfs/S202.pdf`, `data/02_screening/pdfs/S206.pdf`.
- Additional local source PDFs secured on 2026-06-08 from the OneDrive PDF archive into the ignored adjudication source-PDF folder: `data/04_extraction/03_source_document_adjudication/source_pdfs/S014.pdf`, `S021.pdf`, `S056.pdf`, and `S092.pdf`.
- `S021` online supplementary files were recovered from Springer on 2026-06-08 and copied into the ignored source-PDF folder as `S021_supplementary_file1.pdf` and `S021_supplementary_file2.docx`. `Supplementary Table S4` reports `f Squared` effect sizes, not target path coefficients or correlations.

## Researcher Decisions Recorded 2026-06-08

These decisions were provided by the researcher after the evidence split was
prepared. They update the freeze plan but do not themselves create a frozen
reference file.

| Item | Researcher decision | Operational implication |
|---|---|---|
| S195/S206 duplicate handling | Use S195 as the canonical duplicate audit row and mark S206 as duplicate of S195. | Freeze S195/S206 as exclusion/duplicate decisions; do not count the duplicated source twice. |
| S014 indirect effects | Indirect mediated effects through perceived risk are not admissible as direct target-pair reference values. | Drop R1's indirect PE/SI -> perceived-risk -> adoption rows from candidate reference values unless a source PDF shows separate direct standardized mapped paths. |
| S021 wave handling | Use separate T1/T2 strata. | Do not pool pre- and post-training coefficients into one row set; source extraction must preserve time-point strata. |
| S014 population eligibility | Academic researchers/faculty are eligible under the Paper B educational-population rule. | S014 should not be excluded on population grounds; remaining exclusion or inclusion depends on usable direct target-pair evidence. |
| S014/S021/S056/S092 assignment and source-access check | Assignment confirmed from the combined study review queue: S014 = Pair C (R1+R4); S021/S056/S092 = Pair D (R2+R3). PDFs are now available in the ignored local adjudication source-PDF folder. | These are assigned review-source items with source-PDF access, but source locations, construct mapping, and values still need adjudication before any extractable values are frozen. |
| S121 sample handling | Split students and teachers as separate samples when teacher values are extracted. | Do not pool student and teacher estimates; freeze separate strata only after source-location/value transcription. |
| S202 focal-technology rule | Do not include AI-driven LMS administrative automation inside the Paper B AI-adoption target universe. | Exclude S202 from the target MASEM matrix despite local numeric SEM evidence. |

## Source-Value Update Recorded 2026-06-08

Source-value checks were added to
`data/04_extraction/03_source_document_adjudication/phase2/decision_log_20260608.md`.
They do not freeze the reference standard, but they narrow the Step 3 queue:

| Study | Source-value status | Operational implication |
|---|---|---|
| S195/S206 | Duplicate/exclusion decision logged. | Use `S195` as the canonical duplicate audit row, mark `S206` as duplicate, and exclude the carried S195 one-coder-only target rows. |
| S202 | Target-matrix exclusion decision logged. | Exclude AI-driven LMS administrative automation from the Paper B target MASEM matrix despite local numeric SEM evidence. |
| S014 | Source-checked; Table 4 contains indirect and interaction effects via perceived risk, and Table 3 is HTMT. No direct standardized mapped target-pair coefficient was found. | Exclude R1's `PE-UB = 0.31` and `SI-UB = 0.30` candidate rows from the target matrix unless a separate direct-path source is later supplied. |
| S021 | Main PDF and online supplement source-checked; Supplementary Table S4 is `f Squared` effect sizes only. Researcher decision is to include a limited main-PDF primary Model 1 row set. | Apply the T1/T2 beta-converted rows recorded in `s021_primary_model_row_set_20260608.md`; do not treat Table S4 as a coefficient source. |
| S056 | Source-checked; Table 2 provides source-reported construct correlations, while Table 3 provides standardized paths. | Source-correct the three R2 beta-converted rows to Table 2 values if retained: `ATT-EE = 0.816`, `ATT-PE = 0.803`, `EE-PE = 0.854`. |
| S092 | Source-checked; Table 3 provides direct standardized SEM paths and no usable target correlation matrix was reported. | Accept the three mapped R3 rows, but treat the source values as original standardized betas: `BI-EE beta = 0.174`, `BI-PE beta = 0.234`, `EE-PE beta = 0.354`; Step 4 converted `r` values are `0.224`, `0.284`, and `0.404`. |
| S121 | Figure 2 source-checked and full student/teacher target row set transcribed in `s121_figure2_row_set_20260608.md`. | Apply separate student and teacher rows in Step 4; correct student `FC-UB` to `0.29` and student `PE-SE` to `0.40`; retain `SE` as a medium-confidence subjective-competence/self-efficacy mapping. |

## Source-Anchored Recommendations

| Study | Evidence Type / Source Location | Raw Coder Conflict | Rule Applied | Recommendation | Unresolved Questions | Can Enter Reference Freeze? |
|---|---|---|---|---|---|---|
| S195 | Local PDF `S195.pdf`; same DOI/PDF hash as S206. Source-check points to Figure 3, Table 3, and Table 4. Local PDF text confirms an item/variable correlation figure plus PLSR loading/variance tables rather than a construct-level correlation or path table. | Queue: R1 and R4 both normalized to `excluded`, but disagreement rows still carry five R1 one-coder-only direct values (BI-PE, BI-UB, EE-UB, PE-UB, SI-UB). | E-FT1; do not code item-level/image-only correlations or PLSR component loadings as target construct-pair evidence; duplicate-source guard with S206. | Freeze as confirmed exclusion; drop all S195 one-coder-only values from the reference matrix. | None material for exclusion. Record duplicate link to S206 and identical SHA-256 in audit notes. | Yes, as an exclusion decision only. |
| S206 | Local PDF `S206.pdf`; identical SHA-256 and same DOI as S195. Source-check points to the same Figure 3/Table 3/Table 4 evidence. | Queue: R2 and R3 both `excluded`, with metadata-only disagreement and no coder correlation rows. | E-FT1; duplicate-source guard with S195. | Freeze as confirmed exclusion; do not retain as a second study/source record. | None material for exclusion. Choose one canonical duplicate-exclusion note so S195/S206 are not counted twice. | Yes, as an exclusion decision only. |
| S014 | Existing source-check says PLS-SEM path analysis for AI-based data-analysis tool adoption among academic researchers, with source locations Abstract, Figure 1, Results 4.3, and Table 4. Local source PDF is now available in `source_pdfs/S014.pdf`; text extraction confirms the academic-researcher setting. | Queue: R1 `done` with indirect PE/SI -> perceived-risk -> adoption beta-converted rows; R4 `review_source` and no values. R4 notes say Table 4 reports indirect/interaction effects, HTMT is available but disallowed, and no direct standardized mapped-pair coefficients were coded. | HTMT exclusion; perceived-risk exclusion-by-default; beta-to-r only for standardized direct path coefficients, not mediated indirect effects. The researcher confirmed that indirect mediated effects through perceived risk are not admissible as direct target-pair reference values and that academic researchers/faculty are eligible educational populations. | Do not freeze R1's two indirect-effect rows as reference values. Keep S014 in adjudication as a source-review item; likely final matrix value is no usable target pair unless the PDF shows separate direct standardized coefficients for mapped target pairs. | Source PDF is now available; final source check must confirm whether Table 4 or other source locations contain direct target-pair coefficients separate from indirect perceived-risk effects. | No, not as extractable values until direct source evidence is checked. |
| S021 | Existing source-check says PLS-SEM paths for genAI acceptance among higher-education staff before/after training, with source locations Abstract, Methods 3.4, Results 4.2-4.3, Figures 1-2, and Supplementary Table S4. Local source PDF is available in `source_pdfs/S021.pdf`; Springer supplementary files are available as `source_pdfs/S021_supplementary_file1.pdf` and `source_pdfs/S021_supplementary_file2.docx`. Supplementary Table S4 is an `f Squared` effect-size table, not a path-coefficient or correlation source. Source row set is transcribed in `s021_primary_model_row_set_20260608.md`. | Queue: both R2 and R3 are `review_source`; no coder correlation rows appear in the pairwise disagreement extract. | Inclusion criteria allow standardized paths, but pre/post T1/T2 construct separation must be preserved. `f Squared` values are not target correlations and are not beta-to-r inputs. | Include as limited primary Model 1 main-PDF beta-converted row set: `ATT-BI`, `BI-UB`, `EE-BI`, `FC-BI`, `PE-BI`, and `SI-BI` for both T1 and T2. | None blocking for source-value transcription; Step 4 should preserve T1/T2 strata, exclude Habit/Hedonic Motivation/cross-time paths, and mark AIAS-4-to-`ATT` mapping confidence as medium. | Yes, as source-transcribed rows for Step 4 draft, not yet frozen. |
| S056 | Existing source-check says TAM/PLS-SEM standardized path coefficients for ChatGPT acceptance among CFL learners, source locations Abstract, Methods 3.4, Results 4.1.2, and Table 3. Local source PDF is now available in `source_pdfs/S056.pdf`; text extraction confirms the CFL learner and Table 3 path-result context. | Queue: R2 `done`; R3 `review_source`; three one-coder-only beta-converted rows from R2 (ATT-EE, ATT-PE, EE-PE). | Beta-to-r conversion is allowed for standardized path coefficients when no usable correlation matrix is reported; source location must be verified. | Candidate for inclusion, but do not freeze until Table 3 is source-checked and construct directions are confirmed. | Confirm whether coded ATT-EE/ATT-PE/EE-PE values are direct standardized paths or transformed correlations; confirm whether any direct Pearson/latent correlations supersede paths. | Conditional no: source-PDF access is ready, but values are not freeze-ready until Table 3 is adjudicated. |
| S092 | Existing source-check says SEM model fit and standardized path estimates for ChatGPT adoption among ESP/business-communication students, source location Table 3. Local source PDF is now available in `source_pdfs/S092.pdf`; text extraction confirms the ESP/business-communication student setting. | Queue: R2 `review_source`; R3 `done`; three one-coder-only beta-converted rows from R3 (BI-EE, BI-PE, EE-PE). | Beta-to-r conversion may be admissible for standardized SEM paths; source table and construct mapping must be checked. | Candidate for inclusion, but freeze only after Table 3 or Figure 3 confirms standardized coefficients and target constructs. | Confirm source table/figure values, coefficient standardization, and whether integrity/privacy/ease constructs map or stay excluded. | Conditional no: source-PDF access is ready, but values are not freeze-ready until source table/figure adjudication is complete. |
| S121 | Local PDF `S121.pdf`; source-check says UTAUT/SEM/PLS-SEM evidence for genAI use/intention among Austrian higher-education students and teachers. PDF text confirms SEM path estimates for students and teachers plus correlation heatmaps in Figure 2. Full target row set is transcribed in `s121_figure2_row_set_20260608.md`. | Queue: R2 `done`; R3 `review_source`; 21 R2 one-coder-only direct rows involving BI, EE, FC, PE, SI, TRU, UB, and SE. | Available-case direct correlations are preferred when source Figure 2 gives target-construct correlations. Student and teacher estimates must be handled as separate samples. `SE` is retained as a medium-confidence subjective-competence/self-efficacy mapping; intrinsic motivation, challenge appraisal, and threat appraisal are not transcribed into the target row set. | Include-candidate with sufficient local source evidence. Step 4 can apply separate student and teacher Figure 2 rows with source type marked as direct Spearman correlation. | None blocking for source-value transcription; Step 4 should preserve the `SE` mapping-confidence flag. | Yes, as source-transcribed rows for Step 4 draft, not yet frozen. |
| S202 | Local PDF `S202.pdf`; source-check says SEM path coefficients plus a Fornell-Larcker-style construct correlation table for AI-driven LMS automation and student readiness, source locations Research model, Table 4, and Table 5. PDF text confirms Table 4 off-diagonal construct correlations and Table 5 standardized SEM path coefficients. | Queue: both R2 and R3 `review_source`; no pairwise value rows, metadata conflict only. R2 notes say no correlations between key variables; R3 notes say constructs are different. | Focal-technology boundary supersedes numeric availability: AI-driven LMS administrative automation is outside the current Paper B AI-adoption target universe. | Exclude from the target MASEM matrix despite local numeric SEM evidence. | None for target-matrix exclusion; record source-backed focal-technology rationale in the decision log. | Yes, as a target-matrix exclusion decision only. |

## Freeze Queue Split

- Decision-log entry ready for Step 4 application as exclusion/duplicate
  decisions: S195 as the canonical row and S206 as duplicate of S195.
- Decision-log entry ready for Step 4 application as a target-matrix exclusion:
  S202, because AI-driven LMS administrative automation is outside the Paper B
  target universe.
- Source-value checked and ready for Step 4 application as an exclusion/no-value
  decision: S014.
- Source-value checked and ready for Step 4 application as retained or corrected
  rows: S056 and S092.
- Source-value checked and row-set transcribed for Step 4 draft: S121, with
  students and teachers handled as separate samples and `SE` carried as a
  medium-confidence subjective-competence/self-efficacy mapping.
- Source-value checked and row-set transcribed for Step 4 draft: S021, with
  T1 and T2 handled as separate strata.
- S021 must preserve separate T1/T2 strata when applied.
- S021 supplement access is resolved; `Supplementary Table S4` is not a
  coefficient source.
- No raw coder workbooks were edited.
- No Step 5/LLM comparison artifacts were created.

## Remaining Work Before Reference Freeze

1. Step 4 preparation: apply S014 exclusion/no-value, S021 limited primary
   Model 1 beta-converted rows, S056 source-corrected values, S092
   source-beta-corrected beta-converted values, and S121 Figure 2
   student/teacher rows to the
   reference-standard draft.
2. Reference freeze audit: keep raw coder workbooks untouched, mark all
   beta-converted rows for sensitivity analysis, and verify duplicate/exclusion
   handling for S195/S206 and S202.

## Audit Notes

- `S195.pdf` and `S206.pdf` have identical SHA-256: `46479063603e21fb40a977740eee6e1cab22f4ced5c259cea400d78eb0c4f259`.
- `S014.pdf`, `S021.pdf`, `S056.pdf`, and `S092.pdf` were copied into the
  ignored adjudication source-PDF folder on 2026-06-08. Their SHA-256 values are:
  `7406e1a1f243d7c528cf76bc4dc0b1aef3069974a176c4a28e6eb3ead7ee63a2`,
  `996998dc117d00ee107c32513c57d3a13f008780fce77b22a7cd27fcf3077fbb`,
  `40f7b99a8c2544dce9716a6e5b761de7eb93b37d66277bba68652cf6272008e8`,
  and `f08e50d771aec9b231bd4ce71d02df53dd844d25cf545ed8d4259e734887b1af`.
- `S021_supplementary_file1.pdf` and `S021_supplementary_file2.docx` were
  copied into the ignored source-PDF folder from Springer supplementary links
  on 2026-06-08.
- `s021_primary_model_row_set_20260608.md` records the researcher's include
  decision and the limited primary Model 1 T1/T2 row set.
- Team run: `paper-b-step-3-source-9a96bfc2`.
- Team terminal status before shutdown: `pending=0`, `in_progress=0`, `completed=3`, `failed=0`.
- Team shutdown completed cleanly after terminal task state was confirmed.
