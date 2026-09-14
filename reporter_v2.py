#!/usr/bin/env python3

import json
import sys


def load_report(path):
    """Load an assertion test report JSON file."""
    with open(path, "r") as f:
        return json.load(f)


def compare_reports(unwatermarked_report, watermarked_report):
    """
    Compare unwatermarked and watermarked assertion test reports.

    Tasks are matched using task_id.
    """

    # Create lookup dictionaries keyed by task_id
    unwatermarked = {
        item["task_id"]: item
        for item in unwatermarked_report
    }

    watermarked = {
        item["task_id"]: item
        for item in watermarked_report
    }

    unwatermarked_ids = set(unwatermarked.keys())
    watermarked_ids = set(watermarked.keys())

    matched_ids = unwatermarked_ids & watermarked_ids
    only_unwatermarked = unwatermarked_ids - watermarked_ids
    only_watermarked = watermarked_ids - unwatermarked_ids

    # Summary counters
    pass_to_pass = 0
    pass_to_fail = 0
    fail_to_pass = 0
    fail_to_fail = 0

    tasks = []

    # Compare matched tasks
    for task_id in sorted(matched_ids):
        uw = unwatermarked[task_id]
        wm = watermarked[task_id]

        uw_passed = uw.get("passed", False)
        wm_passed = wm.get("passed", False)

        if uw_passed and wm_passed:
            result = "pass_to_pass"
            pass_to_pass += 1

        elif uw_passed and not wm_passed:
            result = "pass_to_fail"
            pass_to_fail += 1

        elif not uw_passed and wm_passed:
            result = "fail_to_pass"
            fail_to_pass += 1

        else:
            result = "fail_to_fail"
            fail_to_fail += 1

        tasks.append({
            "task_id": task_id,
            "unwatermarked": {
                "passed": uw_passed,
                "error": uw.get("error")
            },
            "watermarked": {
                "passed": wm_passed,
                "error": wm.get("error")
            },
            "comparison": result
        })

    # Add tasks that exist only in the unwatermarked report
    for task_id in sorted(only_unwatermarked):
        uw = unwatermarked[task_id]

        tasks.append({
            "task_id": task_id,
            "unwatermarked": {
                "passed": uw.get("passed", False),
                "error": uw.get("error")
            },
            "watermarked": None,
            "comparison": "only_unwatermarked"
        })

    # Add tasks that exist only in the watermarked report
    for task_id in sorted(only_watermarked):
        wm = watermarked[task_id]

        tasks.append({
            "task_id": task_id,
            "unwatermarked": None,
            "watermarked": {
                "passed": wm.get("passed", False),
                "error": wm.get("error")
            },
            "comparison": "only_watermarked"
        })

    return {
        "summary": {
            "pass_to_pass": pass_to_pass,
            "pass_to_fail": pass_to_fail,
            "fail_to_pass": fail_to_pass,
            "fail_to_fail": fail_to_fail,
            "matched_tasks": len(matched_ids),
            "only_unwatermarked": len(only_unwatermarked),
            "only_watermarked": len(only_watermarked)
        },
        "tasks": tasks
    }


def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print(
            "Usage: python reporter_v2.py "
            "<unwatermarked.json> <watermarked.json> [output.json]"
        )
        sys.exit(1)

    unwatermarked_path = sys.argv[1]
    watermarked_path = sys.argv[2]

    output_path = (
        sys.argv[3]
        if len(sys.argv) == 4
        else None
    )

    try:
        unwatermarked_report = load_report(unwatermarked_path)
        watermarked_report = load_report(watermarked_path)

        comparison = compare_reports(
            unwatermarked_report,
            watermarked_report
        )

        if output_path:
            with open(output_path, "w") as f:
                json.dump(comparison, f, indent=4)

            print(f"Comparison saved to: {output_path}")
        else:
            print(json.dumps(comparison, indent=4))

    except FileNotFoundError as e:
        print(f"ERROR: File not found: {e}")
        sys.exit(1)

    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON: {e}")
        sys.exit(1)

    except KeyError as e:
        print(f"ERROR: Missing required field: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
