from gate import GateResult, QualityGate, GateExecutionContext
from task import SourceTask, Task
from task.model import FileSourceOrigin, StringSourceOrigin

from gate.model import AssertionGateSpecification

#Dummy assertion gate.
class PythonAssertionGate(QualityGate):

    @property
    def id(self) -> "GateId":
        return "assertion"

    def run(
        self,
        context: GateExecutionContext
    ) -> GateResult:
        task = context.task
        if not isinstance(task, SourceTask):
            raise TypeError(f"Task is not specified {type(task).__name__}")
        source = task.source
        assertions = []
        if isinstance(task.origin, FileSourceOrigin):
            origin = str(task.origin.path)
        elif isinstance(task.origin, StringSourceOrigin):
            origin = "<string>"
        else:
            origin = "<unknown>"
        try:
            print(context.gate_spec)
            print("---exitt---")
            import sys;sys.exit(0)
            namespace = {}

            exec(compile(source, origin, "exec"), namespace) #noqa: S102

            for assertion in assertions:
                exec(compile(assertion, "<string>", "exec"), namespace) #noqa: S102

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
        except AssertionError as e:
            return GateResult(
                gate_id=self.id,
                task_id=task.id,
                passed=False,
                origin=origin,
                source=source,
                error = str(e),
            )
