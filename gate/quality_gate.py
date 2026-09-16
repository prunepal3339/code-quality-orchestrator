from abc import ABC, abstractmethod

from .model import GateSpecification

class QualityGate(ABC):
    @abstractmethod
    def run(self, task: "Task", spec: GateSpecification | None = None) -> "GateResult":
        raise NotImplementedError

    @property
    @abstractmethod
    def id(self) -> "GateId":
        ...
