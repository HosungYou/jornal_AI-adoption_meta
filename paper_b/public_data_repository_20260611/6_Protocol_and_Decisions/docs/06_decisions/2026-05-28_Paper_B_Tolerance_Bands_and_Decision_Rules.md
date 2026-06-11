# Paper B Tolerance Bands and Decision Rules

Date: 2026-05-28

## Decision

Paper B accepts `paper_b/PAPER_B_TOLERANCE_AND_DECISION_RULES.md` as the
working pre-analysis rule set for:

1. element-level tolerance bands,
2. source-document adjudication priority,
3. task-family decision categories,
4. downstream MASEM substitution stability classes.

These rules are accepted as a methodology and reporting framework, not as
empirical LLM results.

## Scope

The accepted rules apply to the Paper B validation design for the 213-study
Phase 1+2 educational AI adoption MASEM extraction corpus.

They support:

- RQ0 human-human disagreement interpretation,
- RQ1 post-freeze LLM validity by task family,
- RQ2 error taxonomy and source-condition analysis,
- RQ3 expert-review triage,
- RQ4 downstream substitution stability.

## Boundary

The source-anchored adjudicated human reference standard is not frozen yet.
Therefore:

- do not report LLM accuracy as a current result;
- do not run or interpret final MASEM substitution analysis;
- do not use raw unresolved human disagreement as the LLM evaluation target;
- do not treat the accepted rules as evidence that automated substitution is
  safe.

## Operational Implication

The next manuscript and analysis documents should use the accepted rule set as
their default language for tolerance, triage, and decision categories. Any
threshold change after this point should be logged as a protocol amendment before
post-freeze LLM comparison or substitution analysis begins.

## Evidence Anchors

- `paper_b/PAPER_B_TOLERANCE_AND_DECISION_RULES.md`
- `paper_b/ANALYSIS_PLAN.md`
- `paper_b/PAPER_B_TASK_CONTINGENT_AUGMENTATION_MEMO.md`
- `data/04_extraction/README.md`
- `data/04_extraction/WORKFLOW_STATUS_LOG.md`
- `docs/06_decisions/2026-04-25_Reference_Standard_and_Disagreement_Analysis.md`
- `data/04_extraction/02_pre_adjudication_disagreement/RATER_COMPARISON_PLAYBOOK.md`
