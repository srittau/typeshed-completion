#!/usr/bin/env python3

import argparse
import glob
import os
import os.path
import sys
import typed_ast.ast3 as ast
from pathlib import Path
from typing import Optional, Iterable, Sequence, List, Tuple

_current_file = ""

TYPESHED_BASE_PATH = Path(os.path.join("typeshed", "stdlib"))


class Logger:
    def __init__(self, *, log_any: bool = False, log_missing: bool = True,
                 log_type_comments: bool = False) \
            -> None:
        self.log_any = log_any
        self.log_missing = log_missing
        self.log_type_comments = log_type_comments

    def problem(self, lineno: int, problem: str) -> None:
        print(f"{_current_file}:{lineno}:{problem}")

    def missing(self, lineno: int, name: str) -> None:
        if not self.log_missing:
            return
        message = f"'{name}' is missing an annotation"
        print(f"{_current_file}:{lineno}:{message}")

    def type_comment(self, lineno: int, name: str) -> None:
        if not self.log_type_comments:
            return
        message = f"'{name}' has a type comment"
        print(f"{_current_file}:{lineno}:{message}")

    def any(self, lineno: int, name: str) -> None:
        if not self.log_any:
            return
        message = f"'{name}' is annotated with Any"
        print(f"{_current_file}:{lineno}:{message}")


log = Logger()


def main() -> None:
    file = parse_args()
    if file is None:
        check_completion()
    else:
        if os.path.isdir(file):
            check_dir(file)
        else:
            check_file(file)


def parse_args() -> Optional[str]:
    parser = argparse.ArgumentParser(description="Find typeshed problems.")
    parser.add_argument("path", nargs="?",
                        help="stub file or directory containing stubs")
    parser.add_argument("-a", "--warn-any", action="store_true",
                        help="warn about annotations with Any")
    parser.add_argument("-c", "--warn-type-comments", action="store_true",
                        help="warn about type comments")
    parser.add_argument("-M", "--hide-missing", action="store_true",
                        help="do not warn about missing annotations")
    args = parser.parse_args()
    if args.warn_any:
        log.log_any = True
    if args.warn_type_comments:
        log.log_type_comments = True
    if args.hide_missing:
        log.log_missing = False
    return args.path


def check_completion() -> None:
    to_check = read_completion()
    for module in to_check:
        filename = find_module_file(module)
        check_file(filename)


def read_completion() -> List[str]:
    modules = []
    with open("COMPLETION.md") as f:
        state = "start"
        lineno = 1
        for line in f:
            if state == "start":
                if line.startswith("| Package"):
                    state = "table-start"
            elif state == "table-start":
                if not line.startswith("| -------"):
                    raise ValueError(f"{lineno}:invalid COMPLETION.md file")
                state = "table-body"
            elif state == "table-body":
                if line.startswith("| "):
                    modules.append(parse_completion_line(line, lineno))
                else:
                    state = "table-end"
            lineno += 1
        if state not in ["table-body", "table-end"]:
            raise ValueError("no completion table found in COMPLETION.md")
    return [m for m, c in modules if c]


def parse_completion_line(line: str, lineno: int) -> Tuple[str, bool]:
    line = line.rstrip()
    if not line.startswith("|") or not line.endswith("|"):
        raise ValueError(f"{lineno}:invalid table row")
    cells = [l.strip() for l in line[1:-1].split("|")]
    if len(cells) < 2:
        raise ValueError(f"{lineno}:not enough table cells")
    module = cells[0].replace("*", "").replace("\\", "")
    unchecked = cells[1] == "*unchecked*"
    return module, unchecked


_dirs: Optional[List[Path]] = None


def find_module_file(module: str) -> str:
    global _dirs
    if _dirs is None:
        _dirs = [TYPESHED_BASE_PATH / "2and3"] + \
            list(TYPESHED_BASE_PATH.glob("3*"))
    module_path = os.path.join(*module.split("."))
    for dir in _dirs:
        paths = [
            dir / (module_path + ".pyi"),
            dir / module_path / "__init__.pyi",
        ]
        for path in paths:
            if path.exists():
                return str(path)
    raise FileNotFoundError(module + ".pyi")

def check_dir(dirname: str) -> None:
    for file in os.scandir(dirname):
        if file.is_dir():
            check_dir(file.path)
        else:
            check_file(file.path)


def check_file(filename: str) -> None:
    global _current_file
    with open(filename, "r") as f:
        source = f.read()
    module = ast.parse(source, filename)
    _current_file = filename
    parse_module(module)


def unhandled_ast_type_msg(node: ast.AST) -> str:
    return f"{_current_file}:{node.lineno}:unhandled ast type {type(node)}"


def is_docstring(child: ast.AST) -> bool:
    return isinstance(child, ast.Expr) and isinstance(child.value, ast.Str)


def targets_name(targets: Sequence[ast.AST]) -> str:
    if len(targets) != 1:
        raise ValueError("multiple assignment targets are not supported")
    if not isinstance(targets[0], ast.Name):
        raise ValueError("assignment target is not a simple name")
    return targets[0].id


def parse_module(module: ast.Module) -> None:
    parse_module_body(module.body)


def parse_module_body(body: Iterable[ast.stmt]) -> None:
    for child in body:
        if isinstance(child, ast.Import) or isinstance(child, ast.ImportFrom):
            pass  # ignore
        elif is_docstring(child):
            pass  # ignore
        elif isinstance(child, ast.If):
            parse_module_body(child.body)
            parse_module_body(child.orelse)
        elif isinstance(child, ast.Assign):
            parse_assign(child)
        elif isinstance(child, ast.AnnAssign):
            parse_ann_assign(child)
        elif isinstance(child, ast.FunctionDef):
            parse_function_def(child)
        elif isinstance(child, ast.ClassDef):
            parse_class_def(child)
        else:
            raise ValueError(unhandled_ast_type_msg(child))


def parse_assign(assign: ast.Assign) -> None:
    name = targets_name(assign.targets)
    if assign.type_comment is not None:
        check_annotation(name, assign, None, assign.type_comment)
    elif isinstance(assign.value, ast.Name) or \
            isinstance(assign.value, ast.Subscript) or \
            isinstance(assign.value, ast.Call) or \
            isinstance(assign.value, ast.Attribute):
        pass  # alias
    elif isinstance(assign.value, ast.Ellipsis) or \
            isinstance(assign.value, ast.Str) or \
            isinstance(assign.value, ast.Num) or \
            isinstance(assign.value, ast.NameConstant):
        log.missing(assign.lineno, name)
    else:
        raise ValueError(unhandled_ast_type_msg(assign.value))


def parse_ann_assign(assign: ast.AnnAssign) -> None:
    assert isinstance(assign.target, ast.Name)
    check_annotation(assign.target.id, assign, assign.annotation)


def parse_function_def(function_def: ast.FunctionDef,
                       name: Optional[str] = None, *,
                       ignore_first_argument: bool = False) -> None:
    if name is None:
        name = function_def.name

    def parse_argument(argument: ast.arg) -> None:
        arg_name = f"{name}({argument.arg})"
        check_annotation(arg_name, function_def, argument.annotation,
                         argument.type_comment)

    check_annotation(name, function_def, function_def.returns,
                     function_def.type_comment)
    args = function_def.args
    normal_args = args.args
    if ignore_first_argument:
        if len(normal_args) < 1:
            log.problem(function_def.lineno,
                        f"'{name}' requires at least one argument")
        normal_args = normal_args[1:]

    for arg in normal_args:
        parse_argument(arg)
    for arg in args.kwonlyargs:
        parse_argument(arg)
    if args.vararg is not None:
        parse_argument(args.vararg)
    if args.kwarg is not None:
        parse_argument(args.kwarg)


def parse_class_def(class_def: ast.ClassDef) -> None:
    if is_empty_class(class_def):
        return
    parse_class_body(class_def.name, class_def.body)


def parse_class_body(class_name: str, body: Iterable[ast.stmt]) -> None:
    for child in body:
        if is_docstring(child):
            pass
        elif isinstance(child, ast.If):
            parse_class_body(class_name, child.body)
            parse_class_body(class_name, child.orelse)
        elif isinstance(child, ast.Assign):
            parse_class_assign(class_name, child)
        elif isinstance(child, ast.AnnAssign):
            parse_class_ann_assign(class_name, child)
        elif isinstance(child, ast.FunctionDef):
            parse_method(class_name, child)
        else:
            raise ValueError(unhandled_ast_type_msg(child))


def parse_class_assign(class_name: str, assign: ast.Assign) -> None:
    name = targets_name(assign.targets)
    check_annotation(name, assign, None, assign.type_comment)


def parse_class_ann_assign(class_name: str, assign: ast.AnnAssign) -> None:
    assert isinstance(assign.target, ast.Name)
    name = f"{class_name}.{assign.target.id}"
    check_annotation(name, assign, assign.annotation)


def parse_method(class_name: str, method: ast.FunctionDef) -> None:
    name = f"{class_name}.{method.name}"
    decorators = \
        [d.id for d in method.decorator_list if isinstance(d, ast.Name)]
    ignore_first_argument = "staticmethod" not in decorators
    return parse_function_def(method, name=name,
                              ignore_first_argument=ignore_first_argument)


def is_empty_class(class_def: ast.ClassDef) -> bool:
    if len(class_def.body) != 1:
        return False
    body = class_def.body[0]
    if isinstance(body, ast.Pass):
        return True
    if not isinstance(body, ast.Expr):
        return False
    if not isinstance(body.value, ast.Ellipsis):
        return False
    return True


def check_annotation(name: str, parent: ast.AST,
                     annotation: Optional[ast.AST],
                     type_comment: Optional[str] = None) -> None:
    if annotation is not None and type_comment is not None:
        log.problem(parent.lineno,
                    f"'{name}' has a type annotation and a type comment")
    elif annotation is None and type_comment is None:
        log.missing(parent.lineno, name)
    elif type_comment is not None:
        log.type_comment(parent.lineno, name)
        if type_comment == "Any":
            log.any(parent.lineno, name)
    elif isinstance(annotation, ast.Ellipsis):
        log.problem(annotation.lineno, f"'{name}' is annotated with ellipsis")
    elif isinstance(annotation, ast.Name):
        if annotation.id == "Any":
            log.any(annotation.lineno, name)
    elif isinstance(annotation, ast.NameConstant):
        if annotation.value is not None:
            log.problem(annotation.lineno,
                        f"'{name}' is annotated with {annotation.value}")
    elif isinstance(annotation, ast.Str):
        pass
    elif isinstance(annotation, ast.Subscript):
        pass  # generic
    elif isinstance(annotation, ast.Attribute):
        pass
    else:
        raise ValueError(unhandled_ast_type_msg(annotation))


if __name__ == "__main__":
    main()

