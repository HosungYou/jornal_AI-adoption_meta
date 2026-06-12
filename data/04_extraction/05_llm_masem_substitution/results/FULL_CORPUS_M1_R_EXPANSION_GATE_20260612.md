# Full-Corpus M1-R Expansion Completion

Date: 2026-06-12

Decision: The user approved and completed full-corpus expansion centered on the post-freeze 213-study full-corpus gate. The 2,043-row source-packet-required `M1-R` run is locked, registered, and exception-aware scored.

## Current Completion State

| Item | Value | Status |
| --- | --- | --- |
| Full-corpus shell | data/04_extraction/05_llm_masem_substitution/full_corpus_step5_task_unit_shell_20260609.csv | 2043 rows |
| Primary direct/source-r rows | 697 | Ready in shell |
| Primary latent/construct correlation rows | 931 | Ready in shell |
| Secondary beta/path converted rows | 415 | Ready in shell |
| Full-corpus M1-R locked rows | 2,043 | Completed across nine shards |
| Exception-aware scorer | scripts/llm_scoring_20260606/score_full_corpus_m1_r_with_exception_layer.py | Available |
| Exception-layer rows | 15 | Interpret by gate status, not as generic accuracy |
| SEM reporting lane | Core-6 diagnostic only | No all-construct/all-row claim without final specification |

## Required Interpretation Boundary

1. Report the full-corpus `M1-R` result by denominator family.
2. Keep source-reference contract caveats outside the generic full-accuracy numerator.
3. Treat converted beta/path rows as an explicit sensitivity stratum unless a source-type-approved model rebuild is specified.
4. Do not use this run for model-vendor ranking or autonomous replacement claims.

## Claim Boundary

Paper B may report the completed full-corpus `M1-R` denominator-family outcomes and the bounded core-6 TSSEM diagnostic. It may not report one pooled full-corpus accuracy denominator or all-row SEM substitution stability.
