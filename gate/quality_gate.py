from abc import ABC, abstractmethod

from .model import GateSpecification, GateExecutionContext

class QualityGate(ABC):
    @abstractmethod
    def run(self, context: GateExecutionContext) -> "GateResult":
        raise NotImplementedError

    @property
    @abstractmethod
    def id(self) -> "GateId":
        ...
