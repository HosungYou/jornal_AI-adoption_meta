# Can a Prespecified LLM Workflow Augment MASEM-Ready Evidence Extraction?

Target journal: Research Synthesis Methods

Draft date: 2026-06-12

## Submission Package State

This target-journal draft updates the existing APA-style shell for Research Synthesis Methods. It keeps the claim boundary approved by the lead: Paper B is an LLM augmentation and validation study against a source-anchored adjudicated human reference standard, with bounded downstream diagnostics. It is not an autonomous replacement paper and not a vendor-ranking benchmark.

## Abstract

Data extraction for meta-analytic structural equation modeling requires more than article summarization: reviewers must recover numeric source evidence, map constructs, preserve provenance, distinguish direct correlations from converted statistics, and maintain sample-size eligibility for downstream models. We evaluate a prespecified locked-output LLM workflow against a source-anchored adjudicated human reference standard in an AI adoption evidence-synthesis project. Task units are analyzed by denominator family rather than as one pooled accuracy score. The workflow records model provenance, source conditions, abstentions, human-disagreement traces, and review-priority signals. Current post-freeze evidence includes a 213-study reference standard, clean model-explicit legacy outputs for Codex GPT-5.5, Claude Sonnet, and Gemini 3 Flash, a completed 2,043-row source-rendered full-corpus M1-R run, and a bounded six-construct TSSEM substitution diagnostic. The results support a workflow-augmentation claim: locked LLM outputs and cross-model disagreement can structure review triage, but high-consequence numeric extraction should remain under human review and exception-aware scoring. Full-corpus results are reported by denominator family and gate status; all-row SEM stability and autonomous replacement claims remain outside the current evidence.

Keywords: evidence synthesis; data extraction; large language models; MASEM; validation; human-in-the-loop

## Highlights

### What is already known

LLMs can support parts of systematic review workflows, but extraction performance is task-dependent and usually needs human verification.

### What is new

This study evaluates LLM-assisted extraction for MASEM-ready evidence using source-anchored adjudication, locked outputs, task-family scoring, and downstream substitution diagnostics.

### Potential impact for Research Synthesis Methods readers

The workflow shows how evidence-synthesis teams can evaluate LLM extraction without collapsing heterogeneous tasks into one accuracy denominator or overstating replacement claims.

## Introduction

Evidence synthesis for MASEM requires extraction decisions that are more demanding than simple article summarization. A usable evidence record must distinguish source-reported direct correlations from converted statistics, map constructs consistently, preserve source provenance, identify source-absence cases, handle human-coder disagreement, and maintain enough sample-size and matrix information to support downstream SEM weighting and model fitting.

Large language models may help with this work, but their value depends on the unit of evaluation. Treating thousands of heterogeneous task units as one accuracy denominator would obscure the difference between low-consequence metadata, high-consequence direct-r extraction, source-risk triage, and downstream substitution risk.

## Literature Review

[Reserved for team contribution. Use the Team Writing Brief in `docs/07_manuscript_exemplars/20260612/TEAM_WRITING_BRIEF_LIT_REVIEW_DISCUSSION_20260612.md`.]

## Method

### Corpus and Reference Standard

Paper B uses the validation and extraction subset derived from the AI adoption in higher education MASEM project. The workflow separates raw independent human coder workbooks, pre-adjudication human-human disagreement queues, source-document adjudication decisions, a frozen source-anchored adjudicated human reference layer, locked LLM outputs, and downstream diagnostic analysis files. The post-freeze full-corpus reference contains 213 studies and preserves caveats rather than silently rewriting raw coder workbooks.

### Task Families and Scoring Rules

Task units are not interpreted as one accuracy denominator. Direct-r extraction rows, converted or source-statistic numeric rows, metadata rows, human-review decision rows, source-absence rows, duplicate-source exclusions, blank/absence consensus rows, and trace rows are scored or interpreted separately. Abstentions on scorable rows count as incorrect and are reported as workflow behavior.

### Model Scope and Locked Outputs

Codex GPT-5.5 is the primary prespecified workflow. Claude Sonnet and Gemini 3 Flash are retained as supplementary sensitivity and triage evidence only. Earlier Claude default-unspecified rows are retained only as audit provenance after the Sonnet backfill.

### Analysis Plan

RQ1 evaluates extraction validity by denominator family and task stratum. RQ2 classifies errors by source condition and downstream consequence. RQ3 evaluates whether model behavior, cross-model disagreement, source-risk flags, and human-disagreement traces prioritize expert review. Downstream substitution analyses are reported only as bounded diagnostics.

## Results

### Data States and Claim Roles

| Data state | Current evidence | Claim role |
| --- | --- | --- |
| Frozen full-corpus reference | 213 studies frozen on 2026-06-09 | Current governing reference layer |
| Legacy task-unit package | 8,783 task units | Pre-full-corpus reproducibility and denominator-family evidence |
| Clean model-explicit outputs | 7,859 rows per model | RQ1-RQ3 task-family scoring and sensitivity |
| Bounded source-rendered M1-R shard | 90 rows | Staged diagnostic only |
| Full-corpus source-rendered M1-R | 2,043 rows | Denominator-family and exception-aware Step 5 evidence |
| Core-6 TSSEM diagnostic | 15 complete-case studies | Subset substitution-stability diagnostic |

### Post-Freeze M1-R Full-Corpus Results

The completed full-corpus M1-R run covers 2,043 source-rendered task rows across nine shards, with 0 duplicate task IDs and 0 model CLI failures. Denominator-family outcomes are reported separately: 931 primary latent/source-flagged correlation rows (715 scored, 672 correct, 216 abstentions), 697 primary direct/source-r rows (572 scored, 517 correct, 125 abstentions), and 415 secondary beta/path converted-effect rows (338 scored, 153 correct, 77 abstentions). Fifteen exception-layer rows remain gated by source-reference contract, structural-path evidence, or manual adjudication status.

### Downstream Diagnostic

The bounded core-6 TSSEM diagnostic used PE, EE, SI, FC, BI, and UB in 15 complete-case studies. The current manuscript lane is core-6 diagnostic only. It supports subset diagnostic stability and does not support all-construct or all-row substitution claims.

## Discussion

[Reserved for team contribution after the lead confirms whether the manuscript should remain on the core-6 diagnostic lane or later add a source-type-approved broader TSSEM/MASEM specification.]

## Data Availability

The share-safe Paper B public repository is available at https://osf.io/mkrgd/overview. It excludes raw PDFs, raw human coder workbooks, and private OneDrive-only working materials.
