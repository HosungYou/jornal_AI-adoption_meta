# R1 Phase 1 Coding Progress - 2026-04-24

## Scope

- Coder: R1
- Workbook edited in place: `data/04_extraction/01_raw_human_coder_data_freeze/phase1/coder_packages/R1/AI_Adoption_MASEM_Coding_v3_R1.xlsx`
- Pairwise consensus workbook added: `data/04_extraction/02_pre_adjudication_disagreement/phase1/AI_Adoption_Phase1_Pairwise_Comparison_R1R2_R3R4_20260424.xlsx`
- Phase target completed through S033.
- Included the 20 unfinished Phase 1 studies: S168, S054, S220, S011, S180, S044, S151, S087, S051, S086, S074, S189, S120, S081, S035, S191, S041, S217, S166, S033.

## File Handling

- Merged the 2026-04-24 AI Adoption package from Downloads into `data/04_extraction`.
- Moved, not copied, the source folder.
- Cleaned `.DS_Store` and Excel lock files.

## Coding Outcome

- Assignment status set to `done` for all 20 target studies.
- STUDY_METADATA updated for all 20 target studies.
- CORRELATIONS updated for 17 included studies.
- EXCLUSION_LOG updated for 3 excluded studies.
- Total correlation rows entered or refreshed: 197.

## Exclusions

| Study ID | Code | Stage | Rationale |
|---|---|---|---|
| S220 | E-FT3 | full_text | Digital mental healthcare chatbot/content acceptance among university members; focal technology/use case is mental health care, not teaching/learning or educational AI adoption. |
| S180 | E-FT1 | data_extraction | Experimental explainable-AI classroom dialogue study reports group comparisons/acceptance outcomes but does not report at least two usable target construct-pair r or beta statistics. |
| S041 | E-FT3 | full_text | General AI technology acceptance/use-frequency study among university students; AI tools include broad consumer/general tools and the focal outcome is not educational AI adoption. |

## Review Flags and Special Coding Decisions

- S164: Accepted adjudication values are EE-SI = -0.024, FC-PE = 0.716, and PE-UB = 0.632.
- S091: Sample size is N = 382. Code the tool as ChatGPT-specific and retain the statistical coding decision; remaining checked differences were accepted.
- S187: Map stress/anxious wording to ANX with a flag for adjudication traceability.
- S079: Treat the relevant effects as path coefficients.
- S223: R1-coded value accepted.
- S005: Exclude JOY. Do not map CON -> FC; FC is not adopted for that case.
- S054: Teacher and student samples were reported separately. Consensus uses the teacher-only sample (n=299); the high-school student sample was excluded. Perceived Playfulness was not mapped to ATT.
- S011: Only structural path coefficients were usable. TAM paths were beta-converted, but TTF -> ATT and TTF -> BI were not mapped to FC and were excluded from the target matrix.
- S044: GAAIS Positive Attitudes toward AI was mapped to ATT as the primary coding decision. Negative Attitudes was not averaged into ATT; retain it only as a sensitivity or separate negative-attitude candidate if needed.
- S151: UB included use-frequency items plus one continuation-intention item, so UB rows were flagged.
- S087: Satisfaction was initially mapped to ATT; superseded by the 2026-04-29
  amendment below.
- S051: Perceived risk was initially mapped to ANX; superseded by the 2026-04-29
  amendment below.
- S074: AI anxiety correlations were positive; these rows were flagged as a possible scale-orientation issue.
- S189: Perception using ChatGPT was mapped to ATT. Article text reports N=236, while the table note appears to show n=237.
- S120: Student and instructor path coefficients were reported separately. Beta-converted subgroup effects were Fisher-z weighted across students (n=320) and instructors (n=31).
- S035: ChatGPT Adoption was mapped to UB, but items include continuation-intention wording.
- S191: Computer self-efficacy was mapped to SE.
- S166: Only HTMT and structural paths were reported; target paths were beta-converted.
- S033: No construct correlation matrix was reported; target direct paths were beta-converted. Ethics was not coded as a target construct.

## Verification

- Workbook was saved after spreadsheet-tool import/export.
- Pairwise consensus workbook was validated after final edits: no Excel table XML, worksheet relationships, hyperlinks, or external links.
- Key assignment range A42:I61 was inspected after saving logic and all 20 target studies showed `done`.
- Render checks were run for ASSIGNMENT, CORRELATIONS, STUDY_METADATA, and EXCLUSION_LOG ranges.
- Formula scan found one pre-existing `#NAME?` display in CODEBOOK!E22; no newly edited coding sheets showed formula-error hits.

## 2026-04-29 Adjudication Amendments

- General precision rule: preserve source-reported correlation precision up to
  three decimals when the source table reports three decimals.
- General HTMT rule: HTMT-only evidence is not treated as a usable MASEM
  correlation matrix. HTMT can be recorded as measurement-validity evidence, but
  target correlations must come from Pearson/latent correlations or, if no
  correlation matrix is available, from standardized path coefficients under
  the beta-to-r rule.
- S151: For `FC-UB`, use the source-reported value `.558`.
- S087: Exclude Satisfaction from `ATT`; the `Satisfaction-Performance
  Expectancy` row is not a usable `ATT-PE` correlation.
- S051: Do not map Perceived Risk to `ANX`. Exclude the Perceived Risk rows from
  the target `ANX` matrix unless source items explicitly measure anxiety, fear,
  apprehension, or AI-related threat affect.
- S051: Include R1 direct correlations for the R1-only target pairs:
  `EE-FC = .59`, `EE-PE = .48`, and `FC-PE = .47`.
- S120: Use R1 values. These are beta-converted path coefficients from the
  student/instructor subgroup path table, Fisher-z weighted across students
  (n=320) and instructors (n=31): `BI-EE = .06`, `BI-FC = .19`,
  `BI-PE = .32`, `BI-SI = .14`, and `BI-UB = .69`. Exclude the R2-only
  `SI-TRU`, `SI-UB`, and `TRU-UB` rows for the adjudicated reference.
- S081: Use R1 direct Table 4 values for all unresolved R1-R2 correlation
  differences.
- S035: Use R1 direct Table 4 values for all unresolved R1-R2 correlation
  differences.
- S191: Use R2 direct Table 2 values for all unresolved R1-R2 correlation
  differences.
- S217: Use R1 direct Table 4 values for all unresolved R1-R2 correlation
  differences; exclude R2-only construct-pair placements that duplicate R1
  `IU-PEU` and `IU-PU` mappings under different target labels.
- S033: Use R1 beta-converted Table 5 path-coefficient values. `ATT-EE = .06`
  with original beta `.013` is retained; the R2-only `PE-UB = .013` placement is
  excluded.

## Protocol Amendment After Phase 1

- Phase 1 pairwise coding is treated as complete for the current working version.
- Phase 2 should not follow the earlier AI-first single-verification plan.
- Phase 2 reviewer pairs are reset to:
  - Pair C: R1 + R4
  - Pair D: R2 + R3
- Phase 2 remains human-first: LLM outputs stay hidden until independent coding and cross-pair adjudication are complete.
- Phase 1 and Phase 2 now form the combined Paper B validation corpus.
- Before adjudication, raw human-human disagreement should be summarized by pair, field family, and numeric tolerance band.
- After adjudication, LLM outputs can be compared against the source-anchored adjudicated human reference for LLM accuracy, triage sensitivity, and downstream MASEM substitution.
- Current Phase 2 workload is Pair C = 57 studies (R1+R4, +7 each vs Phase 1) and Pair D = 56 studies (R2+R3, +6 each vs Phase 1).
