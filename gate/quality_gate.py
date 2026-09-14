from abc import ABC, abstractmethod
from dataclasses import dataclass

from task import Task
from task.model import TaskId


@dataclass
class GateResult:
    task: TaskId
    source: str
    origin: str
    passed: bool

class QualityGate(ABC):
    @abstractmethod
    def run(self, task: Task) -> GateResult:
        raise NotImplementedError
