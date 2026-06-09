# Full-Corpus M1-R Beta/Path Source Reference QA

Date: 2026-06-11

## Scope

This report records the bounded source/reference QA pass requested after the
15-row `M1-R-BETA-PATH-CONTRACT-PROBE`. The scope is limited to S009/S010
beta/path rows and the raw-beta versus Peterson-Brown converted-effect contract.

This is not a full-corpus `M1-R` run, does not authorize a larger model shard,
and does not support final accuracy, model-comparison, or MASEM substitution
claims.

No frozen human reference values were edited.

## Evidence Reviewed

- `data/04_extraction/04_reference_standard_freeze/full_corpus_reference_standard_frozen_20260609.csv`
- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_beta_path_contract_probe_scored_20260611.csv`
- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_beta_path_contract_probe_summary_20260611.csv`
- `data/04_extraction/05_llm_masem_substitution/results/FULL_CORPUS_M1_R_BETA_PATH_CONTRACT_PROBE_STATUS_20260611.md`
- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_beta_path_contract_review_20260611.csv`
- Private S009/S010 source packets were consulted locally for source-type and
  path-direction QA only. Source text is not reproduced or committed here.

Row-level QA artifact:

- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_beta_path_source_reference_qa_20260611.csv`

## QA Summary

| Class | Rows | Interpretation |
|---|---:|---|
| S009 raw beta confirmed, reference-contract layer required | 8 | Frozen numeric values behave like raw beta values despite the `beta_converted_peterson_brown` label. These should not be scored in a converted-effect gate until a post-freeze contract layer is authorized. |
| S009 source-value mismatch review required | 1 | `FC-UB` does not match the frozen value or the simple converted-effect expectation from the recovered source-directed raw beta. Manual source/reference adjudication is required before use in an accuracy gate. |
| S010 explicit structural path plus conversion contract pass | 2 | `PE->BI` and `BI->UB` support the intended raw-beta plus Peterson-Brown converted-effect contract, but should remain held until the beta/path family gate is resolved. |
| S010 no explicit structural path in packet / IPMA-only candidate | 4 | The available matching candidates are not acceptable structural path coefficients under the current rule. These rows should be excluded from full accuracy scoring until explicit path evidence or a reference correction is available. |

All 15 row-level records set `frozen_reference_change_made=false`.

## Findings

S009 is not primarily a model-retrieval problem. For eight rows, the probe
recovered source-directed raw beta values that align with the frozen numeric
values, but the frozen source label indicates `beta_converted_peterson_brown`.
This means the scoring contract is unstable: treating the frozen value as a
converted effect would incorrectly penalize raw-beta recovery.

S009 `FC-UB` remains a narrower source/reference issue. The recovered
source-directed raw beta differs from the frozen value and from the converted
effect calculated from that raw beta under the probe contract. This row should
not be repaired silently; it needs manual source/reference adjudication or an
explicit exclusion caveat.

S010 shows that the proposed raw-beta plus converted-effect contract can work
when explicit structural path evidence is present. `PE->BI` and `BI->UB` pass
that contract. The other four S010 rows remain unsafe for scoring because the
source packet does not provide explicit structural path coefficients for those
paths under the current evidence rule, and IPMA/importance values must not be
used as substitutes.

## Gate Decision

Full-corpus `M1-R` remains blocked.

The next defensible step is to prepare a post-freeze beta/path
reference-contract exception/correction layer that leaves the frozen reference
files unchanged while making scoring eligibility explicit. That layer should:

- mark the eight S009 raw-beta-confirmed rows as excluded from the converted
  full-accuracy gate until a reference-contract layer is authorized;
- mark S009 `FC-UB` for manual source/reference adjudication before any
  accuracy-gate use;
- mark the four S010 IPMA-only/no-explicit-path rows as excluded until explicit
  path evidence or reference correction is available;
- keep the two S010 contract-pass rows eligible only for a later
  contract-aware beta/path gate after the family-level exception layer is in
  place;
- preserve the rule that IPMA, importance, total-effect, indirect-effect, HTMT,
  and discriminant-validity evidence are not structural path coefficients.

No larger staged shard should be run until this exception/correction layer is
created, logged, and explicitly referenced by the Step 5 scorer/gate.
