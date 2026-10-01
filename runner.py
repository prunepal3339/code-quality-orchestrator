import argparse
import json
from pathlib import Path

from loader import SpecificationLoader

from gate import GateRegistry
from runtime.python import PythonSyntaxValidator, PythonUnitTestGate

parser = argparse.ArgumentParser(
    description="Run quality gate checks on test specifications."
)
parser.add_argument(
    "spec_path",
    type=str,
    help="Path to the test specifications file."
)
parser.add_argument(
    '--source-dir',
    type=str,
    default= Path.cwd(),
    help="Path to the source directory."
)

parser.add_argument(
    '--output-file',
    type=str,
    default= Path(".") / "result.json",
    help="Path to the output file for reporting."
)

args = parser.parse_args()

registry = GateRegistry({
    "python": {
        "syntax": PythonSyntaxValidator(),
        "unit": PythonUnitTestGate(),
    }
})

loader = SpecificationLoader()
specs = loader.load(Path(args.spec_path))

results = []
for spec in specs:
    try:
        # resolved_source = SourceResolver(root_dir=Path(".").resolve()).resolve(spec.source)
        gate = registry.get(
            kind=spec.kind,
            language=spec.language
        )
        #polymorphic test handling..
        if spec.source['kind'] == 'file' and args.source_dir:
            spec.source['path'] = Path(args.source_dir) / spec.source['path']
        result = gate.run(spec)
        if result is None:
            print(f"ERROR: {spec} is malformed.")
        elif isinstance(result, list):
            results.extend(result)
        else:
            results.append(result)
    except Exception as e: #noqa: BLE001
        print(f"ErRoRR: {spec} failed: {e}")
with open(args.output_file, "w", encoding="utf-8") as f:
    f.write(json.dumps([r.to_dict() for r in results], indent=4))
