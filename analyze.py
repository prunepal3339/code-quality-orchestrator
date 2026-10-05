#!/usr/bin/python3
import json
from pathlib import Path

report = json.loads(Path("report.json").read_text())

syntax_passed_count = 0; execution_passed_count = 0; assertion_passed_count = 0
for item in report:
    for gate_result in item['gate_results']:
        if gate_result['gate_id'] == 'syntax':
            syntax_passed_count += int(gate_result['passed'])
        if gate_result['gate_id'] == 'execution':
            execution_passed_count += int(gate_result['passed'])
        if gate_result['gate_id'] == 'assertion':
            assertion_passed_count += int(gate_result['passed'])

print(
    f"syntax: {syntax_passed_count}\nexecution: {execution_passed_count}\nassertion: {assertion_passed_count}"
)
