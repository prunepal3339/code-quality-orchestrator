from .quality_gate import QualityGate
class GateRegistry:
    def __init__(self, gates: dict):
        self.gates = gates
    def get(
        self,
        kind: str,
        language: str,
    ) -> QualityGate:
        gate = (
            self.gates
            .get(language, {})
            .get(kind)
        )
        if gate is None:
            raise ValueError(
                f"No gate available for "
                f"language={language} "
                f"and kind={kind}"
            )
        return gate
