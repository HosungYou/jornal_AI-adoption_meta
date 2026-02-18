#!/usr/bin/env python3
"""
Post-process T1 records to add detailed exclude codes.
Runs after screening completes to upgrade T1 from generic E2 to specific reasons.
"""
import pandas as pd
import re
import sys

AI_TERMS = [
    r"\bartificial\s+intelligence\b", r"\bAI\b", r"\bmachine\s+learning\b",
    r"\bdeep\s+learning\b", r"\bintelligent\s+tutoring\b", r"\bchatbot\b",
    r"\bgenerative\s+AI\b", r"\bChatGPT\b", r"\bGPT[-\s]?4\b", r"\bGPT\b",
    r"\blarge\s+language\s+model\b", r"\bLLM\b", r"\bNLP\b",
    r"\bnatural\s+language\s+processing\b", r"\bautomated\s+grading\b",
    r"\badaptive\s+learning\b", r"\bconversational\s+AI\b",
    r"\bAI\s+tutor\b", r"\bAI\s+agent\b", r"\bagentic\s+AI\b",
    r"\bneural\s+network\b", r"\btransformer\b", r"\bBERT\b",
    r"\bGPT[-\s]?3\b", r"\bClaude\b", r"\bGemini\b", r"\bCopilot\b",
    r"\bLLaMA\b", r"\btext\s+generation\b", r"\bprompt\s+engineering\b",
]
EDU_TERMS = [
    r"\beducat\w*\b", r"\bstudent\b", r"\binstructor\b", r"\bteacher\b",
    r"\bpedagog\w*\b", r"\bclassroom\b", r"\buniversit\w*\b",
    r"\bhigher\s+education\b", r"\bK-12\b", r"\bacademi\w*\b",
    r"\bcurricul\w*\b", r"\blearning\b", r"\bschool\b",
]
ADOPT_TERMS = [
    r"\badoption\b", r"\bacceptance\b", r"\bintention\b", r"\bTAM\b",
    r"\bUTAUT\b", r"\btechnology\s+acceptance\b", r"\buser\s+acceptance\b",
    r"\bbehavioral\s+intention\b", r"\bperceived\s+usefulness\b",
    r"\bperceived\s+ease\s+of\s+use\b", r"\bself-efficacy\b",
    r"\btrust\b", r"\bresistance\b", r"\battitude\b",
]

AI_PAT = re.compile("|".join(AI_TERMS), re.IGNORECASE)
EDU_PAT = re.compile("|".join(EDU_TERMS), re.IGNORECASE)
ADOPT_PAT = re.compile("|".join(ADOPT_TERMS), re.IGNORECASE)


def classify_t1_reason(row):
    text = f"{row.get('title', '')} {row.get('abstract', '')} {row.get('keywords', '')}"
    has_ai = bool(AI_PAT.search(text))
    has_edu = bool(EDU_PAT.search(text))
    has_adopt = bool(ADOPT_PAT.search(text))

    if not has_ai:
        return "E2", "T1_keyword(E2)", "T1 keyword pre-filter: no AI-related terms found in title/abstract/keywords"
    elif has_ai and not has_edu and not has_adopt:
        return "E2+E3", "T1_keyword(E2+E3)", "T1 keyword pre-filter: AI terms present but no education context AND no adoption/acceptance constructs"
    else:
        return "E2", "T1_keyword", "T1 keyword pre-filter"


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "/Users/hosung/jornal_AI-adoption_meta/data/01_extracted/screening_ai_dual.csv"
    df = pd.read_csv(path)

    t1_mask = df["screening_tier"].str.startswith("T1", na=False)
    t1_count = t1_mask.sum()
    print(f"T1 records to update: {t1_count}")

    updated = 0
    for idx in df[t1_mask].index:
        code, tier, rationale = classify_t1_reason(df.loc[idx])
        df.loc[idx, "exclude_code_codex"] = code
        df.loc[idx, "exclude_code_gemini"] = code
        df.loc[idx, "screening_tier"] = tier
        df.loc[idx, "rationale_codex"] = rationale
        df.loc[idx, "rationale_gemini"] = rationale
        updated += 1

    df.to_csv(path, index=False)
    print(f"Updated {updated} T1 records with detailed exclude codes")

    # Summary
    print("\nUpdated tier distribution:")
    print(df[t1_mask]["screening_tier"].value_counts().to_string())


if __name__ == "__main__":
    main()
