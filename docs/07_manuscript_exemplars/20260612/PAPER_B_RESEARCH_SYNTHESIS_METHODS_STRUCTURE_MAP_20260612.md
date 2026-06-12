# Paper B Target-Journal Structure Map

Target journal: Research Synthesis Methods

Decision state: Paper B is a source-anchored, human-adjudicated LLM augmentation/validation study with downstream MASEM/TSSEM diagnostic checks. It is not an LLM replacement paper and not a vendor-ranking benchmark.

## Current Full-Corpus Gate

| Check | Current value | Implication |
| --- | --- | --- |
| Full-corpus Step 5 shell exists | True | Anchors the completed 2,043-row M1-R run |
| Task rows in shell | 2043 | Full-corpus denominator before exception handling |
| Full-corpus M1-R execution | Completed 2026-06-12 | Nine source-packet-required shards locked and scored |
| Locked/scored rows | 2,043 | 0 duplicates, 0 model CLI failures, 15 exception-layer rows |
| SEM reporting lane | Core-6 diagnostic only | No all-construct/all-row SEM claim until final specification |
| Post-freeze reference | 213 studies frozen on 2026-06-09 | Governing reference layer |
| OSF archive | https://osf.io/mkrgd/overview | Share-safe public repository exists |

Denominator-family shell counts:

| Family | Rows |
| --- | --- |
| primary_latent_or_construct_correlation_with_source_type_flag | 931 |
| primary_direct_r_or_source_reported_correlation | 697 |
| secondary_beta_or_path_converted_effect_size | 415 |

## RSM Submission Components

- Abstract: no more than 250 words and readable to a multidisciplinary audience.
- Keywords: 4 to 6, plus RSM-specific keywords at submission.
- Required highlights in manuscript: What is already known; What is new; Potential impact for Research Synthesis Methods readers.
- Data availability statement with repository DOI/URL or explanation.
- AI-methods transparency: model names/versions, dates, access path, prompts, validation, and output-locking process.

## Proposed RSM Highlights

### What is already known

Systematic review data extraction is labor-intensive, and LLMs can sometimes support extraction workflows. Existing studies show promising but task-dependent accuracy and require human verification.

### What is new

This study validates a locked LLM workflow against a source-anchored adjudicated human reference standard for MASEM-ready extraction. It reports task-family denominators, source conditions, human-disagreement traces, and downstream substitution diagnostics rather than one pooled accuracy score.

### Potential impact for Research Synthesis Methods readers

The design shows how to evaluate LLM extraction as auditable workflow augmentation for complex evidence synthesis, especially when downstream meta-analytic models depend on numeric source accuracy and sample-size eligibility.

## Table Spine

| Table | Title | Status |
| --- | --- | --- |
| Table 1 | Data states and claim roles | Ready |
| Table 2 | Reference construction and source-adjudication workflow | Ready |
| Table 3 | Task-family denominators and scoring rules | Ready |
| Table 4 | Locked model outputs and coverage | Ready for legacy plus completed full-corpus M1-R |
| Table 5 | RQ1 extraction validity by denominator family | Ready with full-corpus M1-R evidence and exception caveat |
| Table 6 | RQ2 error taxonomy by source condition | Ready with legacy package |
| Table 7 | RQ3 review-priority triage | Ready with legacy package |
| Table 8 | Post-freeze full-corpus M1-R outcomes | Ready as denominator-family result, not pooled accuracy |
| Table 9 | Downstream substitution and TSSEM diagnostics | Ready as core-6 diagnostic only |

## Figure Spine

| Figure | Purpose | Status |
| --- | --- | --- |
| Figure 1 | Five-step source-anchored validation workflow | Ready |
| Figure 2 | Task-family scoring architecture | Ready |
| Figure 3 | Locked-output and model-provenance flow | Ready |
| Figure 4 | Accuracy/abstention profile by denominator family | Ready with caveats |
| Figure 5 | Source-risk and human-disagreement triage heatmap | Ready |
| Figure 6 | Downstream substitution diagnostic | Ready as bounded subset only |

## Manuscript Boundary

Permitted: Paper B can claim a reproducible, source-anchored workflow for evaluating LLM-assisted extraction by task family, report the completed full-corpus `M1-R` outcomes by denominator family and exception-aware gate status, and report bounded diagnostic evidence that the expert-reviewed primary LLM-assisted input did not change the current primary pooled-correlation subset.

Not permitted: one pooled full-corpus accuracy denominator, all-construct/all-row SEM substitution stability, autonomous LLM replacement, silent pooling of direct-r/source-flagged/converted rows, or vendor ranking.
