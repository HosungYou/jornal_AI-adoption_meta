# MASEM Codebook: AI Adoption Meta-Analysis
## Data Dictionary for Multi-Sheet Coding Template

**Version:** 1.0.0
**Last Updated:** 2026-02-16
**Contact:** Hosung Hwang

---

## SHEET 1: Study_Metadata

Complete bibliographic and methodological information for each included study.

| Variable Name | Type | Description | Valid Values / Range | Coding Instructions |
|---|---|---|---|---|
| `study_id` | text | Unique identifier for the study | Format: `AuthorYYYY_v#` (e.g., `Smith2023_v1`) | Assign sequentially. Add `_v2`, `_v3` for multiple independent samples in one publication. |
| `authors` | text | All authors in citation order | Last, F., Last, F., & Last, F. | Use APA format. Maximum 20 authors, then "et al." |
| `year` | int | Publication year | Range: 2000-2026 | Use year of publication, not data collection. For in-press: use 9999. |
| `title` | text | Full article title | Free text | Copy exactly, including subtitle after colon. |
| `journal` | text | Journal or source name | Free text | Use full journal name (not abbreviation). For dissertations: "Dissertation: [University]". |
| `doi` | text | Digital Object Identifier | Format: `10.####/######` | Include full DOI. If unavailable: "NA". |
| `country` | text | Country/region of data collection | ISO 3166-1 alpha-2 codes | Use 2-letter codes (US, CN, DE, GB, AU). For multi-country: "XX" (mixed). |
| `education_level` | cat | Education level of participants | `k12`, `undergraduate`, `graduate`, `mixed` | **k12**: K-12 students/teachers. **undergraduate**: college/university undergrad. **graduate**: master's/doctoral students. **mixed**: 2+ levels. |
| `user_role` | cat | Role in educational setting | `student`, `instructor`, `administrator`, `mixed` | **student**: learners. **instructor**: teachers/faculty. **administrator**: educational administrators. **mixed**: 2+ roles. |
| `discipline` | cat | Academic discipline | `stem`, `humanities`, `social_science`, `health_science`, `mixed` | **stem**: science, technology, engineering, math. **humanities**: arts, literature, languages. **social_science**: psychology, sociology, education. **health_science**: medicine, nursing. **mixed**: multiple disciplines. |
| `ai_tool_type` | cat | Type of AI tool in education | `chatbot_llm`, `its`, `lms_ai`, `auto_grading`, `writing_assistant`, `adaptive_learning`, `general` | **chatbot_llm**: ChatGPT, conversational AI. **its**: intelligent tutoring systems. **lms_ai**: LMS-integrated AI. **auto_grading**: automated grading systems. **writing_assistant**: Grammarly, AI writing tools. **adaptive_learning**: personalized learning platforms. **general**: unspecified educational AI. |
| `institutional_type` | cat | Type of institution | `public`, `private`, `online`, `community_college`, `mixed` | **public**: public schools/universities. **private**: private institutions. **online**: fully online/distance education. **community_college**: 2-year colleges. **mixed**: multiple types. |
| `n_total` | int | Total sample size | Range: 30-999999 | After listwise deletion for analysis. |
| `pct_female` | float | Percentage female participants | Range: 0-100 | If unreported: "NA". |
| `mean_age` | float | Mean age of sample | Range: 10-90 | If unreported: "NA". For categorical age: compute midpoint-weighted mean. |
| `pub_type` | cat | Publication type | `journal`, `conference`, `dissertation`, `preprint`, `book_chapter` | **journal**: peer-reviewed journal article. **conference**: published proceedings. **dissertation**: PhD/Master's thesis. **preprint**: ArXiv, SSRN, OSF. |
| `study_design` | cat | Research design | `cross_sectional`, `longitudinal`, `experimental`, `quasi_experimental` | **cross_sectional**: single time point. **longitudinal**: 2+ waves. **experimental**: random assignment. |
| `data_collection` | cat | Data collection method | `online_survey`, `in_person_survey`, `interview`, `mixed_methods`, `secondary_data` | Primary method used. |
| `response_rate` | float | Survey response rate (%) | Range: 0-100 | If unreported: "NA". Only for survey designs. |
| `cmb_control` | cat | Common method bias control | `none`, `procedural`, `statistical`, `both` | **none**: no controls mentioned. **procedural**: temporal/psychological separation, anonymity. **statistical**: Harman's test, marker variable, CFA. **both**: procedural + statistical. |

---

## SHEET 2: Correlation_Matrix

Pairwise correlation data for all 66 construct pairs (12 constructs = 66 unique pairs).

| Variable Name | Type | Description | Valid Values / Range | Coding Instructions |
|---|---|---|---|---|
| `study_id` | text | Foreign key to Study_Metadata | Format: `AuthorYYYY_v#` | Must match `study_id` in Sheet 1. One row per study-construct_pair. |
| `construct_1` | cat | First construct in pair | `PE`, `EE`, `SI`, `FC`, `BI`, `UB`, `ATT`, `SE`, `TRU`, `ANX`, `TRA`, `AUT` | Always use standardized abbreviation. Order alphabetically (construct_1 < construct_2). |
| `construct_2` | cat | Second construct in pair | Same as construct_1 | See above. For PE-EE pair: `construct_1=EE`, `construct_2=PE`. |
| `r` | float | Pearson correlation coefficient | Range: -1.00 to +1.00 | Extract from correlation matrix. If β/path coefficient: convert using **Aloe & Becker (2012)** formula. If d/t-test: convert to r first. Round to 3 decimals. |
| `n` | int | Sample size for this correlation | Range: 30-999999 | Use pairwise n if available. Otherwise use study `n_total`. |
| `se` | float | Standard error of r | Range: 0-1 | If available, extract directly. Otherwise computed as: `SE = sqrt((1-r²)/(n-2))`. |
| `p_value` | float | Statistical significance | Range: 0-1 | Extract if reported. If only sig stars: `***` = 0.001, `**` = 0.01, `*` = 0.05, `ns` = 0.99. |
| `ci_lower` | float | Lower bound 95% CI | Range: -1 to +1 | Extract if reported, else compute from r and SE. |
| `ci_upper` | float | Upper bound 95% CI | Range: -1 to +1 | Extract if reported, else compute from r and SE. |
| `data_source` | cat | Source of correlation | `correlation_matrix`, `path_coefficient`, `regression_table`, `text`, `imputed` | **correlation_matrix**: Pearson r table. **path_coefficient**: SEM β converted to r. **regression_table**: standardized β. **text**: reported in narrative. **imputed**: not reported, computed from other cells. |
| `conversion_method` | cat | Method if converted from β | `aloe_becker_2012`, `peterson_brown_2005`, `none` | Use **Aloe & Becker (2012)** for β→r conversion when SEM model available. `none` if r was directly reported. |

**Note:** Studies must report ≥50% of construct pairs (33/66) to be eligible. Missing cells coded as `NA`.

---

## SHEET 3: Construct_Mapping

Maps study-specific construct labels to standardized 12-construct taxonomy.

| Variable Name | Type | Description | Valid Values / Range | Coding Instructions |
|---|---|---|---|---|
| `study_id` | text | Foreign key to Study_Metadata | Format: `AuthorYYYY_v#` | Must match Sheet 1. |
| `original_construct_name` | text | Exact label used in study | Free text | Copy verbatim from study (e.g., "Perceived Usefulness", "PU", "Expected Performance"). |
| `standard_construct` | cat | Mapped standardized construct | `PE`, `EE`, `SI`, `FC`, `BI`, `UB`, `ATT`, `SE`, `TRU`, `ANX`, `TRA`, `AUT` | Use crosswalk table (see `TAM_UTAUT_AI_construct_crosswalk.md`). |
| `mapping_confidence` | cat | Confidence in mapping | `exact`, `high`, `moderate`, `low` | **exact**: identical label + definition. **high**: synonymous label, matching definition. **moderate**: label differs, definition matches. **low**: ambiguous, required judgment call. |
| `num_items` | int | Number of scale items | Range: 1-20 | Number of survey items measuring this construct. If unreported: "NA". |
| `scale_citation` | text | Source of measurement scale | Free text | Original scale development citation (e.g., "Davis, 1989"). If ad-hoc: "Author-developed". |
| `cronbach_alpha` | float | Reliability coefficient | Range: 0-1 | Cronbach's α if reported. If composite reliability (CR): note in `notes`. |
| `ave` | float | Average Variance Extracted | Range: 0-1 | For SEM studies. If unavailable: "NA". |
| `notes` | text | Additional mapping notes | Free text | Flag unusual operationalizations, reversed scales, ambiguities. |
| `flagged_for_review` | bool | Requires expert adjudication | `TRUE`, `FALSE` | Mark `TRUE` if `mapping_confidence=low` or construct definition deviates substantially. |

---

## SHEET 4: Moderator_Variables

Study-level characteristics for meta-regression and subgroup analysis.

| Variable Name | Type | Description | Valid Values / Range | Coding Instructions |
|---|---|---|---|---|
| `study_id` | text | Foreign key to Study_Metadata | Format: `AuthorYYYY_v#` | Must match Sheet 1. |
| `pub_year_tertile` | cat | Publication year tercile | `early` (2000-2018), `mid` (2019-2022), `recent` (2023-2026) | Split included studies into 3 equal groups by year. |
| `mandatory_use` | cat | Voluntariness of AI use | `voluntary`, `mandatory`, `mixed`, `unclear` | **voluntary**: users choose to adopt. **mandatory**: required by institution/instructor. **unclear**: not specified. |
| `experience_level` | cat | Prior AI experience | `novice`, `intermediate`, `expert`, `mixed`, `unclear` | Based on study's sample description. |
| `culture_region` | cat | Cultural region | `north_america`, `europe`, `east_asia`, `south_asia`, `middle_east`, `africa`, `latin_america`, `oceania`, `multi_region` | Based on Hofstede cultural classifications. |
| `theory_base` | cat | Primary theoretical framework | `TAM`, `UTAUT`, `TPB`, `SCT`, `IDT`, `TTF`, `mixed`, `other` | **TAM**: Technology Acceptance Model. **UTAUT**: Unified Theory. **TPB**: Theory of Planned Behavior. **SCT**: Social Cognitive Theory. **IDT**: Innovation Diffusion Theory. **TTF**: Task-Technology Fit. |
| `measurement_quality` | cat | Overall scale quality | `high`, `moderate`, `low` | **high**: all α > 0.80, validated scales. **moderate**: most α > 0.70. **low**: α < 0.70 or ad-hoc scales. |
| `student_convenience_sample` | cat | Student convenience sampling | `no`, `yes` | **no**: probability sample or diverse recruitment. **yes**: single class/course convenience sample. |
| `single_institution` | cat | Single institution study | `no`, `yes` | **no**: multi-institutional sample. **yes**: data from only one school/university. |
| `self_selection_bias` | cat | Self-selection in AI adoption | `no`, `yes` | **no**: random assignment or all students. **yes**: only AI adopters/volunteers studied. |
| `course_embedded_participation` | cat | Course requirement participation | `no`, `yes` | **no**: voluntary research participation. **yes**: participation tied to course credit/requirement. |

---

## SHEET 5: AI_Extraction_Provenance

AI-assisted coding provenance tracking.

| Variable Name | Type | Description | Valid Values / Range | Coding Instructions |
|---|---|---|---|---|
| `study_id` | text | Foreign key to Study_Metadata | Format: `AuthorYYYY_v#` | Must match Sheet 1. |
| `extraction_phase` | cat | Pipeline phase | `phase0_rag`, `phase1_extraction`, `phase2_mapping`, `phase3_consensus`, `phase4_sampling`, `phase5_resolution`, `phase6_qa` | See pipeline documentation. |
| `ai_model_primary` | text | Primary AI model used | `claude-sonnet-4-5`, `gpt-4o`, `llama-3.3-70b`, `human` | Model that produced the extraction. |
| `extraction_timestamp` | text | ISO 8601 timestamp | Format: `YYYY-MM-DDTHH:MM:SSZ` | Automated by pipeline. |
| `confidence_score` | float | AI confidence rating | Range: 0-1 | Self-reported confidence from AI model. If human: "NA". |
| `consensus_agreement` | int | Number of models agreeing | Range: 0-3 | In Phase 3. How many models produced identical extraction. |
| `human_verified` | bool | Expert adjudication flag | `TRUE`, `FALSE` | `TRUE` if human coder reviewed/modified this extraction. |
| `discrepancy_notes` | text | Inter-coder differences | Free text | Document disagreements between AI models or human override reasons. |
| `cost_usd` | float | Extraction cost | Range: 0-100 | API cost for this study's extraction (in USD). |

---

## SHEET 6: Quality_Assessment

Risk of bias assessment.

| Variable Name | Type | Description | Valid Values / Range | Coding Instructions |
|---|---|---|---|---|
| `study_id` | text | Foreign key to Study_Metadata | Format: `AuthorYYYY_v#` | Must match Sheet 1. |
| `selection_bias` | cat | Representativeness of sample | `low_risk`, `some_concerns`, `high_risk` | **low_risk**: probability sampling. **some_concerns**: convenience but diverse. **high_risk**: highly selected (e.g., single organization). |
| `measurement_bias` | cat | Construct validity | `low_risk`, `some_concerns`, `high_risk` | **low_risk**: validated scales, high reliability. **some_concerns**: adapted scales, moderate reliability. **high_risk**: ad-hoc scales, low reliability. |
| `reporting_bias` | cat | Selective reporting | `low_risk`, `some_concerns`, `high_risk` | **low_risk**: all constructs/paths reported. **some_concerns**: some missing correlations. **high_risk**: incomplete correlation matrix. |
| `cmb_risk` | cat | Common method bias | `low_risk`, `some_concerns`, `high_risk` | **low_risk**: procedural + statistical controls. **some_concerns**: procedural OR statistical. **high_risk**: no controls. |
| `overall_quality` | cat | Overall risk of bias | `low_risk`, `some_concerns`, `high_risk` | Aggregate judgment. If ANY domain = high_risk → overall = high_risk. |
| `sensitivity_exclusion` | bool | Exclude from sensitivity analysis | `TRUE`, `FALSE` | `TRUE` if `overall_quality = high_risk`. |

---

## Notes on Multi-Sheet Structure

- **Primary key:** `study_id` links all sheets.
- **66 correlation pairs:** Sheet 2 will have 66 rows per study (if complete matrix).
- **Missing data:** Use `NA` for numeric fields, leave categorical blank if truly unknown.
- **Conversion formulas:**
  - **β to r (Aloe & Becker, 2012):** `r ≈ β + 0.05λ` where λ = standardized residual (if available, else assume λ=0).
  - **Peterson & Brown (2005):** `r = β × sqrt(R²)` (if full model R² available).
  - **SE computation:** `SE = sqrt((1-r²)/(n-2))`.

---

## Version Control

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | 2026-02-16 | Initial codebook |

**End of Codebook**
