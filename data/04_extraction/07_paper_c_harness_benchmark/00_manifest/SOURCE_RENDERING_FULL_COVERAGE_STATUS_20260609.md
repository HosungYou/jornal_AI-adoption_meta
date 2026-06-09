# Source Rendering Full Coverage Status

Date: 2026-06-09

Status: full source-rendering coverage is clean for the post-freeze Step 5
target shell. This artifact does not by itself authorize a full-corpus model
run, but it clears the prior source materialization/readability blocker.

## Rendered Private Packets

- Studies in coverage manifest: 194
- Studies with private rendered packets: 194
- Studies without rendered packets: 0
- Target rows covered by rendered packets: 2043
- Target rows not yet source-rendered: 0
- Source-rendered smoke task rows selected: 30

## Rendering Status Counts

- `packet_rendered_private`: 194

## Smoke Task Family Counts

- `primary_direct_r_or_source_reported_correlation`: 10
- `primary_latent_or_construct_correlation_with_source_type_flag`: 10
- `secondary_beta_or_path_converted_effect_size`: 10

## Safety Boundary

- PDF files and rendered source text remain local/private and are not committed.
- Share-safe artifacts record study IDs, task IDs, counts, packet hashes, and status only.
- Human reference values, adjudication rationales, and human-adjudicated source locators are not inserted into source packets.
- The source-rendered smoke should suppress `model_source_quote` so locked CSV output does not commit source-document text.

## Next Gate

The source-rendering coverage gate is cleared, and the balanced 30-row
full-coverage source-rendered smoke has now been executed and locked as
`paper_b_full_corpus_m1_raw_source_rendered_full_coverage_smoke_20260609`.
The next defensible gate is to review the smoke's 17 abstentions and 13
nonblank answers for prompt/path behavior, then either authorize a larger staged
`M1-R` shard plan or explicitly authorize a full-corpus `M1-R`. Full-corpus
`M1-R`, `M1-P`, `M2-R`, and optional `M3-R` remain pending exact model selector,
budget, and run-condition authorization.
