from pathlib import Path

from gate import GateRegistry, GateSpecRegistry
from gate.loader import GateSpecificationLoader
from pipeline import PipelineBuilder, PipelineExecutor, PipelineLoader
from pipeline.strategy import (
    PipelineStrategyRegistry,
    StagedExecutionStrategy,
    TaskExecutionStrategy,
)
from runtime.python import PythonAssertionGate, PythonExecutionGate, PythonSyntaxGate
from runtime.python.python_assertion_executor import SpecAssertionExecutor
from task.loader import TaskSpecificationLoader
from task.resolver import TaskSpecificationResolver


def main():
    gate_registry = GateRegistry({
        "python": {
            "syntax": PythonSyntaxGate(),
            "execution": PythonExecutionGate(),
            "assertion": PythonAssertionGate(SpecAssertionExecutor()),
        }
    })
    strategy_registry = PipelineStrategyRegistry({
        "staged": StagedExecutionStrategy(),
        "task": TaskExecutionStrategy()
    })

    gate_specs, bindings = GateSpecificationLoader.load(Path("config/specs.json"))
    gate_spec_registry = GateSpecRegistry(bindings, gate_specs)

    specs = TaskSpecificationLoader.load(Path('config/tasks.json'))
    tasks = TaskSpecificationResolver.resolve(specs)

    conduit = PipelineLoader.load(Path("config/pipeline.json"))
    context = PipelineBuilder(conduit).build()
    results = PipelineExecutor(context, strategy_registry).execute(
        tasks,
        gate_registry,
        gate_spec_registry
    )

    print(results)

if __name__ == "__main__":
    main()
