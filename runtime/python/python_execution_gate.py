from gate import GateExecutionContext, GateResult, QualityGate
from gate.model import GateId
from task import SourceTask
from task.model import FileSourceOrigin, StringSourceOrigin


class PythonExecutionGate(QualityGate):

    @property
    def id(self) -> GateId:
        return "execution"

    def run(
        self,
        context: GateExecutionContext
    ) -> GateResult:
        task = context.task
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
            namespace = {}

            executable_code = compile(
                source,
                origin,
                "exec"
            )

            exec(executable_code, namespace) #noqa: S102
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
                source=source,
                origin=origin,
                passed=False,
                error = str(e),
            )
        except TypeError as e:
            return GateResult(
                gate_id=self.id,
                task_id=task.id,
                source=source,
                origin=origin,
                passed=False,
                error = str(e),
            )
        except Exception as e: #noqa: BLE001
            return GateResult(
                gate_id=self.id,
                task_id=task.id,
                source=source,
                origin=origin,
                passed=False,
                error = str(e)
            )
        except SystemExit as e:
            return GateResult(
                gate_id=self.id,
                task_id=task.id,
                source=source,
                origin=origin,
                passed=False,
                error=str(e)
            )
