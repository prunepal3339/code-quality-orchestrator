
from gate import GateExecutor, GateRegistry, GateSpecRegistry
from task import Task

from .builder import PipelineExecutionContext
from .strategy import PipelineStrategyRegistry


class PipelineExecutor:
    def __init__(self,  context: PipelineExecutionContext, strategy_registry: PipelineStrategyRegistry):
        self.context = context
        strategy = self.context.pipeline.get_config('execution.strategy')
        self.strategy = strategy_registry.get(strategy)
    def execute(self, tasks: list[Task], gate_registry: GateRegistry, gate_spec_registry: GateSpecRegistry, gate_executor: GateExecutor):
        return self.strategy.execute(
            self.context,
            tasks,
            gate_registry,
            gate_spec_registry,
            gate_executor,
        )
