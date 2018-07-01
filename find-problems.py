#!/usr/bin/env python3

import ast
import os
import sys
from typing import Optional

_current_file = ""


class Logger:
    def problem(self, lineno: int, problem: str) -> None:
        print(f"{_current_file}:{lineno}:{problem}")

    def warn(self, lineno: int, problem: str) -> None:
        print(f"{_current_file}:{lineno}:{problem}")

    def missing(self, lineno: int, name: str) -> None:
        message = f"'{name}' is missing an annotation"
        print(f"{_current_file}:{lineno}:{message}")
    
    def any(self, lineno: int, name: str) -> None:
        message = f"'{name}' is annotated with Any"
        print(f"{_current_file}:{lineno}:{message}")


log = Logger()


def main() -> None:
    file = parse_args()
    if os.path.isdir(file):
        check_dir(file)
    else:
        check_file(file)


def parse_args() -> str:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} FILENAME_OR_DIRECTORY", file=sys.stderr)
        sys.exit(1)
    return sys.argv[1]


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


def parse_module(module: ast.Module) -> None:
    for child in module.body:
        if isinstance(child, ast.ImportFrom):
            pass  # ignore
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
    names = ", ".join(n.id for n in assign.targets)
    if isinstance(assign.value, ast.Subscript):
        pass  # alias
    elif isinstance(assign.value, ast.Ellipsis) or \
            isinstance(assign.value, ast.Str) or \
            isinstance(assign.value, ast.Num):
        log.missing(assign.lineno, names)
    else:
        log.warn(assign.lineno,
                 f"'{names}'is potentially missing an annotation")


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
        check_annotation(arg_name, function_def, argument.annotation)        

    check_annotation(name, function_def, function_def.returns)
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
    class_name = class_def.name
    for child in class_def.body:
        if isinstance(child, ast.Assign):
            parse_class_assign(class_name, child)
        elif isinstance(child, ast.AnnAssign):
            parse_class_ann_assign(class_name, child)
        elif isinstance(child, ast.FunctionDef):
            parse_method(class_name, child)
        else:
            raise ValueError(unhandled_ast_type_msg(child))


def parse_class_assign(class_name: str, assign: ast.Assign) -> None:
    names = ", ".join(f"{class_name}.{t.id}" for t in assign.targets)
    log.missing(assign.lineno, names)


def parse_class_ann_assign(class_name: str, assign: ast.AnnAssign) -> None:
    assert isinstance(assign.target, ast.Name)
    name = f"{class_name}.{assign.target.id}"
    check_annotation(name, assign, assign.annotation)


def parse_method(class_name: str, method: ast.FunctionDef) -> None:
    name = f"{class_name}.{method.name}"
    decorators = [d.id for d in method.decorator_list]
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
                     annotation: Optional[ast.AST]) -> None:
    if annotation is None:
        log.missing(parent.lineno, name)
    elif isinstance(annotation, ast.Ellipsis):
        log.problem(annotation.lineno, f"'{name}' is annotated with ellipsis")
    elif isinstance(annotation, ast.Name):
        if annotation.id == "Any":
            log.any(annotation.lineno, name)
    elif isinstance(annotation, ast.NameConstant):
        if annotation.value is not None:
            log.problem(annotation.lineno,
                        f"'{name}' is annotated with {annotation.value}")
    elif isinstance(annotation, ast.Subscript):
        pass  # generic
    else:
        raise ValueError(unhandled_ast_type_msg(annotation))


if __name__ == "__main__":
    main()

