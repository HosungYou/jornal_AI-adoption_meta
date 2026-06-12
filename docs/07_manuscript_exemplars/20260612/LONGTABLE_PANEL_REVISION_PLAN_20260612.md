# LongTable Panel Revision Plan

Date: 2026-06-12

Decision recorded: revise before proceeding.

## Diagnosis

The 2026-06-12 target-journal drafts are not yet full manuscript drafts. They are boundary-aware submission shells. The problem is not Word formatting. The problem is that the promised table/figure spine is not claim-carrying.

Current Paper A evidence:

- The Paper A draft reports a readiness table, but it does not report Stage 1 pooled correlations, heterogeneity, Stage 2 path estimates, indirect effects, fit, or sensitivity estimates.
- The Paper A gate explicitly states that a defensible N-weighted TSSEM/OSMASEM run is blocked because 754 of 796 usable rows lack numeric sample size and there are 0 complete 10-construct studies.
- Therefore, any table or figure that looks like a final MASEM result would currently overstate the evidence.

Current Paper B evidence:

- The Paper B draft reports data states and claim roles, but it does not yet report full-corpus post-freeze M1-R accuracy by denominator family.
- The full-corpus shell has 2,043 rows, but the inherited workspace has only 10 private source packets where 194 study packets are expected for full coverage.
- The bounded 90-row M1-R shard and core-6 TSSEM diagnostic are useful staged diagnostics, but they cannot carry a full-corpus extraction-validity or all-row substitution-stability claim.

## LongTable Synthesis

The manuscripts need to be rebuilt around empirical load-bearing artifacts:

1. Paper A should become a target-journal meta-analytic SEM manuscript only after the sample-size reconciliation gate is cleared and actual TSSEM/OSMASEM outputs exist.
2. Paper B should become a validation manuscript organized by denominator family, source condition, human-review triage signal, and downstream diagnostic consequence.
3. Literature Review and Discussion can be delegated to teammates, but Introduction, Methods, Results, and all table/figure shells must remain lead-controlled until the analysis gates are resolved.

## Panel Opinions By Role

### Reviewer

Main objection: The current drafts tell the reader what the study intends to do, but not what the evidence shows.

Required repair:

- Replace readiness/status tables with results tables once estimates exist.
- Add one table that ties each research question to the exact analysis output, denominator, and claim boundary.
- Do not send teammates a draft that invites them to write Discussion around results that are still gated.

### Methods Critic

Main objection: The table spine does not yet map to the analytic estimands.

Required repair:

- Paper A needs an explicit matrix-construction table before any structural table.
- Paper A must distinguish primary direct-r analysis, expanded direct-r-form sensitivity, and converted beta/path/source-statistic sensitivity.
- Paper B must score by denominator family and exception layer, not by one pooled accuracy number.
- Downstream substitution must be framed as diagnostic unless the full-corpus run is complete and scored.

### Measurement Auditor

Main objection: The current shells hide the measurement risk that should be central to both papers.

Required repair:

- Paper A must show construct-pair coverage and matrix completeness in a way that explains which paths are estimable.
- Paper B must show direct-r, latent/source-flagged, beta/path-converted, HTMT/Fornell-Larcker, source-absence, and duplicate-source categories separately.
- Error taxonomy needs to distinguish numeric extraction error, wrong source type, wrong sample, construct mapping ambiguity, abstention, and source-unavailable cases.

### Ethics Reviewer

Main objection: The current wording is mostly safe, but the artifacts do not yet make the human oversight boundary visible enough.

Required repair:

- Keep "source-anchored adjudicated human reference standard"; do not use "gold standard."
- Make PSU-licensed/closed PDFs clearly local/private and exclude raw PDFs/source text from public artifacts.
- State that LLM outputs are evaluated as assistive extraction behavior, not autonomous replacement.

### Voice Keeper

Main objection: The drafts lost the researcher's real intellectual trace. The project is not just "AI extraction works or fails"; it is about where human and AI extraction break differently under MASEM constraints.

Required repair:

- Preserve the task-contingent augmentation claim.
- Make source-adjudication, disagreement, caveats, and downstream consequence the narrative spine.
- Avoid a generic "LLM accuracy paper" voice.

### Venue Strategist

Main objection: The current target fit is plausible, but each paper needs a journal-specific evidence contract.

Required repair:

- Paper A for Computers & Education needs a real education-technology theory model plus actual MASEM estimates.
- Paper B for Research Synthesis Methods needs transparent validation methodology, public reproducibility package, denominator-specific scoring, and source-governed limitations.

## Conflict Summary

The panel agrees that the current outputs should not be treated as full manuscripts.

The main unresolved conflict is timing:

- Reviewer and Venue Strategist prefer delaying manuscript drafting until actual estimates are available.
- Voice Keeper and Ethics Reviewer support drafting a methods-heavy manuscript shell now, but only if every result placeholder is explicitly gated.
- Methods Critic and Measurement Auditor require the analysis gates to drive the table/figure spine before any full Results section is written.

Recommended synthesis: revise the manuscript architecture now, but do not produce a submission-claim draft until the analysis gates are cleared.

## Revised Paper A Table Spine

Minimum main-text tables:

1. Study selection and inclusion flow summary.
2. Construct harmonization and 10-construct model map.
3. Matrix readiness by construct pair: available studies, rows, N coverage, source class.
4. Stage 1 pooled correlation matrix with uncertainty and heterogeneity.
5. Stage 2 structural path estimates, indirect effects, and model fit.
6. Sensitivity comparison: primary direct-r versus expanded direct-r-form versus converted evidence.

Minimum supplement tables:

- Study-level extracted matrix inventory.
- Moderator missingness and eligibility.
- Excluded/sensitivity rows and source-statistic conversion audit.

## Revised Paper A Figure Spine

Minimum main-text figures:

1. PRISMA flow.
2. Theory/model diagram for the 10-construct architecture.
3. Construct-pair evidence heatmap: k, N coverage, and source class.
4. Stage 2 path diagram with coefficients and confidence intervals.

Optional supplement figures:

- Influence/sensitivity plots.
- Moderator availability heatmap.

## Revised Paper B Table Spine

Minimum main-text tables:

1. Corpus, human coding waves, adjudication states, and reference-standard construction.
2. Denominator-family table: direct-r, latent/source-flagged, beta/path-converted, source-absence, duplicate-source, and status-only units.
3. RQ1 extraction validity by denominator family: accuracy/tolerance, abstention, source mismatch, and high-consequence error rate.
4. RQ2 error taxonomy by source condition and extraction family.
5. RQ3 triage yield: human disagreement, source-risk flags, cross-model disagreement, abstention, and review-priority capture.
6. RQ4 downstream diagnostic: reference versus LLM-assisted/substituted input, pooled-r deltas, path deltas, fit shifts, and claim consequence.

Minimum supplement tables:

- Field-level scoring dictionary.
- Exception-layer rows and scoring contract.
- Model/procedure provenance.
- Public OSF file map.

## Revised Paper B Figure Spine

Minimum main-text figures:

1. Workflow diagram from raw human coding to source-anchored reference, locked LLM output, scoring, and downstream diagnostic.
2. Denominator-family flow diagram for the 2,043 post-freeze target rows.
3. Error taxonomy stacked bar or alluvial plot by task family.
4. Triage yield curve showing review burden versus high-consequence error capture.
5. Downstream substitution diagnostic plot: path/r delta overlay with claim-boundary bands.

Optional supplement figures:

- Cross-model disagreement heatmap.
- Source-risk by study or source type.
- Bland-Altman or tolerance-band scatter for numeric extraction.

## Goal-Ready Execution Plan

### G001: Replace Shell Spine With Claim-Carrying Blueprint

Output:

- Revised Paper A and Paper B manuscript architecture documents.
- Table and figure specification files with required input columns, scripts, and claim served.

Stop condition:

- Every planned table/figure has a named research question, source data file, script/output path, and claim boundary.

### G002: Paper A Sample-Size Reconciliation Gate

Output:

- Study/sample N reconciliation table.
- Rebuilt primary model-ready matrix input.
- Updated run gate showing whether TSSEM/OSMASEM is defensible.

Stop condition:

- Either primary N-weighted TSSEM/OSMASEM is runnable, or the manuscript explicitly downgrades to diagnostic/no-final-estimate status.

### G003: Paper A MASEM Results Production

Output:

- Stage 1 pooled matrix and heterogeneity.
- Stage 2 path model estimates and fit.
- Sensitivity analyses and figure-ready outputs.

Stop condition:

- All Paper A main tables/figures can be populated without placeholder language.

### G004: Paper B Full-Corpus Source Packet Restoration

Output:

- Verified 194-study private source-packet coverage or a documented missing-packet exception list.

Stop condition:

- Full-corpus M1-R can run with `--require-source-packet`, or the manuscript is explicitly limited to bounded diagnostics.

### G005: Paper B Exception-Aware Full-Corpus M1-R Scoring

Output:

- Locked full-corpus M1-R outputs.
- Exception-aware scoring outputs by denominator family.
- Error taxonomy and triage-yield tables.

Stop condition:

- RQ1-RQ3 can be reported without using one pooled accuracy denominator.

### G006: Downstream Substitution Diagnostics

Output:

- Reference versus LLM-assisted diagnostic inputs.
- Pooled-r/path/fit delta outputs.
- Claim-consequence classification.

Stop condition:

- RQ4 is either populated as bounded diagnostic evidence or explicitly withheld.

### G007: Full Manuscript Rebuild

Output:

- Paper A full target-journal manuscript draft.
- Paper B full target-journal manuscript draft.
- Team writing packets for Literature Review and Discussion only.

Stop condition:

- Introduction, Methods, Results, tables, figures, and claim-boundary language are internally consistent with completed gates.

## Researcher Questions Before Execution

1. Paper A: If N cannot be recovered for most rows, should Paper A delay full manuscript drafting, or proceed as a diagnostic methods/readiness paper?
2. Paper A: Are source-supported study-level Ns available in a local workbook/PDF set, or should the reconciliation pass infer only from existing consensus fields?
3. Paper A: Should the primary model remain all 10 constructs if no complete 10-construct studies exist, or should it use a staged core-plus-extension model?
4. Paper B: Should full-corpus M1-R restoration take priority over writing, even if it delays manuscript drafting?
5. Paper B: If the 194 private source packets cannot be restored quickly, should the paper submit with bounded 90-row diagnostic evidence, or wait for full 2,043-row scoring?
6. Paper B: Should Claude/Gemini remain supplementary triage-only evidence, or should cross-model disagreement become a main RQ3 signal?
7. Both papers: Should team members receive only Literature Review and Discussion briefs now, or should they wait until Results tables are populated?

## Immediate Recommendation

Run G001 first. Do not revise prose first. Rebuild the table/figure specification as an evidence contract, then execute the analysis gates that can populate it.
