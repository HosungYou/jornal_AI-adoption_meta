# S014/S021 Source-Document Adjudication Recommendations

Date: 2026-05-29  
Worker: worker-2  
Scope: Paper B Step 3 source-document adjudication evidence split for S014 and S021 only. Raw coder workbooks were not edited.

## Decision Summary

| Study | Recommendation | Can enter reference freeze? | Rationale |
|---|---|---:|---|
| S014 | Retain source-review decision, but exclude R1's two indirect `beta_converted` rows from the MASEM-ready reference unless PI explicitly expands the rule to allow mediated indirect effects as pair statistics. | No, pending PI rule confirmation | Current protocol allows Pearson/latent correlations or standardized direct path coefficients; S014 evidence available locally is HTMT-only plus indirect paths through perceived risk. Perceived risk is excluded by default, and HTMT-only evidence is not a usable MASEM correlation matrix. |
| S021 | Retain as include-candidate and recover source coefficients from the open full text, choosing one timepoint only; default recommendation is T2 if construct coverage is adequate, otherwise document T1 alternative. | No, pending numeric extraction and timepoint decision | Source is a one-group pre/post design with PLS-SEM paths at T1 and T2. Project rules prohibit averaging dependent T1/T2 statistics or substituting cross-time paths for synchronous within-time relationships. |

## S014: indirect PLS-SEM via perceived risk

### Source and local evidence

- Source-check record: `data/04_extraction/03_source_document_adjudication/phase2/phase2_exclusion_source_check_20260525.md:75-82` and `phase2_source_check_candidates_20260525.csv:2` label S014 as `include_candidate` / `adjudicate_not_exclude`, with source location `Abstract; Figure 1; Results 4.3; Table 4` and affected returns `R1 coded values; R4 no coded values`.
- Review queue: `data/04_extraction/02_pre_adjudication_disagreement/combined/derived/combined_correlation_review_queue_20260525.csv:90` records R1 as `done` with indirect paths beta-converted and R4 as `review_source`.
- Coder-value rows: `combined_coder_values_long_20260525.csv:6084-6085` show R1 coded `PE<->UB = 0.31` and `SI<->UB = 0.30`, both `beta_converted`, source `Table 4`, notes `Indirect effect through perceived risk`; `combined_coder_values_long_20260525.csv:6631` records R4's no-value rationale: no zero-order matrix, no direct standardized path coefficients for mapped pairs, HTMT-only values, and Table 4 indirect/interaction effects.
- Local source-access gap: `data/02_screening/pdf_download_log.json:107-112` records `status=no_oa`, `pdf_url=null`; DOI metadata page confirms title, DOI, journal, 2025 publication, sample description, and subscription preview at https://link.springer.com/article/10.1007/s10639-025-13535-3.

### Rule applied

- Eligibility requires educational population plus correlation matrix or standardized path coefficients: `data/04_extraction/00_protocol/AI_Adoption_MASEM_Coding_Manual_v2.md:82-96`.
- HTMT is measurement-validity evidence only; it is not a usable MASEM correlation matrix: `AI_Adoption_MASEM_Coding_Manual_v2.md:318-328`.
- Standardized beta-to-r conversion applies only when the study reports standardized path coefficients without a correlation matrix: `AI_Adoption_MASEM_Coding_Manual_v2.md:330-340`; `docs/03_data_extraction/coding_manual.md:870-900`.
- Perceived risk/risk concern is excluded by default and should not be mapped to anxiety by label alone: `AI_Adoption_MASEM_Coding_Manual_v2.md:396-405`.

### Recommendation

1. **Do not freeze R1's two indirect path rows as MASEM-ready pair values** under current rules. They are indirect effects via an excluded mediator (`perceived risk`), not source-visible direct PE/SI -> BI/UB coefficients or correlations.
2. **Freeze study-level source adjudication only after PI confirms population scope** for `academic researchers` in universities. If accepted as higher-education staff/faculty, S014 can remain in the corpus with zero eligible MASEM pair statistics; if not accepted, route to exclusion using the education-population rule rather than the effect-size rule.
3. **Do not use HTMT-only values** as fallback correlations.

### Unresolved PI questions

- Does `academic researchers` qualify as a higher-education educational population for this project, or should the sample be excluded as outside the enumerated student/teacher/instructor/faculty/administrator roles?
- Should mediated indirect PLS-SEM effects ever be converted to MASEM pair statistics? Current recommendation: no.

## S021: pre/post genAI acceptance handling

### Source and local evidence

- Source-check record: `phase2_exclusion_source_check_20260525.md:84-91` and `phase2_source_check_candidates_20260525.csv:3` label S021 as `include_candidate` / `adjudicate_not_exclude`, with source location `Abstract; Methods 3.4; Results 4.2-4.3; Figures 1-2; Supplementary Table S4` and affected returns `R2 excluded; R3 no coded values`.
- Review queue: `combined_correlation_review_queue_20260525.csv:126` records both coders as `review_source` and the review note `metadata differences; source review`.
- Coder-value rows: `combined_coder_values_long_20260525.csv:8314-8331` and `9676-9685` are metadata-only for R2/R3; no numeric/path rows are present.
- Local source-access gap: `data/02_screening/pdf_download_log.json:163-168` records `status=no_oa`, `pdf_url=null`. However, the DOI full text is currently open access at https://link.springer.com/article/10.1007/s10758-025-09915-w, with downloadable article PDF and supplementary materials.
- Source text verified from the article PDF: Results 4.2 reports Model 1 PLS-SEM with significant T1 predictors AIAS-4 and Habit, no significant T2 predictors, R2 values of 0.795 at T1 and 0.824 at T2, within-time BI -> use-frequency paths at T1/T2, and a nonsignificant BI T1 -> BI T2 path.
- Source figure verified from downloaded PDF page 12: Fig. 1 contains within-time standardized path coefficients for T1 and T2. T2 candidate paths include PE -> BI (beta .285), FC -> BI (.113), EE -> BI (-.101), SI -> BI (-.064), Hedonic Motivation -> BI (.259), Habit -> BI (.335), and AIAS-4 -> BI (.275); T1 candidate paths include PE -> BI (.175), FC -> BI (-.130), EE -> BI (.232), SI -> BI (.025), Hedonic Motivation -> BI (.038), Habit -> BI (.212), and AIAS-4 -> BI (.508). Habit is not in the 12 target constructs and should be excluded; Hedonic Motivation maps to ATT only with moderate confidence if AI-specific.
- Supplementary Table S4 verified from the DOCX supplement: it reports f-squared effect sizes for PLS-SEM paths, not standardized beta coefficients; use it as model-context evidence, not as beta-to-r input.

### Rule applied

- Same-sample longitudinal/pre-post designs must use one timepoint and document the choice; default is the most mature timepoint unless attrition or construct coverage argues otherwise: `docs/03_data_extraction/coding_manual.md:960-969`.
- Do not average dependent T1/T2 correlations; choose one timepoint: `docs/03_data_extraction/correlation_extraction_guide.md:684-689`.
- Do not code cross-lagged correlations as structural within-time relations: `docs/03_data_extraction/correlation_extraction_guide.md:693-698`.
- UTAUT mappings: PE, EE, SI, FC, BI, and UB are exact target constructs; Hedonic Motivation maps to ATT with moderate confidence if AI-specific; Habit is not in the 12 and should be excluded: `docs/03_data_extraction/coding_manual.md:688-714` and `AI_Adoption_MASEM_Coding_Manual_v2.md:366-392`.

### Recommendation

1. **Do not freeze S021 from current coder rows** because no numeric/path values were entered by R2/R3.
2. **Source recovery is feasible**: the DOI full text and supplements are reachable despite the local PDF log saying `no_oa`.
3. **Use a single within-time model**. Default to T2 as the post-training/mature-adoption timepoint if the PI accepts the attrition from n=149 to n=122 and the construct coverage is sufficient. Use T1 only if the project prioritizes stronger pre-training predictor evidence or lower attrition.
4. **Eligible candidate pairs after timepoint choice:** PE-BI, EE-BI, SI-BI, FC-BI, and possibly ATT-BI through Hedonic Motivation if the moderate mapping is accepted. Exclude Habit. Treat BI->Use Frequency as BI-UB only if the project accepts self-reported use frequency as UB.
5. **Do not use the T1 -> T2 Behavioral Intention path** as a MASEM pair statistic; it is cross-time and nonsignificant in the source text.

### Unresolved PI questions

- Should default longitudinal handling select T2 for this pre/post intervention, or should T1 be used because T2 has attrition and no significant predictors?
- Should Hedonic Motivation be mapped to ATT in this work-context source, and should self-reported use frequency be coded as UB?

## Delegation and verification notes

- Subagents spawned: 2 (`S014 source-risk probe` / agent `019e741b-a545-7cd0-b3e4-df18430b0f7f`; `S021 pre/post probe` / agent `019e741b-c1bc-7222-b881-3208027d5d49`).
- Findings integrated: S014 over-conversion/HTMT/population risks; S021 pre/post same-sample handling and missing local numeric rows.
- Serial searches before spawn: 0 repo-search/read commands after claim; subagents were spawned before repository search per task contract.
