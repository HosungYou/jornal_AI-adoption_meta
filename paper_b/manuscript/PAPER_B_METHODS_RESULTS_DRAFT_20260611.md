# Paper B Methods and Results Draft

Date: 2026-06-11

Working title: Can a Prespecified LLM Workflow Augment MASEM-Ready Evidence Extraction?

## Positioning

This manuscript is framed as a validation study for evidence synthesis and
meta-analysis methods. The focus is not whether one commercial model is better
than another. The focus is whether a prespecified, auditable LLM workflow can
support the kinds of extraction decisions that matter for meta-analytic
structural equation modeling (MASEM): construct harmonization, direct
correlation recovery, source-type separation, moderator coding, matrix
readiness, and downstream inference stability.

The empirical design is intentionally human-first. Independent human coding and
source-document adjudication define a source-anchored adjudicated human
reference standard. LLM outputs are evaluated only after the reference layer,
task-unit definitions, locked-output files, and scoring rules are fixed.

## Methods Draft

### Corpus and Data States

The parent corpus is an AI adoption in higher education MASEM project. Paper B
uses the validation and extraction subset derived from that corpus. The analysis
separates five data states: raw independent human coder workbooks,
pre-adjudication human-human disagreement queues, source-document adjudication
decisions, the frozen source-anchored human reference layer, and locked LLM
outputs scored by task family.

The canonical Paper B human consensus package is the OneDrive folder
`Paper2_Human_Final_Consensus_20260605_v2`. The Git reference-freeze and
scoring artifacts are downstream layers derived from that package. Raw coder
workbooks are preserved as raw returns and are not silently overwritten.

### Reference Standard

The frozen reference layer contains 8,783 task units. These task units are not a
single accuracy denominator. Each row carries `denominator_family` and
`scoring_eligibility` fields that define whether the row is a direct-r
extraction row, converted/source-type numeric row, metadata row, human-review
decision row, trace row, blank/absence row, duplicate-source exclusion, or other
non-final-accuracy family.

S072 ANX-EE `r = 1.0` is excluded from the primary MASEM input and retained only
as trace/influence diagnostic. `source_blank_r` rows with a human consensus
direct-r value remain in the primary direct-r extraction family but are flagged
as weaker source-evidence quality. Converted beta/path/source-statistic rows are
included in the numeric extraction evaluation as explicit source-type strata,
not pooled with source-reported direct-r rows.

### LLM Workflow and Model Scope

The primary LLM workflow is Codex GPT-5.5. Claude Sonnet and Gemini 3 Flash are
retained only as supplementary cross-model sensitivity and triage evidence. This
scope prevents the manuscript from becoming a vendor-ranking benchmark and keeps
the contribution centered on workflow validity for complex evidence synthesis.

Clean model-explicit locked-output coverage is available for Codex GPT-5.5,
Claude Sonnet, and Gemini 3 Flash across 7,859 task units with locked model
rows. The Claude Sonnet `0000-3999` backfill was completed on 2026-06-11; earlier
Claude Code/default-unspecified rows are retained only as audit provenance and
are not relabeled after locking. RQ3 left-joins those model rows back to the full
8,783 task-unit reference universe. Diagnostic, failed, unregistered-probe, or
superseded model outputs are excluded from clean scoring.

### Scoring Rules

Numeric direct-r extraction is scored with an absolute error tolerance of 0.005.
Metadata extraction is reported using both strict exact match and relaxed
normalized match. Abstentions on scorable rows are counted as incorrect and are
reported separately as workflow behavior. `absence_or_blank_consensus`,
`human_disagreement_trace`, and source-absence rows are interpreted as
triage/trace behavior rather than final evidence-content accuracy.

### Analysis Plan

RQ1 evaluates extraction validity by denominator family and task stratum. RQ2
classifies errors by source condition, source-type status, denominator family,
and downstream consequence. RQ3 evaluates whether model behavior, cross-model
disagreement, source-risk flags, and human-disagreement traces prioritize expert
review. Downstream MASEM substitution is treated as a core manuscript result. The
approved 2026-06-12 PDF-supported N override supplies numeric sample sizes for
all 804 derived substitution rerun rows without overwriting raw human workbooks
or frozen reference files. A bounded R/metaSEM TSSEM diagnostic is reported for
the six-construct complete-case subset (PE, EE, SI, FC, BI, UB), while final
all-construct/all-row SEM stability claims remain gated on the approved full
model specification and matrix/source-type reporting boundaries.

## Results Draft

### Reference and Locked-Output Coverage

The frozen Paper B reference contains 8,783 task units. Codex GPT-5.5, Claude
Sonnet, and Gemini 3 Flash each have clean model-explicit locked outputs for
7,859 eligible task units. The direct three-model overlap subset is therefore
7,859 rows and should be used only for sensitivity or triage analyses, not a
vendor-ranking result.

### RQ1: Extraction Validity

For the primary Codex GPT-5.5 workflow, source-reported direct-r extraction
contained 323 scored rows. Codex matched 3 rows within the 0.005 numeric
tolerance and abstained on 320 rows. The 43 `source_blank_direct_r` rows were
kept in the direct-r extraction family but all received abstentions. Converted
numeric rows were evaluated as explicit source-type strata: 30 beta rows, 53
beta/path-converted human-consensus rows, and 5 numeric source-statistic rows,
all of which were abstained under the current locked prompt/input condition.

Metadata performance varied by field. Codex achieved exact/relaxed match for
all scored source-type rows and statistic-count rows, and 16 of 19 study-design
rows. Other metadata families had high abstention rates under the current
locked-output shell. For example, AI type, user role, country, and first-author
metadata rows were often left blank or abstained. These results should be read
as task-family workflow behavior under the locked source-input condition, not
as a general model capability estimate.

### RQ2: Error Taxonomy and Source Conditions

The dominant RQ2 pattern was abstention on scorable rows. In the primary Codex
workflow, source-reported direct-r rows produced 320 abstentions and 3
within-tolerance matches. Source-blank direct-r rows produced 43 abstentions.
Converted/source-type numeric strata produced 88 abstentions. These patterns
indicate that high-consequence MASEM numeric rows cannot be substituted
automatically from the current locked outputs.

Blank/absence consensus rows and human-disagreement trace rows behaved
differently from final accuracy rows. They are useful for review and triage
because they reveal whether the workflow tends to over-answer blank consensus
cases, abstain when source evidence is weak, or respond inconsistently across
models. They should not be collapsed with direct-r or metadata accuracy.

### RQ3: Human-Review Triage Value

The task-unit triage analysis started from the full 8,783 task-unit reference
universe. It classified 1,196 rows as P0 expert-review numeric/MASEM tasks, 649
rows as P1 source or human-disagreement review tasks, 483 rows as P1 general
review-signal tasks, 6,412 rows as P2 blank-behavior audit rows, 1 row as a P2
scoring-completeness check, and 42 rows as low priority after the primary
workflow check.

Cross-model behavior disagreement appeared in 6,592 task units and should be
used as a review-prioritization signal rather than a model-ranking outcome.
Human-disagreement traces appeared in 467 task units, source/trace risk appeared
in 1,525 task units, and 924 task units were reference-only rows without locked
model output. These signals support the manuscript's central claim that LLM
workflows may be useful for targeted review triage even when they are not safe
for unsupervised MASEM substitution.

### Downstream MASEM Substitution Readiness

The human-reference MASEM baseline is the Paper1 tiered primary model-ready file
with 804 rows. The pre-tiered primary file contains 822 rows and is retained for
audit, not as the final baseline. Expanded and converted inputs contain 1,303
and 481 rows respectively and should be treated as sensitivity layers.

Primary Codex locked outputs do not support autonomous downstream substitution.
The P0/P1 expert-review layer covered 1,845 task units, including 1,196 P0
numeric/MASEM rows and 649 P1 source or human-disagreement rows. The
expert-reviewed LLM-assisted primary input contains 804 rows. It applies 3 exact
numeric replacements, all of which match the frozen human-reference values, so
the primary substitution-input rerun produces 0 nonzero value deltas relative to
the human-reference baseline.

At the pooled-correlation level, the primary expert-reviewed LLM-assisted input
has a maximum absolute mean-r delta of 0.000000 and no structural edges with
nonzero change. Source-risk exclusion and converted-input augmentation are
therefore treated as sensitivity diagnostics rather than primary replacements;
their maximum absolute mean-r deltas are 0.407000 and 0.116229 respectively,
with nonzero changes on 9 structural edges in each sensitivity layer.

The bounded R/metaSEM TSSEM diagnostic used the N-weighted eligible rows and the
six-construct complete-case subset PE, EE, SI, FC, BI, and UB. Fifteen studies
reported all 15 pairwise correlations for this subset, yielding 225 aggregated
pair rows. Stage 1 random-effects TSSEM and Stage 2 path models converged for
both the human-reference baseline and the expert-reviewed LLM-assisted input.
The maximum absolute pooled-correlation delta was 0.00000000, and the structural
paths were identical across scenarios: PE to BI = 0.376578, EE to BI = 0.271255,
SI to BI = 0.242604, FC to UB = 0.222908, and BI to UB = 0.566349. Model fit was
also identical: chi-square = 3.554181, df = 4, p = 0.469688, CFI = 1.000000,
RMSEA = 0.000000, and SRMR = 0.025199. These results support a narrow diagnostic
stability claim for this core complete-case subset, not a final all-construct or
all-row SEM stability claim.

A post-freeze 2,043-row `M1-R` full-corpus expansion also reported denominator-family
boundaries. In this layer, `primary_latent_or_construct_correlation_with_source_type_flag`
had 931 rows (715 scored, 672 correct), `primary_direct_r_or_source_reported_correlation`
had 697 rows (572 scored, 517 correct), and `secondary_beta_or_path_converted_effect_size`
had 415 rows (338 scored, 153 correct). Converted-effect rows remain a sensitivity
stratum because this layer is contract-aware and source-reference caveats are still
tracked as exception-bounded exclusions.

## Table and Figure Targets

Table 1 should describe the five data states and artifact boundaries. Table 2
should report RQ1 extraction validity by task family and stratum. Table 3 should
report RQ2 error classes by source condition. Table 4 should report RQ3 review
priority and triage signal counts. Table 5 should report the deterministic
substitution-input, pooled-correlation sensitivity rerun, and bounded core-6
TSSEM diagnostic, and the 2,043-row full-corpus Stage-5 `M1-R` outcomes by
denominator family. Pre-existing 10-construct and all-row SEM claims should remain
explicitly gated as a separate TSSEM section until missing-N and structural-path
evidence decisions are finalized.

Figure 1 should show the workflow from raw human coding through reference freeze,
locked LLM outputs, task-family scoring, triage, and downstream substitution.
Figure 2 should visualize the error-consequence gradient across task families.
Figure 3 should visualize downstream substitution stability after rerun.

### Table 2. RQ1 Extraction Validity by Denominator Family

| Evidence layer | Denominator family or stratum | Rows total | Scored rows | Correct rows | Abstention rows | Manuscript boundary |
|---|---|---:|---:|---:|---:|---|
| Post-freeze full-corpus `M1-R` | `primary_latent_or_construct_correlation_with_source_type_flag` | 931 | 715 | 672 | 216 | Source-flagged primary correlation evidence; report separately from direct-r and converted-effect rows. |
| Post-freeze full-corpus `M1-R` | `primary_direct_r_or_source_reported_correlation` | 697 | 572 | 517 | 125 | Primary source-reported/direct-r evidence; report as a separate denominator family. |
| Post-freeze full-corpus `M1-R` | `secondary_beta_or_path_converted_effect_size` | 415 | 338 | 153 | 77 | Converted-effect sensitivity stratum; do not collapse into primary direct-r accuracy. |
| Exception-aware full-corpus gate | Source-reference contract caveat | 8 | 0 | 0 | 0 | Exclude from generic full-accuracy numerator until the contract layer is explicitly consumed. |
| Exception-aware full-corpus gate | No explicit structural-path evidence | 4 | 0 | 0 | 0 | Exclude pending structural-path evidence or reference correction. |
| Exception-aware full-corpus gate | Manual source/reference adjudication required | 1 | 0 | 0 | 0 | Hold out of automated accuracy interpretation. |
| Exception-aware full-corpus gate | Contract-aware converted-effect allowed | 2 | 0 | 0 | 0 | Policy-allowed rows; do not count as scored/correct in the generic full-corpus exception summary unless the contract-aware layer is explicitly consumed with locked answers. |

Note. Correct rows are counted only within the denominator family or exception
gate listed in the row. This table should not be collapsed into a single
full-corpus accuracy denominator.

### Table 5. Substitution and SEM Readiness

| Analysis layer | Scope | Main result | Manuscript boundary |
|---|---|---|---|
| Expert-reviewed LLM-assisted primary input | 804 MASEM input rows | 3 exact numeric replacements; 0 nonzero primary value deltas relative to the human-reference baseline | Supports deterministic assisted-input stability only, not autonomous replacement. |
| Pooled-correlation rerun | Primary expert-reviewed input | Maximum absolute mean-r delta = 0.000000; no structural edges with nonzero change | Primary claim is bounded to the rerun input and denominator-family review layer. |
| Sensitivity reruns | Source-risk exclusion and converted-input augmentation | Maximum absolute mean-r deltas = 0.407000 and 0.116229; 9 changed structural edges in each layer | Sensitivity diagnostics only; not primary replacements. |
| Core-6 TSSEM diagnostic | PE, EE, SI, FC, BI, UB in 15 complete-case studies | 225 aggregated pair rows; pooled correlations, paths, and fit identical across baseline and assisted input | Narrow complete-case diagnostic; not an all-construct/all-row SEM claim. |
| Post-freeze full-corpus `M1-R` | 2,043 task units across nine source-packet-required shards | 0 duplicates, 0 model CLI failures, denominator-family scoring complete, 15 exception-layer rows | Stage-5 extraction/review evidence; use with exception-aware gate and no vendor-ranking or broad replacement claim. |

Note. Table 5 separates deterministic substitution-input stability, sensitivity
diagnostics, bounded TSSEM evidence, and the full-corpus Step-5 extraction layer.
It should not be used to imply all-row SEM stability or autonomous replacement.

## Data and Code Availability

The share-safe Paper 2 public repository is available at
https://osf.io/mkrgd/overview. It contains prompts, schemas, scoring rules,
manifest-registered locked model outputs, derived analysis outputs, scripts,
reporting checklists, and decision records. Raw article PDFs, raw human coder
workbooks, and private OneDrive-only working materials are excluded. The
repository should be interpreted with the same claim boundary used in this
draft: denominator-family scoring is required, legacy Claude default-unspecified
outputs remain audit provenance only, and the bounded TSSEM diagnostic is limited
to the documented source-supported N-eligible core complete-case subset. Under
the approved missing-N rule, broader SEM wording must use N-eligible subset
language. Final all-construct/all-row SEM substitution-stability claims require
the approved full model specification and source-supported numeric N for every
SEM input row.

## Claim Boundary

The current results support a bounded augmentation claim: the workflow is useful
for structured locked-output evaluation and review triage, but current locked
outputs are not sufficient for unsupervised MASEM substitution. The
expert-reviewed deterministic rerun supports a narrow claim that the primary
LLM-assisted input made no nonzero pooled-correlation changes relative to the
human-reference baseline. The bounded core-6 TSSEM diagnostic further shows
identical pooled correlations, structural paths, and fit for PE, EE, SI, FC, BI,
and UB in the 15-study complete-case subset. Any broader statement about all
constructs, all rows, indirect effects, or substantive conclusions must wait for
the approved full model specification. Any all-row wording additionally requires
source-supported numeric N for every SEM input row.

The post-freeze full-corpus Stage-5 `M1-R` expansion is complete under the
source-packet contract, with 2,043 unique task units and 0 model CLI failures.
No model-vendor ranking claim is supported by the current evidence; model-specific
results remain bounded to contract-aware workflow interpretation and review triage
diagnostics.

## Post-Freeze Step 5 Boundary Update (2026-06-12)

The full post-freeze `M1-R` expansion was completed with the source-rendered,
denominator-family-aware, exception-aware workflow. Nine shards were run and
registered under one manifest, covering exactly 2,043 eligible task units with
no duplicates and no model CLI failures.

### Post-Freeze Coverage and Scoring Facts

- Manifest: `05_llm_masem_substitution/locked_outputs/FULL_CORPUS_M1_R_FULL_RUN_MANIFEST_20260612.csv`
- Shards: `paper_b_full_corpus_m1_raw_full_0000_0249_20260612.csv` through
  `paper_b_full_corpus_m1_raw_full_2000_2042_20260612.csv`
- Run scope: 2,043 rows, task IDs `FC-S5-TASK-00001` to `FC-S5-TASK-02043`
- Coverage: 2,043 rows, 2,043 unique task IDs, 0 duplicates
- Lock quality: 0 `model_cli_error` rows after repair-aware wrapper completion
- Source quote policy: 0 rows with `model_source_quote` content

### Denominator-Family Scoring Outcomes

For this full-corpus post-freeze run (`..._full_scored_20260612.csv`):

- `primary_latent_or_construct_correlation_with_source_type_flag`
  - 931 rows total
  - 715 scored rows, 672 correct
  - 216 abstention rows
- `primary_direct_r_or_source_reported_correlation`
  - 697 rows total
  - 572 scored rows, 517 correct
  - 125 abstention rows
- `secondary_beta_or_path_converted_effect_size`
  - 415 rows total
  - 338 scored rows, 153 correct
  - 77 abstention rows

### Exception-Aware Layer Effects

The full exception layer file records 15 rows with gate status effects:

- 8 `not_scored_reference_contract_caveat`
- 4 `not_scored_no_explicit_structural_path_evidence`
- 1 `not_scored_manual_source_reference_adjudication_required`
- 2 `contract_aware_converted_effect_scoring_allowed_after_layer_consumed`
- 2,028 rows without a matching exception record (`not_scored_no_exception_layer_record`)

### Claim Boundary for Interpretation

In the manuscript, these 2,043-row full-corpus results should be labeled as
post-freeze Stage-5 bound evidence, not a broad final replacement result. Primary
accuracy statements must be reported with denominator-family separation, and
source-reference contract caveat rows should be treated as excluded from the
generic full-accuracy numerator until the approved contract layer is explicitly
consumed.
