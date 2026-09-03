#!/usr/bin/env python3
from __future__ import annotations

import ast
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
TESTS_DIR = ROOT / "tests" / "claude"
SOURCES_DIR = ROOT / "sources" / "synthid" / "unwatermarked"
OUTPUT_PATH = ROOT / "unit-spec-v4.json"

NAME_RE = re.compile(r"^\s*(def|class)\s+([A-Za-z_][A-Za-z0-9_]*)", re.MULTILINE)
TASK_DIR_RE = re.compile(r"Task(\d+)_")


def path_for_json(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def try_parse(path: Path) -> ast.AST | None:
    try:
        return ast.parse(read_text(path))
    except SyntaxError:
        return None


def list_task_numbers() -> list[int]:
    numbers = []
    for path in SOURCES_DIR.glob("task_*.py"):
        try:
            numbers.append(int(path.stem.split("_")[1]))
        except Exception:
            continue
    return sorted(numbers)


def find_test_file(task_number: int) -> Path | None:
    matches = sorted(TESTS_DIR.glob(f"Task{task_number}_CLAUDE_*/*.py"))
    if not matches:
        return None
    primary = [p for p in matches if p.name.startswith(f"Task{task_number}_")]
    return primary[0] if primary else matches[0]


def extract_source_symbols(path: Path) -> dict[str, list[str]]:
    text = read_text(path)
    tree = try_parse(path)
    functions: list[str] = []
    classes: list[str] = []

    if tree is not None:
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                functions.append(node.name)
            elif isinstance(node, ast.ClassDef):
                classes.append(node.name)
    else:
        for kind, name in NAME_RE.findall(text):
            if kind == "def":
                functions.append(name)
            elif kind == "class":
                classes.append(name)

    seen_f = []
    for name in functions:
        if name not in seen_f and not name.startswith("test"):
            seen_f.append(name)
    seen_c = []
    for name in classes:
        if name not in seen_c and not name.startswith("Test"):
            seen_c.append(name)
    return {"functions": seen_f, "classes": seen_c}


def constant_value(node: ast.AST) -> Any:
    try:
        return ast.literal_eval(node)
    except Exception:
        return None


def is_self_assert_call(node: ast.AST) -> bool:
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "self"
        and node.func.attr.startswith("assert")
    )


def expr_to_ref(node: ast.AST, aliases: dict[str, str]) -> str | None:
    if isinstance(node, ast.Name):
        return aliases.get(node.id, node.id)
    if isinstance(node, ast.Attribute):
        text = ast.unparse(node)
        for key, value in sorted(aliases.items(), key=lambda item: -len(item[0])):
            if text == key:
                return value
            if text.startswith(key + "."):
                return value + text[len(key):]
        return text
    return None


def expr_to_jsonish(node: ast.AST, aliases: dict[str, str]) -> Any:
    value = constant_value(node)
    if value is not None or isinstance(node, ast.Constant):
        return value
    if isinstance(node, ast.Call):
        return {
            "call": call_to_step(node, aliases),
        }
    ref = expr_to_ref(node, aliases)
    if ref is not None:
        return {"ref": ref}
    return {"expr": ast.unparse(node)}


def call_target_parts(node: ast.Call, aliases: dict[str, str]) -> tuple[str | None, str | None]:
    func = node.func
    if isinstance(func, ast.Name):
        return aliases.get(func.id, func.id), None
    if isinstance(func, ast.Attribute):
        base = expr_to_ref(func.value, aliases)
        if base is None:
            base = ast.unparse(func.value)
        return base, func.attr
    return None, None


def call_to_step(node: ast.Call, aliases: dict[str, str], save_as: str | None = None, target_class: str | None = None) -> dict[str, Any]:
    target, method = call_target_parts(node, aliases)
    step: dict[str, Any] = {
        "action": "call",
        "args": [expr_to_jsonish(arg, aliases) for arg in node.args],
    }
    if node.keywords:
        step["kwargs"] = {
            kw.arg if kw.arg is not None else "**": expr_to_jsonish(kw.value, aliases)
            for kw in node.keywords
        }

    if method is None:
        if target_class is not None and target == target_class:
            step["action"] = "construct"
            step["target"] = target_class
        else:
            step["target"] = target
    else:
        step["on"] = target
        step["method"] = method

    if save_as is not None:
        step["save_as"] = save_as
    return step


def stmt_to_steps(stmt: ast.stmt, aliases: dict[str, str], target_class: str | None) -> list[dict[str, Any]]:
    steps: list[dict[str, Any]] = []

    if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1:
        target = stmt.targets[0]
        save_as = None
        if isinstance(target, ast.Name):
            save_as = target.id
            aliases[target.id] = save_as
        elif isinstance(target, ast.Attribute):
            target_text = ast.unparse(target)
            if target_text.startswith("self."):
                save_as = target.attr
                aliases[target_text] = save_as

        if isinstance(stmt.value, ast.Call):
            steps.append(call_to_step(stmt.value, aliases, save_as=save_as, target_class=target_class))
            return steps

        if save_as is not None:
            steps.append({
                "action": "assign",
                "name": save_as,
                "value": expr_to_jsonish(stmt.value, aliases),
            })
            return steps

    if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
        call = stmt.value
        if isinstance(call.func, ast.Attribute):
            text = ast.unparse(call.func)
            if text == "time.sleep" and call.args:
                seconds = constant_value(call.args[0])
                steps.append({"action": "sleep", "seconds": seconds})
                return steps
        steps.append(call_to_step(call, aliases, target_class=target_class))
        return steps

    if isinstance(stmt, ast.Assert):
        return steps

    steps.append({
        "action": "raw",
        "code": ast.unparse(stmt),
    })
    return steps


def assert_call_to_check(call: ast.Call, aliases: dict[str, str]) -> dict[str, Any] | None:
    kind = call.func.attr
    args = call.args

    if kind == "assertEqual" and len(args) >= 2:
        return {"kind": "equals", "actual": expr_to_jsonish(args[0], aliases), "expected": expr_to_jsonish(args[1], aliases)}
    if kind == "assertNotEqual" and len(args) >= 2:
        return {"kind": "not_equals", "actual": expr_to_jsonish(args[0], aliases), "expected": expr_to_jsonish(args[1], aliases)}
    if kind == "assertTrue" and len(args) >= 1:
        return {"kind": "truthy", "actual": expr_to_jsonish(args[0], aliases)}
    if kind == "assertFalse" and len(args) >= 1:
        return {"kind": "falsy", "actual": expr_to_jsonish(args[0], aliases)}
    if kind == "assertIsNone" and len(args) >= 1:
        return {"kind": "is_none", "actual": expr_to_jsonish(args[0], aliases)}
    if kind == "assertIsNotNone" and len(args) >= 1:
        return {"kind": "is_not_none", "actual": expr_to_jsonish(args[0], aliases)}
    if kind == "assertIn" and len(args) >= 2:
        return {"kind": "in", "member": expr_to_jsonish(args[0], aliases), "container": expr_to_jsonish(args[1], aliases)}
    if kind == "assertNotIn" and len(args) >= 2:
        return {"kind": "not_in", "member": expr_to_jsonish(args[0], aliases), "container": expr_to_jsonish(args[1], aliases)}
    if kind == "assertGreater" and len(args) >= 2:
        return {"kind": "greater", "left": expr_to_jsonish(args[0], aliases), "right": expr_to_jsonish(args[1], aliases)}
    if kind == "assertIsInstance" and len(args) >= 2:
        return {"kind": "is_instance", "actual": expr_to_jsonish(args[0], aliases), "expected_type": expr_to_jsonish(args[1], aliases)}
    if kind == "assertAlmostEqual" and len(args) >= 2:
        result = {"kind": "almost_equals", "actual": expr_to_jsonish(args[0], aliases), "expected": expr_to_jsonish(args[1], aliases)}
        for kw in call.keywords:
            if kw.arg == "places":
                result["places"] = constant_value(kw.value)
        return result
    return {"kind": "raw_assert", "expr": ast.unparse(call)}


def bare_assert_to_check(node: ast.Assert, aliases: dict[str, str]) -> dict[str, Any] | None:
    test = node.test
    if isinstance(test, ast.Compare) and len(test.ops) == 1 and len(test.comparators) == 1:
        op = test.ops[0]
        left = expr_to_jsonish(test.left, aliases)
        right = expr_to_jsonish(test.comparators[0], aliases)
        if isinstance(op, ast.Eq):
            return {"kind": "equals", "actual": left, "expected": right}
        if isinstance(op, ast.NotEq):
            return {"kind": "not_equals", "actual": left, "expected": right}
        if isinstance(op, ast.Is):
            return {"kind": "is", "actual": left, "expected": right}
        if isinstance(op, ast.IsNot):
            return {"kind": "is_not", "actual": left, "expected": right}
        if isinstance(op, ast.In):
            return {"kind": "in", "member": left, "container": right}
        if isinstance(op, ast.NotIn):
            return {"kind": "not_in", "member": left, "container": right}
        if isinstance(op, ast.Gt):
            return {"kind": "greater", "left": left, "right": right}
    return {"kind": "raw_assert", "expr": ast.unparse(test)}


def simplify_direct_function_case(case: dict[str, Any], target_name: str) -> dict[str, Any] | None:
    steps = case.get("steps", [])
    checks = case.get("checks", [])

    if len(steps) == 1 and len(checks) == 1:
        step = steps[0]
        check = checks[0]
        if step.get("action") == "call" and step.get("target") == target_name and check.get("kind") == "equals":
            actual = check.get("actual")
            if actual == {"ref": step.get("save_as")}:
                return {
                    "name": case["name"],
                    "args": step.get("args", []),
                    "expect": check.get("expected"),
                }

    if not steps and len(checks) == 1:
        check = checks[0]
        if check.get("kind") != "equals":
            return None
        actual = check.get("actual")
        if not isinstance(actual, dict):
            return None
        call = actual.get("call")
        if not isinstance(call, dict):
            return None
        if call.get("action") != "call" or call.get("target") != target_name:
            return None
        return {
            "name": case["name"],
            "args": call.get("args", []),
            "expect": check.get("expected"),
        }

    return None


def extract_import_aliases(test_tree: ast.AST | None, task_number: int) -> dict[str, str]:
    aliases: dict[str, str] = {}
    if test_tree is None:
        return aliases
    for node in ast.walk(test_tree):
        if isinstance(node, ast.ImportFrom) and node.module and f"Task{task_number}_" in node.module:
            for alias in node.names:
                actual_name = alias.name
                alias_name = alias.asname or alias.name
                aliases[alias_name] = actual_name
    return aliases



def infer_primary_target(symbols: dict[str, list[str]], test_tree: ast.AST | None, task_number: int) -> dict[str, Any]:
    functions = symbols["functions"]
    classes = symbols["classes"]

    import_aliases = extract_import_aliases(test_tree, task_number)
    imported_names: list[str] = []
    for alias_name, actual_name in import_aliases.items():
        imported_names.append(actual_name)
        imported_names.append(alias_name)

    for name in imported_names:
        if name in functions:
            return {"kind": "function", "name": name}
        if name in classes:
            return {"kind": "class", "name": name}

    non_helper_functions = [name for name in functions if name not in {"main", "printNumber"}]
    if len(classes) == 1 and not non_helper_functions:
        return {"kind": "class", "name": classes[0]}
    if len(non_helper_functions) == 1 and not classes:
        return {"kind": "function", "name": non_helper_functions[0]}
    if classes:
        return {"kind": "class", "name": classes[0]}
    if non_helper_functions:
        return {"kind": "function", "name": non_helper_functions[0]}
    if functions:
        return {"kind": "function", "name": functions[0]}
    return {"kind": "module", "name": f"task_{task_number}"}


def collect_test_methods(tree: ast.AST) -> list[ast.FunctionDef]:
    methods: list[ast.FunctionDef] = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name.startswith("test"):
                    methods.append(item)
        elif isinstance(node, ast.FunctionDef) and node.name.startswith("test"):
            methods.append(node)
    return methods


def find_setup_methods(tree: ast.AST) -> list[ast.FunctionDef]:
    setup_methods: list[ast.FunctionDef] = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name in {"setUp", "tearDown"}:
                    setup_methods.append(item)
    return setup_methods


def build_common_context(tree: ast.AST, target: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, str]]:
    setup: list[dict[str, Any]] = []
    teardown: list[dict[str, Any]] = []
    aliases: dict[str, str] = {}
    target_class = target["name"] if target["kind"] == "class" else None

    for fn in find_setup_methods(tree):
        if fn.name == "setUp":
            local_aliases = dict(aliases)
            for stmt in fn.body:
                for step in stmt_to_steps(stmt, local_aliases, target_class):
                    setup.append(step)
            aliases.update(local_aliases)
        elif fn.name == "tearDown":
            local_aliases = dict(aliases)
            for stmt in fn.body:
                for step in stmt_to_steps(stmt, local_aliases, target_class):
                    teardown.append(step)
    return setup, teardown, aliases


def extract_patches(fn: ast.FunctionDef) -> list[dict[str, Any]]:
    patches: list[dict[str, Any]] = []
    for decorator in fn.decorator_list:
        if isinstance(decorator, ast.Call):
            name = ast.unparse(decorator.func)
            if name.endswith("patch") and decorator.args:
                entry: dict[str, Any] = {
                    "target": constant_value(decorator.args[0]) or ast.unparse(decorator.args[0]),
                    "decorator": name,
                }
                for kw in decorator.keywords:
                    entry[kw.arg or "**"] = expr_to_jsonish(kw.value, {})
                patches.append(entry)
    return patches


def convert_case(fn: ast.FunctionDef, target: dict[str, Any], base_aliases: dict[str, str]) -> dict[str, Any]:
    aliases = dict(base_aliases)
    target_class = target["name"] if target["kind"] == "class" else None
    steps: list[dict[str, Any]] = []
    checks: list[dict[str, Any]] = []

    for stmt in fn.body:
        if isinstance(stmt, ast.Expr) and is_self_assert_call(stmt.value):
            check = assert_call_to_check(stmt.value, aliases)
            if check is not None:
                checks.append(check)
            continue
        if isinstance(stmt, ast.Assert):
            check = bare_assert_to_check(stmt, aliases)
            if check is not None:
                checks.append(check)
            continue
        steps.extend(stmt_to_steps(stmt, aliases, target_class))

    case: dict[str, Any] = {
        "name": fn.name,
        "steps": steps,
        "checks": checks,
    }
    patches = extract_patches(fn)
    if patches:
        case["patch"] = patches
    return case


def build_test_entry(task_number: int) -> dict[str, Any]:
    source_path = SOURCES_DIR / f"task_{task_number}.py"
    test_path = find_test_file(task_number)
    symbols = extract_source_symbols(source_path)

    entry: dict[str, Any] = {
        "source": {"kind": "file", "path": f"task_{task_number}.py"},
        "meta": {
            "source_dataset": "sources/synthid/unwatermarked",
            "source_symbols": symbols,
        },
    }

    if test_path is None:
        entry["target"] = infer_primary_target(symbols, None, task_number)
        entry["assertions"] = []
        entry["meta"]["conversion_status"] = "missing_test"
        return entry

    entry["meta"]["test_path"] = path_for_json(test_path)
    test_tree = try_parse(test_path)
    import_aliases = extract_import_aliases(test_tree, task_number)
    target = infer_primary_target(symbols, test_tree, task_number)
    entry["target"] = target

    if test_tree is None:
        entry["assertions"] = []
        entry["meta"]["conversion_status"] = "unparsed_test_file"
        return entry

    setup, teardown, aliases = build_common_context(test_tree, target)
    aliases.update(import_aliases)
    if setup:
        entry["setup"] = setup
    if teardown:
        entry["teardown"] = teardown

    methods = collect_test_methods(test_tree)
    cases = [convert_case(fn, target, aliases) for fn in methods]

    if target["kind"] == "function":
        simplified: list[dict[str, Any]] = []
        complex_cases: list[dict[str, Any]] = []
        for case in cases:
            simple = simplify_direct_function_case(case, target["name"])
            if simple is not None and "patch" not in case:
                simplified.append(simple)
            else:
                complex_cases.append(case)
        if complex_cases:
            entry["assertions"] = complex_cases if not simplified else simplified + complex_cases
            entry["meta"]["conversion_status"] = "mixed"
        else:
            entry["assertions"] = simplified
            entry["meta"]["conversion_status"] = "direct_function"
    elif target["kind"] == "class":
        method_names: list[str] = []
        for case in cases:
            for step in case.get("steps", []):
                method = step.get("method")
                if isinstance(method, str) and method not in method_names:
                    method_names.append(method)
            for check in case.get("checks", []):
                actual = check.get("actual")
                if isinstance(actual, dict):
                    call = actual.get("call")
                    if isinstance(call, dict):
                        method = call.get("method")
                        if isinstance(method, str) and method not in method_names:
                            method_names.append(method)
        if method_names:
            entry["target"]["methods"] = method_names
        entry["assertions"] = cases
        entry["meta"]["conversion_status"] = "class_or_stateful"
    else:
        entry["assertions"] = cases
        entry["meta"]["conversion_status"] = "module_level"

    return entry


def main() -> None:
    tests = [build_test_entry(task_number) for task_number in list_task_numbers()]
    spec = {
        "defaults": {
            "language": "python",
            "kind": "unit",
        },
        "specs": [
            {
                "tests": tests,
            }
        ],
    }
    OUTPUT_PATH.write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH.relative_to(ROOT)} with {len(tests)} test entries")


if __name__ == "__main__":
    main()
