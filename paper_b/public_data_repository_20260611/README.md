# Paper 2 Public Data Repository Archive

Date prepared: 2026-06-11

This local archive is prepared for the OSF public repository:
https://osf.io/mkrgd/overview. It contains share-safe prompts, schemas, locked model output metadata,
manifest-registered locked model output CSVs, derived analysis outputs, scripts, reporting checklists, and
decision records for the Paper 2 LLM-assisted MASEM extraction study.

The human reference should be described as the source-anchored adjudicated human
reference standard. Do not describe it as a gold standard. Raw PDFs, raw human
coder workbooks, and private OneDrive-only materials are excluded from this
archive.

Public copies of text artifacts replace local machine and OneDrive paths with
placeholders such as `<REPO_ROOT>` and `<PRIVATE_AI_ADOPTION_DOCUMENTS_ROOT>`.

## Top-Level Structure

- `1_Prompts/`: prompt modules, scoring rules, and locked-output schemas.
- `2_Raw_AI_Outputs/`: manifest-registered locked model output shards and
  provenance metadata.
- `3_Source_Rendering_Audit/`: share-safe source-rendering manifests and task
  bundles; private packet text and PDF paths are excluded.
- `4_Analysis_Outputs/`: RQ1-RQ3 outputs, expert-review layers, MASEM bridge
  outputs, and redacted PDF source-text audit summaries. Row-level PDF text
  snippets and local PDF paths are excluded.
- `4_Analysis/scripts/`: scripts needed to recreate scoring and derived outputs.
- `5_Checklists/`: reporting checklist materials.
- `6_Protocol_and_Decisions/`: methods, decision logs, and workflow records.

## Provenance Boundary

Claude output provenance is preserved exactly. Shards with `claude_code` or
`claude_full_allfamilies` names are legacy default-unspecified Claude Code
outputs and are not relabeled as Sonnet. Shards with `claude_sonnet` in the
run ID are Sonnet runs. The 2026-06-11 Sonnet backfill shards for `0000-3999`
plus the existing Sonnet continuation shards should be used for the Claude
Sonnet comparison. Legacy default Claude runs are retained only as audit
provenance.

## Manifest

`MANIFEST.csv` and `CHECKSUMS_SHA256.csv` list every copied/generated file and
checksum. Copied source file count before generated archive documentation:
308. The final manifest also includes the generated archive
documentation files.
