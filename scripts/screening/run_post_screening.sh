#!/bin/bash
# Post-screening pipeline: runs after ai_screening_tiered.py completes
# Usage: bash scripts/screening/run_post_screening.sh

set -euo pipefail
PROJ="/Users/hosung/jornal_AI-adoption_meta"
CSV="$PROJ/data/03_screening/screening_ai_dual.csv"

echo "=== Post-Screening Pipeline ==="
echo "$(date): Starting"

# Step 1: Upgrade T1 exclude codes
echo ""
echo "--- Step 1: T1 Exclude Code Post-processing ---"
python3 "$PROJ/scripts/screening/postprocess_t1_codes.py" "$CSV"

# Step 2: Retry Gemini failures (T2→Codex, T3→Gemini Flash)
echo ""
echo "--- Step 2: Retry Gemini Failures ---"
python3 "$PROJ/scripts/screening/retry_gemini_failures.py" "$CSV" --workers 8 --timeout 300

# Step 3: Generate PRISMA counts
echo ""
echo "--- Step 3: PRISMA Statistics ---"
python3 -c "
import pandas as pd
df = pd.read_csv('$CSV')
total = len(df)
inc = len(df[df['screen_consensus']=='include'])
exc = len(df[df['screen_consensus']=='exclude'])
conf = len(df[df['screen_consensus']=='conflict'])
unc = len(df[df['screen_consensus']=='uncertain'])
gf = len(df[df['rationale_gemini'].str.contains('failed|exhausted|timed', case=False, na=False)])

print(f'PRISMA Flow Summary')
print(f'==================')
print(f'Records identified: 22,166')
print(f'After deduplication: 16,189')
print(f'')
print(f'AI Screening Results:')
print(f'  T1 auto-exclude (keyword): {len(df[df[\"screening_tier\"].str.startswith(\"T1\", na=False)])}')
print(f'  T2 single AI:              {len(df[df[\"screening_tier\"].str.startswith(\"T2\", na=False)])}')
print(f'  T3 dual AI:                {len(df[df[\"screening_tier\"].str.startswith(\"T3\", na=False)])}')
print(f'')
print(f'Consensus:')
print(f'  Include:   {inc}')
print(f'  Exclude:   {exc}')
print(f'  Conflict:  {conf} (→ human adjudication)')
print(f'  Uncertain: {unc} (→ human review)')
print(f'')
print(f'Remaining Gemini failures: {gf}')
print(f'Records for human review: {inc + conf + unc}')
"

echo ""
echo "$(date): Post-screening pipeline complete"
