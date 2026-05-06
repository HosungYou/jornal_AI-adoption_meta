# R1 Pair C 17-Study Working Coding Notes

Date documented: 2026-05-06

Workbook basename:
`AI_Adoption_MASEM_Coding_v3_R1_Phase0_1_2_coded17_20260505.xlsx`

These notes document the 17-study R1 Phase 2 Pair C working coding batch. They
are intended to help later Phase 2 pairwise comparison and source-document
adjudication. They are not a source-anchored adjudicated human reference
standard.

## Batch Rules Applied

- Local PDFs were the only source documents used.
- Pearson or zero-order correlations were preferred where available.
- Fornell-Larcker off-diagonal latent correlations were used only when the table
  structure was usable and no better zero-order matrix was available.
- Fornell-Larcker diagonal values, AVE, CR, and HTMT values were not coded as
  target construct correlations.
- Standardized path coefficients were beta-converted only when no usable
  correlation matrix was available.
- Perceived risk was excluded by default and was not mapped to `ANX` by label
  alone.
- `HM` and habit were excluded from the target matrix in this batch following
  reviewer correction. The current manual permits `HM -> ATT` as a moderate
  mapping, so this should be treated as an explicit batch-level decision to
  revisit during R1-R4 comparison if R4 codes HM differently.
- `n_constructs_measured`, `n_correlations_reported`, and
  `matrix_completeness` were left blank, matching the existing R1 workbook
  pattern.

## Batch Counts

| Study ID | Status | Rows populated | Evidence type |
|---|---|---:|---|
| `S089` | Included | 5 | beta-converted paths |
| `S075` | Included | 15 | direct/Fornell-Larcker off-diagonal |
| `S058` | Included | 6 | beta-converted paths |
| `S108` | Excluded | 0 | no usable matrix/path evidence |
| `S067` | Included | 15 | direct/Fornell-Larcker off-diagonal |
| `S103` | Included | 10 | Pearson correlations |
| `S069` | Included | 6 | direct/Fornell-Larcker off-diagonal |
| `S063` | Included | 10 | direct/Fornell-Larcker off-diagonal |
| `S119` | Included | 10 | direct/Fornell-Larcker off-diagonal |
| `S093` | Included | 6 | beta-converted paths |
| `S153` | Included | 15 | direct/Fornell-Larcker off-diagonal |
| `S132` | Excluded | 0 | no usable target adoption evidence |
| `S049` | Included | 15 | direct/Fornell-Larcker off-diagonal |
| `S066` | Included | 12 | beta-converted paths |
| `S162` | Included | 15 | direct/Fornell-Larcker off-diagonal |
| `S136` | Included | 10 | direct/Fornell-Larcker off-diagonal |
| `S188` | Included | 6 | direct/Fornell-Larcker off-diagonal |

Total populated rows: 156.

## Study-Level Notes

### S089 - Tran

- Included; `N = 322`; Vietnam; undergraduate students; general AI.
- Framework coded as TAM.
- No usable correlation matrix was located.
- Beta-converted PLS path coefficients were used for target TAM adoption paths:
  `EE-BI`, `PE-BI`, `BI-UB`, `EE-UB`, and `PE-UB`.
- `AI adoption` was mapped to `UB`; `AI using intention` was mapped to `BI`.
- Common method bias was coded as not addressed.

### S075 - Rana

- Included; `N = 402`; India; mixed undergraduate/graduate students;
  ChatGPT/generative AI.
- Framework coded as UTAUT2.
- Table 4 Fornell-Larcker off-diagonal latent correlations were used.
- `In` was mapped to `BI` (`Intention`) and `Be` was mapped to `UB`
  (`Behavior`).
- `HM`, habit, and personal innovativeness were excluded from the target matrix.
- Common method bias was coded as addressed.

### S058 - Boz

- Included; `N = 541`; Turkiye; undergraduate/associate GCA students;
  generative AI.
- Framework coded as TAM.
- No usable correlation matrix was located.
- Table 4 direct SEM paths were beta-converted.
- `ATUGAI` was mapped to `ATT`; `IUGAI` to `BI`; `PU` to `PE`; `PEU` to
  `EE`.
- Innovativeness, perceived risk, and digital financial literacy were excluded.
- Common method bias was coded as addressed.

### S108 - Quintana-Ordorika

- Excluded with code `E-FT1`.
- `N = 114`; Spain; trainee teachers; experimental design; GenAI.
- The source reports TAM/RIMMS group comparison means and t-tests only.
- No usable target construct-pair `r` or standardized path coefficient matrix
  was available.
- Common method bias was coded as not addressed.

### S067 - Yadav

- Included; `N = 598`; India; mixed undergraduate/postgraduate students.
- Framework coded as other/SOR.
- Table 4 Fornell-Larcker off-diagonal correlations were used.
- `Perceived Credibility` was mapped to `TRU`.
- Task-Technology Fit and Cost Effectiveness were excluded from the target
  matrix.
- Common method bias was coded as addressed.

### S103 - Lenart

- Included; `N = 770`; Poland; mixed bachelor/master students; GenAI.
- Framework coded as other.
- Table 2 Pearson correlation matrix was used.
- Higher education institution support was mapped to `FC`.
- Perceived Quality and Ethical Perception were excluded from the target matrix.
- Common method bias was coded as addressed.

### S069 - Al-Khresheh

- Included; `N = 597`; Yemen; undergraduate/pre-service EFL teacher students;
  ChatGPT/generative AI.
- Framework coded as TAM.
- Table 2 Fornell-Larcker/discriminant-validity off-diagonal correlations were
  used.
- `PEU` was mapped to `EE`; `PU` to `PE`; `SN` to `SI`; `IU` to `BI`.
- Perceived Ethics was excluded from the target matrix.
- Common method bias was coded as not addressed.

### S063 - Sustaningrum

- Included; `N = 388`; Indonesia; mixed undergraduate/postgraduate students;
  AI tools including ChatGPT, Gemini, and Perplexity.
- Framework coded as UTAUT.
- Table 3 Fornell-Larcker off-diagonal correlations were used.
- `AH`/Adoption of AI was mapped to `UB`.
- Perceived Risk was excluded and not mapped to `ANX`.
- Common method bias was coded as partial because only procedural handling was
  reported.

### S119 - Cao

- Included; `N = 432`; China; undergraduate students; generative AI.
- Framework coded as other.
- Table 5 Fornell-Larcker off-diagonal correlations were used.
- `PU` was selected as the primary `PE` construct.
- Perceived learning performance, perceived learning efficiency, and user
  satisfaction were excluded to avoid duplicate `PE`/`ATT` mapping.
- Common method bias was coded as not addressed.

### S093 - Alqaisi

- Included; `N = 127`; Jordan; medical students and teaching staff; ChatGPT.
- Framework coded as UTAUT.
- No usable correlation matrix was located.
- Table 3 SEM path weights were beta-converted.
- Perceived Risk was excluded.
- `ACME`/ChatGPT adoption in medical education was mapped to `UB`.
- Common method bias was coded as not addressed.

### S153 - Bilquise

- Included; `N = 207`; UAE; students; academic-advising chatbot.
- Framework coded as UTAUT.
- Table 4 Fornell-Larcker off-diagonal correlations were used.
- `PA` was mapped to `AUT`; `PT` was mapped to `TRU`.
- Anthropomorphism was excluded from the target matrix.
- Common method bias was coded as not addressed.

### S132 - Lee

- Excluded with code `E-FT1`.
- `N = 147`; United States; undergraduate students; ChatGPT.
- No usable target AI-adoption correlation matrix or SEM path coefficients were
  available.
- Reported correlations concern response helpfulness, caring, and likelihood to
  reach out again by perceived source, not target adoption constructs.
- Common method bias was coded as not addressed.

### S049 - Yang

- Included; `N = 419`; China; graduate students; GAI-assisted writing.
- Framework coded as UTAUT.
- Table 3 Fornell-Larcker off-diagonal correlations were used.
- `AU` was mapped to `UB`.
- Common method bias was coded as not addressed.

### S066 - Joshi

- Included; `N = 175`; India; mixed undergraduate/postgraduate students;
  generative AI tools.
- Framework coded as UTAUT_AI.
- HTMT was not coded as target construct correlations.
- Table 7 path coefficients were beta-converted because no usable Pearson or
  Fornell-Larcker correlation matrix was available.
- The path table has inconsistent p/t reporting; anxiety-related paths were
  flagged.
- `Technological Anxiety -> Behavioral Intention` was coded as beta `.070`
  rather than the printed `.700` because Table 8 indirect-effect logic supports
  `.070`.
- Common method bias was coded as addressed.

### S162 - Saif

- Included; `N = 156`; Pakistan; MBA graduate students; ChatGPT.
- Framework coded as TAM.
- Table 3 Fornell-Larcker off-diagonal correlations were used.
- `Actual use of ChatGPT` was mapped to `UB`; `Behavioral Intention` to `BI`;
  `Anxiety` to `ANX`.
- Perceived Stress was excluded because a separate anxiety construct was already
  available.
- Common method bias was coded as not addressed.

### S136 - Zou

- Included; `N = 105`; China; vocational computer science students; AI tools.
- Framework coded as UTAUT2.
- Table 3 Fornell-Larcker off-diagonal correlations were used.
- `HM` and habit were excluded from the target matrix.
- On 2026-05-06, five previously populated `HM -> ATT` rows were cleared:
  `ATT-BI`, `ATT-EE`, `ATT-PE`, `ATT-SI`, and `ATT-UB`.
- Common method bias was coded as not addressed.

### S188 - Musyaffi

- Included; `N = 147`; Indonesia; undergraduate/accounting-related students;
  general AI tools for accounting tasks.
- Framework coded as TAM.
- Table 3 Fornell-Larcker off-diagonal correlations were used.
- `PTA` was mapped to `TRU`.
- AIQ, personal innovativeness, and student satisfaction were excluded from the
  target matrix.
- Common method bias was coded as not addressed.

## Follow-Up For Pairwise Review

- Compare `HM` handling explicitly if R4 includes hedonic motivation for
  `S075` or `S136`.
- Confirm all beta-converted rows for `S089`, `S058`, `S093`, and `S066`
  against the source tables before Phase 2 reference freezing.
- Re-check the `S066` technological anxiety coefficient during adjudication
  because the source table appears internally inconsistent.
- Keep `S108` and `S132` as exclusion-first review items.
