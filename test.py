from gate.loader import GateSpecificationLoader

loader = GateSpecificationLoader()
specs = loader.load(Path("config/specs.json"))
print(specs)
