#!/usr/bin/env python3

import json
import sys
from pathlib import Path
from collections import Counter


def load_results(path):
    """Load a JSON file containing a list of result objects."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError(f"{path} must contain a JSON array.")

    return data


def get_task_name(source):
    """
    Extract the task filename from the source path.

    Example:
        sources/it01/unwatermarked/Task253.py
        -> Task253.py
    """
    return Path(source).name


def index_results(results):
    """
    Index results by the basename of their source path.
    """
    indexed = {}

    for result in results:
        source = result.get("source")

        if not source:
            continue

        task_name = get_task_name(source)

        if task_name in indexed:
            print(
                f"WARNING: Duplicate task found: {task_name}",
                file=sys.stderr,
            )

        indexed[task_name] = result

    return indexed


def compare_results(unwatermarked, watermarked):
    """
    Compare unwatermarked and watermarked results.

    Returns:
        {
            "pass_to_pass": [...],
            "pass_to_fail": [...],
            "fail_to_pass": [...],
            "fail_to_fail": [...]
        }
    """

    unwatermarked_index = index_results(unwatermarked)
    watermarked_index = index_results(watermarked)

    transitions = {
        "pass_to_pass": [],
        "pass_to_fail": [],
        "fail_to_pass": [],
        "fail_to_fail": [],
    }

    only_unwatermarked = []
    only_watermarked = []

    # Compare tasks that exist in the unwatermarked results.
    for task_name, unwatermarked_result in unwatermarked_index.items():

        if task_name not in watermarked_index:
            only_unwatermarked.append(task_name)
            continue

        watermarked_result = watermarked_index[task_name]

        unwatermarked_passed = bool(unwatermarked_result.get("passed", False))
        watermarked_passed = bool(watermarked_result.get("passed", False))

        if unwatermarked_passed and watermarked_passed:
            transitions["pass_to_pass"].append(task_name)

        elif unwatermarked_passed and not watermarked_passed:
            transitions["pass_to_fail"].append(task_name)

        elif not unwatermarked_passed and watermarked_passed:
            transitions["fail_to_pass"].append(task_name)

        else:
            transitions["fail_to_fail"].append(task_name)

    # Find tasks that exist only in the watermarked results.
    for task_name in watermarked_index:
        if task_name not in unwatermarked_index:
            only_watermarked.append(task_name)

    return transitions, only_unwatermarked, only_watermarked


def print_report(
    transitions,
    only_unwatermarked,
    only_watermarked,
):
    """Print a human-readable report."""

    print("=" * 70)
    print("WATERMARKED vs UNWATERMARKED RESULT COMPARISON")
    print("=" * 70)

    pass_to_pass = len(transitions["pass_to_pass"])
    pass_to_fail = len(transitions["pass_to_fail"])
    fail_to_pass = len(transitions["fail_to_pass"])
    fail_to_fail = len(transitions["fail_to_fail"])

    total = (
        pass_to_pass
        + pass_to_fail
        + fail_to_pass
        + fail_to_fail
    )

    print()
    print("2x2 TRANSITION TABLE")
    print("-" * 70)

    print(f"{'':20} {'Watermarked PASS':20} {'Watermarked FAIL':20}")
    print(
        f"{'Unwatermarked PASS':20} "
        f"{pass_to_pass:<20} "
        f"{pass_to_fail:<20}"
    )
    print(
        f"{'Unwatermarked FAIL':20} "
        f"{fail_to_pass:<20} "
        f"{fail_to_fail:<20}"
    )

    print()
    print("TRANSITIONS")
    print("-" * 70)

    print(f"PASS -> PASS : {pass_to_pass}")
    print(f"PASS -> FAIL : {pass_to_fail}")
    print(f"FAIL -> PASS : {fail_to_pass}")
    print(f"FAIL -> FAIL : {fail_to_fail}")

    print()
    print(f"Matched tasks: {total}")

    if only_unwatermarked:
        print()
        print(
            f"Only in unwatermarked: "
            f"{len(only_unwatermarked)}"
        )

    if only_watermarked:
        print()
        print(
            f"Only in watermarked: "
            f"{len(only_watermarked)}"
        )

    print()
    print("=" * 70)


def save_report(
    output_path,
    transitions,
    only_unwatermarked,
    only_watermarked,
):
    """Save the comparison result as JSON."""

    report = {
        "summary": {
            "pass_to_pass": len(transitions["pass_to_pass"]),
            "pass_to_fail": len(transitions["pass_to_fail"]),
            "fail_to_pass": len(transitions["fail_to_pass"]),
            "fail_to_fail": len(transitions["fail_to_fail"]),
            "matched_tasks": sum(
                len(tasks)
                for tasks in transitions.values()
            ),
            "only_unwatermarked": len(only_unwatermarked),
            "only_watermarked": len(only_watermarked),
        },
        "transitions": transitions,
        "only_unwatermarked": only_unwatermarked,
        "only_watermarked": only_watermarked,
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)


def main():
    if len(sys.argv) < 3:
        print(
            "Usage:\n"
            "  python compare_results.py "
            "<unwatermarked.json> <watermarked.json> "
            "[output.json]"
        )
        sys.exit(1)

    unwatermarked_path = sys.argv[1]
    watermarked_path = sys.argv[2]

    output_path = (
        sys.argv[3]
        if len(sys.argv) >= 4
        else "comparison_report.json"
    )

    unwatermarked = load_results(unwatermarked_path)
    watermarked = load_results(watermarked_path)

    transitions, only_unwatermarked, only_watermarked = (
        compare_results(
            unwatermarked,
            watermarked,
        )
    )

    print_report(
        transitions,
        only_unwatermarked,
        only_watermarked,
    )

    save_report(
        output_path,
        transitions,
        only_unwatermarked,
        only_watermarked,
    )

    print()
    print(f"Detailed report written to: {output_path}")


if __name__ == "__main__":
    main()
