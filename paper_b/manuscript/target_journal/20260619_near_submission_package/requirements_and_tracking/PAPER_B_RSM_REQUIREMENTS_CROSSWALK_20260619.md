# Research Synthesis Methods Crosswalk for Paper B

Date: 2026-06-19

## Current RSM-facing Fit

Paper B directly fits the Research Synthesis Methods GenAI evaluation guidance because it reports research design, source data conditions, prompts/locked outputs, validation, quality assurance, reproducibility, and claim limitations.

## Crosswalk

| RSM/GenAI expectation | Paper B current evidence | Remaining action |
| --- | --- | --- |
| Research design and dataset characteristics | 213-study source-anchored reference; denominator-family task units; full-corpus Step 5 M1-R run | Keep counts and subset definitions in Methods and Results |
| Variables/task families | Direct/source-reported r, source-flagged latent r, converted beta/path rows, metadata/trace families | Do not collapse families into one pooled score |
| Prompt/model documentation | Locked output shards and model provenance are preserved | Add model access date/API/workflow parameter note before final submission |
| Validation | Source-anchored human reference standard and exception-aware scoring | Keep human adjudication and source-risk gate visible |
| Evaluation metrics | Scored-only and all-scorable accuracy, abstentions, exception gates, triage precision/recall | Report conservative interpretation first |
| Reproducibility | Scripts, locked outputs, manifests, OSF/public repository boundary | Refresh public manifest/checksums if 2026-06-12 full-corpus files are redistributed |
| Transparency and disclosure | Claim-boundary notes and no-replacement framing | Add final AI-use disclosure and conflicts/funding text |
