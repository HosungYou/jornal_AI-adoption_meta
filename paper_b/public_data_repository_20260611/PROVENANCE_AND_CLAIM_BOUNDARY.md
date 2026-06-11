# Claim Boundary and Provenance Note

Repository URL: https://osf.io/mkrgd/overview

This archive supports a paper claim that a prespecified LLM workflow can be
evaluated against a source-anchored adjudicated human reference standard and can
be used for bounded substitution-stability diagnostics.

It does not support an unrestricted replacement claim. Model performance must be
reported by denominator family and source condition. Pointer-only source rows
require the PDF source-text audit boundary. Rows where the audit did not locate
the numeric value in extracted PDF text require manual table review or OCR
before they can be upgraded.

Claude provenance must remain exact: default-unspecified Claude Code outputs are
not Sonnet outputs. The 2026-06-11 Sonnet-labeled `0000-3999` backfill plus the
existing Sonnet continuation provide the Claude Sonnet comparison rows; legacy
default-unspecified Claude Code rows are audit provenance only.
