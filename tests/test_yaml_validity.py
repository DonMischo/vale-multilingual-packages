#!/usr/bin/env python3
"""Validate every Vale style YAML file in styles/.

Checks:
  1. The file parses as valid YAML.
  2. Required Vale fields are present (extends, message, level).
  3. `existence` rules have a non-empty `tokens` list.
  4. `substitution` rules have a non-empty `swap` mapping, and no value
     contains a stray "->"/"→" artifact (the corruption bug fixed in
     commit c306ea2 — a key→value pair got concatenated into one value).

Usage:
    python tests/test_yaml_validity.py

Exits with status 1 and prints every problem found if any file fails.
"""
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
STYLES_DIR = REPO_ROOT / "styles"
ARROW_MARKERS = ("->", "→")  # ASCII arrow and U+2192 RIGHTWARDS ARROW


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    rel = path.relative_to(REPO_ROOT)

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return [f"{rel}: not valid UTF-8 ({exc})"]

    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        return [f"{rel}: YAML parse error: {exc}"]

    if not isinstance(data, dict):
        return [f"{rel}: top-level YAML is not a mapping"]

    for field in ("extends", "message", "level"):
        if field not in data:
            errors.append(f"{rel}: missing required field '{field}'")

    extends = data.get("extends")

    if extends == "existence":
        tokens = data.get("tokens")
        if not isinstance(tokens, list) or not tokens:
            errors.append(f"{rel}: 'existence' rule has empty/missing 'tokens' list")

    elif extends == "substitution":
        swap = data.get("swap")
        if not isinstance(swap, dict) or not swap:
            errors.append(f"{rel}: 'substitution' rule has empty/missing 'swap' mapping")
        else:
            for key, value in swap.items():
                if not isinstance(value, str):
                    errors.append(f"{rel}: swap value for key {key!r} is not a string: {value!r}")
                    continue
                if any(marker in value for marker in ARROW_MARKERS):
                    errors.append(
                        f"{rel}: swap value for key {key!r} contains a stray arrow artifact: {value!r}"
                    )
                if value.rstrip().endswith(":"):
                    errors.append(
                        f"{rel}: swap value for key {key!r} ends with ':' (likely YAML corruption): {value!r}"
                    )

    return errors


def main() -> int:
    if not STYLES_DIR.is_dir():
        print(f"styles/ directory not found at {STYLES_DIR}", file=sys.stderr)
        return 1

    yaml_files = sorted(STYLES_DIR.rglob("*.yml"))
    if not yaml_files:
        print("No YAML files found under styles/", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    for path in yaml_files:
        all_errors.extend(check_file(path))

    if all_errors:
        print(f"FAILED — {len(all_errors)} problem(s) in {len(yaml_files)} file(s):\n")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    print(f"OK — {len(yaml_files)} YAML files parsed and validated cleanly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
