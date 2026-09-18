
from gate import GateRegistry
from gate import GateSpecRegistry
from task import Task

from .builder import PipelineExecutionContext
from .strategy import PipelineStrategyRegistry


class PipelineExecutor:
    def __init__(self,  context: PipelineExecutionContext, strategy_registry: PipelineStrategyRegistry):
        self.context = context
        strategy = self.context.pipeline.get_config('execution.strategy')
        self.strategy = strategy_registry.get(strategy)
    def execute(self, tasks: list[Task], gate_registry: GateRegistry, gate_spec_registry: GateSpecRegistry):
        # context = self.context

        # for node_id in context.order:
        #     node = context.pipeline.nodes[node_id]
        #     gate = self.gate_registry.get(language=context.pipeline.get_config("language"), kind=node.gate)

        #     #testing with single task here.
        #     result = gate.run({})
        #     context.set_result(node_id, result)
        # return context # for method chaining.

        return self.strategy.execute(
            self.context,
            tasks,
            gate_registry,
            gate_spec_registry,
        )
