# Full-Corpus Step 5 Prompt/Path Review

Date: 2026-06-09

Status: prompt/path review completed after the 30-row balanced source-rendered smoke. This is a gate review only. It is not a full-corpus model run, accuracy result, model comparison, procedure comparison, or MASEM substitution claim.

## Inputs Reviewed

- Locked smoke output: `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_source_rendered_full_coverage_smoke_20260609.csv`
- Smoke scoring file: `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_source_rendered_full_coverage_smoke_scored_20260609.csv`
- Row-level prompt/path review: `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_source_rendered_smoke_prompt_path_review_20260609.csv`
- Beta-family routing audit: `data/04_extraction/05_llm_masem_substitution/results/full_corpus_step5_beta_family_routing_audit_20260609.csv`
- Revised smoke task bundle: `data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/source_rendered_revised_smoke_task_ids_20260609.csv`

Private source packets were inspected only to classify prompt/path behavior. Source text and PDF paths remain uncommitted.

## Smoke Review Findings

| Finding category | Rows | Interpretation |
|---|---:|---|
| `correct_source_packet_path_worked` | 9 | The source-packet prompt path can produce locked, quote-suppressed, scoreable numeric outputs when the relevant table and task route align. |
| `nonblank_matrix_cell_selection_error` | 1 | The model found the expected table/locator but selected a neighboring or otherwise wrong matrix value for one construct pair. |
| `direct_r_abstention_probable_packet_table_coverage_gap` | 10 | The direct-r smoke rows all came from S003. The private source packet was rendered, but the packet did not expose the requested direct-correlation matrix values strongly enough for the model to answer. |
| `beta_family_abstention_under_non_path_reference_evidence` | 7 | These S007 rows were routed as beta/path tasks, but the frozen reference evidence points to source-reported direct/latent values rather than path coefficients. |
| `beta_family_nonblank_path_value_under_non_path_reference_evidence` | 3 | The model followed the beta/path route and returned path coefficients, while the frozen reference rows point to source-reported direct/latent values. |

## Full-Shell Routing Audit

The smoke result exposed a broader downstream routing issue in the Step 5 task shell. Among 415 rows currently assigned to `secondary_beta_or_path_converted_effect_size`:

| Route compatibility | Rows |
|---|---:|
| Path/beta-compatible evidence | 269 |
| Non-path source-value evidence inside beta/path family | 146 |

The 146 non-path rows are not human-value edits. They are downstream model-input routing conflicts: the frozen reference values remain unchanged, but the model should not be instructed to recover beta/path coefficients when the frozen reference row says the evidence is a source-reported direct, latent, discriminant-validity, or construct-correlation value.

The non-path rows are concentrated in caveat-bearing rows:

- `CAV005`: 136 rows
- `CAV005;CAV007;ROW_CAVEAT`: 10 rows

## Gate Decision

Full-corpus `M1-R` should remain blocked. The blocker is no longer source materialization or source-rendering coverage. The active blocker is prompt/path validity:

1. Direct-r source packet retrieval needs a revised packet selection rule that better exposes direct-correlation, Fornell-Larcker, HTMT, and correlation-matrix table content without inserting human reference values or human-adjudicated source locators into the prompt.
2. The Step 5 model-input route needs a downstream correction or overlay so beta/path-family rows with non-path frozen reference evidence are routed as source-reported direct/latent/construct-correlation extraction tasks.
3. The revised smoke should include positive controls, the S003 direct-r failure cluster, S007-style non-path secondary rows, and true path/beta-compatible rows.

## Recommended Next Gate

Prepare a revised source-rendered smoke condition before any larger shard or full-corpus run:

- Condition label: `M1-R-SOURCE-SMOKE-REVISED`
- Scope: small targeted smoke, not a result claim.
- Prepared task bundle: 40 rows, with 10 rows in each revised smoke category.
- Required coverage:
  - 10 previously correct or near-correct latent/construct positive-control rows;
  - 10 S003-style direct-r rows after revised packet selection;
  - 10 non-path secondary rows currently living in the beta/path denominator family;
  - 10 true path/beta-compatible rows.
- Success criteria:
  - no model CLI errors;
  - zero committed source quotes;
  - no beta/path answer returned for rows whose reference evidence is non-path;
  - materially fewer direct-r abstentions when the source packet contains the relevant correlation table content;
  - row-level diagnostic report generated before any larger run authorization.

Do not authorize full-corpus `M1-R`, `M1-P`, `M2-R`, or `M3-R` from the current smoke.

## Revised Smoke Follow-Up

`M1-R-SOURCE-SMOKE-REVISED` was executed after this review using a leakage-safe
route overlay and revised private packet stubs. The 40-row smoke completed with
CLI errors 0, source quote policy violations 0, committed source quotes 0,
nonblank answers 23, abstentions 17, route violations 0, and 21/40 diagnostic
correct rows. The route overlay resolved the observed non-path secondary
beta/path conflict in this smoke, but S003 direct-r rows still abstained 10/10
and true beta/path controls remained partially answerable.

Current gate decision: do not authorize full-corpus `M1-R`; revise packet/table
retrieval for direct-r and true beta/path controls, then rerun a focused
retrieval smoke before scaling.
