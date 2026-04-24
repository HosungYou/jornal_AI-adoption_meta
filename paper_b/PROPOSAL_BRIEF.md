# Paper B: Proposal Brief

## Title

**Can a Prespecified Large Language Model Workflow Augment MASEM-Ready Data Extraction?**

## Author

Hosung You, College of Education, The Pennsylvania State University

## Status

RSM-oriented summarized manuscript and validation plan | April 24, 2026

## Abstract

Meta-analytic structural equation modeling (MASEM) requires extraction decisions that are more complex than ordinary effect-size coding because researchers must harmonize constructs, recover correlation matrices, attach study-specific sample sizes, and preserve moderator information. This study evaluates whether a prespecified large language model (LLM) workflow can augment human extraction of MASEM-ready evidence from studies of artificial intelligence adoption in higher education. The design compares structured LLM outputs against an adjudicated human reference standard and evaluates performance at three levels: element-level extraction, matrix-level validity, and downstream inferential stability. The primary contribution is not a vendor comparison. Instead, the study asks whether one transparent and reproducible LLM workflow can reduce routine extraction burden while preserving the substantive conclusions of a synthesis. Optional additional models may be used only as sensitivity checks or triage signals for cases requiring human review. The proposed reporting structure includes complete prompt documentation, model and access details, preprocessing records, human oversight procedures, code availability, and open validation data where legally permissible.

**Keywords:** evidence synthesis; large language models; data extraction; meta-analytic structural equation modeling; validation; research synthesis methods

## Problem Statement

Data extraction is a major bottleneck in systematic reviews and meta-analyses. In MASEM, the burden is amplified because extraction must produce a coherent evidentiary structure rather than a simple table of study characteristics. Errors in construct harmonization or correlation extraction can propagate into pooled correlation matrices, structural path estimates, indirect effects, and moderator conclusions.

LLMs may assist with this work, but their usefulness must be tested under conditions relevant to MASEM. A workflow that summarizes articles well may still misread a Fornell-Larcker table, confuse observed and latent correlations, map conceptually distinct constructs into the same family, or miss sample-size changes across correlations. Paper B therefore evaluates workflow validity, not just text-generation capability.

## Current Positioning

The manuscript is positioned as a human-supervised augmentation study. It uses one prespecified primary LLM workflow, currently planned as Codex 5.5, and evaluates whether the workflow can assist with MASEM-ready extraction. Additional models may be retained only as supplementary robustness or triage analyses.

This positioning is deliberately narrower than a three-model comparison. Model rankings can become obsolete quickly and may depend on interface, prompt, and document-processing choices. A reproducible workflow-validation design is more durable and better aligned with research synthesis methodology.

## Research Questions

**RQ1. Extraction validity.** How accurately does the prespecified LLM workflow extract bibliographic, sample, construct, measurement, correlation, and moderator information relative to an adjudicated human reference standard?

**RQ2. Systematic error.** Which extraction families and study conditions are most associated with LLM extraction errors?

**RQ3. Downstream stability.** Do LLM-assisted inputs preserve the pooled correlations, structural path estimates, indirect effects, and substantive conclusions obtained from human-coded inputs?

**Supplementary RQ. Model sensitivity.** If additional models are evaluated, does cross-model disagreement help identify fields requiring human adjudication?

## Method Summary

| Component | Planned approach |
|---|---|
| Parent corpus | AI adoption in higher education MASEM corpus |
| Validation subset | Stratified subset representing construct, design, region, year, and reporting-format diversity |
| Human reference | Independent coding followed by adjudication and audit trail |
| Primary LLM workflow | Prespecified Codex 5.5 workflow with documented prompts, access dates, settings, and preprocessing |
| Extraction families | Bibliographic metadata, sample characteristics, construct harmonization, measurement details, correlation coefficients, matrix reconstruction, moderator coding |
| Main analyses | Agreement metrics, numeric error, matrix diagnostics, systematic error modeling, downstream substitution analysis |
| Optional analyses | Supplementary model sensitivity and triage-disagreement analysis |

## Expected Contributions

1. **MASEM-specific validation**: Evaluates LLM assistance for correlation matrix recovery and construct harmonization, not only generic data extraction.
2. **Inferential consequence testing**: Connects extraction accuracy to downstream pooled correlations and structural conclusions.
3. **Human-supervised workflow logic**: Frames LLM use as augmentation and triage rather than replacement.
4. **Reproducible GenAI reporting**: Documents prompts, model details, preprocessing, validation, QA, code, and data availability.

## Relationship to Paper A

| Dimension | Paper A | Paper B |
|---|---|---|
| Focus | Substantive MASEM of AI adoption | Methodological validation of LLM-assisted extraction |
| Corpus | Full synthesis corpus | Validation subset from the Paper A corpus |
| Primary outcome | Structural path coefficients and theory testing | Extraction validity and inference stability |
| Audience | Education technology and information systems researchers | Research synthesis and meta-analysis methodology readers |
| Target venue | Computers & Education or adjacent EdTech venue | Research Synthesis Methods |

Paper B can be submitted independently if Paper A is available as an OSF preprint or cited as a manuscript in preparation.

## Current Manuscript Files

| Artifact | Location |
|---|---|
| Summarized Word draft | `paper_b/manuscript/Paper_B_RSM_Summarized_Manuscript_v0.2.docx` |
| Markdown source | `paper_b/manuscript/Paper_B_RSM_Summarized_Manuscript_v0.2.md` |
| Simulation figure | `paper_b/manuscript/figures/figure1_substitution_stability_simulation.png` |
| Manuscript artifact notes | `paper_b/manuscript/README.md` |

## Target Journal

Research Synthesis Methods remains the first-choice venue because the paper is now framed as a methodological evaluation of GenAI-assisted evidence synthesis. JMIR AI remains a secondary option if the article is reframed toward applied AI workflow evaluation.

## Next Steps

1. Freeze the extraction schema and prompt version.
2. Complete human reference coding and adjudication.
3. Run the prespecified Codex 5.5 extraction workflow.
4. Populate extraction validity and systematic error tables.
5. Replace the simulation figure with empirical substitution analysis.
6. Archive prompts, codebook, validation data, logs, and scripts before submission.
