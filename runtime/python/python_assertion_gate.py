from pathlib import Path

from gate import GateExecutionContext, GateResult, QualityGate
from gate.model import AssertionGateResult, AssertionGateSpecification, GateId
from runtime.python.python_assertion_executor import ExecAssertionExecutionContext
from task import SourceTask
from task.model import FileSourceOrigin, StringSourceOrigin


class MissingSpecificationError(ValueError):
    pass

class PythonAssertionGate(QualityGate):

    def __init__(self, executor):
        self.executor = executor

    @property
    def id(self) -> GateId:
        return "assertion"

    def run(
        self,
        context: GateExecutionContext
    ) -> GateResult:
        task = context.task
        if not isinstance(task, SourceTask):
            raise TypeError(f"Expected type SourceTask, got type {type(task).__name__}")
        source = task.source
        spec = context.gate_spec
        if spec is None:
            raise MissingSpecificationError(f"Gate specification missing for assertion gate for task {task.id}.")
        if not isinstance(spec, AssertionGateSpecification):
            raise TypeError(f"Expected type AssertionGateSpecification, got type {type(spec).__name__}")
        if isinstance(task.origin, FileSourceOrigin):
            origin = str(task.origin.path)
        elif isinstance(task.origin, StringSourceOrigin):
            origin = "<string>"
        else:
            origin = "<unknown>"
        try:
            namespace = {}

            exec(compile(source, origin, "exec"), namespace) #noqa: S102

            results = []

            origin_path = Path(origin)
            original_task_id = origin_path.stem.removeprefix("task_")

            for assertion in spec.assertions:
                if int(assertion.source.task_id) != int(original_task_id):
                    continue
                result = self.executor.execute(assertion, ExecAssertionExecutionContext(namespace=namespace))
                results.append(result)
                break
            passed = True
            for result in results:
                for assertion_result in result.results:
                    if not assertion_result.passed:
                        passed = False
                        break

            return AssertionGateResult(
                gate_id=self.id,
                task_id=task.id,
                source=source,
                origin=origin,
                passed=passed,
                assertion_results=results
            )
        except SyntaxError as e:
            return GateResult(
                gate_id=self.id,
                task_id=task.id,
                origin=origin,
                source=source,
                passed=False,
                error = e,
            )
        except TypeError as e:
            return GateResult(
                gate_id=self.id,
                task_id=task.id,
                passed=False,
                origin=origin,
                source=source,
                error = e,
            )
        except AssertionError as e:
            return GateResult(
                gate_id=self.id,
                task_id=task.id,
                passed=False,
                origin=origin,
                source=source,
                error = e,
            )
        except Exception as e: #noqa: BLE001
            return GateResult(
                gate_id=self.id,
                task_id=task.id,
                passed=False,
                origin=origin,
                source=source,
                error = e,
            )
        except SystemExit as e:
            return GateResult(
                gate_id=self.id,
                task_id=task.id,
                passed=False,
                origin=origin,
                source=source,
                error = e,
            )
