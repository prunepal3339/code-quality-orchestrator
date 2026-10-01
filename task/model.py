from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from gate.model import GateResult

type TaskId = str

@dataclass(frozen=True)
class SourceOrigin:
    ...
@dataclass(frozen=True)
class StringSourceOrigin(SourceOrigin):
    ...

@dataclass(frozen=True)
class FileSourceOrigin(SourceOrigin):
    path: Path

@dataclass(frozen=True)
class Task:
    id: TaskId

@dataclass(frozen=True)
class SourceTask(Task):
    source: str
    origin: SourceOrigin

@dataclass
class TaskResult:
    task_id: TaskId
    gate_results: list[GateResult] = field(default_factory=list)

#delete me if you find no reference of me in future use case..
@dataclass
class TaskExecutionContext:
    task: Task
    results: list[TaskResult] = field(default_factory=list)

@dataclass(frozen=True)
class TaskSpecification:
    id: TaskId
    kind: str

@dataclass(frozen=True)
class SourceTaskSpecification(TaskSpecification):
    source_type: str
    value: Any # polymorphic value based on the source_type.
