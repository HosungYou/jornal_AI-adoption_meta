# Literature Review Map: Paper C

## LLM Data Extraction in Evidence Synthesis

- Gartlehner et al. evaluated LLM-based data extraction for evidence synthesis,
  establishing a direct precedent for comparing LLM outputs against human
  extraction in systematic-review workflows.
- Konet et al. compared large language models for data extraction in evidence
  synthesis and highlighted the need for validation against human-reviewed
  references.
- AI-assisted data extraction SWAR studies show that workflow-level evaluation
  can be meaningful even when accuracy gains over human-only or baseline
  processes are modest.
- "What level of automation is good enough?" provides a useful automation-tier
  framing for distinguishing routine fields from fields requiring human review.

## Workflow Validation Rather Than Model Leaderboard

Paper C builds on the distinction between model validation and workflow
validation. The relevant question is not whether one vendor wins at a fixed
moment, but whether the research procedure becomes more reliable, auditable, and
reproducible.

## Source-Grounded Structured Extraction

SciDaSynth is the closest system-level precedent because it evaluates LLM-based
structured extraction from scientific literature with user validation and
correction. Paper C differs by using a same-model harness ablation:
raw Codex versus Codex mediated by LongTable.

LangExtract is a practical open-source signal that source-grounded structured
extraction and visualization are becoming central expectations for LLM document
extraction systems.

## Harness and Agent-Interface Precedents

SWE-agent supports the premise that the interface around an LLM can change model
behavior and task performance. Paper C applies that principle to evidence coding
rather than software engineering.

Self-Refine, Reflexion, ReAct, and Chain-of-Verification provide broader
precedent that feedback, state, tool use, and verification steps can improve or
stabilize LLM outputs without changing the underlying model.

## Reproducibility and Provenance

Transparent provenance capture in data-science pipelines provides the computing
foundation for Paper C. The LongTable condition should be treated as a
provenance-preserving research procedure that records prompts, schemas, model
metadata, source spans, validation results, correction history, and rerun
manifests.

## Reporting and Research Integrity

PRISMA-trAIce and RAISE provide reporting and responsible-use context for AI in
evidence synthesis. Paper C should use these not as checklists alone, but as
support for the broader claim that AI-assisted review workflows require
transparent reporting, human oversight, and reproducible artifacts.

## Working Reference Set

- Gartlehner et al. Data extraction for evidence synthesis using a large
  language model: a proof-of-concept study. Research Synthesis Methods.
- Konet et al. Performance of two large language models for data extraction in
  evidence synthesis. Research Synthesis Methods.
- Bianchi et al. Data extractions using a large language model, Elicit, and
  human reviewers. Cochrane Evidence Synthesis and Methods.
- SciDaSynth: LLM-based structured data extraction from scientific literature.
- SWE-agent: Agent-computer interfaces enable software engineering language
  models.
- Rupprecht et al. Improving reproducibility of data science pipelines through
  transparent provenance capture.
- PRISMA-trAIce: transparent reporting of AI in systematic reviews.
- RAISE: responsible AI in evidence synthesis.
