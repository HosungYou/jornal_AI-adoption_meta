# Can a Prespecified LLM Workflow Augment MASEM-Ready Evidence Extraction?

Draft date: 2026-06-11

## Draft Scope and Team Boundary

This file drafts the Introduction, Method/Analysis, Results, claim boundary, and data-availability components for Paper B. It does not draft the team-authored Literature Review or Discussion. The manuscript is framed as an LLM augmentation and validation study for evidence synthesis, not as an LLM replacement claim or vendor-ranking benchmark.

## Introduction

Evidence synthesis for meta-analytic structural equation modeling requires extraction decisions that are more demanding than simple article summarization. A usable evidence record must distinguish source-reported direct correlations from converted statistics, map constructs consistently, preserve source provenance, identify source-absence cases, handle human-coder disagreement, and maintain enough sample-size and matrix information to support downstream SEM weighting and model fitting.

Large language models may help with this work, but their value depends on the unit of evaluation. Treating thousands of heterogeneous task units as one accuracy denominator would obscure the difference between low-consequence metadata, high-consequence direct-r extraction, source-risk triage, and downstream substitution risk. A defensible validation study therefore requires a source-anchored adjudicated human reference standard, locked model outputs, prespecified task-family scoring rules, and claim boundaries that separate workflow augmentation from autonomous replacement.

Paper B evaluates whether a prespecified LLM workflow can augment MASEM-ready extraction in an AI adoption evidence-synthesis project. The primary workflow is Codex GPT-5.5. Claude Sonnet and Gemini 3 Flash are used only as supplementary cross-model sensitivity and triage signals. The study asks whether the workflow can recover extraction targets, characterize errors by source condition, prioritize expert review, and preserve downstream MASEM or TSSEM conclusions under bounded diagnostic substitution checks.

## Literature Review [Reserved for Team Contribution]

[Reserved. Team authors should draft prior work on LLM-assisted systematic reviews, extraction automation, human-in-the-loop evidence synthesis, and benchmark limitations. This draft does not supply Literature Review prose.]

## Method

### Corpus, Data States, and Reference Standard

The parent corpus is an AI adoption in higher education MASEM project. Paper B uses the validation and extraction subset derived from that corpus. The workflow separates raw independent human coder workbooks, pre-adjudication human-human disagreement queues, source-document adjudication decisions, a frozen source-anchored adjudicated human reference layer, locked LLM outputs, and downstream diagnostic analysis files.

The canonical human-consensus package is the OneDrive folder Paper2_Human_Final_Consensus_20260605_v2, with Git reference-freeze and scoring artifacts derived downstream. The post-freeze full-corpus reference contains 213 studies and preserves caveats rather than silently rewriting raw coder workbooks. The legacy model-explicit denominator-family package contains 8,783 task units and remains useful as pre-full-corpus reproducibility evidence, but final full-corpus result claims are governed by the 2026-06-09 post-freeze Step 5 gate.

### Task Families and Scoring Rules

Task units are not interpreted as one accuracy denominator. Each row is assigned a denominator family and scoring eligibility rule. Direct-r extraction rows, converted or source-statistic numeric rows, metadata rows, human-review decision rows, source-absence rows, duplicate-source exclusions, blank/absence consensus rows, and trace rows are scored or interpreted separately.

Direct-r numeric extraction is scored with an absolute error tolerance of 0.005. Metadata extraction is reported using strict exact match and relaxed normalized match. Abstentions on scorable rows count as incorrect and are reported as workflow behavior. Blank/absence consensus and human-disagreement trace rows are interpreted as triage evidence rather than final content-accuracy rows.

### Model Scope and Locked Outputs

Codex GPT-5.5 is the primary prespecified workflow. Claude Sonnet and Gemini 3 Flash are retained as supplementary sensitivity and triage evidence only. Clean model-explicit locked outputs are available for Codex GPT-5.5, Claude Sonnet, and Gemini 3 Flash across 7,859 task units in the legacy model-explicit package. Earlier Claude default-unspecified rows are retained only as audit provenance after the Sonnet backfill.

### Analysis Plan

RQ1 evaluates extraction validity by denominator family and task stratum. RQ2 classifies errors by source condition, source-type status, denominator family, and downstream consequence. RQ3 evaluates whether model behavior, cross-model disagreement, source-risk flags, and human-disagreement traces prioritize expert review. Downstream substitution analyses are reported only as bounded diagnostics: they test whether expert-reviewed LLM-assisted inputs change human-reference pooled correlations or TSSEM paths under the current eligible subset.

The approved missing-N rule excludes rows without source-supported numeric sample size from N-weighted TSSEM/MASEM weighting unless later source checks supply numeric N. The deterministic reconciliation layer fills numeric N for 741 of 804 legacy primary rerun rows and excludes the remaining 63 rows from N-weighted SEM weighting. Therefore, all-row SEM wording is prohibited unless numeric N is completed for every SEM input row.

## Results

### Reference and Locked-Output Coverage

The legacy model-explicit package contains 8,783 task units. Codex GPT-5.5, Claude Sonnet, and Gemini 3 Flash each have clean model-explicit locked outputs for 7,859 eligible task units. These rows support denominator-family scoring and supplementary cross-model triage, not a single pooled vendor-ranking denominator.

**Table 1**

*Paper B Data States and Claim Roles*

| Data state | Current evidence | Claim role |
| --- | --- | --- |
| Frozen full-corpus reference | 213 studies frozen on 2026-06-09 | Current governing reference layer |
| Legacy task-unit package | 8,783 task units | Pre-full-corpus reproducibility and denominator-family evidence |
| Clean model-explicit outputs | 7,859 rows per model | RQ1-RQ3 task-family scoring and sensitivity |
| Bounded source-rendered M1-R shard | 90 rows | Staged diagnostic only, not full-corpus accuracy |
| Core-6 TSSEM diagnostic | 15 complete-case studies | Subset substitution-stability diagnostic |

Note. Draft table; update after lead analysis lock where indicated.

### RQ1: Extraction Validity by Task Family

For the primary Codex GPT-5.5 workflow in the legacy model-explicit package, source-reported direct-r extraction contained 323 scored rows. Codex matched 3 rows within the 0.005 tolerance and abstained on 320 rows. The 43 source_blank_direct_r rows were retained in the direct-r extraction family but all received abstentions. Converted numeric strata included 30 beta rows, 53 beta/path-converted human-consensus rows, and 5 numeric source-statistic rows; all were abstained under the current locked prompt/input condition.

Metadata performance varied by field. Codex achieved exact and relaxed match for all scored source-type rows and statistic-count rows, and 16 of 19 study-design rows. Other metadata families, including AI type, user role, country, and first author, showed high abstention rates. These results describe task-family workflow behavior under locked inputs rather than general model capability.

**Table 2**

*Primary Codex GPT-5.5 RQ1 Numeric and Metadata Results*

| Task stratum | Scored rows | Correct | Abstentions | Interpretation |
| --- | --- | --- | --- | --- |
| Source-reported direct-r | 323 | 3 | 320 | Not safe for autonomous numeric substitution |
| Source-blank direct-r | 43 | 0 | 43 | Direct-r family with weaker source evidence |
| Converted beta | 30 | 0 | 30 | High-consequence numeric stratum |
| Beta/path converted by human consensus | 53 | 0 | 53 | High-consequence numeric stratum |
| Numeric source-statistic converted by human consensus | 5 | 0 | 5 | High-consequence numeric stratum |
| Metadata source type | 18 | 18 | 0 | Strong field-specific performance |
| Metadata study design | 19 | 16 | 0 | Relatively strong field-specific performance |

Note. Draft table; update after lead analysis lock where indicated.

### RQ2: Error Taxonomy and Source Conditions

The dominant RQ2 pattern was abstention on scorable rows. Codex produced 320 abstentions for source-reported direct-r rows, 43 abstentions for source-blank direct-r rows, and 88 abstentions across converted/source-type numeric strata. Metadata extraction also contained 381 abstentions on scorable source-evidence rows and 29 metadata mismatches. These patterns show why high-consequence MASEM numeric rows cannot be replaced automatically under the current workflow.

Blank/absence consensus and human-disagreement trace rows behaved differently from final content-accuracy rows. They are useful because they show over-answering, abstention, and cross-model inconsistency in cases where source evidence is absent, ambiguous, or disputed. They should not be collapsed with direct-r or metadata accuracy.

### RQ3: Human-Review Triage and Cross-Model Sensitivity

The RQ3 triage analysis used the full 8,783 task-unit reference universe and left-joined locked model rows where available. It classified 1,196 rows as P0 expert-review numeric or MASEM tasks, 649 rows as P1 source or human-disagreement review tasks, 483 rows as P1 general review-signal tasks, 6,412 rows as P2 blank-behavior audit rows, 1 row as a P2 scoring-completeness check, and 42 rows as low priority after the primary workflow check.

Cross-model behavior disagreement appeared in 6,592 task units and is interpreted only as a review-prioritization signal. Human-disagreement traces appeared in 467 task units, source or trace risk appeared in 1,525 task units, and 924 task units were reference-only rows without locked model output. These signals support targeted review triage, not model ranking.

**Table 3**

*RQ3 Review Priority Counts*

| Review priority | Task units | Manuscript interpretation |
| --- | --- | --- |
| P0 expert-review numeric or MASEM | 1,196 | High-consequence numeric review |
| P1 source or human-disagreement review | 649 | Source-risk or human-disagreement review |
| P1 general review signal | 483 | Other review-prioritization signal |
| P2 blank-behavior audit | 6,412 | Workflow behavior, not final accuracy |
| P2 scoring-completeness check | 1 | Completeness audit |
| P3 low priority after primary check | 42 | Low priority under current scoring |

Note. Draft table; update after lead analysis lock where indicated.

### Post-Freeze Source-Rendered Diagnostic Evidence

After the 2026-06-09 full-corpus reference freeze, a source-rendered Step 5 workflow reached full target source-rendering coverage and executed a bounded 90-row M1-R shard with Codex GPT-5.5. The shard produced 90 of 90 locked rows, model_cli_error = 0, source quote policy violations = 0, 65 nonblank answers, and 25 abstentions. Exception-aware generic numeric scoring was 15 of 30 for direct/source-r rows, 27 of 30 for latent or construct correlations, and 13 of 30 for secondary beta/path rows. This is staged diagnostic evidence only and must not be interpreted as full-corpus accuracy.

### Downstream MASEM and TSSEM Diagnostic

The human-reference MASEM baseline is the Paper1 tiered primary model-ready file with 804 rows. The pre-tiered primary file contains 822 rows and is retained for audit. Expanded and converted inputs contain 1,303 and 481 rows, respectively, and are treated as sensitivity layers.

The P0/P1 expert-review layer covered 1,845 task units, including 1,196 P0 numeric/MASEM rows and 649 P1 source or human-disagreement rows. The expert-reviewed LLM-assisted primary input contains 804 rows. It applies 3 exact numeric replacements, all of which match the frozen human-reference values, yielding 0 nonzero value deltas relative to the human-reference baseline.

At the pooled-correlation level, the primary expert-reviewed LLM-assisted input has maximum absolute mean-r delta = 0.000000 and no structural edges with nonzero change. Source-risk exclusion and converted-input augmentation are sensitivity diagnostics, with maximum absolute mean-r deltas of 0.407000 and 0.116229, respectively, and nonzero changes on 9 structural edges in each sensitivity layer.

The bounded R/metaSEM TSSEM diagnostic used N-weighted eligible rows and the six-construct complete-case subset PE, EE, SI, FC, BI, and UB. Fifteen studies reported all 15 pairwise correlations for this subset, yielding 225 aggregated pair rows. Stage 1 random-effects TSSEM and Stage 2 path models converged for both the human-reference baseline and the expert-reviewed LLM-assisted input. The maximum absolute pooled-correlation delta was 0.00000000, and the structural paths were identical across scenarios: PE to BI = 0.376578, EE to BI = 0.271255, SI to BI = 0.242604, FC to UB = 0.222908, and BI to UB = 0.566349. Model fit was also identical: chi-square = 3.554181, df = 4, p = 0.469688, CFI = 1.000000, RMSEA = 0.000000, and SRMR = 0.025199.

**Table 4**

*Downstream Substitution and TSSEM Diagnostic*

| Diagnostic layer | Current result | Permitted claim |
| --- | --- | --- |
| Expert-reviewed primary input | 804 rows; 3 exact replacements; 0 nonzero value deltas | No primary input change relative to human reference |
| Pooled-correlation rerun | Max abs mean-r delta = 0.000000 | Primary pooled-r unchanged |
| Source-risk exclusion sensitivity | Max abs mean-r delta = 0.407000; 9 edges changed | Sensitivity only |
| Converted-input augmentation sensitivity | Max abs mean-r delta = 0.116229; 9 edges changed | Sensitivity only |
| Core-6 TSSEM diagnostic | 15 studies; paths and fit identical | Subset diagnostic stability only |

Note. Draft table; update after lead analysis lock where indicated.

### Claim Boundary

The current results support a bounded augmentation claim: the workflow is useful for structured locked-output evaluation and review triage, but current locked outputs are not sufficient for unsupervised MASEM substitution. The deterministic expert-reviewed rerun supports a narrow claim that the primary LLM-assisted input made no nonzero pooled-correlation changes relative to the human-reference baseline. The bounded core-6 TSSEM diagnostic supports subset stability for PE, EE, SI, FC, BI, and UB only. Broader statements about all constructs, all rows, indirect effects, or substantive SEM conclusions require the final approved TSSEM/MASEM specification and source-supported numeric N for every SEM input row.

## Discussion [Reserved for Team Contribution]

[Reserved. Team authors should draft interpretation of augmentation value, limitations of current locked outputs, implications for human-in-the-loop extraction, and future workflow improvements after the lead approves the final claim boundary.]

## Data and Code Availability

The share-safe Paper 2 public repository is available at https://osf.io/mkrgd/overview. It contains prompts, schemas, scoring rules, manifest-registered locked model outputs, derived analysis outputs, scripts, reporting checklists, and decision records. Raw article PDFs, raw human coder workbooks, and private OneDrive-only working materials are excluded. The public package should be interpreted with the same claim boundary used in this manuscript.

## References

- Cheung, M. W.-L. (2015). Meta-analysis: A structural equation modeling approach. Wiley.
- Jak, S., & Cheung, M. W.-L. (2020). Meta-analytic structural equation modeling with moderating effects on SEM parameters. Psychological Methods, 25(4), 430-449.
- Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hrobjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S., ... Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. BMJ, 372, n71.
