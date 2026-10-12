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
    passed: bool
    source: str = field(default='', kw_only=True)
    origin: str = field(default='', kw_only=True)
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
class GateConfig:
    config: dict[str, Any] = field(default_factory=dict)
    fallback: dict[str, Any] = field(default_factory=dict)
    def get(self, config_key: str, default: Any = None) -> Any:
        return self.config.get(config_key, self.fallback.get(config_key, default))
    def get_config(self, config_key: str,default: Any = None) -> Any:
        value = self.config
        for key in config_key.split("."):
            value = value.get(key)
        return value if value is not None else default

    def get_timeout(self, config_key: str = "timeout", default_seconds: float = 5.0) -> float:
        """
        Retrieves the timeout dictionary block and resolves into the float value representing seconds.
        Defaults: { config_key: "timeout", default_seconds: 5.0 }
        """
        try:
            timeout_block = self.get_config(config_key)
            if not isinstance(timeout_block, dict):
                return float(timeout_block)
            
            microseconds = timeout_block.get("microseconds", 0) + timeout_block.get("nanoseconds", 0) / 1000
            duration = timedelta(
                seconds=timeout_block.get("seconds", 0),
                milliseconds=timeout_block.get("milliseconds", 0),
                microseconds=microseconds
            )
            return duration.total_seconds()
        except (KeyError, TypeError, ValueError):
            return default_seconds

@dataclass
class GateExecutionContext:
    task: Task
    gate_spec: GateSpecification | None = None
    config: GateConfig = field(default_factory=GateConfig)