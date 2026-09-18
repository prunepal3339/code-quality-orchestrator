from dataclasses import dataclass, field
from typing import Any
from pathlib import Path


@dataclass
class GateResult:
    gate_id: "GateId"
    task_id: "TaskId"
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
class AssertionTarget:
    ...

@dataclass
class FunctionAssertionTarget(AssertionTarget):
    name: str

@dataclass
class AssertionRule:
    arguments: dict[str, Any]
    expected: Any

@dataclass
class AssertionResult:
    expected: Any
    actual: Any


@dataclass
class AssertionSpecification:
    source: AssertionSource
    target: AssertionTarget
    rules: list[AssertionRule]

@dataclass
class AssertionGateSpecification(GateSpecification):
    assertions: list[AssertionSpecification]

@dataclass
class AssertionGateResult(GateResult):
    assertion_results: list[AssertionResult]

@dataclass
class GateExecutionContext:
    task: "Task"
    gate_spec: GateSpecification | None = None
