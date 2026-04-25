# Phase 1 Coding Decision Application Check - 2026-04-25

## Purpose

This check verifies whether the coding decisions discussed during Phase 1 review
are reflected in the current workflow after the raw human coder data freeze.

## Interpretation Rule

Raw coder workbooks are treated as frozen source data. They should not be edited
to force consensus. If a raw workbook value differs from a reviewed decision, the
decision must be applied during Step 3 source-document adjudication and then
carried into the Step 4 source-anchored adjudicated human reference standard.

## Check Summary

| Study ID | Decision | Decision log reflected? | Raw workbook state | Step 3 action |
|---|---|---:|---|---|
| S164 | `EE-SI = -0.024`, `FC-PE = 0.716`, `PE-UB = 0.632` | Yes | R1 and R2 raw entries still differ; R2 stores 0.716 and 0.632 in `original_beta` while R1 has conflicting extracted values | Apply source-checked final values in adjudicated reference |
| S091 | `N = 382`; ChatGPT-specific; statistical coding retained | Yes | R1 has `N = 382` but tool label is generic; R2 has ChatGPT but `N = 451` | Apply `N = 382` and ChatGPT-specific coding in adjudicated reference |
| S187 | Stress/anxious wording mapped to `ANX` with flag | Yes | R1 maps stress-related entries to `ANX` and flags review | Keep flagged `ANX` mapping unless source check overturns |
| S079 | Treat relevant effects as path coefficients | Yes | R1 rows use `r_source = path_coefficient` with beta values in `original_beta` | Carry forward as path coefficients after source check |
| S223 | R1-coded value accepted | Yes | Decision is recorded; final reference still not frozen | Carry R1 value into adjudicated reference |
| S005 | Exclude `JOY`; do not map `CON -> FC`; do not adopt `FC` | Yes | R1 raw workbook still contains `CON -> FC` mappings flagged for review | Remove those `FC` mappings in adjudicated reference |
| S054 | Use teacher-only sample; exclude high-school student sample; exclude `PP -> ATT` | Yes | R2 raw workbook shows teacher-only `N = 299`; R1 still shows mixed `N = 646` | Apply teacher-only coding in adjudicated reference |
| S011 | Exclude `TTF -> ATT` and `TTF -> BI` from `FC` mapping | Yes | Decision is recorded; final reference still not frozen | Remove TTF-as-FC mappings in adjudicated reference |
| S044 | Use GAAIS Positive Attitudes toward AI as primary `ATT`; do not average Negative Attitudes | Yes | Raw rows reviewed show Positive Attitudes mapped to `ATT` | Carry positive-attitude `ATT` decision forward |
| S180 | Exclude because no usable target construct-pair `r` or beta matrix is available | Yes | R1 exclusion log records exclusion | Carry exclusion forward after source check |
| S220 | Exclude because focal use case is mental healthcare chatbot/content | Yes | R1 exclusion log records exclusion | Carry exclusion forward after source check |

## Conclusion

The early coding decisions are documented, but they should not be interpreted as
fully applied to the frozen raw coder workbooks. The project is therefore still
in Step 3. The next active task is to create the source-anchored adjudicated
reference file where these reviewed decisions become the analysis-ready standard.
