from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, TYPE_CHECKING

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
    def __str__(self):
        return self.id

@dataclass(frozen=True)
class SourceTask(Task):
    source: str
    origin: SourceOrigin

@dataclass
class TaskResult:
    task: Task
    gate_results: list[GateResult] = field(default_factory=list)
