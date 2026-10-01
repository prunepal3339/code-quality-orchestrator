from abc import ABC, abstractmethod
from dataclasses import dataclass

from gate.model import (
    AssertionResult,
    AssertionSpecification,
    FunctionAssertionTarget,
    ObjectAssertionRule,
    ObjectAssertionRuleResult,
    PythonAssertionRule,
    PythonAssertionRuleResult,
)


@dataclass
class AssertionExecutionContext:
    ...

@dataclass
class ExecAssertionExecutionContext(AssertionExecutionContext):
    namespace: dict

class AssertionExecutor(ABC):
    @abstractmethod
    def execute(self, spec: AssertionSpecification, context: AssertionExecutionContext) -> AssertionResult:
        ...

class SpecAssertionExecutor(AssertionExecutor):
    def execute(self, spec: AssertionSpecification, context: AssertionExecutionContext) -> AssertionResult:
        if not isinstance(context, ExecAssertionExecutionContext):
            raise TypeError(f"Expected type ExecAssertionExecutionContext, got type {type(context).__name__}")

        results = []

        for rule in spec.rules:
            if isinstance(rule, ObjectAssertionRule):
                namespace = context.namespace
                assertion_target = spec.target
                if not isinstance(assertion_target, FunctionAssertionTarget):
                    raise TypeError(f"Target not implemented for type: {type(assertion_target).__name__}")

                function = namespace.get(assertion_target.name)
                if function is None:
                    raise ValueError(f"Target {assertion_target.name} not available for assertion.")

                if rule is None or rule.arguments is None:
                    continue
                actual = function(*rule.arguments)

                result = ObjectAssertionRuleResult(
                    expected=rule.expected,
                    actual=actual,
                    passed=actual == rule.expected,
                )
                results.append(result)
            try:
                if isinstance(rule, PythonAssertionRule):
                    namespace = context.namespace
                    exec(rule.rule, namespace) #noqa: S102
            except Exception as e: #noqa
                result = PythonAssertionRuleResult(
                    passed=False,
                    error=str(e)
                )
                results.append(result)

        return AssertionResult(results=results)
