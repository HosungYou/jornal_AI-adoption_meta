# 2026-05-06 Coding Transfer Log

This date folder documents the R1 Phase 2 Pair C working coding batch for 17
studies prepared from local source PDFs. The coded workbook itself remains
outside Git because it is a working raw-coding return, not a share-safe frozen
reference artifact.

## Scope

- Pair/wave: Phase 2 Pair C (`R1 + R4`)
- Coder/workbook role: R1 working batch
- Studies:
  `S089`, `S075`, `S058`, `S108`, `S067`, `S103`, `S069`, `S063`,
  `S119`, `S093`, `S153`, `S132`, `S049`, `S066`, `S162`, `S136`,
  `S188`
- Workbook basename:
  `AI_Adoption_MASEM_Coding_v3_R1_Phase0_1_2_coded17_20260505.xlsx`
- Source evidence: local PDFs only; no PDF links were added to any workbook or
  Git-tracked document.

## Output Summary

| Item | Count |
|---|---:|
| Studies reviewed | 17 |
| Studies included for target matrix coding | 15 |
| Studies excluded | 2 |
| Correlation/path rows populated | 156 |
| Direct or Fornell-Larcker off-diagonal rows | 127 |
| Beta-converted path rows | 29 |

Excluded studies:

- `S108`: no usable target construct-pair `r` or standardized path coefficient
  matrix; source reports TAM/RIMMS mean comparisons and t-tests only.
- `S132`: no usable target AI-adoption matrix or structural path coefficients;
  reported correlations concern response-evaluation outcomes.

## 2026-05-06 Correction

`HM` (`Hedonic Motivation`) was removed from the `S136` target matrix after
reviewer correction. The five previously populated `HM -> ATT` rows were cleared:

- `ATT-BI`
- `ATT-EE`
- `ATT-PE`
- `ATT-SI`
- `ATT-UB`

The final `S136` note is: `Fornell-Larcker off-diagonal correlations used. HM
and habit excluded.`

## Git Handling

Committed to Git:

- This transfer log.
- `manifest.csv`.
- `r1_pairc_17_study_coding_notes.md`.
- Workflow documentation updates.

Not committed to Git:

- The local coded workbook.
- Local PDFs.
- Excel lock files.
- Any machine-specific file paths.

This batch is not a source-anchored adjudicated human reference standard and
does not start LLM comparison or MASEM substitution analysis.
