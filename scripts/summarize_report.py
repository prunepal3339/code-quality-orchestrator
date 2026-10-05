import json
import sys
from pathlib import Path

def extract_original_task_id(origin: str) -> str:
    return Path(origin).stem.removeprefix("task_")

def summarize_task(task: dict) -> dict:
    gate_results = task.get("gate_results", [])
    passed = bool(gate_results) and all(
        gate.get("passed", False) for gate in gate_results if gate.get("gate_id") != "assertion"
    )
    origin = gate_results[0].get("origin") if gate_results else None
    original_task_id = extract_original_task_id(origin) if origin else None
    return {
        "task_id": task["task_id"],
        "original_task_id": original_task_id,
        "passed": passed,
    }

def summarize_report(input_path: str, output_path: str) -> None:
    with open(input_path, "r", encoding="utf-8") as file:
        report = json.load(file)
    summary = [summarize_task(task) for task in report]
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)
    print(f"Summary written to: {output_path}")

def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python summarize_report.py <input.json> <output.json>")
        sys.exit(1)
    summarize_report(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
