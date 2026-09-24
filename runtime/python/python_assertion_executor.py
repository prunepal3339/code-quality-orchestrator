from abc import ABC, abstractmethod
from dataclasses import dataclass

from gate.model import AssertionGateSpecification, AssertionResult, AssertionRuleResult, AssertionSpecification, FunctionAssertionTarget
from runtime.python.python_assertion_gate_old import AssertionGateResult


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

        namespace = context.namespace
        results = []
        assertion_target = spec.target
        if not isinstance(assertion_target, FunctionAssertionTarget):
            raise TypeError(f"Target not implemented for type: {type(assertion_target).__name__}")

        function = namespace.get(assertion_target.name)
        if function is None:
            raise ValueError(f"Target {assertion_target.name} not available for assertion.")
        for rule in spec.rules:
            if rule is None or rule.arguments is None:
                continue
            actual = function(*rule.arguments)

            result = AssertionRuleResult(
                expected=rule.expected,
                actual=actual,
            )
            results.append(result)

        return AssertionResult(results=results)
