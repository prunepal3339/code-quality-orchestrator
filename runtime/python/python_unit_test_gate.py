from typing import Any
from gate import QualityGate
from framework import (
    UnitTestSpec,
    UnitTestResult,
    AssertionResult,
)

class PythonUnitTestGate(QualityGate):
    def run(
        self,
        spec: UnitTestSpec,
    ) -> UnitTestResult:

        source = spec.source["kind"]
        if source == "file":
            source = spec.source["path"]
        if source  == "string":
            source = spec.source["content"]

        target = spec.target["kind"]
        if target == "function":
            target = f"{target}: {spec.target["name"]}"
        try:
            function = self.load_target(spec)
            # if there exists at least one assertion.
            if len(spec.assertions) > 0:
                args = spec.assertions[0]['args']
                result = function(*args) # check whether function works or not.
        except Exception as e:
            return UnitTestResult(
                passed=False,
                status="error",
                source=source,
                target=target,
                error={
                    "type": type(e).__name__,
                    "message": str(e),
            })
        assertion_results = []
        for assertion in spec.assertions:
            result = self.run_assertion(
                function,
                assertion,
            )

            assertion_results.append(result)

        passed = all(
            result.passed
            for result in assertion_results
        )

        status = "success"
        if not passed:
            status = "failure"

        return UnitTestResult(
            passed=passed,
            status=status,
            source=source,
            target=target,
            assertions=assertion_results,
        )
    def load_target(
        self,
        spec: UnitTestSpec,
    ):
        source = self.load_source(
            spec.source
        )
        target = spec.target
        if target["kind"] != "function":
            raise ValueError(
                f"Unsupported target kind: "
                f"{target['kind']}"
            )
        namespace = {}
        exec(
            compile(
                source,
                "<source>",
                "exec",
            ),
            namespace,
        )
        function_name = target["name"]
        function = namespace.get(
            function_name
        )
        if function is None:
            raise ValueError(
                f"Function '{function_name}' "
                f"not found in source"
            )
        return function

    def load_source(
        self,
        source: dict[str, Any],
    ) -> str:
        if source["kind"] == "string":
            return source["content"]
        if source["kind"] == "file":
            with open(
                source["path"],
                "r",
                encoding="utf-8",
            ) as file:
                return file.read()
        raise ValueError(
            f"Unsupported source kind: "
            f"{source['kind']}"
        )
    def run_assertion(
        self,
        function,
        assertion: dict[str, Any],
    ) -> AssertionResult:
        args = assertion["args"]
        expected = assertion["expect"]
        try:
            actual = function(*args)
            passed = actual == expected
            return AssertionResult(
                args=args,
                expected=expected,
                actual=actual,
                passed=passed,
            )
        except Exception as error:
            return AssertionResult(
                args=args,
                expected=expected,
                actual=None,
                passed=False,
                error={
                    "type": type(error).__name__,
                    "message": str(error),
                },
            )
