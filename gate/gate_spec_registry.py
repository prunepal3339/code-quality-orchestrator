from .model import GateId
from .model import GateSpecification
class GateSpecRegistry:
    def __init__(self, bindings: dict, gate_specs: dict[str, GateSpecification]):
        self.bindings = bindings
        self.gate_specs = gate_specs
    def get(
        self,
        gate_id: GateId
    ) -> GateSpecification:
        gate_spec = (
            self.bindings
            .get(gate_id)
        )
        return self.gate_specs.get(gate_spec)
