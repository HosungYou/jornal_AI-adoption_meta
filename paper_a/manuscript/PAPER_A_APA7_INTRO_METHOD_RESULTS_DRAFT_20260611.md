# AI Adoption in Higher Education: A Meta-Analytic Structural Equation Modeling Study

Draft date: 2026-06-11

## Draft Scope and Team Boundary

This file drafts the portions of Paper A that can be assembled from the current project evidence without taking over the team-authored Literature Review or Discussion. The Literature Review and Discussion headings are retained only as insertion points for team authors. Final structural path estimates, indirect effects, moderator estimates, and fit statistics remain lead-analysis insertion points.

## Introduction

Artificial intelligence tools are now embedded in higher education through large language models, intelligent tutoring systems, automated assessment systems, writing assistants, recommendation tools, and analytics platforms. Their spread has produced a rapidly expanding empirical literature on adoption, acceptance, and use. Yet this literature remains difficult to interpret cumulatively because studies draw from overlapping but nonidentical acceptance frameworks, measure different subsets of constructs, and report evidence in formats that do not directly support a single structural synthesis.

Meta-analytic structural equation modeling (MASEM) is well suited to this problem because it can synthesize study-level correlation matrices and test a theory-guided network of relationships. In AI adoption research, this is especially important. Performance expectancy, effort expectancy, social influence, facilitating conditions, attitude, self-efficacy, behavioral intention, and use behavior provide continuity with TAM, TPB, and UTAUT. At the same time, trust in AI and AI anxiety capture psychological features of AI systems that are not fully reducible to general usefulness or ease-of-use beliefs.

The present study therefore develops a MASEM of AI adoption in higher education that integrates traditional technology acceptance constructs with AI-specific psychological constructs. The working model treats attitude as a theoretically meaningful mediator rather than assuming that the parsimonious UTAUT exclusion of attitude applies unchanged to AI adoption contexts. It also tests whether trust and anxiety contribute to behavioral intention beyond standard acceptance predictors.

The study is designed to answer four research questions: (a) whether core TAM/UTAUT structural paths hold in the pooled AI adoption evidence base, (b) whether AI-specific trust and anxiety add explanatory value beyond traditional predictors, (c) whether attitude mediates effects from performance and effort expectancy to behavioral intention, and (d) whether year, cultural context, education level, and AI tool type moderate focal relationships.

## Literature Review [Reserved for Team Contribution]

[Reserved. Team authors should draft the theory synthesis, construct definitions, prior TAM/UTAUT MASEM evidence, AI trust/anxiety evidence, and hypothesis-development prose here. This draft does not supply Literature Review prose.]

## Method

### Design and Reporting Standards

Paper A is the parent meta-analysis for the AI adoption evidence-synthesis project. It uses systematic-review procedures to identify eligible studies and applies MASEM to synthesize construct-level relationships. Reporting is organized for PRISMA 2020 and APA Meta-Analysis Reporting Standards alignment, with a separate public or supplementary package expected for search records, coding rules, analytic scripts, and model outputs.

### Search, Screening, and Eligibility

The documented search workflow yielded 22,166 records. After deduplication, 16,189 records remained for screening. The screening workflow used tiered AI-assisted and human-verification procedures. The current Paper A proposal brief reports 224 included empirical studies at the proposal checkpoint; the repository README separately marks the final full-text MASEM-eligible count as a lead-analysis value to be locked before submission. The manuscript should harmonize this count before journal submission.

Studies were eligible when they examined AI technology adoption, acceptance, or use in higher education; reported quantitative relationships among at least two focal constructs; included undergraduate students, graduate students, instructors, faculty, or comparable higher-education users; and provided direct correlations, matrix tables, Fornell-Larcker or related evidence, HTMT or sufficient statistics that could be evaluated for MASEM readiness. Studies without usable target construct-pair evidence were excluded from the primary MASEM input while preserving audit trails for sensitivity and source-risk review.

### Constructs and Model Architecture

The primary structural model uses 10 constructs: performance expectancy, effort expectancy, social influence, facilitating conditions, attitude, self-efficacy, trust in AI, AI anxiety, behavioral intention, and use behavior. The planned structural architecture places performance expectancy and effort expectancy upstream of attitude, attitude upstream of behavioral intention, and behavioral intention upstream of use behavior. Social influence, self-efficacy, trust, and anxiety are modeled as additional antecedents of behavioral intention, and facilitating conditions are modeled as an antecedent of use behavior.

### Coding, Source Adjudication, and Analysis-Ready Inputs

The extraction workflow separates raw coder workbooks, pre-adjudication disagreement records, source-document decisions, analysis-ready direct-r inputs, expanded direct-r-form inputs, and converted/source-statistic sensitivity inputs. Raw coder workbooks are preserved as returns and are not overwritten by downstream consensus or analysis scripts.

The 2026-06-05 Paper1 analysis-ready package defines three analysis sets. The primary set keeps source-reported or source-adjudicated direct-r rows for the main MASEM input. The expanded set retains all human-consensus direct-r-form rows while explicitly marking model-derived or converted rows. The sensitivity set keeps beta/path/source-statistic converted rows for sensitivity analysis rather than treating them as direct-r equivalents.

### Meta-Analytic Structural Equation Modeling Plan

The primary analysis will use two-stage MASEM. Stage 1 will pool study-level correlation matrices using a random-effects model and full-information handling of incomplete construct-pair coverage when supported by the software and data structure. Stage 2 will fit the prespecified structural model to the pooled matrix using weighted least squares. Moderator analyses will be evaluated with one-stage MASEM or equivalent meta-regression methods when the moderator data are sufficiently complete.

Sensitivity analyses will evaluate whether conclusions change when expanded direct-r-form rows, converted beta/path/source-statistic rows, source-risk exclusions, and influence diagnostics are included or excluded. The S072 ANX-EE r = 1.0 row is excluded from the primary model input and retained only as a trace/influence diagnostic.

## Results

### Search and Screening Status

The current project records document 22,166 identified records and 16,189 records after deduplication. The screening pipeline further reduced records through keyword filtering, AI-assisted classification, and human verification. The lead-analysis manuscript should insert the final PRISMA counts for full-text assessment, exclusions with reasons, and final MASEM-eligible studies after the final inclusion file is locked.

**Table 1**

*Current Paper A Search and Screening Counts*

| Stage | Count | Status for manuscript |
| --- | --- | --- |
| Records identified | 22,166 | Ready to report |
| After deduplication | 16,189 | Ready to report |
| After keyword filter | 3,274 | Repository README checkpoint |
| AI-assisted human review queue | 1,457 | Repository README checkpoint |
| Included studies | 224 proposal checkpoint; final count to lock | Lead confirmation required before submission |

Note. Draft table; update after lead analysis lock where indicated.

### Analysis-Ready Evidence Base

At the 2026-06-05 analysis-ready checkpoint, the primary direct-r input contained 822 rows, the expanded direct-r-form input contained 1,303 rows, the converted/source-statistic sensitivity input contained 481 rows, and the long stacked file contained 2,606 rows. Within the primary file, 805 rows were direct-r-like and 17 rows remained non-direct or source-statistic review candidates.

**Table 2**

*Paper A Analysis-Ready Input Sets*

| Input set | Rows | Manuscript role |
| --- | --- | --- |
| Primary direct-r | 822 | Main MASEM input after final source and sample-size policy checks |
| Expanded direct-r-form | 1,303 | Sensitivity or expanded coverage layer |
| Converted beta/path/source-statistic | 481 | Sensitivity layer, not direct-r equivalence |
| Long stacked file | 2,606 | Audit and workflow trace layer |

Note. Draft table; update after lead analysis lock where indicated.

### Pre-Model Quality-Control Findings

The pre-model QC report identified 55 construct-pair coverage rows and no duplicate study-pair keys. It also flagged moderator missingness and numeric QC issues. Sample-size and moderator missingness remain the main analysis-readiness risk for moderator and N-weighted SEM claims. The S072 ANX-EE r = 1.0 row is treated as an influence diagnostic and excluded from the primary model input.

**Table 3**

*Paper A Pre-Model QC Items*

| QC item | Current count or rate | Draft interpretation |
| --- | --- | --- |
| Construct-pair coverage rows | 55 | Supports pair-level coverage reporting |
| Duplicate study-pair keys | 0 | No duplicate key blocker in QC report |
| Moderator missingness fields | 7 | Moderator claims require missingness caveats |
| Numeric QC flagged rows | 2,482 | Driven primarily by missing sample-size numeric fields |
| r = +/-1 influence check | 2 rows: S072 ANX-EE in primary and expanded | Exclude from primary; retain as diagnostic |

Note. Draft table; update after lead analysis lock where indicated.

### Primary MASEM Results [Lead Analysis Insertion Point]

[Insert Stage 1 pooled correlation matrix, heterogeneity estimates, Stage 2 path coefficients, indirect effects, model fit, and sensitivity results after the lead-analysis run is locked. Do not convert this placeholder into substantive conclusions until the final TSSEM/OSMASEM specification, sample-size policy, and source-risk rules are finalized.]

## Discussion [Reserved for Team Contribution]

[Reserved. Team authors should draft interpretation, theoretical implications, practical implications, limitations, and future research after the lead-analysis Results are inserted.]

## References

- Ajzen, I. (1991). The theory of planned behavior. Organizational Behavior and Human Decision Processes, 50(2), 179-211.
- Blut, M., Chong, A., Tsiga, Z., & Venkatesh, V. (2022). Meta-analysis of the unified theory of acceptance and use of technology (UTAUT). Journal of the Association for Information Systems, 23(1), 13-95.
- Cheung, M. W.-L. (2015). Meta-analysis: A structural equation modeling approach. Wiley.
- Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13(3), 319-340.
- Fishbein, M., & Ajzen, I. (1975). Belief, attitude, intention and behavior: An introduction to theory and research. Addison-Wesley.
- Jak, S., & Cheung, M. W.-L. (2020). Meta-analytic structural equation modeling with moderating effects on SEM parameters. Psychological Methods, 25(4), 430-449.
- Scherer, R., Siddiq, F., & Tondeur, J. (2019). The technology acceptance model (TAM): A meta-analytic structural equation modeling approach. Computers & Education, 128, 13-35.
- Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. MIS Quarterly, 27(3), 425-478.
