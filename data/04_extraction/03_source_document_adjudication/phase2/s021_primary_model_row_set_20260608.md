# S021 Primary Model 1 Source Row Set

Date: 2026-06-08

Boundary: This is a Step 3 source-document adjudication artifact only. It
transcribes a limited main-PDF row set for later Step 4 reference-standard
drafting; it does not freeze the human reference standard and does not start
Step 5.

Researcher decision: Include S021 using the main PDF primary Model 1, with T1
and T2 retained as separate strata.

Source: `data/04_extraction/03_source_document_adjudication/source_pdfs/S021.pdf`,
Figure 1 and Results 4.2. Online supplementary files are available in the
ignored source folder, but Supplementary Table S4 reports `f Squared` effect
sizes only and is not a coefficient source.

Conversion rule: Peterson & Brown beta-to-r approximation from the coding
manual, `r = beta + 0.05 * lambda`, where `lambda = 1` for positive beta and
`lambda = -1` for negative beta.

## Construct Mapping

| Source label | Reference construct | Mapping note |
|---|---|---|
| Performance expectancy | `PE` | Standard UTAUT2 construct. |
| Facilitating conditions | `FC` | Standard UTAUT2 construct. |
| Effort expectancy | `EE` | Standard UTAUT2 construct. |
| Social influence | `SI` | Standard UTAUT2 construct. |
| AIAS-4 | `ATT` | General AI attitude scale; retain as attitude with medium mapping confidence. |
| Behavioral intentions | `BI` | Standard intention construct. |
| Use frequency | `UB` | Use behavior/use frequency. |

`Habit` and `Hedonic motivation` are not transcribed into this target row set.
Cross-time paths are also not transcribed because the researcher decision is to
preserve T1 and T2 as separate strata rather than build a longitudinal
cross-time matrix.

## T1 Stratum

Sample size: `n = 149`.

| Study | Stratum | n | Pair | original_beta | converted_r | Source |
|---|---|---:|---|---:|---:|---|
| S021 | T1 | 149 | ATT-BI | 0.508 | 0.558 | Figure 1, AIAS-4 T1 -> Behavioral intentions T1 |
| S021 | T1 | 149 | BI-UB | 0.571 | 0.621 | Figure 1/Results 4.2, Behavioral intentions T1 -> Use frequency T1 |
| S021 | T1 | 149 | EE-BI | 0.232 | 0.282 | Figure 1, Effort expectancy T1 -> Behavioral intentions T1 |
| S021 | T1 | 149 | FC-BI | -0.130 | -0.180 | Figure 1, Facilitating conditions T1 -> Behavioral intentions T1 |
| S021 | T1 | 149 | PE-BI | 0.175 | 0.225 | Figure 1, Performance expectancy T1 -> Behavioral intentions T1 |
| S021 | T1 | 149 | SI-BI | 0.025 | 0.075 | Figure 1, Social influence T1 -> Behavioral intentions T1 |

## T2 Stratum

Sample size: `n = 122`.

| Study | Stratum | n | Pair | original_beta | converted_r | Source |
|---|---|---:|---|---:|---:|---|
| S021 | T2 | 122 | ATT-BI | 0.275 | 0.325 | Figure 1, AIAS-4 T2 -> Behavioral intentions T2 |
| S021 | T2 | 122 | BI-UB | 0.566 | 0.616 | Figure 1/Results 4.2, Behavioral intentions T2 -> Use frequency T2 |
| S021 | T2 | 122 | EE-BI | -0.101 | -0.151 | Figure 1, Effort expectancy T2 -> Behavioral intentions T2 |
| S021 | T2 | 122 | FC-BI | 0.113 | 0.163 | Figure 1, Facilitating conditions T2 -> Behavioral intentions T2 |
| S021 | T2 | 122 | PE-BI | 0.285 | 0.335 | Figure 1, Performance expectancy T2 -> Behavioral intentions T2 |
| S021 | T2 | 122 | SI-BI | -0.064 | -0.114 | Figure 1, Social influence T2 -> Behavioral intentions T2 |

## Excluded From This Row Set

- `Habit -> BI`: Habit is not in the current target construct set.
- `Hedonic motivation -> BI`: Excluded from the current target set; AIAS-4 is
  used as the dedicated attitude construct in Model 1.
- `BI T1 -> BI T2` and `Use frequency T1 -> Use frequency T2`: Cross-time paths
  are not used for the separate T1/T2 strata.
- Moderator paths and interaction terms: not target construct-pair evidence.

## Step 4 Application Note

Apply the rows as two separate S021 strata. Mark `r_source = beta_converted`,
record `original_beta`, and flag the study for beta-converted sensitivity
analysis. Mark the AIAS-4-to-`ATT` mapping confidence as medium.
