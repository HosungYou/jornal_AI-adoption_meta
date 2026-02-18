# Screening Protocol (Operational)

## Canonical Source
- This operational protocol is derived from:
  `docs/03_data_extraction/AI_Adoption_MASEM_Coding_Manual_v1.docx`
- If conflicts occur across files, the `docx` coding manual is authoritative.

## Scope
- Review type: Systematic review for educational AI adoption MASEM.
- Screening phases:
  1. Title/Abstract screening
  2. Full-text eligibility screening
- Current corpus scale: high-volume batch workflow (e.g., 16,189 records).

## Governance and Roles
- AI coders: Codex CLI and Gemini CLI (OAuth-authenticated sessions).
- Human coders: two independent human coders for 100% of records.
- Human coders can view AI suggestions during coding (non-blinded mode).
- Adjudicator: PI makes final decision for unresolved conflicts.
- Final exclusion decisions are human-adjudicated only.

## Workflow Summary
1. Deduplicate merged search results.
2. Run AI pre-screening with Codex and Gemini independently.
3. Route AI outputs into consensus buckets:
   - `include`
   - `exclude` (candidate only, never final by AI)
   - `conflict`
4. Human coder 1 and coder 2 independently code all records.
5. Resolve disagreements via PI adjudication.
6. Apply exclusion codes (E1-E12) and rationale.
7. Export PRISMA counts and audit logs.

## Title/Abstract Screening Rules
For each record, determine:
1. Quantitative empirical study
2. AI is focal technology
3. Educational context/population
4. Adoption/acceptance/intention/use outcome
5. Correlation or standardized beta/path data likely available
6. English-language report

Decision logic:
- Liberal inclusion at title/abstract stage: uncertainty advances to full-text.
- AI recommendations are advisory; humans issue final decision.

## Full-Text Screening Rules
- Apply inclusion/exclusion criteria from:
  `docs/02_study_selection/inclusion_exclusion_criteria.md`
- Assign canonical exclusion codes (E1-E12) for all final exclusions.
- Record free-text decision rationale for every exclusion.

## Inter-Rater Reliability (IRR)
- Title/Abstract threshold: Cohen's kappa >= 0.80
- Full-text threshold: Cohen's kappa >= 0.85
- If threshold not met:
  1. Recalibrate coder interpretation with examples
  2. Re-screen calibration subset
  3. Recompute IRR before continuing

## Conflict Resolution
1. Human coder conflict identified.
2. Evidence reviewed (title/abstract/full-text excerpts and coding notes).
3. PI adjudicates final decision.
4. Log the adjudicator ID and final rationale.

## Required Data Fields
Screening output must include:
- `record_id`
- `screen_decision_codex`
- `screen_decision_gemini`
- `screen_consensus`
- `human1_decision`
- `human2_decision`
- `adjudicated_final_decision`
- `exclude_code`
- `decision_rationale`
- `adjudicator_id`
- `screen_run_id`
- `oauth_auth_method_codex`
- `oauth_auth_method_gemini`

## Audit and Reproducibility
- Preserve raw AI outputs and parsed decisions.
- Preserve human coding timestamps and coder IDs.
- Generate PRISMA input files from final adjudicated decisions.
- Keep all intermediate files for reproducibility and reviewer audit.
