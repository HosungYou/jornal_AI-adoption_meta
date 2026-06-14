# Paper A ANX-TRU Rescue and MASEM Status

Date: 2026-06-14

## Current decision state

Researcher decision already applied: `PKC` is not approved as `SE`. Therefore S004 `PKC`-derived `SE` rows remain excluded from Paper A promotion.

This packet documents the next blocker: `ANX-TRU` in the full 10-construct Paper A route.

## Source-level finding

`ANX-TRU` was not absent from the PDF/source corpus.

| Study | Source evidence | Decision |
| --- | --- | --- |
| S036 | PDF Table 4 Fornell-Larcker row `PT`, column `AI-ANX` = `-0.260`; frozen reference has `ANX-TRU = -0.26`, `n = 480` | Diagnostic primary-plausible candidate, pending researcher promotion |
| S102 | PDF Tab. 4 Fornell-Larcker row `T`, column `TS` = `0.027`; frozen reference has `ANX-TRU = 0.027`, `n = 284`; `technostress -> ANX` caveat retained | Diagnostic primary-plausible candidate with mapping caveat, pending researcher promotion |
| S066 | PDF Table 7 reports path coefficient `Perceived Trust -> Technological Anxiety`; frozen row is beta/path converted | Exclude from primary; keep sensitivity/secondary only |
| S142 | Source constructs are `ATAI`, `FCs`, `PE`, `PTAI`, `TCs`, `USEAI`; no approved target `ANX-TRU` construct pair | Exclude as target-construct mismatch |

## Diagnostic input generated

Rows added to diagnostic input only:

- S036 `ANX-TRU = -0.260`, `n = 480`
- S102 `ANX-TRU = 0.027`, `n = 284`

These rows are not final Paper A promotion rows. They are marked as `diagnostic_only_pending_researcher_promotion`.

## Coverage consequence

| State | Full10 observed pairs | Missing pairs | Full10 complete-case studies |
| --- | ---: | --- | ---: |
| Before ANX-TRU rescue | 44/45 | ANX-TRU | 0 |
| After S036/S102 diagnostic rescue | 45/45 | none | 0 |

Interpretation: the previous full10 pair-level gap is repairable, but full10 complete-case estimation remains blocked.

## Partial-matrix TSSEM execution consequence

The existing partial-matrix TSSEM execution was re-run on the diagnostic input.

| Route | Observed pairs | Min pair k | Complete cases | Stage 1 | Stage 2 | Pairwise pooled min eigen |
| --- | ---: | ---: | ---: | --- | --- | ---: |
| core7 ATT mediation | 21/21 | 11 | 4 | failed | not run | 0.314159 |
| trust6 mechanism | 15/15 | 9 | 7 | failed | not run | 0.315163 |
| full10 theory target | 45/45 | 1 | 0 | failed | not run | -0.010232 |

The non-positive-definite implied covariance error is therefore not solved by filling `ANX-TRU`. It is a sparse partial-matrix estimation problem.

## Highest-density full10 studies after rescue

| Study | Observed pairs | Missing pairs | Key implication |
| --- | ---: | ---: | --- |
| S048 | 28 | 17 | Dense for core constructs, but lacks ANX and SE block pairs |
| S176 | 28 | 17 | Dense for core constructs, but lacks ANX and SE block pairs |
| S004 | 21 | 24 | Dense enough for trust6, but `PKC->SE` remains rejected |
| S016 | 21 | 24 | Missing many SI/TRU/UB and ANX block pairs |
| S025 | 21 | 24 | Missing ANX/ATT and TRU block pairs |

## Method conclusion

The current evidence supports this status:

1. `ANX-TRU` should be offered to the researcher as a source-confirmed diagnostic rescue for S036 and S102 only.
2. Even if those two rows are promoted, full10 primary MASEM is not yet submission-ready because full10 has zero complete-case matrices and sparse partial-matrix TSSEM still fails.
3. The viable empirically estimated routes remain reduced diagnostic/sensitivity routes, especially the complete-case trust6 and core7 models already run after S004/S048 correction.
4. To make full10 primary defensible, the next work must either densify same-study matrices substantially or specify a defensible missing-data TSSEM/MASEM strategy; simply filling one missing pair is insufficient.

## Generated artifacts

- `paper_a_anx_tru_rescue_candidates_20260614.csv`
- `paper_a_source_corrected_plus_anx_tru_diagnostic_input_20260614.csv`
- `paper_a_source_corrected_plus_anx_tru_coverage_20260614.csv`
- `paper_a_source_corrected_plus_anx_tru_top_study_missing_pairs_20260614.csv`
- `PAPER_A_ANX_TRU_RESCUE_AFTER_SOURCE_CORRECTION_20260614.md`
- `paper_a_source_corrected_plus_anx_tru_masem_execution_summary_20260614.csv`

## Next work recommendation

Next step should not be another broad PDF search. It should be a bounded densification audit focused on whether any high-density studies can become complete or near-complete full10 matrices without violating construct/source rules.

Priority order:

1. Build a high-density study densification queue from `paper_a_source_corrected_plus_anx_tru_top_study_missing_pairs_20260614.csv`.
2. Start with `S048` and `S176`, because each already has 28/45 pairs.
3. For each missing pair, classify as source-visible add, construct absent, source-type mismatch, or researcher mapping decision required.
4. Re-run coverage after each accepted batch; do not rerun full partial TSSEM until either complete-case count improves or sparse-matrix handling strategy changes.
