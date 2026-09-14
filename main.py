from pathlib import Path

from gate import GateRegistry
from pipeline import PipelineBuilder, PipelineExecutor, PipelineLoader
from pipeline.strategy import (
    PipelineStrategyRegistry,
    StagedExecutionStrategy,
    TaskExecutionStrategy,
)
from runtime.python import PythonSyntaxValidator, PythonUnitTestGate
from task import Task


def main():
    gate_registry = GateRegistry({
        "python": {
            "syntax": PythonSyntaxValidator(),
            "unit": PythonUnitTestGate(),
        }
    })
    strategy_registry = PipelineStrategyRegistry({
        "staged": StagedExecutionStrategy(),
        "task": TaskExecutionStrategy()
    })
    conduit = PipelineLoader.load(Path("config/pipeline.json"))
    context = PipelineBuilder(conduit).build()
    results = PipelineExecutor(context, strategy_registry).execute([
        Task("Task#1"),
        Task("Task#2"),
        Task("Task#3")
    ], gate_registry)
    print(results)
if __name__ == "__main__":
    main()
