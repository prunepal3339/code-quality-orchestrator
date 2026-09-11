from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Result Models
# ---------------------------------------------------------------------------

@dataclass
class AssertionResult:
    assertion: str
    passed: bool
    error_type: str | None = None
    error_message: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class AssertionGateResult:
    task_number: int
    source: str
    passed: bool
    total_tests: int
    passed_tests: int
    failed_tests: int
    tests: list[AssertionResult]

    def to_dict(self) -> dict[str, Any]:
        return {
            "task_number": self.task_number,
            "source": self.source,
            "passed": self.passed,
            "total_tests": self.total_tests,
            "passed_tests": self.passed_tests,
            "failed_tests": self.failed_tests,
            "tests": [
                test.to_dict()
                for test in self.tests
            ],
        }


# ---------------------------------------------------------------------------
# Assertion Gate
# ---------------------------------------------------------------------------

class AssertionGate:
    """
    Executes MBPP assertions against source files that have already
    passed the syntax gate.

    Pipeline:

        syntax_result.json
                |
                v
        filter passed == true
                |
                v
        extract Task<number>
                |
                v
        lookup task_number in mbpp.jsonl
                |
                v
        obtain test_list
                |
                v
        execute assertions
                |
                v
        assertion_result.json
    """

    TASK_PATTERN = re.compile(
        r"Task(\d+)\.py$",
        re.IGNORECASE,
    )

    def __init__(
        self,
        mbpp_file: str | Path,
        timeout: int = 10,
    ) -> None:
        self.mbpp_file = Path(mbpp_file)
        self.timeout = timeout

        self._tasks: dict[int, dict[str, Any]] = {}

        self._load_mbpp_dataset()

    # -----------------------------------------------------------------------
    # Dataset loading
    # -----------------------------------------------------------------------

    def _load_mbpp_dataset(self) -> None:
        """
        Load MBPP JSONL and index rows by task_number.

        Expected format:

        {
            "task_number": 23,
            "text": "...",
            "code": "...",
            "test_list": [
                "assert foo(...) == ...",
                "assert foo(...) == ..."
            ]
        }
        """

        if not self.mbpp_file.exists():
            raise FileNotFoundError(
                f"MBPP dataset not found: {self.mbpp_file}"
            )

        with self.mbpp_file.open(
            "r",
            encoding="utf-8",
        ) as file:
            for line_number, line in enumerate(file, start=1):

                line = line.strip()

                if not line:
                    continue

                try:
                    row = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(
                        f"Invalid JSON in MBPP dataset at "
                        f"line {line_number}: {exc}"
                    ) from exc

                if "task_number" not in row:
                    continue

                task_number = self._normalize_task_number(
                    row["task_number"]
                )

                self._tasks[task_number] = row

    # -----------------------------------------------------------------------
    # Public API
    # -----------------------------------------------------------------------

    def run(
        self,
        syntax_result_file: str | Path,
    ) -> list[dict[str, Any]]:
        """
        Run assertions for every source file that passed the syntax gate.
        """

        syntax_result_file = Path(syntax_result_file)

        if not syntax_result_file.exists():
            raise FileNotFoundError(
                f"Syntax result file not found: "
                f"{syntax_result_file}"
            )

        syntax_results = self._load_json(
            syntax_result_file
        )

        if not isinstance(syntax_results, list):
            raise ValueError(
                "Syntax result JSON must contain a list."
            )

        results: list[dict[str, Any]] = []

        for syntax_result in syntax_results:

            # ---------------------------------------------------------------
            # Only process syntax-valid sources.
            # ---------------------------------------------------------------

            if syntax_result.get("passed") is not True:
                continue

            source = syntax_result.get("source")

            if not source:
                continue

            # ---------------------------------------------------------------
            # Extract Task ID
            # ---------------------------------------------------------------

            task_number = self.extract_task_number(source)

            if task_number is None:
                results.append(
                    self._make_gate_error(
                        source=source,
                        task_number=None,
                        error_type="TaskNumberError",
                        error_message=(
                            "Could not extract task number from "
                            f"source path: {source}"
                        ),
                    )
                )

                continue

            # ---------------------------------------------------------------
            # Find corresponding MBPP task
            # ---------------------------------------------------------------

            task = self._tasks.get(task_number)

            if task is None:
                results.append(
                    self._make_gate_error(
                        source=source,
                        task_number=task_number,
                        error_type="TaskNotFoundError",
                        error_message=(
                            f"Task {task_number} was not found "
                            "in the MBPP dataset."
                        ),
                    )
                )

                continue

            # ---------------------------------------------------------------
            # Get test_list
            # ---------------------------------------------------------------

            test_list = task.get("test_list")

            if not isinstance(test_list, list):
                results.append(
                    self._make_gate_error(
                        source=source,
                        task_number=task_number,
                        error_type="TestListError",
                        error_message=(
                            f"Task {task_number} does not contain "
                            "a valid test_list."
                        ),
                    )
                )

                continue

            # ---------------------------------------------------------------
            # Resolve source path
            # ---------------------------------------------------------------

            source_path = Path(source)

            if not source_path.exists():
                results.append(
                    self._make_gate_error(
                        source=source,
                        task_number=task_number,
                        error_type="SourceNotFoundError",
                        error_message=(
                            f"Source file does not exist: "
                            f"{source_path}"
                        ),
                    )
                )

                continue

            # ---------------------------------------------------------------
            # Execute assertions
            # ---------------------------------------------------------------

            result = self._run_task(
                task_number=task_number,
                source=source,
                source_path=source_path,
                test_list=test_list,
            )

            results.append(result.to_dict())

        return results

    # -----------------------------------------------------------------------
    # Task execution
    # -----------------------------------------------------------------------

    def _run_task(
        self,
        task_number: int,
        source: str,
        source_path: Path,
        test_list: list[Any],
    ) -> AssertionGateResult:

        assertion_results: list[AssertionResult] = []

        for assertion in test_list:

            if not isinstance(assertion, str):
                assertion_results.append(
                    AssertionResult(
                        assertion=str(assertion),
                        passed=False,
                        error_type="InvalidAssertion",
                        error_message=(
                            "Assertion must be a string."
                        ),
                    )
                )

                continue

            result = self._execute_assertion(
                source_path=source_path,
                assertion=assertion,
            )

            assertion_results.append(result)

        total_tests = len(assertion_results)

        passed_tests = sum(
            1
            for result in assertion_results
            if result.passed
        )

        failed_tests = total_tests - passed_tests

        return AssertionGateResult(
            task_number=task_number,
            source=source,
            passed=(
                total_tests > 0
                and failed_tests == 0
            ),
            total_tests=total_tests,
            passed_tests=passed_tests,
            failed_tests=failed_tests,
            tests=assertion_results,
        )

    # -----------------------------------------------------------------------
    # Assertion execution
    # -----------------------------------------------------------------------

    def _execute_assertion(
        self,
        source_path: Path,
        assertion: str,
    ) -> AssertionResult:

        """
        Execute one assertion in an isolated Python subprocess.

        The subprocess first executes the generated source and then
        executes the MBPP assertion.

        Example:

            source:
                def add(a, b):
                    return a + b

            assertion:
                assert add(2, 3) == 5
        """

        runner_code = r"""
import json
import sys
import traceback

source_file = sys.argv[1]
assertion = sys.argv[2]

try:
    namespace = {
        "__name__": "__generated__",
        "__file__": source_file,
    }

    with open(
        source_file,
        "r",
        encoding="utf-8",
    ) as file:
        source_code = file.read()

    # Compile first so that syntax/runtime import problems
    # are reported cleanly.
    compiled = compile(
        source_code,
        source_file,
        "exec",
    )

    exec(compiled, namespace)

    # Execute the MBPP assertion against the namespace
    # containing the generated functions/classes.
    exec(
        compile(
            assertion,
            "<mbpp_assertion>",
            "exec",
        ),
        namespace,
    )

    print(
        json.dumps(
            {
                "passed": True,
            }
        )
    )

except AssertionError as exc:
    print(
        json.dumps(
            {
                "passed": False,
                "error_type": "AssertionError",
                "error_message": str(exc),
            }
        )
    )

except Exception as exc:
    print(
        json.dumps(
            {
                "passed": False,
                "error_type": type(exc).__name__,
                "error_message": str(exc),
                "traceback": traceback.format_exc(),
            }
        )
    )
"""

        try:
            process = subprocess.run(
                [
                    sys.executable,
                    "-I",
                    "-c",
                    runner_code,
                    str(source_path),
                    assertion,
                ],
                capture_output=True,
                text=True,
                timeout=self.timeout,
            )

        except subprocess.TimeoutExpired:
            return AssertionResult(
                assertion=assertion,
                passed=False,
                error_type="TimeoutError",
                error_message=(
                    f"Assertion execution exceeded "
                    f"{self.timeout} seconds."
                ),
            )

        except Exception as exc:
            return AssertionResult(
                assertion=assertion,
                passed=False,
                error_type=type(exc).__name__,
                error_message=str(exc),
            )

        stdout = process.stdout.strip()

        if not stdout:
            return AssertionResult(
                assertion=assertion,
                passed=False,
                error_type="RunnerError",
                error_message=(
                    process.stderr.strip()
                    or "Assertion runner produced no output."
                ),
            )

        try:
            result = json.loads(stdout)
        except json.JSONDecodeError:
            return AssertionResult(
                assertion=assertion,
                passed=False,
                error_type="RunnerError",
                error_message=(
                    "Invalid output from assertion runner: "
                    f"{stdout}"
                ),
            )

        if result.get("passed") is True:
            return AssertionResult(
                assertion=assertion,
                passed=True,
            )

        return AssertionResult(
            assertion=assertion,
            passed=False,
            error_type=result.get(
                "error_type",
                "AssertionError",
            ),
            error_message=result.get(
                "error_message"
            ),
        )

    # -----------------------------------------------------------------------
    # Helpers
    # -----------------------------------------------------------------------

    @classmethod
    def extract_task_number(
        cls,
        source: str,
    ) -> int | None:
        """
        Extract task number from paths such as:

            finalized/watermarked/Task23.py
            finalized/unwatermarked/Task23.py
            Task23.py
            /tmp/results/Task123.py
        """

        match = cls.TASK_PATTERN.search(
            Path(source).name
        )

        if not match:
            return None

        return int(match.group(1))

    @staticmethod
    def _normalize_task_number(
        task_number: Any,
    ) -> int:
        try:
            return int(task_number)
        except (TypeError, ValueError) as exc:
            raise ValueError(
                f"Invalid task_number: {task_number!r}"
            ) from exc

    @staticmethod
    def _load_json(
        path: Path,
    ) -> Any:

        with path.open(
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)

    @staticmethod
    def _make_gate_error(
        source: str,
        task_number: int | None,
        error_type: str,
        error_message: str,
    ) -> dict[str, Any]:

        result = {
            "task_number": task_number,
            "source": source,
            "passed": False,
            "total_tests": 0,
            "passed_tests": 0,
            "failed_tests": 0,
            "tests": [],
            "error": {
                "type": error_type,
                "message": error_message,
            },
        }

        return result


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:

    parser = argparse.ArgumentParser(
        description=(
            "Run MBPP assertions against source files "
            "that passed the syntax gate."
        )
    )

    parser.add_argument(
        "syntax_result",
        help=(
            "JSON result produced by the syntax gate."
        ),
    )

    parser.add_argument(
        "--mbpp",
        default="mbpp.jsonl",
        help=(
            "Path to MBPP JSONL dataset "
            "(default: mbpp.jsonl)"
        ),
    )

    parser.add_argument(
        "--output",
        default="assertion_result.json",
        help=(
            "Output JSON file "
            "(default: assertion_result.json)"
        ),
    )

    parser.add_argument(
        "--timeout",
        type=int,
        default=10,
        help=(
            "Maximum execution time for one assertion "
            "in seconds (default: 10)"
        ),
    )

    args = parser.parse_args()

    gate = AssertionGate(
        mbpp_file=args.mbpp,
        timeout=args.timeout,
    )

    results = gate.run(
        syntax_result_file=args.syntax_result,
    )

    output_path = Path(args.output)

    with output_path.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            results,
            file,
            indent=4,
            ensure_ascii=False,
        )

    print(
        f"Assertion gate completed."
    )

    print(
        f"Tasks tested: {len(results)}"
    )

    passed = sum(
        1
        for result in results
        if result.get("passed") is True
    )

    failed = len(results) - passed

    print(
        f"Passed: {passed}"
    )

    print(
        f"Failed: {failed}"
    )

    print(
        f"Result: {output_path}"
    )


if __name__ == "__main__":
    main()
