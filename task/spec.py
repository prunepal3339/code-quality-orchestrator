from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING

from .model import TaskId

@dataclass(frozen=True)
class TaskSpecification(ABC):
    id: TaskId
    kind: str

@dataclass(frozen=True)
class SourceTaskSpecification(TaskSpecification):
    source_type: str
    value: Any # polymorphic value based on the source_type.