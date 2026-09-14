import json
import sys
from typing import Any

"""
First arg: path to syntax report file
Second arg: path to MBPP test file
Third arg: path to output file
"""
def find_sources_for_assertion(syntaxreportfile):
    sources = []
    with open(syntaxreportfile, 'r') as f:
        reports = json.loads(f.read())
        for report in reports:
            if report['passed']:
                sources.append(report['source'])
    return sources

def extract_task_id(source: str) -> str:
    import os
    filename = os.path.basename(source)
    task_id = filename.replace('.py', '').replace('Task', '')
    return task_id

def load_mbpp_tests(mbpp_path: str, target_lines: list[str]) -> dict[int, Any]:
    tests = {}
    target_lines = [ int(line) for line in target_lines ]
    with open(mbpp_path, 'r') as f:
        for line_num, line in enumerate(f, start = 1):
            if line_num in target_lines:
                line = line.strip()
                if line:
                    tests[line_num] = json.loads(line)
    return tests
if __name__ == "__main__":
    sources = find_sources_for_assertion(sys.argv[1])
    ids = []
    source_with_id = {}
    for source in sources:
        task_id = int(extract_task_id(source))
        ids.append(task_id)
        source_with_id[task_id] = source
    tests = load_mbpp_tests(sys.argv[2], ids)
    test_results = []
    for test_id, test_dict in tests.items():
        test_result = {
            'task_id': test_id,
            'source': source_with_id[test_id]
        }
        assertions = test_dict['test_list']
        namespace = {}
        with open(source_with_id[test_id], 'r') as f:
            source_content = f.read()
        passed = True
        try:
            exec(
                compile(source_content, source_with_id[test_id], "exec"),
                namespace
            )
            for assertion in assertions:
                exec(compile(assertion, "<string>", "exec"), namespace)
        except Exception as e:
            passed = False
            test_result['error'] = {}
            test_result['error']['type'] = type(e).__name__
            test_result['error']['message'] = str(e)
        test_result['passed'] = passed
        test_results.append(test_result)

    with open(sys.argv[3], 'w') as f:
        f.write(json.dumps(test_results, indent=4))
