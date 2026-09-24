from typing import Protocol

from gate import GateExecutionContext, GateRegistry, GateSpecRegistry
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
                when_condition = context.pipeline.get_config("transition.when")
                if is_executable(task_results[i].gate_results, when_condition):
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
            when_condition = context.pipeline.get_config("transition.when")
            for node_id in context.order:
                node = context.pipeline.nodes[node_id]
                if node is None:
                    raise ValueError(f"Error while executing pipeline {context.pipeline.name}, no node with id {node_id}")
                gate = gate_registry.get(kind=node.gate, language=context.pipeline.get_config("language"))
                gate_spec = gate_spec_registry.get(node.gate)

                if is_executable(task_results[i].gate_results, when_condition):
                    task_results[i].gate_results.append(gate.run(GateExecutionContext(task=task, gate_spec=gate_spec)))
        return task_results

def is_executable(results, condition):
    for result in results:
        for field, expected in condition.items():
            actual = getattr(result, field)
            if expected != actual:
                return False
    return True
