from abc import ABC, abstractmethod
from framework import TestResult
class QualityGate(ABC):
    @abstractmethod
    def run(self, spec) -> TestResult | list[TestResult]:
        raise NotImplementedError
