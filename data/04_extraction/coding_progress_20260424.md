# R1 Phase 1 Coding Progress - 2026-04-24

## Scope

- Coder: R1
- Workbook edited in place: `coder_packages/R1/AI_Adoption_MASEM_Coding_v3_R1.xlsx`
- Pairwise consensus workbook added: `consensus/AI_Adoption_Phase1_Pairwise_Comparison_R1R2_R3R4_20260424.xlsx`
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

- S054: Teacher and student samples were reported separately. Consensus uses the teacher-only sample (n=299); the high-school student sample was excluded. Perceived Playfulness was not mapped to ATT.
- S011: Only structural path coefficients were usable. TAM paths were beta-converted, but TTF -> ATT and TTF -> BI were not mapped to FC and were excluded from the target matrix.
- S044: GAAIS Positive Attitudes toward AI was mapped to ATT as the primary coding decision. Negative Attitudes was not averaged into ATT; retain it only as a sensitivity or separate negative-attitude candidate if needed.
- S151: UB included use-frequency items plus one continuation-intention item, so UB rows were flagged.
- S087: Satisfaction was mapped to ATT.
- S051: Perceived risk was mapped to ANX.
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
