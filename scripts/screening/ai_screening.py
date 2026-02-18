#!/usr/bin/env python3
"""
OAuth-oriented dual-AI title/abstract screening.

Primary use case:
- Codex CLI + Gemini CLI run independently on each record
- Store both decisions + rationale + confidence
- Route to consensus buckets (include / exclude / conflict)
- Human coders finalize all decisions
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd
import yaml

logger = logging.getLogger(__name__)


SCREENING_PROMPT = """You are screening studies for an educational AI adoption meta-analysis.

Apply these criteria:
1) Empirical quantitative study with primary data
2) AI technology is focal (not general ICT/IT)
3) Educational setting/population (students, instructors, administrators)
4) Adoption/acceptance/intention/use is measured
5) Correlation matrix or standardized beta/path data appears available or likely
6) English language
7) Publication window target: 2015-2025
8) Sample size n >= 50 (if stated or inferable from abstract)
9) Peer-reviewed journal article or full conference paper

Exclude codes:
E1=Not empirical/quantitative, E2=AI not focal, E3=Not education context,
E4=No adoption/acceptance outcome, E5=No effect size data,
E6=Not English, E7=Outside 2015-2025, E8=n<50, E9=Not peer-reviewed,
E10=Duplicate sample, E11=Qualitative/review only, E12=Other

Return strict JSON:
{{
  "decision": "include|exclude|uncertain",
  "confidence": 0.0,
  "exclude_code": "E1|E2|E3|E4|E5|E6|E7|E8|E9|E10|E11|E12|NA",
  "criteria_flags": {{
    "quantitative": "yes|no|unclear",
    "ai_focal": "yes|no|unclear",
    "education_context": "yes|no|unclear",
    "adoption_outcome": "yes|no|unclear",
    "effect_size_reported": "yes|no|unclear",
    "english": "yes|no|unclear",
    "sample_size_adequate": "yes|no|unclear"
  }},
  "rationale": "1-2 sentences"
}}

Title: {title}
Abstract: {abstract}
Keywords: {keywords}
Year: {year}
Source: {source}
"""


@dataclass
class ProviderCommandSet:
    name: str
    screen_cmd: list[str]
    version_cmd: list[str]
    auth_check_cmd: list[str] | None = None
    login_cmd: list[str] | None = None
    auth_method: str = "oauth"


def default_provider_config(provider: str) -> ProviderCommandSet:
    if provider == "codex":
        return ProviderCommandSet(
            name="codex",
            screen_cmd=["codex", "exec", "{prompt}"],
            version_cmd=["codex", "--version"],
            auth_check_cmd=["codex", "exec", "Say OK."],
            login_cmd=["codex", "--login"],
            auth_method="oauth",
        )
    if provider == "gemini":
        return ProviderCommandSet(
            name="gemini",
            screen_cmd=["gemini", "-p", "{prompt}"],
            version_cmd=["gemini", "--version"],
            auth_check_cmd=["gemini", "-p", "Say OK."],
            login_cmd=["gemini", "auth", "login"],
            auth_method="oauth",
        )
    raise ValueError(f"Unsupported provider: {provider}")


def load_provider_config(config: dict[str, Any], provider: str) -> ProviderCommandSet:
    defaults = default_provider_config(provider)
    block = config.get("screening_cli", {}).get(provider, {})
    return ProviderCommandSet(
        name=provider,
        screen_cmd=block.get("screen_cmd", defaults.screen_cmd),
        version_cmd=block.get("version_cmd", defaults.version_cmd),
        auth_check_cmd=block.get("auth_check_cmd", defaults.auth_check_cmd),
        login_cmd=block.get("login_cmd", defaults.login_cmd),
        auth_method=block.get("auth_method", defaults.auth_method),
    )


def run_command(cmd: list[str], timeout_s: int = 120, capture: bool = True) -> subprocess.CompletedProcess:
    logger.debug("Running command: %s", cmd)
    return subprocess.run(
        cmd,
        text=True,
        capture_output=capture,
        timeout=timeout_s,
        check=False,
    )


def try_extract_json(text: str) -> dict[str, Any]:
    text = text.strip()
    if not text:
        raise ValueError("Empty model output")

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    codeblock = re.search(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if codeblock:
        return json.loads(codeblock.group(1))

    obj = re.search(r"(\{.*\})", text, flags=re.DOTALL)
    if obj:
        return json.loads(obj.group(1))

    raise ValueError("No JSON object found in output")


def normalize_decision(value: str) -> str:
    v = (value or "").strip().lower()
    if v in {"include", "included"}:
        return "include"
    if v in {"exclude", "excluded"}:
        return "exclude"
    return "uncertain"


def auth_preflight(provider: ProviderCommandSet, auto_login: bool, timeout_s: int) -> None:
    version = run_command(provider.version_cmd, timeout_s=timeout_s)
    if version.returncode != 0:
        raise RuntimeError(f"{provider.name} CLI unavailable: {version.stderr.strip()}")

    if not provider.auth_check_cmd:
        return

    check = run_command(provider.auth_check_cmd, timeout_s=timeout_s)
    if check.returncode == 0:
        return

    if not auto_login or not provider.login_cmd:
        raise RuntimeError(
            f"{provider.name} auth check failed. Run login manually then retry.\n"
            f"stderr: {check.stderr.strip()}"
        )

    print(f"[AUTH] {provider.name}: launching login flow...", file=sys.stderr)
    login_rc = subprocess.run(provider.login_cmd, check=False).returncode
    if login_rc != 0:
        raise RuntimeError(f"{provider.name} login failed with exit code {login_rc}")

    recheck = run_command(provider.auth_check_cmd, timeout_s=timeout_s)
    if recheck.returncode != 0:
        raise RuntimeError(f"{provider.name} auth still invalid after login")


def build_prompt(row: pd.Series) -> str:
    return SCREENING_PROMPT.format(
        title=str(row.get("title", "")),
        abstract=str(row.get("abstract", "")),
        keywords=str(row.get("keywords", "")),
        year=str(row.get("year", "")),
        source=str(row.get("search_source", row.get("source_database", ""))),
    )


def invoke_provider(provider: ProviderCommandSet, prompt: str, timeout_s: int) -> dict[str, Any]:
    cmd = [part.replace("{prompt}", prompt) for part in provider.screen_cmd]
    try:
        result = run_command(cmd, timeout_s=timeout_s)
    except subprocess.TimeoutExpired:
        logger.warning("%s timed out after %ss", provider.name, timeout_s)
        return {
            "decision": "uncertain",
            "confidence": 0.0,
            "exclude_code": "NA",
            "criteria_flags": {},
            "rationale": f"{provider.name} timed out after {timeout_s}s",
            "raw_output": "",
        }

    if result.returncode != 0:
        return {
            "decision": "uncertain",
            "confidence": 0.0,
            "exclude_code": "NA",
            "criteria_flags": {},
            "rationale": f"{provider.name} command failed: {result.stderr.strip()}",
            "raw_output": result.stdout,
        }

    try:
        payload = try_extract_json(result.stdout)
    except Exception as exc:
        payload = {
            "decision": "uncertain",
            "confidence": 0.0,
            "exclude_code": "NA",
            "criteria_flags": {},
            "rationale": f"Failed to parse JSON from {provider.name}: {exc}",
        }

    payload["decision"] = normalize_decision(str(payload.get("decision", "uncertain")))
    payload["confidence"] = float(payload.get("confidence", 0.0) or 0.0)
    payload["exclude_code"] = payload.get("exclude_code", "NA") or "NA"
    payload["rationale"] = str(payload.get("rationale", "")).strip()
    payload["raw_output"] = result.stdout
    return payload


def consensus(dec1: str, dec2: str) -> str:
    if dec1 == dec2 == "include":
        return "include"
    if dec1 == dec2 == "exclude":
        return "exclude"
    return "conflict"


def prepare_record_id(df: pd.DataFrame) -> pd.DataFrame:
    if "record_id" in df.columns:
        return df
    out = df.copy()
    out.insert(0, "record_id", range(1, len(out) + 1))
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Dual-provider AI screening (Codex + Gemini)")
    parser.add_argument("input", type=str, help="Input CSV file")
    parser.add_argument("output", type=str, help="Output CSV file")
    _default_config = str(Path(__file__).resolve().parent.parent / "ai_coding_pipeline" / "config.yaml")
    parser.add_argument("--config", type=str, default=_default_config)
    parser.add_argument("--engine", type=str, choices=["codex", "gemini", "both"], default="both")
    parser.add_argument("--resume", action="store_true", help="Resume from existing output file")
    parser.add_argument("--save-every", type=int, default=50, help="Checkpoint interval")
    parser.add_argument("--timeout", type=int, default=180, help="Provider timeout (seconds)")
    parser.add_argument("--auto-login", action="store_true", help="Attempt OAuth login on auth failure")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    with open(args.config, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    records = pd.read_csv(args.input)
    records = prepare_record_id(records)

    providers: list[ProviderCommandSet] = []
    if args.engine in {"codex", "both"}:
        providers.append(load_provider_config(config, "codex"))
    if args.engine in {"gemini", "both"}:
        providers.append(load_provider_config(config, "gemini"))

    for provider in providers:
        auth_preflight(provider, auto_login=args.auto_login, timeout_s=args.timeout)
    auth_method_by_provider = {p.name: p.auth_method for p in providers}

    output_path = Path(args.output)
    if args.resume and output_path.exists():
        existing = pd.read_csv(output_path)
        done_ids = set(existing["record_id"].astype(str).tolist())
        todo = records[~records["record_id"].astype(str).isin(done_ids)].copy()
        results = existing.to_dict("records")
        logger.info("Resume mode: %s done / %s remaining", len(done_ids), len(todo))
    else:
        todo = records
        results = []

    for idx, row in todo.iterrows():
        prompt = build_prompt(row)
        payloads: dict[str, dict[str, Any]] = {}
        for provider in providers:
            payloads[provider.name] = invoke_provider(provider, prompt, timeout_s=args.timeout)

        codex_p = payloads.get("codex", {"decision": "uncertain", "confidence": 0.0, "exclude_code": "NA", "rationale": ""})
        gemini_p = payloads.get("gemini", {"decision": "uncertain", "confidence": 0.0, "exclude_code": "NA", "rationale": ""})
        row_out = {
            "record_id": row["record_id"],
            "title": row.get("title", ""),
            "year": row.get("year", ""),
            "search_source": row.get("search_source", row.get("source_database", "")),
            "screen_decision_codex": codex_p["decision"],
            "screen_decision_gemini": gemini_p["decision"],
            "screen_confidence_codex": codex_p["confidence"],
            "screen_confidence_gemini": gemini_p["confidence"],
            "exclude_code_codex": codex_p["exclude_code"],
            "exclude_code_gemini": gemini_p["exclude_code"],
            "rationale_codex": codex_p["rationale"],
            "rationale_gemini": gemini_p["rationale"],
            "screen_consensus": consensus(codex_p["decision"], gemini_p["decision"]),
            "oauth_auth_method_codex": auth_method_by_provider.get("codex", "NA"),
            "oauth_auth_method_gemini": auth_method_by_provider.get("gemini", "NA"),
            "human1_decision": "",
            "human2_decision": "",
            "adjudicated_final_decision": "",
            "exclude_code": "",
            "decision_rationale": "",
            "adjudicator_id": "",
        }
        results.append(row_out)

        if (len(results) % args.save_every) == 0:
            pd.DataFrame(results).to_csv(output_path, index=False)
            logger.info("Checkpoint saved: %s rows", len(results))

        if (idx + 1) % 10 == 0:
            logger.info("Processed %s/%s", idx + 1, len(records))

    pd.DataFrame(results).to_csv(output_path, index=False)
    logger.info("Done. Output saved to %s", output_path)


if __name__ == "__main__":
    main()
