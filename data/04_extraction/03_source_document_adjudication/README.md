# Step 3: Source-Document Adjudication

Use this folder for source-check decisions after raw human-human disagreement has
been identified.

Every adjudication record should include:

- Study ID
- Field or construct pair
- Raw coder values
- Source location
- Final source-anchored adjudicated value
- Rule applied
- Rationale
- Adjudicator
- Date

Use `../02_pre_adjudication_disagreement/RATER_COMPARISON_PLAYBOOK.md` to triage
which pairwise differences require adjudication and which can be marked as
rounding-only or source-type mismatches before opening PDFs.

Do not overwrite raw coder workbooks. Step 4 starts only after adjudication is
complete and the reference file is frozen.

Local source PDFs, when present, should live in `source_pdfs/`. That folder is
ignored by Git because source-document access differs by machine and license
status.
