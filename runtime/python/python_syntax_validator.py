import py_compile
from pathlib import Path

from framework import (
    SyntaxTestResult,
    TestSpecification,
)
from gate import GateResult, QualityGate
from task import Task, SourceTask
from task.model import FileSourceOrigin, StringSourceOrigin

class PythonSyntaxGate(QualityGate):
    def run(
        self,
        task: Task
    ) -> GateResult:
        if not isinstance(task, SourceTask):
            raise TypeError(f"Task is not specified {type(task).__name__}")
        source = task.source
        if isinstance(task.origin, FileSourceOrigin):
            origin = str(task.origin.path)
        elif isinstance(task.origin, StringSourceOrigin):
            origin = "<string>"
        else:
            origin = "<unknown>"
        try:
            compile(
                source,
                origin,
                "exec"
            )
            return GateResult(
                task=task.id,
                source=source,
                origin=origin,
                passed=True
            )
        except SyntaxError as e:
            return GateResult(
                task=task.id,
                origin=origin,
                source=source,
                passed=False
            )
        except Exception as e:
            return GateResult(
                task=task.id,
                passed=False,
                origin=origin,
                source=source
            )
