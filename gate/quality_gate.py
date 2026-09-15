from abc import ABC, abstractmethod


class QualityGate(ABC):
    @abstractmethod
    def run(self, task: "Task") -> "GateResult":
        raise NotImplementedError

    @property
    @abstractmethod
    def id(self) -> "GateId":
        ...
