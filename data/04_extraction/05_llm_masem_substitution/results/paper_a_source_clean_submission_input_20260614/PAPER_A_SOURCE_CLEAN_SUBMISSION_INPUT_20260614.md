# Paper A source-clean submission input

Date: 2026-06-14

## Input rule

This layer is the Paper A source-clean input for the model-family MASEM submission run.
It includes researcher-approved S036/S102 ANX-TRU promotions and the S048 source correction, while preserving the S004 PKC->SE rejection and excluding beta/path, HTMT, loading, and theory-only evidence from the primary input.

It does not mutate raw coder workbooks, PDFs, or frozen Paper B reference files.

## Route coverage

| Route | Required pairs | Observed pairs | Missing pairs | Complete-case studies | Complete-case IDs |
| --- | ---: | ---: | --- | ---: | --- |
| full10_theory_target | 45 | 45 | none | 0 | none |
| core7_att_mediation | 21 | 21 | none | 4 | S048;S055;S176;S214 |
| trust6_mechanism | 15 | 15 | none | 7 | S004;S048;S121;S121-1;S121-2;S173;S176 |

## Next action

Use this input for the Paper A model-family MASEM submission run: core7 and trust6 are empirical primary model-family members; full10 remains the theory target/evidence map unless later estimable under a validated missing-data strategy.
