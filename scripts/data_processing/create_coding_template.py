#!/usr/bin/env python3
"""
Wrapper for generating the canonical coding template workbook.

Canonical generator:
  data/templates/create_masem_template.py
"""

from pathlib import Path
import runpy


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    generator = repo_root / "data" / "templates" / "create_masem_template.py"
    if not generator.exists():
        raise FileNotFoundError(f"Template generator not found: {generator}")
    runpy.run_path(str(generator), run_name="__main__")


if __name__ == "__main__":
    main()
