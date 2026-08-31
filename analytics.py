#!/usr/bin/env python3
"""
Compare two quality-gate JSON result files.

Usage:
    python analytics.py unwatermarked.json watermarked.json
    python analytics.py unwatermarked.json watermarked.json --output comparison.json
    python analytics.py unwatermarked.json watermarked.json --plot comparison.png
"""

import argparse
import json
from pathlib import Path
from typing import Any


def load_results(path: str | Path) -> list[dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError(f"{path}: expected a JSON array")

    return data


def safe_ratio(passed: int, total: int) -> float:
    return passed / total if total else 0.0


def analyze(results: list[dict[str, Any]]) -> dict[str, Any]:
    total_tests = len(results)
    passed_tests = sum(bool(r.get("passed")) for r in results)
    failed_tests = total_tests - passed_tests

    total_assertions = sum(r.get("total", 0) for r in results)
    passed_assertions = sum(r.get("passed_count", 0) for r in results)
    failed_assertions = sum(r.get("failed_count", 0) for r in results)

    assertion_pass_ratio = safe_ratio(passed_assertions, total_assertions)
    test_pass_ratio = safe_ratio(passed_tests, total_tests)

    assertion_failures = [
        {
            "source": r.get("source"),
            "target": r.get("target"),
            "expected": a.get("expected"),
            "actual": a.get("actual"),
            "error": a.get("error"),
        }
        for r in results
        for a in r.get("assertions", [])
        if not a.get("passed", False)
    ]

    failed_tests_detail = [
        {
            "source": r.get("source"),
            "target": r.get("target"),
            "passed_count": r.get("passed_count", 0),
            "failed_count": r.get("failed_count", 0),
            "total": r.get("total", 0),
        }
        for r in results
        if not r.get("passed", False)
    ]

    return {
        "test_count": total_tests,
        "passed_tests": passed_tests,
        "failed_tests": failed_tests,
        "test_pass_ratio": test_pass_ratio,
        "test_pass_percentage": test_pass_ratio * 100,
        "assertion_count": total_assertions,
        "passed_assertions": passed_assertions,
        "failed_assertions": failed_assertions,
        "assertion_pass_ratio": assertion_pass_ratio,
        "assertion_pass_percentage": assertion_pass_ratio * 100,
        "failed_tests_detail": failed_tests_detail,
        "assertion_failures": assertion_failures,
    }


def compare(
    unwatermarked: dict[str, Any],
    watermarked: dict[str, Any],
) -> dict[str, Any]:
    def delta(key: str) -> float | int:
        return watermarked[key] - unwatermarked[key]

    def percentage_point_delta(key: str) -> float:
        return (watermarked[key] - unwatermarked[key]) * 100

    return {
        "test_pass_ratio": {
            "unwatermarked": unwatermarked["test_pass_ratio"],
            "watermarked": watermarked["test_pass_ratio"],
            "delta": delta("test_pass_ratio"),
            "percentage_points": percentage_point_delta("test_pass_ratio"),
        },
        "assertion_pass_ratio": {
            "unwatermarked": unwatermarked["assertion_pass_ratio"],
            "watermarked": watermarked["assertion_pass_ratio"],
            "delta": delta("assertion_pass_ratio"),
            "percentage_points": percentage_point_delta("assertion_pass_ratio"),
        },
        "test_count_delta": delta("test_count"),
        "passed_tests_delta": delta("passed_tests"),
        "failed_tests_delta": delta("failed_tests"),
        "assertion_count_delta": delta("assertion_count"),
        "passed_assertions_delta": delta("passed_assertions"),
        "failed_assertions_delta": delta("failed_assertions"),
    }


def print_analysis(name: str, analysis: dict[str, Any]) -> None:
    print(f"\n{name}")
    print("-" * len(name))
    print(f"Tests:              {analysis['test_count']}")
    print(f"Passed tests:       {analysis['passed_tests']}")
    print(f"Failed tests:       {analysis['failed_tests']}")
    print(f"Test pass ratio:    {analysis['test_pass_percentage']:.2f}%")
    print()
    print(f"Assertions:         {analysis['assertion_count']}")
    print(f"Passed assertions:  {analysis['passed_assertions']}")
    print(f"Failed assertions:  {analysis['failed_assertions']}")
    print(f"Assertion ratio:    {analysis['assertion_pass_percentage']:.2f}%")

    if analysis["failed_tests_detail"]:
        print("\nFailed tests:")
        for item in analysis["failed_tests_detail"]:
            print(
                f"  - {item['target']} "
                f"({item['failed_count']}/{item['total']} assertions failed)"
            )


def print_comparison(comparison: dict[str, Any]) -> None:
    print("\nComparison: watermarked - unwatermarked")
    print("----------------------------------------")

    for metric in ("test_pass_ratio", "assertion_pass_ratio"):
        item = comparison[metric]
        print(
            f"{metric}: "
            f"{item['unwatermarked'] * 100:.2f}% -> "
            f"{item['watermarked'] * 100:.2f}% "
            f"({item['percentage_points']:+.2f} percentage points)"
        )

    for metric in (
        "passed_tests_delta",
        "failed_tests_delta",
        "passed_assertions_delta",
        "failed_assertions_delta",
    ):
        print(f"{metric}: {comparison[metric]:+d}")


def generate_plot(
    unwatermarked: dict[str, Any],
    watermarked: dict[str, Any],
    output: str,
) -> None:
    import matplotlib.pyplot as plt

    labels = ["Test pass ratio", "Assertion pass ratio"]
    before = [
        unwatermarked["test_pass_percentage"],
        unwatermarked["assertion_pass_percentage"],
    ]
    after = [
        watermarked["test_pass_percentage"],
        watermarked["assertion_pass_percentage"],
    ]

    x = range(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar([i - width / 2 for i in x], before, width, label="Unwatermarked")
    ax.bar([i + width / 2 for i in x], after, width, label="Watermarked")

    ax.set_ylabel("Pass percentage")
    ax.set_title("Quality-gate comparison")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 100)
    ax.legend()

    for bars in ax.containers:
        ax.bar_label(bars, fmt="%.1f%%")

    fig.tight_layout()
    fig.savefig(output, dpi=150)
    plt.close(fig)

    print(f"\nChart written to: {output}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Analyze and compare quality-gate JSON results."
    )
    parser.add_argument("unwatermarked")
    parser.add_argument("watermarked")
    parser.add_argument(
        "--output",
        help="Write complete comparison report as JSON.",
    )
    parser.add_argument(
        "--plot",
        help="Write a comparison chart as PNG.",
    )

    args = parser.parse_args()

    unwatermarked_results = load_results(args.unwatermarked)
    watermarked_results = load_results(args.watermarked)

    unwatermarked = analyze(unwatermarked_results)
    watermarked = analyze(watermarked_results)
    comparison = compare(unwatermarked, watermarked)

    print_analysis("Unwatermarked", unwatermarked)
    print_analysis("Watermarked", watermarked)
    print_comparison(comparison)

    report = {
        "unwatermarked": unwatermarked,
        "watermarked": watermarked,
        "comparison": comparison,
    }

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)

        print(f"\nReport written to: {args.output}")

    if args.plot:
        generate_plot(unwatermarked, watermarked, args.plot)


if __name__ == "__main__":
    main()
