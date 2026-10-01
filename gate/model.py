from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from task.model import Task, TaskId

@dataclass
class GateResult:
    gate_id: GateId
    task_id: TaskId
    source: str
    origin: str
    passed: bool
    error: Any = field(default=None, kw_only=True)

type GateId = str

@dataclass
class GateSpecification:
    """
    Configuration supplied for the quality gate.
    """
    id: str
    kind: str

@dataclass
class AssertionSource:
    ...

@dataclass
class FileAssertionSource(AssertionSource):
    path: Path

@dataclass
class TaskAssertionSource(AssertionSource):
    task_id: TaskId

@dataclass
class AssertionTarget:
    ...

@dataclass
class FunctionAssertionTarget(AssertionTarget):
    name: str

@dataclass
class AssertionRule:
    ...

@dataclass
class AssertionRuleResult:
    ...

@dataclass
class PythonAssertionRule(AssertionRule):
    rule: str

@dataclass
class PythonAssertionRuleResult(AssertionRuleResult):
    passed: bool
    error: str | None = None

@dataclass
class ObjectAssertionRule(AssertionRule):
    arguments: list[Any]
    expected: Any

@dataclass
class ObjectAssertionRuleResult(AssertionRuleResult):
    """
    This is mapped one-to-one with AssertionRule.
    For each assertion rule, there exists one assertion rule result.
    """
    expected: Any
    actual: Any
    passed: bool

@dataclass
class AssertionResult:
    """
    This is mapped one-to-one with AssertionSpecification.
    For each specification, there exists one assertion result.
    """
    results: list[AssertionRuleResult] = field(default_factory=list)

@dataclass
class AssertionSpecification:
    rules: list[AssertionRule]
    source: AssertionSource

@dataclass
class ObjectAssertionSpecification(AssertionSpecification):
    target: AssertionTarget

@dataclass
class PythonAssertionSpecification(AssertionSpecification):
    ...

@dataclass
class AssertionGateSpecification(GateSpecification):
    assertions: list[AssertionSpecification]

@dataclass
class AssertionGateResult(GateResult):
    assertion_results: list[AssertionResult]

@dataclass
class GateExecutionContext:
    task: Task
    gate_spec: GateSpecification | None = None
