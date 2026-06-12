# Paper A TSSEM/OSMASEM Run Gate

Date: 2026-06-12

Decision: The lead approved actual TSSEM/OSMASEM/sensitivity estimation for Paper A. The current model-ready primary file is not yet sufficient for a defensible N-weighted metaSEM run because most usable rows do not carry numeric sample size.

## Readiness Snapshot

| Metric | Value |
| --- | --- |
| Primary rows | 804 |
| Usable rows after 10-construct and r checks | 796 |
| Rows missing numeric N | 754 |
| Studies represented | 74 |
| Construct-pair coverage | 44/45 |
| Complete 10-construct studies | 0 |
| Studies with 15 or more pairs | 26 |

## Stop Condition

Do not run or report a primary N-weighted TSSEM/OSMASEM estimate from this file until one of the following is true:

1. Source-supported numeric N is filled for the rows entering the SEM input; or
2. A Paper A-specific N-eligible subset rule is approved and documented; or
3. A methodological decision is made to run an explicitly labeled non-primary unweighted/pseudo-N diagnostic, with no final substantive path claims.

## Recommended Next Action

Apply a Paper A sample-size reconciliation pass analogous to the Paper B deterministic N reconciliation layer, using source-supported study/sample N from the frozen consensus/reference materials. Then rerun this gate and execute TSSEM/OSMASEM from the reconciled input.
