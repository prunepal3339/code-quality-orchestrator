#!/usr/bin/env python3

import argparse
import json
import re
from pathlib import Path
from typing import Any

CODE_PATTERN = re.compile(
    r"assistant\s*```(?:python|py)\s*\r?\n(.*?)```",
    re.DOTALL | re.IGNORECASE,
)

verboseLevel = 0

def get_nested_value(data: dict[str, Any], path: str) -> Any:
    """Get a nested value using a dot-separated path."""
    value: Any = data

    for key in path.split("."):
        value = value[key]

    return value


def extract_code(content: str) -> str | None:
    """Extract Python code from an assistant fenced code block."""
    match = CODE_PATTERN.search(content)

    if not match:
        return None

    return match.group(1).rstrip() + "\n"


def extract_tasks(
    input_file: Path,
    output_dir: Path,
    source: str,
) -> None:
    with input_file.open("r", encoding="utf-8") as f:
        data = json.load(f)

    output_dir.mkdir(parents=True, exist_ok=True)

    for task in data:
        task_id = task["task_id"]

        try:
            content = get_nested_value(task, source)
        except (KeyError, TypeError):
            print(f"[SKIP] Source '{source}' not found for task {task_id}")
            continue

        if not isinstance(content, str):
            print(f"[SKIP] Source '{source}' is not a string for task {task_id}")
            continue

        code = extract_code(content)

        if code is None:
            print(f"[SKIP] No Python code found for task {task_id}")
            continue

        output_file = output_dir / f"task_{task_id}.py"
        output_file.write_text(code, encoding="utf-8")

        if verboseLevel >= 2:
            print(f"[OK] task_{task_id}.py")


def main() -> None:
    global verboseLevel

    parser = argparse.ArgumentParser(
        description="Extract Python source code from JSON task outputs."
    )

    parser.add_argument(
        "-v", 
        "--verbose", 
        action="count", 
        default=0, 
        help="Increase verbosity level (e.g., -v, -vv, -vvv)"
    )

    parser.add_argument(
        "input",
        type=Path,
        help="Input JSON file",
    )

    parser.add_argument(
        "--source",
        required=True,
        help="Dot-separated JSON path containing the assistant content, "
             "e.g. outputs.watermarked.content",
    )

    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=Path("extracted"),
        help="Directory where extracted files will be written",
    )

    args = parser.parse_args()

    verboseLevel = args.verbose

    extract_tasks(
        input_file=args.input,
        output_dir=args.output_dir,
        source=args.source,
    )


if __name__ == "__main__":
    main()


# python3 extractor.py --source outputs.unwatermarked.content --output-dir sources/unwatermarked/ sources/result-sanitized-mbpp-it-1.json

# python3 extractor.py --source outputs.watermarked.content --output-dir sources/watermarked/ sources/result-sanitized-mbpp-it-1.json
