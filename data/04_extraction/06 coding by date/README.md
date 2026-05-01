# Coding By Date

Use this folder for date-stamped coding work packets, returned coding files, and
share-safe transfer artifacts that need to be grouped by the day they were
created or received.

This folder is an operational staging area. It is not a replacement for the
five-step validation workflow:

1. Raw human coder data freeze
2. Pre-adjudication human-human disagreement analysis
3. Source-document adjudication
4. Source-anchored adjudicated human reference standard freeze
5. LLM comparison + MASEM substitution analysis

## Recommended Structure

Create one subfolder per working date:

```text
06 coding by date/
├── 2026-05-01/
│   ├── README.md
│   ├── manifest.csv
│   └── share-safe files only
└── YYYY-MM-DD/
```

Use the date on which the file was generated, received, or redistributed. If a
date folder mixes multiple purposes, add a short `README.md` inside that date
folder explaining what changed and where each file should move next.

## What Can Go Here

- Share-safe coder package snapshots approved for Git.
- Comparison workbooks without PDF hyperlinks or machine-specific paths.
- Date-stamped manifests, checklists, meeting notes, and transfer logs.
- Clean documentation needed to reconstruct what was shared on a given date.

## What Should Not Go Here

- Local PDFs.
- Excel lock files such as `~$*.xlsx`.
- Machine-specific local path exports.
- Private raw coder workbooks unless the team explicitly approves Git sharing.
- Raw LLM outputs before the source-anchored adjudicated human reference standard
  is frozen.

## After Intake

Move or copy finalized artifacts into the canonical workflow folder:

- Raw frozen coder returns: `../01_raw_human_coder_data_freeze/`
- Pairwise comparisons: `../02_pre_adjudication_disagreement/`
- Adjudication logs: `../03_source_document_adjudication/`
- Frozen reference files: `../04_reference_standard_freeze/`
- Post-freeze LLM and MASEM analyses: `../05_llm_masem_substitution/`

Keep this folder as a chronological audit trail of what was exchanged and when.
