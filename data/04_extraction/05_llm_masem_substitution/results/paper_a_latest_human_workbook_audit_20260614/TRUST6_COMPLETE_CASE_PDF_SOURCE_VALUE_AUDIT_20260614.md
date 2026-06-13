# Trust6 Complete-Case PDF/Source Value Audit

Date: 2026-06-14

Scope: automated source presence check for the 8 latest-human-workbook trust6 complete-case studies. This checks local PDF/source-packet availability and simple numeric value presence in extracted text; it is not a final manual table-level adjudication.

| Study | Unique trust6 pairs | Source packet | PDF | Rows with value in source packet text | Rows with value in PDF text |
| --- | ---: | --- | --- | ---: | ---: |
| S004 | 15 | True | True | 28/28 | 28/28 |
| S035 | 15 | True | True | 15/15 | 15/15 |
| S086 | 15 | True | True | 14/15 | 14/15 |
| S088 | 15 | True | True | 16/30 | 30/30 |
| S138 | 15 | True | True | 30/30 | 30/30 |
| S173 | 15 | True | True | 26/26 | 26/26 |
| S176 | 15 | True | True | 45/45 | 45/45 |
| S223 | 15 | True | True | 15/15 | 15/15 |

Interpretation: failures to find a value in raw `pdftotext` output are not definitive evidence that the coding is wrong, because tables may be split or rendered poorly. Positive hits support that the coded value is visible in local source text. Full source adjudication still requires human/PDF table inspection for flagged rows.
