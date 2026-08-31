#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

DEFAULT_FIELD_TO_SUBDIR: dict[str, str] = {
    "watermarked": "watermarked",
    "unwatermarked": "unwatermarked",
}

PYTHON_CODE_BLOCK_RE = re.compile(
    r"```(?:python|py)\b(.*?)```",
    re.IGNORECASE | re.DOTALL,
)

def parse_field_dir(value: str) -> tuple[str, str]:
    field_name, separator, subdirectory = value.partition("=")
    if not separator or not field_name.strip() or not subdirectory.strip():
        raise argparse.ArgumentTypeError(
            "Expected OUTPUT_FIELD=SUBDIR, for example reviewed=reviewed"
        )
    return field_name.strip(), subdirectory.strip()



def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Extract the longest fenced Python code block from task outputs in a JSON file "
            "and write it to task_{task_number}.py files."
        ),
        epilog=(
            "Examples:\n"
            "  python extract_python_code.py result/result.json --output-dir outputs/result\n"
            "  python extract_python_code.py result/result.json --output-dir outputs/result --field-dir reviewed=reviewed\n"
            "  python extract_python_code.py result/result.json --output-dir outputs/result --field-dir watermarked=watermark"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "input_json",
        help="Path to the input JSON file, for example result/result.json.",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Base directory where extracted files will be written.",
    )
    parser.add_argument(
        "--field-dir",
        action="append",
        default=[],
        type=parse_field_dir,
        metavar="OUTPUT_FIELD=SUBDIR",
        help=(
            "Map an outputs field to an output subdirectory. Can be passed multiple "
            "times. By default, watermarked -> watermarked and unwatermarked -> "
            "unwatermarked. Use this to add extra folders or override the default "
            "subdirectory names."
        ),
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with a non-zero status if any configured output field cannot be extracted.",
    )
    return parser



def load_records(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, list):
        raise ValueError("Expected the input JSON file to contain a top-level list of tasks.")

    return data



def resolve_output_text(output_value: Any) -> str | None:
    if isinstance(output_value, str):
        return output_value

    if isinstance(output_value, dict):
        content = output_value.get("content")
        if isinstance(content, str):
            return content

    return None



def normalize_python_code_block(code: str) -> str:
    if code.startswith("\r\n"):
        code = code[2:]
    elif code.startswith("\n"):
        code = code[1:]

    return code.rstrip() + "\n"



def extract_last_python_code_block(text: str) -> str | None:
    matches = list(PYTHON_CODE_BLOCK_RE.finditer(text))
    if not matches:
        return None

    normalized_blocks = [
        normalize_python_code_block(match.group(1))
        for match in matches
    ]

    return max(normalized_blocks, key=len)



def write_task_file(output_root: Path, subdirectory: str, task_number: Any, code: str) -> None:
    destination_directory = output_root / subdirectory
    destination_directory.mkdir(parents=True, exist_ok=True)
    destination_path = destination_directory / f"task_{task_number}.py"
    destination_path.write_text(code, encoding="utf-8")



def extract_files(
    records: list[dict[str, Any]],
    output_root: Path,
    field_to_subdir: dict[str, str],
) -> tuple[int, list[str]]:
    written_files = 0
    warnings: list[str] = []

    for record in records:
        task_number = record.get("task_number")
        if task_number is None:
            warnings.append("Skipped one record because it does not contain task_number.")
            continue

        outputs = record.get("outputs")
        if not isinstance(outputs, dict):
            warnings.append(f"Skipped task {task_number} because outputs is missing or not an object.")
            continue

        for field_name, subdirectory in field_to_subdir.items():
            output_text = resolve_output_text(outputs.get(field_name))
            if output_text is None:
                warnings.append(
                    f"Skipped task {task_number} field '{field_name}' because it is missing or not a string/content object."
                )
                continue

            code = extract_last_python_code_block(output_text)
            if code is None:
                warnings.append(
                    f"Skipped task {task_number} field '{field_name}' because no fenced Python code block was found."
                )
                continue

            write_task_file(output_root, subdirectory, task_number, code)
            written_files += 1

    return written_files, warnings



def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    field_to_subdir = dict(DEFAULT_FIELD_TO_SUBDIR)
    for field_name, subdirectory in args.field_dir:
        field_to_subdir[field_name] = subdirectory

    input_path = Path(args.input_json)
    output_root = Path(args.output_dir)

    try:
        records = load_records(input_path)
    except FileNotFoundError:
        parser.error(f"Input JSON file not found: {input_path}")
    except json.JSONDecodeError as error:
        parser.error(f"Failed to parse JSON from {input_path}: {error}")
    except ValueError as error:
        parser.error(str(error))

    written_files, warnings = extract_files(records, output_root, field_to_subdir)

    print(f"Wrote {written_files} file(s) under {output_root}")

    for warning in warnings:
        print(f"Warning: {warning}", file=sys.stderr)

    if warnings and args.strict:
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
