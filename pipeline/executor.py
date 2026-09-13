from .model import NodeId
from gate import GateRegistry

class PipelineExecutor:
    def __init__(self, gate_registry: GateRegistry):
        self.gate_registry = gate_registry
    def execute(self, context: PipelineExecutionContext) -> Any:
        for node_id in context.order:
            gate = self.gate_registry.get(node_id)
            result = gate.execute()
            context.set_result(node_id, result)
        return None
