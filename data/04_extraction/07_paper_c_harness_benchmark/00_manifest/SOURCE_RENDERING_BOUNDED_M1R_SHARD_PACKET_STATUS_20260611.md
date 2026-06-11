# Source Rendering Preflight Status

Date: 2026-06-11

Status: source-rendering coverage prepared for the bounded 90-row M1-R diagnostic shard. This artifact does not authorize or evidence a full-corpus model run.

## Rendered Private Packets

- Studies in coverage manifest: 10
- Studies with private rendered packets: 10
- Studies without rendered packets: 0
- Target rows covered by rendered packets: 108
- Target rows not yet source-rendered: 0
- Source-rendered bounded task rows selected: 90

## Rendering Status Counts

- `packet_rendered_private`: 10

## Smoke Task Family Counts


## Safety Boundary

- PDF files and rendered source text remain local/private and are not committed.
- Share-safe artifacts record study IDs, task IDs, counts, packet hashes, and status only.
- Human reference values, adjudication rationales, and human-adjudicated source locators are not inserted into source packets.
- The source-rendered smoke should suppress `model_source_quote` so locked CSV output does not commit source-document text.

## Next Gate

The bounded 90-row M1-R diagnostic shard can be run only while these private packets are present locally. Full-corpus `M1-R` claims remain blocked until source PDFs are locally materialized or share-safe source renderings are available for the full 2,043-row target shell and the full scoring denominator is complete.
