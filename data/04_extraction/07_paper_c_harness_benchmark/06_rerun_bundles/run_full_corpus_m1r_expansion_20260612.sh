#!/usr/bin/env bash
set -euo pipefail

# Generated full-corpus M1-R expansion commands. Uses a dedicated manifest
# so full-run scoring is isolated from prior smoke/probe/bounded-shard outputs.

run_id=paper_b_full_corpus_m1_raw_full_0000_0249_20260612
python3 scripts/llm_scoring_20260606/run_model_locked_output_batch.py \
  --provider codex \
  --model-selector gpt-5.5 \
  --template data/04_extraction/05_llm_masem_substitution/locked_outputs/full_corpus_locked_output_template_20260609.csv \
  --manifest data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_M1_R_FULL_RUN_MANIFEST_20260612.csv \
  --source-packet-dir data/04_extraction/07_paper_c_harness_benchmark/private/source_renderings_20260609_full_coverage/source_packets \
  --require-source-packet \
  --suppress-source-quotes \
  --prompt-version paper_b_step5_full_corpus_prompt_v1_20260609_source_packet_full_corpus \
  --procedure-id raw_model_extraction_source_rendered_full_corpus \
  --run-id "$run_id" \
  --offset 0 \
  --limit 250 \
  --chunk-size 10 \
  --timeout 900 \
  --register \
  --fail-on-model-cli-error

run_id=paper_b_full_corpus_m1_raw_full_0250_0499_20260612
python3 scripts/llm_scoring_20260606/run_model_locked_output_batch.py \
  --provider codex \
  --model-selector gpt-5.5 \
  --template data/04_extraction/05_llm_masem_substitution/locked_outputs/full_corpus_locked_output_template_20260609.csv \
  --manifest data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_M1_R_FULL_RUN_MANIFEST_20260612.csv \
  --source-packet-dir data/04_extraction/07_paper_c_harness_benchmark/private/source_renderings_20260609_full_coverage/source_packets \
  --require-source-packet \
  --suppress-source-quotes \
  --prompt-version paper_b_step5_full_corpus_prompt_v1_20260609_source_packet_full_corpus \
  --procedure-id raw_model_extraction_source_rendered_full_corpus \
  --run-id "$run_id" \
  --offset 250 \
  --limit 250 \
  --chunk-size 10 \
  --timeout 900 \
  --register \
  --fail-on-model-cli-error

run_id=paper_b_full_corpus_m1_raw_full_0500_0749_20260612
python3 scripts/llm_scoring_20260606/run_model_locked_output_batch.py \
  --provider codex \
  --model-selector gpt-5.5 \
  --template data/04_extraction/05_llm_masem_substitution/locked_outputs/full_corpus_locked_output_template_20260609.csv \
  --manifest data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_M1_R_FULL_RUN_MANIFEST_20260612.csv \
  --source-packet-dir data/04_extraction/07_paper_c_harness_benchmark/private/source_renderings_20260609_full_coverage/source_packets \
  --require-source-packet \
  --suppress-source-quotes \
  --prompt-version paper_b_step5_full_corpus_prompt_v1_20260609_source_packet_full_corpus \
  --procedure-id raw_model_extraction_source_rendered_full_corpus \
  --run-id "$run_id" \
  --offset 500 \
  --limit 250 \
  --chunk-size 10 \
  --timeout 900 \
  --register \
  --fail-on-model-cli-error

run_id=paper_b_full_corpus_m1_raw_full_0750_0999_20260612
python3 scripts/llm_scoring_20260606/run_model_locked_output_batch.py \
  --provider codex \
  --model-selector gpt-5.5 \
  --template data/04_extraction/05_llm_masem_substitution/locked_outputs/full_corpus_locked_output_template_20260609.csv \
  --manifest data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_M1_R_FULL_RUN_MANIFEST_20260612.csv \
  --source-packet-dir data/04_extraction/07_paper_c_harness_benchmark/private/source_renderings_20260609_full_coverage/source_packets \
  --require-source-packet \
  --suppress-source-quotes \
  --prompt-version paper_b_step5_full_corpus_prompt_v1_20260609_source_packet_full_corpus \
  --procedure-id raw_model_extraction_source_rendered_full_corpus \
  --run-id "$run_id" \
  --offset 750 \
  --limit 250 \
  --chunk-size 10 \
  --timeout 900 \
  --register \
  --fail-on-model-cli-error

run_id=paper_b_full_corpus_m1_raw_full_1000_1249_20260612
python3 scripts/llm_scoring_20260606/run_model_locked_output_batch.py \
  --provider codex \
  --model-selector gpt-5.5 \
  --template data/04_extraction/05_llm_masem_substitution/locked_outputs/full_corpus_locked_output_template_20260609.csv \
  --manifest data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_M1_R_FULL_RUN_MANIFEST_20260612.csv \
  --source-packet-dir data/04_extraction/07_paper_c_harness_benchmark/private/source_renderings_20260609_full_coverage/source_packets \
  --require-source-packet \
  --suppress-source-quotes \
  --prompt-version paper_b_step5_full_corpus_prompt_v1_20260609_source_packet_full_corpus \
  --procedure-id raw_model_extraction_source_rendered_full_corpus \
  --run-id "$run_id" \
  --offset 1000 \
  --limit 250 \
  --chunk-size 10 \
  --timeout 900 \
  --register \
  --fail-on-model-cli-error

run_id=paper_b_full_corpus_m1_raw_full_1250_1499_20260612
python3 scripts/llm_scoring_20260606/run_model_locked_output_batch.py \
  --provider codex \
  --model-selector gpt-5.5 \
  --template data/04_extraction/05_llm_masem_substitution/locked_outputs/full_corpus_locked_output_template_20260609.csv \
  --manifest data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_M1_R_FULL_RUN_MANIFEST_20260612.csv \
  --source-packet-dir data/04_extraction/07_paper_c_harness_benchmark/private/source_renderings_20260609_full_coverage/source_packets \
  --require-source-packet \
  --suppress-source-quotes \
  --prompt-version paper_b_step5_full_corpus_prompt_v1_20260609_source_packet_full_corpus \
  --procedure-id raw_model_extraction_source_rendered_full_corpus \
  --run-id "$run_id" \
  --offset 1250 \
  --limit 250 \
  --chunk-size 10 \
  --timeout 900 \
  --register \
  --fail-on-model-cli-error

run_id=paper_b_full_corpus_m1_raw_full_1500_1749_20260612
python3 scripts/llm_scoring_20260606/run_model_locked_output_batch.py \
  --provider codex \
  --model-selector gpt-5.5 \
  --template data/04_extraction/05_llm_masem_substitution/locked_outputs/full_corpus_locked_output_template_20260609.csv \
  --manifest data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_M1_R_FULL_RUN_MANIFEST_20260612.csv \
  --source-packet-dir data/04_extraction/07_paper_c_harness_benchmark/private/source_renderings_20260609_full_coverage/source_packets \
  --require-source-packet \
  --suppress-source-quotes \
  --prompt-version paper_b_step5_full_corpus_prompt_v1_20260609_source_packet_full_corpus \
  --procedure-id raw_model_extraction_source_rendered_full_corpus \
  --run-id "$run_id" \
  --offset 1500 \
  --limit 250 \
  --chunk-size 10 \
  --timeout 900 \
  --register \
  --fail-on-model-cli-error

run_id=paper_b_full_corpus_m1_raw_full_1750_1999_20260612
python3 scripts/llm_scoring_20260606/run_model_locked_output_batch.py \
  --provider codex \
  --model-selector gpt-5.5 \
  --template data/04_extraction/05_llm_masem_substitution/locked_outputs/full_corpus_locked_output_template_20260609.csv \
  --manifest data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_M1_R_FULL_RUN_MANIFEST_20260612.csv \
  --source-packet-dir data/04_extraction/07_paper_c_harness_benchmark/private/source_renderings_20260609_full_coverage/source_packets \
  --require-source-packet \
  --suppress-source-quotes \
  --prompt-version paper_b_step5_full_corpus_prompt_v1_20260609_source_packet_full_corpus \
  --procedure-id raw_model_extraction_source_rendered_full_corpus \
  --run-id "$run_id" \
  --offset 1750 \
  --limit 250 \
  --chunk-size 10 \
  --timeout 900 \
  --register \
  --fail-on-model-cli-error

run_id=paper_b_full_corpus_m1_raw_full_2000_2042_20260612
python3 scripts/llm_scoring_20260606/run_model_locked_output_batch.py \
  --provider codex \
  --model-selector gpt-5.5 \
  --template data/04_extraction/05_llm_masem_substitution/locked_outputs/full_corpus_locked_output_template_20260609.csv \
  --manifest data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_M1_R_FULL_RUN_MANIFEST_20260612.csv \
  --source-packet-dir data/04_extraction/07_paper_c_harness_benchmark/private/source_renderings_20260609_full_coverage/source_packets \
  --require-source-packet \
  --suppress-source-quotes \
  --prompt-version paper_b_step5_full_corpus_prompt_v1_20260609_source_packet_full_corpus \
  --procedure-id raw_model_extraction_source_rendered_full_corpus \
  --run-id "$run_id" \
  --offset 2000 \
  --limit 43 \
  --chunk-size 10 \
  --timeout 900 \
  --register \
  --fail-on-model-cli-error

python3 scripts/llm_scoring_20260606/score_full_corpus_m1_r_with_exception_layer.py \
  --manifest data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_M1_R_FULL_RUN_MANIFEST_20260612.csv \
  --scored-output data/04_extraction/05_llm_masem_substitution/results/paper_b_full_corpus_m1_raw_full_scored_20260612.csv \
  --summary-output data/04_extraction/05_llm_masem_substitution/results/paper_b_full_corpus_m1_raw_full_score_summary_20260612.csv \
  --exception-scored-output data/04_extraction/05_llm_masem_substitution/results/paper_b_full_corpus_m1_raw_full_exception_layer_scored_20260612.csv \
  --exception-summary-output data/04_extraction/05_llm_masem_substitution/results/paper_b_full_corpus_m1_raw_full_exception_layer_scored_summary_20260612.csv
