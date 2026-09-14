from dataclasses import dataclass, field

from gate import GateResult

type TaskId = str

@dataclass(frozen=True)
class Task:
    id: TaskId

@dataclass
class TaskResult:
    task: Task
    gate_results: list[GateResult] = field(default_factory=list)

@dataclass
class TaskExecutionContext:
    task: Task
    results: list[TaskResult] = field(default_factory=list)
