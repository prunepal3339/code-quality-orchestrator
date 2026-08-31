from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from abc import ABC, abstractmethod

@dataclass
class TestSpecification(ABC):
    kind: str
    language: str

@dataclass
class TestResult(ABC):
    passed: bool
    source: str

@dataclass
class SyntaxTestSpec(TestSpecification):
    source: dict[str, Any]
    expect: str
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "TestSpecification":
        return cls(
            kind=data["kind"],
            language=data["language"],
            source=data["source"],
            expect=data["expect"],
        )

@dataclass
class SyntaxTestResult(TestResult):
    expected: str
    actual: str
    error: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        result = {
            "passed": self.passed,
            "source": str(self.source),
            "expected": self.expected,
            "actual": self.actual,
        }
        if self.error is not None:
            result["error"] = self.error
        return result

@dataclass
class UnitTestSpec(TestSpecification):
    source: dict[str, Any]
    target: dict[str, Any]
    assertions: list[dict[str, Any]]

@dataclass
class AssertionResult:
    args: list[Any]
    expected: Any
    actual: Any
    passed: bool
    error: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        result = {
            "args": self.args,
            "expected": self.expected,
            "actual": self.actual,
            "passed": self.passed,
        }

        if self.error is not None:
            result["error"] = self.error

        return result

@dataclass
class UnitTestResult(TestResult):
    target: str
    assertions: list[AssertionResult] = field(default_factory=list)
    status: str = "success"
    error: dict[str, Any] | None = None

    @property
    def total(self) -> int:
        return len(self.assertions)

    @property
    def passed_count(self) -> int:
        return sum(
            assertion.passed
            for assertion in self.assertions
        )

    @property
    def failed_count(self) -> int:
        return self.total - self.passed_count

    def to_dict(self) -> dict[str, Any]:
        result = {
            "passed": self.passed,
            "status": self.status,
            "total": self.total,
            "passed_count": self.passed_count,
            "failed_count": self.failed_count,
            "source": str(self.source),
            "target": str(self.target),
        }
        if self.assertions:
            result["assertions"] = [
                assertion.to_dict()
                for assertion in self.assertions
            ]
        if self.error is not None:
            result["error"] = self.error
        return result
