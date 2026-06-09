# Source Rendering Table Retrieval Target Status

Date: 2026-06-09

Status: focused table-retrieval target packets prepared for S003/S009/S010. This artifact does not authorize a full-corpus model run.

## Rendered Private Packets

- Studies in coverage manifest: 3
- Studies with private rendered packets: 3
- Studies without rendered packets: 0
- Target rows covered by rendered packets: 25
- Target rows not yet source-rendered: 0
- Source-rendered smoke task rows selected: 25

## Rendering Status Counts

- `packet_rendered_private`: 3

## Smoke Task Family Counts

- `primary_direct_r_or_source_reported_correlation`: 10
- `secondary_beta_or_path_converted_effect_size`: 15

## Safety Boundary

- PDF files and rendered source text remain local/private and are not committed.
- Share-safe artifacts record study IDs, task IDs, counts, packet hashes, and status only.
- Human reference values, adjudication rationales, and human-adjudicated source locators are not inserted into source packets.
- The source-rendered smoke should suppress `model_source_quote` so locked CSV output does not commit source-document text.

## Next Gate

The focused table-retrieval smoke has been run separately and is recorded in
`data/04_extraction/05_llm_masem_substitution/results/FULL_CORPUS_M1_R_SOURCE_RENDERED_TABLE_RETRIEVAL_SMOKE_STATUS_20260609.md`.
Full-corpus `M1-R` remains blocked by remaining S009/S010 beta/path
disambiguation, not by source materialization or S003 direct-r coverage.
