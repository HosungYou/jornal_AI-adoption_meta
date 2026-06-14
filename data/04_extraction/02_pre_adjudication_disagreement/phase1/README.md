# Phase 1 Pairwise Consensus Workbook

## Version

- Version date: 2026-04-24
- Workbook: `AI_Adoption_Phase1_Pairwise_Comparison_R1R2_R3R4_20260424.xlsx`
- Scope: Phase 1 pairwise adjudication support for R1-R2 and R3-R4 coding comparisons.
- Protocol link: Phase 2 will use rotated pairs (R1-R4 and R2-R3) after this Phase 1 consensus version. Phase 1 and Phase 2 together form the Paper B validation corpus.
- Current Git branch: `codex/phase1-consensus-20260424`
- Pull request: `https://github.com/HosungYou/journal_AI-adoption_meta/pull/1`

## Purpose

This workbook is the shareable comparison and adjudication artifact for Phase 1 coding. It is designed so reviewers can inspect disagreements in extracted metadata and construct-pair statistics without opening each PDF one by one.

The workbook is not the final MASEM analysis dataset. It records pairwise coder differences, consensus decisions, and audit notes that should be propagated into the final extraction dataset.

## Main Sheets

| Sheet | Purpose |
|---|---|
| `README` | Workbook-level notes and orientation. |
| `DECISION_LOG` | Human consensus decisions made during review. |
| `SUMMARY` | Pairwise comparison summary counts. |
| `FIELD_SUMMARY` | Metadata and correlation status counts by field/status. |
| `PHASE1_ASSIGNMENTS` | Phase 1 study list and coder package coverage. |
| `R1_R2_RECHECK_S164_S033` | Focused R1-R2 review sequence from S164 through S033. |
| `R1_R2_METADATA` | R1-R2 metadata differences and resolutions. |
| `R1_R2_CORRELATIONS` | R1-R2 construct-pair differences and resolutions. |
| `R3_R4_METADATA` | R3-R4 metadata differences and resolutions. |
| `R3_R4_CORRELATIONS` | R3-R4 construct-pair differences and resolutions. |
| `PDF_INDEX` | Local PDF availability index. No hyperlinks are included. |

## Share-Safe File Handling

The workbook intentionally contains no PDF hyperlinks or external references. This avoids Excel recovery warnings and makes the file safer to share across machines with different local PDF paths.

Validation run on 2026-04-24:

- Excel table XML: 0
- Worksheet relationship files: 0
- Hyperlinks or external links: none detected

## Key Consensus Decisions

### S044

- Use GAAIS Positive Attitudes toward AI as the primary `ATT` coding.
- Do not average Negative Attitudes into primary `ATT`.
- Keep Negative Attitudes only as a possible sensitivity or separate negative-attitude/prejudice construct candidate.
- R2 Table 2 values were accepted because they match the PDF table; R1 appears row/column shifted.

### S054

- Use the teacher-only sample (`n = 299`).
- Exclude the high-school student sample (`n = 347`) from the target MASEM coding.
- Do not map Perceived Playfulness to `ATT`.

### S011

- Retain TAM paths as beta-converted values where usable.
- Do not map Task-Technology Fit (`TTF`) to Facilitating Conditions (`FC`).
- Exclude `TTF -> ATT` and `TTF -> BI` from `FC` rows.

### S180

- Exclude from MASEM correlation contribution because no usable target construct-pair `r` or beta matrix is available.
- Metadata correction: participants were mainland China pre-service teachers in Beijing; education level is mixed undergraduate/graduate.

### S220

- Exclude from the education AI adoption dataset because the focal technology/use case is digital mental healthcare chatbot/content, not educational AI adoption.

## Recommended Sharing Note

When sharing this version, include the following note:

> This is the 2026-04-24 Phase 1 pairwise consensus workbook for AI Adoption MASEM coding. It is an adjudication/audit artifact, not the final analysis dataset. PDF hyperlinks were intentionally removed to avoid machine-specific path errors. The current primary ATT decision for S044 uses GAAIS Positive Attitudes only; Negative Attitudes is retained only for possible sensitivity or separate construct analysis.

## Next Step

1. Propagate accepted Phase 1 decisions from `DECISION_LOG` and the `resolution` columns into the final MASEM-ready extraction dataset before running pooled correlation or MASEM analyses.
2. Freeze Phase 2 assignments using rotated pairs:
   - Pair C: R1 + R4, 57 studies
   - Pair D: R2 + R3, 56 studies
3. Analyze raw human-human disagreement before consensus/adjudication.
4. Keep LLM outputs blinded until Phase 2 independent coding, raw disagreement analysis, and cross-pair adjudication are complete.
