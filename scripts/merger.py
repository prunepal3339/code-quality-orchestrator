import json
import sys
from pathlib import Path

def merge_results(aggregate):
    summary = {}
    for task, iterations in aggregate.items():
        passed = False
        first_passing_iteration = float('inf')
        for iteration in iterations:
            passed = passed or iteration.get('passed', False)
            if iteration.get('passed', False):
                first_passing_iteration = min(iteration.get('iteration'), first_passing_iteration)
        summary[task] = {
            "passed": passed,
            "original_task_id": task
        }
        if passed:
            summary[task]['first_passing_iteration'] = first_passing_iteration
    return summary

def main():
    aggregate = json.loads(Path(sys.argv[1]).read_text())
    results = {}

    results['unwatermarked'] = merge_results(aggregate['unwatermarked'])
    results['watermarked'] = merge_results(aggregate['watermarked'])
    
    output = json.dumps(results, indent=2)
    Path(sys.argv[2]).write_text(output + "\n")

if __name__ == "__main__":
    main()

