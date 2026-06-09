# Source Rendering Preflight Status

Date: 2026-06-09

Status: source-rendering coverage preflight prepared. Archive filename coverage
exists for the 194 post-freeze target studies, but local text rendering is
currently blocked for most files. This artifact does not authorize a full-corpus
model run.

## Rendered Private Packets

- Studies in coverage manifest: 194
- Study-ID PDF filename coverage in searched archive roots: 194
- Studies with private rendered packets: 3
- Studies without rendered packets: 191
- Target rows covered by rendered packets: 18
- Target rows not yet source-rendered: 2025
- Source-rendered smoke task rows selected: 10

## Rendering Status Counts

- `packet_rendered_private`: 3
- `render_failed_no_extractable_text`: 191

Dominant failure mode: `Operation timed out` while reading OneDrive PDF files.
Treat this as a local materialization/readability blocker, not as evidence that
the source PDFs are absent from the archive.

## Smoke Task Family Counts

- `secondary_beta_or_path_converted_effect_size`: 10

## Safety Boundary

- PDF files and rendered source text remain local/private and are not committed.
- Share-safe artifacts record study IDs, task IDs, counts, packet hashes, and status only.
- Human reference values, adjudication rationales, and human-adjudicated source locators are not inserted into source packets.
- The source-rendered smoke should suppress `model_source_quote` so locked CSV output does not commit source-document text.

## Next Gate

Run a source-rendered smoke only if the selected task IDs all have private rendered source packets. Full-corpus `M1-R` remains blocked until source PDFs are locally materialized or share-safe source renderings are available for the full 2,043-row target shell.
