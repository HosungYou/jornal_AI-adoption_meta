# Paper A detailed source-review final decisions

Date: 2026-06-14

## Bottom line

After detailed source review of S057, S138, and S176, none of the 51 AI/source-trace missing-pair candidates should be added to the matrix at this time.

Reason: each candidate requires a construct that is absent from the reviewed source matrix or would require an unapproved construct remap.

## Final decision counts

- exclude_ai_false_positive_no_facilitating_conditions_construct: 8
- exclude_ai_false_positive_no_target_construct_in_source_matrix: 34
- exclude_ai_false_positive_perceived_risk_not_anxiety: 9
- add_to_matrix=yes: 0

## Study-level source evidence

| Study/group | Source matrix reviewed | Constructs visible in source matrix | Decision | Rationale |
|---|---|---|---|---|
| S057 all 17 TRU/UB candidates | S057.pdf Table 2 Results of the measurement model evaluation (/tmp/S057_layout.txt lines 811-828) | PEOU, PU, ATT, SN, EXP, PE, ANX, SE, PV, FC, HBT, INT | exclude_ai_false_positive_no_target_construct_in_source_matrix | The AI candidates all require TRU and/or UB, but the source Table 2 does not contain TRU or UB. INT may map to BI; no actual use/use behavior construct is present. Therefore these candidates are not addable Paper A target pairs. |
| S138 9 ANX candidates | S138.pdf Table 5 Fornell-Larcker Criterion (/tmp/S138_layout.txt lines 785-797; Table 2 lines 482-499) | AC, AT, AU, BI, PE, PR, PU, SE, SI, ST | exclude_ai_false_positive_perceived_risk_not_anxiety | The source matrix contains PR (Perceived Risk), not ANX (Anxiety). Perceived Risk cannot be automatically remapped to Anxiety without a researcher-approved construct remap. |
| S138 8 FC candidates | S138.pdf Table 5 Fornell-Larcker Criterion (/tmp/S138_layout.txt lines 785-797; Table 2 lines 607-645) | AC, AT, AU, BI, PE, PR, PU, SE, SI, ST | exclude_ai_false_positive_no_facilitating_conditions_construct | The source matrix does not contain FC (Facilitating Conditions). AC is Acceptance and cannot be automatically remapped to FC. |
| S176 all 17 ANX/SE candidates | S176.pdf Table 4 Discriminant validity (/tmp/S176_layout.txt lines 617-630) | HM, UB, BI, EE, FC, HA, PE, PI, SI, TR | exclude_ai_false_positive_no_target_construct_in_source_matrix | The AI candidates require ANX and/or SE, but the source Table 4 does not contain ANX or SE. PI/HA/TR must not be automatically remapped to SE or ANX. |

## Row-level final decision table

| study_id | missing_pair | final_decision | add_to_matrix |
|---|---|---|---|
| S057 | ANX-TRU | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S057 | ANX-UB | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S057 | ATT-TRU | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S057 | ATT-UB | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S057 | BI-TRU | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S057 | BI-UB | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S057 | EE-TRU | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S057 | EE-UB | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S057 | FC-TRU | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S057 | FC-UB | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S057 | PE-TRU | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S057 | PE-UB | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S057 | SE-TRU | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S057 | SE-UB | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S057 | SI-TRU | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S057 | SI-UB | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S057 | TRU-UB | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S138 | ANX-ATT | exclude_ai_false_positive_perceived_risk_not_anxiety | no |
| S138 | ANX-BI | exclude_ai_false_positive_perceived_risk_not_anxiety | no |
| S138 | ANX-EE | exclude_ai_false_positive_perceived_risk_not_anxiety | no |
| S138 | ANX-FC | exclude_ai_false_positive_perceived_risk_not_anxiety | no |
| S138 | ANX-PE | exclude_ai_false_positive_perceived_risk_not_anxiety | no |
| S138 | ANX-SE | exclude_ai_false_positive_perceived_risk_not_anxiety | no |
| S138 | ANX-SI | exclude_ai_false_positive_perceived_risk_not_anxiety | no |
| S138 | ANX-TRU | exclude_ai_false_positive_perceived_risk_not_anxiety | no |
| S138 | ANX-UB | exclude_ai_false_positive_perceived_risk_not_anxiety | no |
| S138 | ATT-FC | exclude_ai_false_positive_no_facilitating_conditions_construct | no |
| S138 | BI-FC | exclude_ai_false_positive_no_facilitating_conditions_construct | no |
| S138 | EE-FC | exclude_ai_false_positive_no_facilitating_conditions_construct | no |
| S138 | FC-PE | exclude_ai_false_positive_no_facilitating_conditions_construct | no |
| S138 | FC-SE | exclude_ai_false_positive_no_facilitating_conditions_construct | no |
| S138 | FC-SI | exclude_ai_false_positive_no_facilitating_conditions_construct | no |
| S138 | FC-TRU | exclude_ai_false_positive_no_facilitating_conditions_construct | no |
| S138 | FC-UB | exclude_ai_false_positive_no_facilitating_conditions_construct | no |
| S176 | ANX-ATT | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S176 | ANX-BI | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S176 | ANX-EE | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S176 | ANX-FC | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S176 | ANX-PE | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S176 | ANX-SE | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S176 | ANX-SI | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S176 | ANX-TRU | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S176 | ANX-UB | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S176 | ATT-SE | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S176 | BI-SE | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S176 | EE-SE | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S176 | FC-SE | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S176 | PE-SE | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S176 | SE-SI | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S176 | SE-TRU | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
| S176 | SE-UB | exclude_ai_false_positive_no_target_construct_in_source_matrix | no |
