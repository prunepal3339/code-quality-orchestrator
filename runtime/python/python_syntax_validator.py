from gate import SyntaxValidator

from framework import (
    TestSpecification,
    SyntaxTestResult,
)

import py_compile

class PythonSyntaxValidator(SyntaxValidator):

    def run(
        self,
        spec: TestSpecification,
    ) -> SyntaxTestResult:

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

        raise ValueError(
            f"Unsupported source kind: "
            f"{spec.source['kind']}"
        )

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
                spec.expect,
                compile_error={
                    "type": "SyntaxError",
                    "message": str(e),
                    "line": e.lineno,
                    "column": e.offset,
                    "text": e.text.strip()
                    if e.text
                    else None,
                },
            )

        return self.result(
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
                spec.expect,
                compile_error={
                    "type": "PyCompileError",
                    "message": str(e),
                },
            )

        return self.result(
            spec.expect,
            compile_error=None,
        )

    def result(
        self,
        expect: str,
        compile_error: dict | None,
    ) -> SyntaxTestResult:

        if expect == "valid":

            if compile_error:

                return SyntaxTestResult(
                    passed=False,
                    expected="valid",
                    actual="invalid",
                    error=compile_error,
                )

            return SyntaxTestResult(
                passed=True,
                expected="valid",
                actual="valid",
            )

        if expect == "invalid":

            if compile_error:

                return SyntaxTestResult(
                    passed=True,
                    expected="invalid",
                    actual="invalid",
                    error=compile_error,
                )

            return SyntaxTestResult(
                passed=False,
                expected="invalid",
                actual="valid",
            )

        raise ValueError(
            f"Unsupported expectation: {expect}"
        )
