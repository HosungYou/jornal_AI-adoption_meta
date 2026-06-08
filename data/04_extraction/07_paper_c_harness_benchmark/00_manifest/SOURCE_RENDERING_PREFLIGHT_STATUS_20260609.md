# Source Rendering Preflight Status

Date: 2026-06-09

Status: partial source-rendering preflight completed. Local source PDFs are
currently available only for a small subset of the post-freeze target rows, so
this artifact does not authorize a full-corpus model run.

## Rendered Private Packets

- Studies with private rendered packets: 3
- Target rows covered by rendered packets: 18
- Source-rendered smoke task rows selected: 6
- Source-rendered smoke rows run: 6
- Source-rendered smoke `model_cli_error` rows: 0
- Source quote policy violations: 0
- Committed source quotes: 0

## Smoke Task Family Counts

- `secondary_beta_or_path_converted_effect_size`: 6

## Safety Boundary

- PDF files and rendered source text remain local/private and are not committed.
- Share-safe artifacts record study IDs, task IDs, counts, packet hashes, and status only.
- Human reference values, adjudication rationales, and human-adjudicated source locators are not inserted into source packets.
- The source-rendered smoke should suppress `model_source_quote` so locked CSV output does not commit source-document text.

## Next Gate

The source-rendered smoke validates the private source-packet prompt/export
path only. Full-corpus `M1-R` remains blocked until source PDFs or share-safe
source renderings are available for the full 2,043-row target shell, or until
the researcher explicitly authorizes a smaller PDF-available subset analysis.
