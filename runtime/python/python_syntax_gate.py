
from gate import GateResult, QualityGate
from task import SourceTask, Task
from task.model import FileSourceOrigin, StringSourceOrigin


class PythonSyntaxGate(QualityGate):

    @property
    def id(self) -> "GateId":
        return "syntax"

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
                gate_id=self.id,
                task_id=task.id,
                source=source,
                origin=origin,
                passed=True
            )
        except SyntaxError as e:
            return GateResult(
                gate_id=self.id,
                task_id=task.id,
                origin=origin,
                source=source,
                passed=False,
                error = str(e),
            )
        except TypeError as e:
            return GateResult(
                gate_id=self.id,
                task_id=task.id,
                passed=False,
                origin=origin,
                source=source,
                error = str(e),
            )
