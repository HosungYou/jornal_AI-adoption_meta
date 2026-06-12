# Source Rendering Full Coverage Status

Date: 2026-06-09

Status: source-rendering coverage preflight cleared for the post-freeze Step 5
target shell. This artifact documents source-packet availability; it does not
by itself authorize pooled accuracy, replacement, or SEM stability claims.

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

Source packet availability is closed for the full target shell. The subsequent
2026-06-12 source-packet-required full-corpus M1-R run and exception-aware
scoring outputs supersede the preflight as the manuscript evidence base. Report
those outputs by denominator family and exception gate; do not collapse them
into one pooled accuracy, replacement, or all-row SEM stability claim.
