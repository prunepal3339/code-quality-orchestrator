from dataclasses import dataclass
from typing import Any


@dataclass
class GateResult:
    gate_id: "GateId"
    task_id: "TaskId"
    source: str
    origin: str
    passed: bool
    error: Any = None

type GateId = str
