# Project Agent Instructions

These instructions apply to the entire repository.

## LongTable Workspace Contract

This repository can also operate as a LongTable research workspace.

- Read `CURRENT.md` or `.longtable/current-session.json` before giving
  substantial project-specific research guidance when those files are present.
- Treat `.longtable/` as local runtime state, not as the primary
  researcher-facing publication artifact.
- Preserve open tensions and researcher decisions; do not collapse Paper B,
  Paper C, or Paper A into a single manuscript claim.
- For factual, current, or external claims, provide source links or file
  references when possible. Label unsupported claims as inference or estimate.

## Required Orientation For Paper B

Before changing Paper B extraction, coding, adjudication, LLM comparison, or
MASEM substitution materials, read:

1. `data/04_extraction/README.md`
2. `data/04_extraction/WORKFLOW_STATUS_LOG.md`
3. `docs/06_decisions/2026-04-25_Reference_Standard_and_Disagreement_Analysis.md`
4. `data/04_extraction/02_pre_adjudication_disagreement/RATER_COMPARISON_PLAYBOOK.md`

## Current Paper B Workflow Rule

Maintain this order:

1. Raw human coder data freeze
2. Pre-adjudication human-human disagreement analysis
3. Source-document adjudication
4. Source-anchored adjudicated human reference standard freeze
5. LLM comparison + MASEM substitution analysis

Do not run or document LLM accuracy analysis as current unless the relevant
human reference file has been frozen in `data/04_extraction/04_reference_standard_freeze/`.

## Paper C Model-Procedure Benchmark Rule

Paper C lives in `paper_c/` and
`data/04_extraction/07_paper_c_harness_benchmark/`.

The current Paper C design is:

- Primary target: JMIR Metascience and Research Integrity.
- Corpus: full 213-study Paper B validation corpus.
- Primary comparison: frozen human reference (`H`) versus model/procedure
  conditions that separate model choice from procedure or harness choice.
- Minimum procedure comparison: raw model extraction versus the same model with
  LongTable or equivalent stateful research harness.
- Minimum model comparison: at least one clearly versioned cross-model contrast
  if the final design has resources to run it consistently.
- Primary claim: model differences may be more directly interpretable for
  extraction capability, while the harness contribution should be framed as
  reproducibility, auditability, source verification, triage utility, correction
  traceability, and error visibility rather than presumed accuracy superiority.
- Main boundary: Paper C evaluates computational model/procedure behavior;
  Paper B evaluates MASEM-ready extraction validity, human disagreement, error
  taxonomy, and downstream substitution stability.

Do not start final Paper C accuracy analyses until the frozen human reference
standard exists. Pilot infrastructure and schema/prompt development are allowed
before the freeze when clearly labeled as pilot or scaffold work.

## Terminology

Use `source-anchored adjudicated human reference standard` for the current
protocol. Avoid `gold standard` except when quoting or preserving historical
decision logs.

For Paper C, describe LongTable as a stateful research harness or
provenance-preserving research procedure. Avoid product-promotion language.

## Data Safety

- Preserve raw coder workbooks; do not overwrite them during adjudication.
- Keep local PDFs, Excel lock files, private raw coder files, private LongTable
  state, raw model transcripts, and raw LLM outputs out of Git unless the team
  explicitly approves a share-safe release artifact.
- Do not add PDF hyperlinks to shareable comparison workbooks.
- If Paper B workflow status changes, update
  `data/04_extraction/WORKFLOW_STATUS_LOG.md` in the same commit.
- For Paper C, commit share-safe manifests, schemas, prompts, aggregate
  comparison tables, redacted audit summaries, and analysis scripts only.

## LongTable Runtime Contract

- Treat researcher interaction as the primary task when a user explicitly invokes LongTable.
- Read `.longtable/current-session.json` before giving substantial LongTable guidance.
- Use `.longtable/project.json` as stable project context.
- Use `.longtable/state.json` as layered working memory.
- Prefer `currentGoal`, `currentBlocker`, `nextAction`, and `openQuestions` over generic assumptions.
- Treat `AGENTS.md` as runtime guidance, not as the researcher-facing resume artifact.

## LongTable Invocation Rules

- If the user message starts with `lt `, `longtable `, `long table `, or `롱테이블 ` followed by a directive and `:`, treat it as an explicit LongTable invocation.
- Supported explicit directives are: explore, review, critique, draft, commit, panel, status, editor, reviewer, methods, theory, measurement, ethics, voice, venue.
- For explicit LongTable invocations, use the current LongTable session files first and answer as LongTable immediately.

## LongTable Research Behavior

- Begin exploratory work with clarifying or tension questions before recommending a direction.
- If you foreground role perspectives, disclose them with `LongTable consulted: ...`.
- Keep one accountable synthesis, but do not hide meaningful disagreement.
- For factual, current, or external claims, provide source links or file references when possible.
- If a statement cannot be sourced, label it as an inference or estimate instead of presenting it as a fact.
- Do not expose internal tool logs, file-search traces, or process commentary in the researcher-facing answer.
