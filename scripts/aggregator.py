import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

TASK_ID_PATTERN = re.compile(r"^Task#it?(\d+)([uw])_(\d)+$", re.IGNORECASE)

def aggregate(results):
    grouped = {
        "unwatermarked": defaultdict(list),
        "watermarked": defaultdict(list),
    }
    
    for row in results:
        match = TASK_ID_PATTERN.fullmatch(row.get("task_id", ""))
        if not match:
            continue
            
        iteration, variation, _ = match.groups()

        variation_key = "unwatermarked" if variation.lower() == "u" else "watermarked"
        task_key = str(row["original_task_id"])
        grouped[variation_key][task_key].append({
            "iteration": int(iteration),
            "task_id": row["task_id"],
            "original_task_id": row["original_task_id"],
            "passed": row.get("passed") is True,
        })
    return grouped
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input",
        help="Input JSON file"
    )
    parser.add_argument(
        "-o",
        "--output",
        default="-",
        help="Output JSON file (default: stdout)"
    )

    args = parser.parse_args()

    results = json.loads(Path(args.input).read_text())
    report = aggregate(results)
    output = json.dumps(report, indent=2)

    if args.output == "-":
        print(output)
    else:
        Path(args.output).write_text(output + "\n")
    
if __name__ == "__main__":
    main()
