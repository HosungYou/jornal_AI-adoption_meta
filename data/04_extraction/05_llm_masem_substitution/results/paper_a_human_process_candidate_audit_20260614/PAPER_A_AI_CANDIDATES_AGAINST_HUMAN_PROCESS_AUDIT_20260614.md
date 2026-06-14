# Paper A AI candidates against human-process audit

Date: 2026-06-14

## Bottom line

The 51 AI/source-trace rows are not confirmed human omissions. Across the audited human-process layers, none of the 51 exact unordered construct pairs appears in raw human coder rows, latest direct human input, or the frozen reference. No study-level human exclusion record was found for S057, S138, or S176 in the audited exclusion file.

Therefore the correct rule is not “no human exclusion means add.” The correct rule is: no human exclusion plus source-confirmed target construct pair plus visible numeric cell means add proposal. Otherwise exclude or defer.

## Recommendation counts

- exclude_ai_false_positive_unless_reopened_by_source_evidence: 17
- exclude_or_defer_unless_anxiety_source_matrix_confirmed: 9
- exclude_or_defer_unless_fc_source_matrix_confirmed: 8
- source_review_required_before_any_add_proposal: 17

## Grouped audit table

| Candidate group | Human exact-pair evidence | Human exclusion evidence | Recommendation | Rationale |
|---|---|---|---|---|
| All 51 candidates | 0 exact raw human rows; 0 latest direct rows; 0 frozen-reference exact rows | No study-level human exclusion found for S057/S138/S176 in the audited exclusion file | No direct additions | A blank candidate_value plus no human exact pair means source review, not automatic insertion. |
| S057 TRU/UB candidates | No exact human-coded TRU/UB pair among the 17 AI candidates | No explicit human exclusion found for these exact pairs | source_review_required_before_any_add_proposal | If source table confirms TRU/UB as target constructs and numeric cells, promote as source_confirmed_add_candidate; otherwise exclude as AI false positive. |
| S138 ANX candidates | No exact human-coded ANX pair among the 9 AI candidates | No explicit human exclusion found for these exact pairs | exclude_or_defer_unless_anxiety_source_matrix_confirmed | Risk/fear term hits are not enough. Add only if anxiety or an approved anxiety-equivalent matrix construct is visible. |
| S138 FC candidates | No exact human-coded FC pair among the 8 AI candidates | No explicit human exclusion found for these exact pairs | exclude_or_defer_unless_fc_source_matrix_confirmed | Resources/support term hits are not enough. Add only if facilitating conditions or an approved equivalent is visible. |
| S176 ANX/SE candidates | No exact human-coded ANX/SE candidate pair | No explicit human exclusion found for these exact pairs | exclude_ai_false_positive_unless_reopened_by_source_evidence | Prior PDF text check showed Table 4 constructs HM, UB, BI, EE, FC, HA, PE, PI, SI, TR; ANX/SE were not visible. |

## Row-level audit file

CSV: `paper_a_ai_candidates_against_human_process_audit_20260614.csv`
