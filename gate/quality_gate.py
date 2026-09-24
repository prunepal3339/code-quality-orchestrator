from abc import ABC, abstractmethod

from .model import GateExecutionContext, GateId, GateResult


class QualityGate(ABC):
    @abstractmethod
    def run(self, context: GateExecutionContext) -> GateResult:
        raise NotImplementedError

    @property
    @abstractmethod
    def id(self) -> GateId:
        ...
