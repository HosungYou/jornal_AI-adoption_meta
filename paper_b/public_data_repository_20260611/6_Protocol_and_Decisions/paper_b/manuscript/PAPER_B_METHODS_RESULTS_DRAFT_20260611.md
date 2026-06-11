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
review. Downstream MASEM substitution is treated as a core manuscript result.
The current N-reconciled legacy rerun input has numeric sample sizes for 741/804
rows. Under the approved missing-N rule, the remaining 63 rows are excluded
from N-weighted SEM weighting unless later source checks supply numeric N. A
bounded R/metaSEM TSSEM diagnostic is reported for the six-construct
complete-case subset (PE, EE, SI, FC, BI, UB), while final all-construct/all-row
SEM stability claims remain gated on the approved full model specification and
source-supported numeric N for every SEM input row.

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

## Table and Figure Targets

Table 1 should describe the five data states and artifact boundaries. Table 2
should report RQ1 extraction validity by task family and stratum. Table 3 should
report RQ2 error classes by source condition. Table 4 should report RQ3 review
priority and triage signal counts. Table 5 should report the deterministic
substitution-input, pooled-correlation sensitivity rerun, and bounded core-6
TSSEM diagnostic, while clearly marking all-construct/all-row SEM claims as
outside the current diagnostic scope.

Figure 1 should show the workflow from raw human coding through reference freeze,
locked LLM outputs, task-family scoring, triage, and downstream substitution.
Figure 2 should visualize the error-consequence gradient across task families.
Figure 3 should visualize downstream substitution stability after rerun.

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
