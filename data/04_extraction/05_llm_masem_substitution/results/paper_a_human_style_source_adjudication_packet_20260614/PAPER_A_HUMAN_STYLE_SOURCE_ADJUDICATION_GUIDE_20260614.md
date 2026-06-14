# Paper A Source-Adjudication Review Packet: AI-Candidate Rows in Human Coding Terms

Date: 2026-06-14

## Plain answer

These rows should not be described as values that human coders definitely failed to find. The current label is: values not present in the latest human-coded Paper A matrix, but flagged by the AI/source-trace workflow as possible source-adjudication candidates.

Important: candidate_value is blank for these rows, so the AI did not add numeric values. It created a review queue for human source adjudication.

## Human-coding terminology

- raw coder value: a value entered by the original human coding workflow.
- source-check queue: an item that must be checked against PDF/source before it can affect the matrix.
- source_confirmed_add: a value absent from the current human matrix but visible in an acceptable source matrix.
- source_corrected_add: a value requiring correction of construct label, row/column orientation, or source location before adding.
- exclude_no_target_construct: the candidate term appears in text, but the source does not contain the Paper A target construct.
- exclude_no_usable_r: the paper discusses the construct but does not provide a usable correlation/latent correlation cell.
- exclude_source_type_mismatch: the value is beta/path coefficient, HTMT, loading, reliability, or another non-target statistic.
- defer_unclear: source or OCR/table structure is not clear enough for a coding decision.

## Current prioritized decision

No high-confidence add-now value is identified in this priority subset. The correct next step is human source adjudication, not direct matrix insertion.

### S057: Manual source-table review priority, not add-now

Evidence summary: 최신 human-coded direct input에는 이 17개 missing-pair 후보가 없고, trace 파일의 candidate_value도 비어 있다. 따라서 AI가 숫자를 추가한 것이 아니라 사람이 source table에서 확인해야 하는 상태다.

Coding decision: source matrix에서 두 construct가 실제 target construct이고 같은 상관행렬의 numeric cell이 보이면 source_confirmed_add 후보가 될 수 있다. 그 전에는 add 금지.

### S138: Mostly construct-remap review, not add-now

Evidence summary: 최신 human-coded input은 Table 5 기반 28개 상관쌍을 이미 포함하지만 ANX/FC 관련 후보는 없다. source text의 risk/fear/resources/support term hit만으로 ANX/FC target construct를 확정할 수 없다.

Coding decision: ANX는 perceived risk/fear를 anxiety로 오코딩할 위험이 있어 낮은 confidence. FC는 resources/support term hit만으로는 부족하므로 facilitating conditions label 확인 전 add 금지.

### S176: Probable do-not-add due to target-construct absence

Evidence summary: PDF text로 확인된 Table 4 construct set은 HM, UB, BI, EE, FC, HA, PE, PI, SI, TR이다. ANX와 SE는 보이지 않는다.

Coding decision: ANX/SE 후보 17개는 현재 human omission이 아니라 target construct absent 또는 construct mismatch로 처리한다. PI/HA/TR을 SE/ANX로 자동 remap하지 않는다.

## Priority candidate table

| study_id | missing_pair | confidence_tier | provisional_decision | human coding reason |
|---|---|---|---|---|
| S057 | ANX-TRU | MEDIUM_REVIEW_PRIORITY | review_before_add_no_numeric_value_yet | 최신 human-coded matrix에는 이 missing pair가 없고 AI trace는 source-review 후보로 올렸다. 그러나 candidate_value가 비어 있으므로 numeric cell은 아직 추출/확정되지 않았다. PDF/source 표에서 두 construct가 실제 target construct로 같은 correlation matrix 안에 있는지 확인해야 한다. |
| S057 | ANX-UB | MEDIUM_REVIEW_PRIORITY | review_before_add_no_numeric_value_yet | 최신 human-coded matrix에는 이 missing pair가 없고 AI trace는 source-review 후보로 올렸다. 그러나 candidate_value가 비어 있으므로 numeric cell은 아직 추출/확정되지 않았다. PDF/source 표에서 두 construct가 실제 target construct로 같은 correlation matrix 안에 있는지 확인해야 한다. |
| S057 | ATT-TRU | MEDIUM_REVIEW_PRIORITY | review_before_add_no_numeric_value_yet | 최신 human-coded matrix에는 이 missing pair가 없고 AI trace는 source-review 후보로 올렸다. 그러나 candidate_value가 비어 있으므로 numeric cell은 아직 추출/확정되지 않았다. PDF/source 표에서 두 construct가 실제 target construct로 같은 correlation matrix 안에 있는지 확인해야 한다. |
| S057 | ATT-UB | MEDIUM_REVIEW_PRIORITY | review_before_add_no_numeric_value_yet | 최신 human-coded matrix에는 이 missing pair가 없고 AI trace는 source-review 후보로 올렸다. 그러나 candidate_value가 비어 있으므로 numeric cell은 아직 추출/확정되지 않았다. PDF/source 표에서 두 construct가 실제 target construct로 같은 correlation matrix 안에 있는지 확인해야 한다. |
| S057 | BI-TRU | MEDIUM_REVIEW_PRIORITY | review_before_add_no_numeric_value_yet | 최신 human-coded matrix에는 이 missing pair가 없고 AI trace는 source-review 후보로 올렸다. 그러나 candidate_value가 비어 있으므로 numeric cell은 아직 추출/확정되지 않았다. PDF/source 표에서 두 construct가 실제 target construct로 같은 correlation matrix 안에 있는지 확인해야 한다. |
| S057 | BI-UB | MEDIUM_REVIEW_PRIORITY | review_before_add_no_numeric_value_yet | 최신 human-coded matrix에는 이 missing pair가 없고 AI trace는 source-review 후보로 올렸다. 그러나 candidate_value가 비어 있으므로 numeric cell은 아직 추출/확정되지 않았다. PDF/source 표에서 두 construct가 실제 target construct로 같은 correlation matrix 안에 있는지 확인해야 한다. |
| S057 | EE-TRU | MEDIUM_REVIEW_PRIORITY | review_before_add_no_numeric_value_yet | 최신 human-coded matrix에는 이 missing pair가 없고 AI trace는 source-review 후보로 올렸다. 그러나 candidate_value가 비어 있으므로 numeric cell은 아직 추출/확정되지 않았다. PDF/source 표에서 두 construct가 실제 target construct로 같은 correlation matrix 안에 있는지 확인해야 한다. |
| S057 | EE-UB | MEDIUM_REVIEW_PRIORITY | review_before_add_no_numeric_value_yet | 최신 human-coded matrix에는 이 missing pair가 없고 AI trace는 source-review 후보로 올렸다. 그러나 candidate_value가 비어 있으므로 numeric cell은 아직 추출/확정되지 않았다. PDF/source 표에서 두 construct가 실제 target construct로 같은 correlation matrix 안에 있는지 확인해야 한다. |
| S057 | FC-TRU | MEDIUM_REVIEW_PRIORITY | review_before_add_no_numeric_value_yet | 최신 human-coded matrix에는 이 missing pair가 없고 AI trace는 source-review 후보로 올렸다. 그러나 candidate_value가 비어 있으므로 numeric cell은 아직 추출/확정되지 않았다. PDF/source 표에서 두 construct가 실제 target construct로 같은 correlation matrix 안에 있는지 확인해야 한다. |
| S057 | FC-UB | MEDIUM_REVIEW_PRIORITY | review_before_add_no_numeric_value_yet | 최신 human-coded matrix에는 이 missing pair가 없고 AI trace는 source-review 후보로 올렸다. 그러나 candidate_value가 비어 있으므로 numeric cell은 아직 추출/확정되지 않았다. PDF/source 표에서 두 construct가 실제 target construct로 같은 correlation matrix 안에 있는지 확인해야 한다. |
| S057 | PE-TRU | MEDIUM_REVIEW_PRIORITY | review_before_add_no_numeric_value_yet | 최신 human-coded matrix에는 이 missing pair가 없고 AI trace는 source-review 후보로 올렸다. 그러나 candidate_value가 비어 있으므로 numeric cell은 아직 추출/확정되지 않았다. PDF/source 표에서 두 construct가 실제 target construct로 같은 correlation matrix 안에 있는지 확인해야 한다. |
| S057 | PE-UB | MEDIUM_REVIEW_PRIORITY | review_before_add_no_numeric_value_yet | 최신 human-coded matrix에는 이 missing pair가 없고 AI trace는 source-review 후보로 올렸다. 그러나 candidate_value가 비어 있으므로 numeric cell은 아직 추출/확정되지 않았다. PDF/source 표에서 두 construct가 실제 target construct로 같은 correlation matrix 안에 있는지 확인해야 한다. |
| S057 | SE-TRU | MEDIUM_REVIEW_PRIORITY | review_before_add_no_numeric_value_yet | 최신 human-coded matrix에는 이 missing pair가 없고 AI trace는 source-review 후보로 올렸다. 그러나 candidate_value가 비어 있으므로 numeric cell은 아직 추출/확정되지 않았다. PDF/source 표에서 두 construct가 실제 target construct로 같은 correlation matrix 안에 있는지 확인해야 한다. |
| S057 | SE-UB | MEDIUM_REVIEW_PRIORITY | review_before_add_no_numeric_value_yet | 최신 human-coded matrix에는 이 missing pair가 없고 AI trace는 source-review 후보로 올렸다. 그러나 candidate_value가 비어 있으므로 numeric cell은 아직 추출/확정되지 않았다. PDF/source 표에서 두 construct가 실제 target construct로 같은 correlation matrix 안에 있는지 확인해야 한다. |
| S057 | SI-TRU | MEDIUM_REVIEW_PRIORITY | review_before_add_no_numeric_value_yet | 최신 human-coded matrix에는 이 missing pair가 없고 AI trace는 source-review 후보로 올렸다. 그러나 candidate_value가 비어 있으므로 numeric cell은 아직 추출/확정되지 않았다. PDF/source 표에서 두 construct가 실제 target construct로 같은 correlation matrix 안에 있는지 확인해야 한다. |
| S057 | SI-UB | MEDIUM_REVIEW_PRIORITY | review_before_add_no_numeric_value_yet | 최신 human-coded matrix에는 이 missing pair가 없고 AI trace는 source-review 후보로 올렸다. 그러나 candidate_value가 비어 있으므로 numeric cell은 아직 추출/확정되지 않았다. PDF/source 표에서 두 construct가 실제 target construct로 같은 correlation matrix 안에 있는지 확인해야 한다. |
| S057 | TRU-UB | MEDIUM_REVIEW_PRIORITY | review_before_add_no_numeric_value_yet | 최신 human-coded matrix에는 이 missing pair가 없고 AI trace는 source-review 후보로 올렸다. 그러나 candidate_value가 비어 있으므로 numeric cell은 아직 추출/확정되지 않았다. PDF/source 표에서 두 construct가 실제 target construct로 같은 correlation matrix 안에 있는지 확인해야 한다. |
| S138 | ANX-ATT | LOW_PROBABLE_CONSTRUCT_MISMATCH | do_not_add_now_unless_anxiety_construct_confirmed | AI term hit는 risk/fear 계열 단어에서 발생했을 가능성이 높다. Paper A의 ANX로 코딩하려면 source가 anxiety 또는 동등한 anxiety construct를 명시하고 상관값을 제공해야 한다. |
| S138 | ANX-BI | LOW_PROBABLE_CONSTRUCT_MISMATCH | do_not_add_now_unless_anxiety_construct_confirmed | AI term hit는 risk/fear 계열 단어에서 발생했을 가능성이 높다. Paper A의 ANX로 코딩하려면 source가 anxiety 또는 동등한 anxiety construct를 명시하고 상관값을 제공해야 한다. |
| S138 | ANX-EE | LOW_PROBABLE_CONSTRUCT_MISMATCH | do_not_add_now_unless_anxiety_construct_confirmed | AI term hit는 risk/fear 계열 단어에서 발생했을 가능성이 높다. Paper A의 ANX로 코딩하려면 source가 anxiety 또는 동등한 anxiety construct를 명시하고 상관값을 제공해야 한다. |
| S138 | ANX-FC | LOW_PROBABLE_CONSTRUCT_MISMATCH | do_not_add_now_unless_anxiety_construct_confirmed | AI term hit는 risk/fear 계열 단어에서 발생했을 가능성이 높다. Paper A의 ANX로 코딩하려면 source가 anxiety 또는 동등한 anxiety construct를 명시하고 상관값을 제공해야 한다. |
| S138 | ANX-PE | LOW_PROBABLE_CONSTRUCT_MISMATCH | do_not_add_now_unless_anxiety_construct_confirmed | AI term hit는 risk/fear 계열 단어에서 발생했을 가능성이 높다. Paper A의 ANX로 코딩하려면 source가 anxiety 또는 동등한 anxiety construct를 명시하고 상관값을 제공해야 한다. |
| S138 | ANX-SE | LOW_PROBABLE_CONSTRUCT_MISMATCH | do_not_add_now_unless_anxiety_construct_confirmed | AI term hit는 risk/fear 계열 단어에서 발생했을 가능성이 높다. Paper A의 ANX로 코딩하려면 source가 anxiety 또는 동등한 anxiety construct를 명시하고 상관값을 제공해야 한다. |
| S138 | ANX-SI | LOW_PROBABLE_CONSTRUCT_MISMATCH | do_not_add_now_unless_anxiety_construct_confirmed | AI term hit는 risk/fear 계열 단어에서 발생했을 가능성이 높다. Paper A의 ANX로 코딩하려면 source가 anxiety 또는 동등한 anxiety construct를 명시하고 상관값을 제공해야 한다. |
| S138 | ANX-TRU | LOW_PROBABLE_CONSTRUCT_MISMATCH | do_not_add_now_unless_anxiety_construct_confirmed | AI term hit는 risk/fear 계열 단어에서 발생했을 가능성이 높다. Paper A의 ANX로 코딩하려면 source가 anxiety 또는 동등한 anxiety construct를 명시하고 상관값을 제공해야 한다. |
| S138 | ANX-UB | LOW_PROBABLE_CONSTRUCT_MISMATCH | do_not_add_now_unless_anxiety_construct_confirmed | AI term hit는 risk/fear 계열 단어에서 발생했을 가능성이 높다. Paper A의 ANX로 코딩하려면 source가 anxiety 또는 동등한 anxiety construct를 명시하고 상관값을 제공해야 한다. |
| S138 | ATT-FC | LOW_TO_MEDIUM_REMAP_REVIEW | do_not_add_now_unless_facilitating_conditions_confirmed | AI term hit는 resources/support 계열 단어에서 발생했을 가능성이 있다. FC로 추가하려면 source가 facilitating conditions 또는 명백한 동등 construct를 쓰고 동일 source matrix에 numeric cell이 있어야 한다. |
| S138 | BI-FC | LOW_TO_MEDIUM_REMAP_REVIEW | do_not_add_now_unless_facilitating_conditions_confirmed | AI term hit는 resources/support 계열 단어에서 발생했을 가능성이 있다. FC로 추가하려면 source가 facilitating conditions 또는 명백한 동등 construct를 쓰고 동일 source matrix에 numeric cell이 있어야 한다. |
| S138 | EE-FC | LOW_TO_MEDIUM_REMAP_REVIEW | do_not_add_now_unless_facilitating_conditions_confirmed | AI term hit는 resources/support 계열 단어에서 발생했을 가능성이 있다. FC로 추가하려면 source가 facilitating conditions 또는 명백한 동등 construct를 쓰고 동일 source matrix에 numeric cell이 있어야 한다. |
| S138 | FC-PE | LOW_TO_MEDIUM_REMAP_REVIEW | do_not_add_now_unless_facilitating_conditions_confirmed | AI term hit는 resources/support 계열 단어에서 발생했을 가능성이 있다. FC로 추가하려면 source가 facilitating conditions 또는 명백한 동등 construct를 쓰고 동일 source matrix에 numeric cell이 있어야 한다. |
| S138 | FC-SE | LOW_TO_MEDIUM_REMAP_REVIEW | do_not_add_now_unless_facilitating_conditions_confirmed | AI term hit는 resources/support 계열 단어에서 발생했을 가능성이 있다. FC로 추가하려면 source가 facilitating conditions 또는 명백한 동등 construct를 쓰고 동일 source matrix에 numeric cell이 있어야 한다. |
| S138 | FC-SI | LOW_TO_MEDIUM_REMAP_REVIEW | do_not_add_now_unless_facilitating_conditions_confirmed | AI term hit는 resources/support 계열 단어에서 발생했을 가능성이 있다. FC로 추가하려면 source가 facilitating conditions 또는 명백한 동등 construct를 쓰고 동일 source matrix에 numeric cell이 있어야 한다. |
| S138 | FC-TRU | LOW_TO_MEDIUM_REMAP_REVIEW | do_not_add_now_unless_facilitating_conditions_confirmed | AI term hit는 resources/support 계열 단어에서 발생했을 가능성이 있다. FC로 추가하려면 source가 facilitating conditions 또는 명백한 동등 construct를 쓰고 동일 source matrix에 numeric cell이 있어야 한다. |
| S138 | FC-UB | LOW_TO_MEDIUM_REMAP_REVIEW | do_not_add_now_unless_facilitating_conditions_confirmed | AI term hit는 resources/support 계열 단어에서 발생했을 가능성이 있다. FC로 추가하려면 source가 facilitating conditions 또는 명백한 동등 construct를 쓰고 동일 source matrix에 numeric cell이 있어야 한다. |
| S176 | ANX-ATT | LOW_PROBABLE_NOT_TARGET_CONSTRUCT | do_not_add_probable_construct_absent | PDF text에서 확인된 Table 4 construct set은 HM, UB, BI, EE, FC, HA, PE, PI, SI, TR이며 ANX가 보이지 않는다. |
| S176 | ANX-BI | LOW_PROBABLE_NOT_TARGET_CONSTRUCT | do_not_add_probable_construct_absent | PDF text에서 확인된 Table 4 construct set은 HM, UB, BI, EE, FC, HA, PE, PI, SI, TR이며 ANX가 보이지 않는다. |
| S176 | ANX-EE | LOW_PROBABLE_NOT_TARGET_CONSTRUCT | do_not_add_probable_construct_absent | PDF text에서 확인된 Table 4 construct set은 HM, UB, BI, EE, FC, HA, PE, PI, SI, TR이며 ANX가 보이지 않는다. |
| S176 | ANX-FC | LOW_PROBABLE_NOT_TARGET_CONSTRUCT | do_not_add_probable_construct_absent | PDF text에서 확인된 Table 4 construct set은 HM, UB, BI, EE, FC, HA, PE, PI, SI, TR이며 ANX가 보이지 않는다. |
| S176 | ANX-PE | LOW_PROBABLE_NOT_TARGET_CONSTRUCT | do_not_add_probable_construct_absent | PDF text에서 확인된 Table 4 construct set은 HM, UB, BI, EE, FC, HA, PE, PI, SI, TR이며 ANX가 보이지 않는다. |
| S176 | ANX-SE | LOW_PROBABLE_NOT_TARGET_CONSTRUCT | do_not_add_probable_construct_absent | PDF text에서 확인된 Table 4 construct set은 HM, UB, BI, EE, FC, HA, PE, PI, SI, TR이며 ANX가 보이지 않는다. |
| S176 | ANX-SI | LOW_PROBABLE_NOT_TARGET_CONSTRUCT | do_not_add_probable_construct_absent | PDF text에서 확인된 Table 4 construct set은 HM, UB, BI, EE, FC, HA, PE, PI, SI, TR이며 ANX가 보이지 않는다. |
| S176 | ANX-TRU | LOW_PROBABLE_NOT_TARGET_CONSTRUCT | do_not_add_probable_construct_absent | PDF text에서 확인된 Table 4 construct set은 HM, UB, BI, EE, FC, HA, PE, PI, SI, TR이며 ANX가 보이지 않는다. |
| S176 | ANX-UB | LOW_PROBABLE_NOT_TARGET_CONSTRUCT | do_not_add_probable_construct_absent | PDF text에서 확인된 Table 4 construct set은 HM, UB, BI, EE, FC, HA, PE, PI, SI, TR이며 ANX가 보이지 않는다. |
| S176 | ATT-SE | LOW_PROBABLE_NOT_TARGET_CONSTRUCT | do_not_add_probable_construct_absent_or_mismatch | PDF text에서 확인된 Table 4 construct set은 HM, UB, BI, EE, FC, HA, PE, PI, SI, TR이며 SE가 보이지 않는다. PI/HA/TR 등은 Paper A의 SE로 자동 remap하면 안 된다. |
| S176 | BI-SE | LOW_PROBABLE_NOT_TARGET_CONSTRUCT | do_not_add_probable_construct_absent_or_mismatch | PDF text에서 확인된 Table 4 construct set은 HM, UB, BI, EE, FC, HA, PE, PI, SI, TR이며 SE가 보이지 않는다. PI/HA/TR 등은 Paper A의 SE로 자동 remap하면 안 된다. |
| S176 | EE-SE | LOW_PROBABLE_NOT_TARGET_CONSTRUCT | do_not_add_probable_construct_absent_or_mismatch | PDF text에서 확인된 Table 4 construct set은 HM, UB, BI, EE, FC, HA, PE, PI, SI, TR이며 SE가 보이지 않는다. PI/HA/TR 등은 Paper A의 SE로 자동 remap하면 안 된다. |
| S176 | FC-SE | LOW_PROBABLE_NOT_TARGET_CONSTRUCT | do_not_add_probable_construct_absent_or_mismatch | PDF text에서 확인된 Table 4 construct set은 HM, UB, BI, EE, FC, HA, PE, PI, SI, TR이며 SE가 보이지 않는다. PI/HA/TR 등은 Paper A의 SE로 자동 remap하면 안 된다. |
| S176 | PE-SE | LOW_PROBABLE_NOT_TARGET_CONSTRUCT | do_not_add_probable_construct_absent_or_mismatch | PDF text에서 확인된 Table 4 construct set은 HM, UB, BI, EE, FC, HA, PE, PI, SI, TR이며 SE가 보이지 않는다. PI/HA/TR 등은 Paper A의 SE로 자동 remap하면 안 된다. |
| S176 | SE-SI | LOW_PROBABLE_NOT_TARGET_CONSTRUCT | do_not_add_probable_construct_absent_or_mismatch | PDF text에서 확인된 Table 4 construct set은 HM, UB, BI, EE, FC, HA, PE, PI, SI, TR이며 SE가 보이지 않는다. PI/HA/TR 등은 Paper A의 SE로 자동 remap하면 안 된다. |
| S176 | SE-TRU | LOW_PROBABLE_NOT_TARGET_CONSTRUCT | do_not_add_probable_construct_absent_or_mismatch | PDF text에서 확인된 Table 4 construct set은 HM, UB, BI, EE, FC, HA, PE, PI, SI, TR이며 SE가 보이지 않는다. PI/HA/TR 등은 Paper A의 SE로 자동 remap하면 안 된다. |
| S176 | SE-UB | LOW_PROBABLE_NOT_TARGET_CONSTRUCT | do_not_add_probable_construct_absent_or_mismatch | PDF text에서 확인된 Table 4 construct set은 HM, UB, BI, EE, FC, HA, PE, PI, SI, TR이며 SE가 보이지 않는다. PI/HA/TR 등은 Paper A의 SE로 자동 remap하면 안 된다. |
