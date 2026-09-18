from typing import Protocol

from gate import GateRegistry, GateSpecRegistry, GateExecutionContext
from task import Task, TaskResult

from .builder import PipelineExecutionContext


class PipelineExecutionStrategy(Protocol):
    def execute(
        self,
        context: PipelineExecutionContext,
        tasks: list[Task],
        gate_registry: GateRegistry,
        gate_spec_registry: GateSpecRegistry,
    ) -> list[TaskResult]:
        ...
class PipelineStrategyRegistry:
    def __init__(self, strategies: dict[str, PipelineExecutionStrategy]):
        self.strategies = strategies

    def get(self, name: str):
        strategy = self.strategies.get(name)
        if strategy is None:
            raise ValueError(
                f"No pipeline execution strategy available for "
                f"name={name}"
            )
        return strategy

class StagedExecutionStrategy:
    def execute(
        self,
        context: PipelineExecutionContext,
        tasks: list[Task],
        gate_registry: GateRegistry,
        gate_spec_registry: GateSpecRegistry
    ) -> list[TaskResult]:
        task_results = [
            TaskResult(task_id=task.id) for task in tasks
        ]
        for node_id in context.order:
            node = context.pipeline.nodes.get(node_id)
            if node is None:
                raise ValueError(f"Error while executing pipeline {context.pipeline.name}, no node with id {node_id}")
            gate = gate_registry.get(kind=node.gate, language=context.pipeline.get_config("language"))
            gate_spec = gate_spec_registry.get(node.gate)
            for i, task in enumerate(tasks):
                print(f"Executing gate {node.gate} for task {task.id}")
                task_results[i].gate_results.append(gate.run(GateExecutionContext(task=task, gate_spec=gate_spec)))
        return task_results

class TaskExecutionStrategy:
    def execute(
        self,
        context: PipelineExecutionContext,
        tasks: list[Task],
        gate_registry: GateRegistry,
        gate_spec_registry: GateSpecRegistry
    ) -> list[TaskResult]:
        task_results = [
            TaskResult(task_id=task.id) for task in tasks
        ]

        for i, task in enumerate(tasks):
            for node_id in context.order:
                node = context.pipeline.nodes[node_id]
                if node is None:
                    raise ValueError(f"Error while executing pipeline {context.pipeline.name}, no node with id {node_id}")
                gate = gate_registry.get(kind=node.gate, language=context.pipeline.get_config("language"))
                gate_spec = gate_spec_registry.get(node.gate)
                task_results[i].gate_results.append(gate.run(GateExecutionContext(task=task, gate_spec=gate_spec)))
        return task_results
