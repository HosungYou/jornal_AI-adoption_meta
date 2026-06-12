#!/usr/bin/env python3
"""Prepare an isolated full-corpus M1-R expansion plan.

The plan intentionally uses a dedicated manifest so full-run interpretation is
not mixed with earlier smoke, probe, and bounded-shard outputs.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from datetime import date
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
STEP5 = REPO / "data/04_extraction/05_llm_masem_substitution"
BENCH = REPO / "data/04_extraction/07_paper_c_harness_benchmark"
RESULTS = STEP5 / "results"
BUNDLES = BENCH / "06_rerun_bundles"

DEFAULT_TEMPLATE = STEP5 / "locked_outputs/full_corpus_locked_output_template_20260609.csv"
DEFAULT_SOURCE_PACKET_DIR = BENCH / "private/source_renderings_20260609_full_coverage/source_packets"
DEFAULT_MANIFEST = STEP5 / "locked_outputs/FULL_CORPUS_M1_R_FULL_RUN_MANIFEST_20260612.csv"
DEFAULT_SHARDS = BUNDLES / "full_corpus_m1r_expansion_shards_20260612.csv"
DEFAULT_COMMANDS = BUNDLES / "run_full_corpus_m1r_expansion_20260612.sh"
DEFAULT_REPORT = RESULTS / "FULL_CORPUS_M1_R_EXPANSION_GATE_20260612.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def eligible_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [
        row
        for row in rows
        if row.get("scoring_eligibility", "").startswith("eligible_after_locked_llm_output")
    ]


def packet_exists(source_packet_dir: Path, study_id: str) -> bool:
    return bool(list(source_packet_dir.glob(f"{study_id}_source_packet*.txt")))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO))
    except ValueError:
        return str(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--source-packet-dir", type=Path, default=DEFAULT_SOURCE_PACKET_DIR)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--shards-output", type=Path, default=DEFAULT_SHARDS)
    parser.add_argument("--commands-output", type=Path, default=DEFAULT_COMMANDS)
    parser.add_argument("--report-output", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--shard-size", type=int, default=250)
    parser.add_argument("--chunk-size", type=int, default=10)
    parser.add_argument("--provider", default="codex")
    parser.add_argument("--model-selector", default="gpt-5.5")
    args = parser.parse_args()

    rows = eligible_rows(read_csv(args.template))
    studies = sorted({row["study_id"] for row in rows})
    missing_packets = [study_id for study_id in studies if not packet_exists(args.source_packet_dir, study_id)]
    family_counts = Counter(row.get("denominator_family", "") for row in rows)

    shard_rows: list[dict[str, object]] = []
    for index, offset in enumerate(range(0, len(rows), args.shard_size), start=1):
        limit = min(args.shard_size, len(rows) - offset)
        shard_rows.append(
            {
                "shard_index": index,
                "offset": offset,
                "limit": limit,
                "run_id": f"paper_b_full_corpus_m1_raw_full_{offset:04d}_{offset + limit - 1:04d}_20260612",
                "provider": args.provider,
                "model_selector": args.model_selector,
                "chunk_size": args.chunk_size,
                "manifest": rel(args.manifest),
                "status": "ready_for_authorized_model_run" if not missing_packets else "blocked_missing_private_source_packets",
            }
        )

    write_csv(
        args.shards_output,
        shard_rows,
        ["shard_index", "offset", "limit", "run_id", "provider", "model_selector", "chunk_size", "manifest", "status"],
    )
    write_csv(
        args.manifest,
        [],
        ["artifact_role", "file", "bytes", "sha256", "locked_status", "notes"],
    )

    args.commands_output.parent.mkdir(parents=True, exist_ok=True)
    commands: list[str] = [
        "#!/usr/bin/env bash",
        "set -euo pipefail",
        "",
        "# Generated full-corpus M1-R expansion commands. Uses a dedicated manifest",
        "# so full-run scoring is isolated from prior smoke/probe/bounded-shard outputs.",
        "",
    ]
    for row in shard_rows:
        commands.extend(
            [
                f"run_id={row['run_id']}",
                "python3 scripts/llm_scoring_20260606/run_model_locked_output_batch.py \\",
                f"  --provider {row['provider']} \\",
                f"  --model-selector {row['model_selector']} \\",
                f"  --template {rel(args.template)} \\",
                f"  --manifest {rel(args.manifest)} \\",
                f"  --source-packet-dir {rel(args.source_packet_dir)} \\",
                "  --require-source-packet \\",
                "  --suppress-source-quotes \\",
                "  --prompt-version paper_b_step5_full_corpus_prompt_v1_20260609_source_packet_full_corpus \\",
                "  --procedure-id raw_model_extraction_source_rendered_full_corpus \\",
                '  --run-id "$run_id" \\',
                f"  --offset {row['offset']} \\",
                f"  --limit {row['limit']} \\",
                f"  --chunk-size {row['chunk_size']} \\",
                "  --timeout 900 \\",
                "  --register \\",
                "  --fail-on-model-cli-error",
                "",
            ]
        )
    commands.extend(
        [
            "python3 scripts/llm_scoring_20260606/score_full_corpus_m1_r_with_exception_layer.py \\",
            f"  --manifest {rel(args.manifest)} \\",
            "  --scored-output data/04_extraction/05_llm_masem_substitution/results/paper_b_full_corpus_m1_raw_full_scored_20260612.csv \\",
            "  --summary-output data/04_extraction/05_llm_masem_substitution/results/paper_b_full_corpus_m1_raw_full_score_summary_20260612.csv \\",
            "  --exception-scored-output data/04_extraction/05_llm_masem_substitution/results/paper_b_full_corpus_m1_raw_full_exception_layer_scored_20260612.csv \\",
            "  --exception-summary-output data/04_extraction/05_llm_masem_substitution/results/paper_b_full_corpus_m1_raw_full_exception_layer_scored_summary_20260612.csv",
            "",
        ]
    )
    args.commands_output.write_text("\n".join(commands), encoding="utf-8")
    args.commands_output.chmod(0o755)

    family_lines = "\n".join(f"- `{family}`: {count}" for family, count in sorted(family_counts.items()))
    shard_lines = "\n".join(
        f"- Shard {row['shard_index']}: offset {row['offset']}, limit {row['limit']}, run_id `{row['run_id']}`"
        for row in shard_rows
    )
    status = "ready_for_authorized_model_run" if not missing_packets else "blocked_missing_private_source_packets"
    missing_preview = ", ".join(missing_packets[:20]) if missing_packets else "none"
    report = f"""# Full-Corpus M1-R Expansion Gate

Date: {date.today().isoformat()}

## Decision

The approved direction is full-corpus expansion centered on the post-freeze
213-study source-anchored reference gate. This plan uses a dedicated full-run
manifest so the claim-bearing run is isolated from earlier smoke, probe, and
bounded-shard outputs.

## Current Preflight

| Item | Value | Status |
| --- | --- | --- |
| Full-corpus shell | `{rel(args.template)}` | {len(rows)} eligible rows |
| Source packet directory | `{rel(args.source_packet_dir)}` | {'present' if args.source_packet_dir.exists() else 'missing'} |
| Required private source packets | {len(studies)} studies | {len(studies) - len(missing_packets)}/{len(studies)} present |
| Missing source packets | {len(missing_packets)} | {missing_preview} |
| Dedicated full-run manifest | `{rel(args.manifest)}` | initialized empty; use for full-run scoring only |
| Shard plan | `{rel(args.shards_output)}` | {len(shard_rows)} shards |
| Command script | `{rel(args.commands_output)}` | generated |
| Gate status | `{status}` | source-packet-required full-run branch |

## Denominator Families

{family_lines}

## Shards

{shard_lines}

## Required Execution Boundary

- Run shards only with `--require-source-packet` and `--suppress-source-quotes`.
- Register full-run shards only to `{rel(args.manifest)}`.
- Score only that dedicated manifest with
  `scripts/llm_scoring_20260606/score_full_corpus_m1_r_with_exception_layer.py`.
- Interpret results by denominator family and exception-layer status.
- Do not pool the 2,043 task units into one accuracy denominator.

## Stop Condition

Full-corpus M1-R accuracy remains unclaimed until all shards in this plan are
locked with zero model CLI errors, the source-quote policy is clean, and the
dedicated manifest is exception-aware scored.
"""
    args.report_output.write_text(report, encoding="utf-8")
    print(
        "full_corpus_m1r_expansion_plan_complete",
        f"eligible_rows={len(rows)}",
        f"studies={len(studies)}",
        f"missing_packets={len(missing_packets)}",
        f"shards={len(shard_rows)}",
        f"status={status}",
    )


if __name__ == "__main__":
    main()
