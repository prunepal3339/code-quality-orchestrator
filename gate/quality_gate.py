from abc import ABC, abstractmethod


class GateResult:
    pass
class QualityGate(ABC):
    @abstractmethod
    def run(self, spec) -> GateResult:
        raise NotImplementedError
