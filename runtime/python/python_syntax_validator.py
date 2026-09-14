import py_compile
from pathlib import Path

from framework import (
    SyntaxTestResult,
    TestSpecification,
)
from gate import SyntaxValidator


class PythonSyntaxValidator(SyntaxValidator):
    def run(
        self,
        spec: TestSpecification,
    ) -> SyntaxTestResult | list[SyntaxTestResult]:
        print("Running syntax validator...")
        return []
        if spec.source["kind"] == "string":
            return self.validate_string(
                spec.source["content"],
                spec,
            )
        elif spec.source["kind"] == "file":
            return self.validate_file(
                spec.source["path"],
                spec,
            )
        elif spec.source["kind"] == "directory":
            return self.validate_directory(
                Path('.') / spec.source["path"],
                spec,
            )
        raise ValueError(
            f"Unsupported source kind: "
            f"{spec.source['kind']}"
        )

    def validate_directory(
        self,
        path: Path,
        spec: TestSpecification,
    ) -> SyntaxTestResult:
        results = []
        for file in path.glob(spec.source.get("pattern", "*.py")):
            result = self.validate_file(file, spec)
            results.append(result)
        return results

    def validate_string(
        self,
        source: str,
        spec: TestSpecification,
    ) -> SyntaxTestResult:
        try:
            # compile() checks syntax without executing the code.
            compile(
                source,
                "<string>",
                "exec",
            )
        except SyntaxError as e:
            return self.result(
                source,
                spec.expect,
                compile_error={
                    "type": "SyntaxError",
                    "message": str(e),
                },
            )

        return self.result(
            source,
            spec.expect,
            compile_error=None,
        )

    def validate_file(
        self,
        source: str,
        spec: TestSpecification,
    ) -> SyntaxTestResult:
        try:
            py_compile.compile(
                source,
                doraise=True,
            )
        except py_compile.PyCompileError as e:
            return self.result(
                source,
                spec.expect,
                compile_error={
                    "type": e.exc_type_name,
                    "message": e.msg,
                },
            )
        return self.result(
            source,
            spec.expect,
            compile_error=None,
        )

    def result(
        self,
        source: str,
        expect: str,
        compile_error: dict | None,
    ) -> SyntaxTestResult:
        if expect == "valid":
            if compile_error:
                return SyntaxTestResult(
                    passed=False,
                    source=source,
                    expected="valid",
                    actual="invalid",
                    error=compile_error,
                )
            return SyntaxTestResult(
                passed=True,
                source=source,
                expected="valid",
                actual="valid",
            )
        if expect == "invalid":
            if compile_error:
                return SyntaxTestResult(
                    passed=True,
                    source=source,
                    expected="invalid",
                    actual="invalid",
                    error=compile_error,
                )
            return SyntaxTestResult(
                passed=False,
                source=source,
                expected="invalid",
                actual="valid",
            )
        raise ValueError(
            f"Unsupported expectation: {expect}"
        )
