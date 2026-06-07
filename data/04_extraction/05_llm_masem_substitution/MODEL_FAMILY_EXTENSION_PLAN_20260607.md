# Paper2 Model-Family Extension Plan

Date: 2026-06-07

## Current Decision

Use model names as the analysis unit:

- `codex:gpt-5.5`
- `claude:sonnet`
- `gemini:gemini-3-flash-preview`

Primary evidence families:

- `direct_r_effect_size_extraction`: primary numeric extraction evidence.
- `metadata_extraction`: primary metadata extraction evidence.

Do not collapse these two primary families into one accuracy denominator.
Direct-r uses numeric tolerance scoring; metadata uses normalized exact-match
scoring.

## Claude Sonnet Backfill

Goal: rerun `0000-3999` as `claude:sonnet` so Claude has full model-explicit
coverage matching the Codex GPT-5.5 full range.

Status: attempted on 2026-06-07 at about 10:00 Asia/Seoul. The first backfill
shards returned Claude session-limit 429 responses:

```text
You've hit your session limit - resets 1pm (Asia/Seoul)
```

Those failed backfill CSVs were not registered in the clean manifest and were
removed from the working tree. The clean manifest remains unchanged.

Retry only after the reset, starting with a one-row probe:

```bash
python3 scripts/llm_scoring_20260606/run_model_locked_output_batch.py \
  --provider claude \
  --model-selector sonnet \
  --run-id paper2_claude_sonnet_backfill_probe1_YYYYMMDD \
  --offset 0 \
  --limit 1 \
  --chunk-size 1 \
  --timeout 300 \
  --max-budget-usd 0.25 \
  --register \
  --fail-on-model-cli-error
```

If the probe is clean, run 250-row shards with fail-fast enabled:

```bash
for start in 0 250 500 750 1000 1250 1500 1750 2000 2250 2500 2750 3000 3250 3500 3750; do
  end=$((start + 249))
  if [ "$start" -eq 3750 ]; then end=3999; fi
  run_id=$(printf 'paper2_claude_sonnet_full_allfamilies_%04d_%04d_backfill_YYYYMMDD' "$start" "$end")
  python3 scripts/llm_scoring_20260606/run_model_locked_output_batch.py \
    --provider claude \
    --model-selector sonnet \
    --run-id "$run_id" \
    --offset "$start" \
    --limit 250 \
    --chunk-size 50 \
    --timeout 900 \
    --max-budget-usd 3.00 \
    --register \
    --fail-on-model-cli-error
done
```

After successful shards:

```bash
python3 scripts/llm_scoring_20260606/score_locked_outputs.py
python3 scripts/llm_scoring_20260606/summarize_denominator_family_results.py
```

## Additional Model-Family Candidate

Installed usable CLIs in this environment:

- `codex`: OpenAI/Codex family.
- `claude`: Anthropic Claude family.
- `gemini`: Google Gemini family.

Not installed in the checked shell path:

- `openai`
- `ollama`
- `lmstudio`
- `llm`
- `mistral`
- `anthropic`

Gemini is the only currently installed non-OpenAI, non-Anthropic family CLI.
`gemini-3-flash-preview` produced a clean model-explicit probe and clean full
shards through `0000-7249` on 2026-06-07. The next shard, `7250-7499`, failed
only in `human_disagreement_trace` rows beginning at offset `7400`.

A direct one-row probe at offset `7400` failed because the Gemini CLI repeatedly
returned:

```text
You have exhausted your capacity on this model.
```

Keep Gemini 3 Flash paused until capacity resets, then resume at offset `7400`
with a one-row probe before any larger shard:

```bash
python3 scripts/llm_scoring_20260606/run_model_locked_output_batch.py \
  --provider gemini \
  --model-selector gemini-3-flash-preview \
  --run-id paper2_gemini3flash_humandisagree_probe_7400_YYYYMMDD \
  --offset 7400 \
  --limit 1 \
  --chunk-size 1 \
  --timeout 300 \
  --register \
  --fail-on-model-cli-error
```

If clean, continue `7400-7858` in 5- or 10-row chunks. Do not register any file
that contains `model_cli_error`.

Gemini CLI also exposes local Gemma routing, but status checks show the local
Gemma binary/model/server are not installed. Gemma setup would be a separate
local-model installation and should be treated as a lower-capability robustness
check, not as equivalent frontier-model evidence.

## Full-Run Gate for Any Added Model

For any added model family:

1. Run a one-row model-explicit clean probe.
2. Register only if there is no `model_cli_error`.
3. If the probe is clean, run the full `0000-7858` range in shards.
4. Regenerate scorer outputs and denominator-family summaries.
5. Report `direct_r_effect_size_extraction` and `metadata_extraction`
   separately as primary evidence families.
