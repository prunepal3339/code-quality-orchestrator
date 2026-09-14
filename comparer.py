#!/usr/bin/env python3
"""
Compare two syntax-test JSON result files.

The comparer treats the two files as two versions of the same test set,
typically:

    unwatermarked.json
    watermarked.json

It matches tests by task number, e.g. task_12.py, rather than by array
position, because the JSON files may be in different orders.

Usage:
    python comparer.py unwatermarked.json watermarked.json

Optional:
    python comparer.py unwatermarked.json watermarked.json --json comparison.json
    python comparer.py unwatermarked.json watermarked.json --plot comparison.png
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

TASK_RE = re.compile(r"task_(\d+)\.py$", re.IGNORECASE)


def load_results(path: str | Path) -> list[dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError(f"{path}: expected a JSON array")

    for index, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(
                f"{path}: item {index} is not a JSON object"
            )

    return data


def task_id(source: str | None) -> str:
    """
    Extract task_XX from a source path.

    Falls back to the complete source when no task number is present.
    """
    if not source:
        return "<unknown>"

    match = TASK_RE.search(source)
    if match:
        return f"task_{match.group(1)}"

    return source


def analyze(results: list[dict[str, Any]]) -> dict[str, Any]:
    total_files = len(results)
    passed_files = sum(1 for r in results if r.get("passed") is True)
    failed_files = total_files - passed_files

    correct_percentage = (
        passed_files / total_files * 100
        if total_files
        else 0.0
    )

    return {
        "total_files": total_files,
        "passed_files": passed_files,
        "failed_files": failed_files,
        "correct_percentage": correct_percentage,
    }


def index_by_task(
    results: list[dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}

    for result in results:
        key = task_id(result.get("source"))

        if key in indexed:
            raise ValueError(
                f"Duplicate test result for {key}: "
                f"{result.get('source')}"
            )

        indexed[key] = result

    return indexed


def compare_results(
    unwatermarked: list[dict[str, Any]],
    watermarked: list[dict[str, Any]],
) -> dict[str, Any]:

    unwatermarked_by_task = index_by_task(unwatermarked)
    watermarked_by_task = index_by_task(watermarked)

    all_tasks = sorted(
        set(unwatermarked_by_task) | set(watermarked_by_task),
        key=lambda x: (
            int(x.split("_")[1])
            if x.startswith("task_") and x.split("_")[1].isdigit()
            else float("inf"),
            x,
        ),
    )

    comparison: list[dict[str, Any]] = []

    for task in all_tasks:
        unwatermarked_result = unwatermarked_by_task.get(task)
        watermarked_result = watermarked_by_task.get(task)

        if unwatermarked_result is None:
            comparison.append({
                "task": task,
                "status": "added_in_watermarked",
                "unwatermarked": None,
                "watermarked": watermarked_result,
            })
            continue

        if watermarked_result is None:
            comparison.append({
                "task": task,
                "status": "missing_in_watermarked",
                "unwatermarked": unwatermarked_result,
                "watermarked": None,
            })
            continue

        before = bool(unwatermarked_result.get("passed"))
        after = bool(watermarked_result.get("passed"))

        if before and after:
            status = "unchanged_pass"
        elif not before and not after:
            status = "unchanged_fail"
        elif before and not after:
            status = "regression"
        else:
            status = "improvement"

        comparison.append({
            "task": task,
            "status": status,
            "unwatermarked": {
                "passed": before,
                "source": unwatermarked_result.get("source"),
                "actual": unwatermarked_result.get("actual"),
                "error": unwatermarked_result.get("error"),
            },
            "watermarked": {
                "passed": after,
                "source": watermarked_result.get("source"),
                "actual": watermarked_result.get("actual"),
                "error": watermarked_result.get("error"),
            },
        })

    unchanged_pass = sum(
        x["status"] == "unchanged_pass" for x in comparison
    )
    unchanged_fail = sum(
        x["status"] == "unchanged_fail" for x in comparison
    )
    regressions = sum(
        x["status"] == "regression" for x in comparison
    )
    improvements = sum(
        x["status"] == "improvement" for x in comparison
    )

    return {
        "summary": {
            "unchanged_pass": unchanged_pass,
            "unchanged_fail": unchanged_fail,
            "regressions": regressions,
            "improvements": improvements,
            "added_in_watermarked": sum(
                x["status"] == "added_in_watermarked"
                for x in comparison
            ),
            "missing_in_watermarked": sum(
                x["status"] == "missing_in_watermarked"
                for x in comparison
            ),
        },
        "tests": comparison,
    }

def error_summary(result: dict[str, Any] | None) -> str:
    """
    Produce a compact, human-readable cause of failure.
    """
    if not result:
        return "No result available."

    error = result.get("error")

    if not error:
        actual = result.get("actual")
        expected = result.get("expected")

        if actual is not None and expected is not None:
            return f"Expected {expected!r}, got {actual!r}."

        return "Test failed without an error message."

    error_type = error.get("type", "Unknown error")
    message = error.get("message", "No error message.")

    # PyCompileError often contains the useful SyntaxError after the
    # "File ..." prefix. Keep it readable.
    lines = [
        line.strip()
        for line in str(message).splitlines()
        if line.strip()
    ]

    if error_type == "PyCompileError":
        for line in reversed(lines):
            if line.startswith(
                (
                    "SyntaxError:",
                    "IndentationError:",
                    "TabError:",
                    "NameError:",
                    "TypeError:",
                )
            ):
                return line

        if lines:
            return lines[-1]

    return f"{error_type}: {message}"


def print_report(
    unwatermarked: dict[str, Any],
    watermarked: dict[str, Any],
    comparison: dict[str, Any],
    unwatermarked_name: str,
    watermarked_name: str,
) -> None:

    def print_stats(
        title: str,
        stats: dict[str, Any],
    ) -> None:
        print(title)
        print("=" * len(title))
        print(f"Total files:       {stats['total_files']}")
        print(f"Passed files:      {stats['passed_files']}")
        print(f"Failed files:      {stats['failed_files']}")
        print(
            f"Correct percentage: "
            f"{stats['correct_percentage']:.2f}%"
        )
        print()

    print()
    print_stats(
        f"Unwatermarked: {unwatermarked_name}",
        unwatermarked,
    )
    print_stats(
        f"Watermarked: {watermarked_name}",
        watermarked,
    )

    summary = comparison["summary"]

    print("Comparison")
    print("==========")
    print(
        f"Pass percentage change: "
        f"{watermarked['correct_percentage'] - unwatermarked['correct_percentage']:+.2f} percentage points"
    )
    print(f"Regressions:            {summary['regressions']}")
    print(f"Improvements:           {summary['improvements']}")
    print(f"Unchanged passes:       {summary['unchanged_pass']}")
    print(f"Unchanged failures:     {summary['unchanged_fail']}")

    if summary["added_in_watermarked"]:
        print(
            f"Added in watermarked:   "
            f"{summary['added_in_watermarked']}"
        )

    if summary["missing_in_watermarked"]:
        print(
            f"Missing in watermarked: "
            f"{summary['missing_in_watermarked']}"
        )

    regressions = [
        x for x in comparison["tests"]
        if x["status"] == "regression"
    ]

    improvements = [
        x for x in comparison["tests"]
        if x["status"] == "improvement"
    ]

    if regressions:
        print()
        print("Regressions")
        print("-----------")

        for item in regressions:
            before = item["unwatermarked"]
            after = item["watermarked"]

            print(f"{item['task']}")
            print("  Unwatermarked: PASS")
            print("  Watermarked:   FAIL")
            print(
                f"  Cause:         "
                f"{error_summary(after)}"
            )

    if improvements:
        print()
        print("Improvements")
        print("------------")

        for item in improvements:
            before = item["unwatermarked"]
            after = item["watermarked"]

            print(f"{item['task']}")
            print("  Unwatermarked: FAIL")
            print(
                f"  Cause before:  "
                f"{error_summary(before)}"
            )
            print("  Watermarked:   PASS")


def generate_plot(
    unwatermarked: dict[str, Any],
    watermarked: dict[str, Any],
    output: str,
) -> None:
    import matplotlib.pyplot as plt

    labels = ["Unwatermarked", "Watermarked"]
    values = [
        unwatermarked["correct_percentage"],
        watermarked["correct_percentage"],
    ]

    fig, ax = plt.subplots(figsize=(7, 5))
    bars = ax.bar(labels, values)

    ax.set_title("Syntax validation correctness")
    ax.set_ylabel("Correct percentage")
    ax.set_ylim(0, 100)

    ax.bar_label(bars, fmt="%.2f%%")

    fig.tight_layout()
    fig.savefig(output, dpi=150)
    plt.close(fig)

    print(f"\nChart written to: {output}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Compare two JSON syntax-test result files."
        )
    )

    parser.add_argument(
        "unwatermarked",
        help="JSON result file for unwatermarked code",
    )
    parser.add_argument(
        "watermarked",
        help="JSON result file for watermarked code",
    )
    parser.add_argument(
        "--json",
        dest="json_output",
        help="Write the comparison report to JSON",
    )
    parser.add_argument(
        "--plot",
        help="Write a correctness comparison chart to PNG",
    )

    args = parser.parse_args()

    unwatermarked_results = load_results(args.unwatermarked)
    watermarked_results = load_results(args.watermarked)

    unwatermarked = analyze(unwatermarked_results)
    watermarked = analyze(watermarked_results)

    comparison = compare_results(
        unwatermarked_results,
        watermarked_results,
    )

    print_report(
        unwatermarked,
        watermarked,
        comparison,
        Path(args.unwatermarked).name,
        Path(args.watermarked).name,
    )

    report = {
        "unwatermarked": unwatermarked,
        "watermarked": watermarked,
        "comparison": comparison,
    }

    if args.json_output:
        with open(
            args.json_output,
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(report, f, indent=4)

        print(
            f"\nComparison report written to: "
            f"{args.json_output}"
        )

    if args.plot:
        generate_plot(
            unwatermarked,
            watermarked,
            args.plot,
        )


if __name__ == "__main__":
    main()
