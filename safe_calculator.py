"""Bounded arithmetic expression evaluator for the Discord bot."""

import ast
import math
import operator


MAX_EXPRESSION_LENGTH = 200
MAX_AST_NODES = 64
MAX_AST_DEPTH = 20
MAX_ABSOLUTE_VALUE = 10**100

_BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def evaluate_expression(expression):
    """Evaluate basic arithmetic without ``eval`` or unbounded inputs."""
    if not isinstance(expression, str):
        raise ValueError("A expressão precisa ser texto.")

    normalized = expression.replace(",", ".").strip()
    if not normalized:
        raise ValueError("A expressão não pode ficar vazia.")
    if len(normalized) > MAX_EXPRESSION_LENGTH:
        raise ValueError("A expressão excede o limite de tamanho.")

    try:
        tree = ast.parse(normalized, mode="eval")
    except (SyntaxError, ValueError) as error:
        raise ValueError("A expressão matemática é inválida.") from error

    if sum(1 for _ in ast.walk(tree)) > MAX_AST_NODES:
        raise ValueError("A expressão contém operações demais.")

    return _evaluate(tree.body, depth=0)


def _evaluate(node, depth):
    if depth > MAX_AST_DEPTH:
        raise ValueError("A expressão está aninhada demais.")

    if isinstance(node, ast.Constant):
        return _validate_number(node.value)

    if isinstance(node, ast.UnaryOp):
        if not isinstance(node.op, (ast.UAdd, ast.USub)):
            raise ValueError("Esse operador não é permitido.")
        value = _evaluate(node.operand, depth + 1)
        result = value if isinstance(node.op, ast.UAdd) else -value
        return _validate_number(result)

    if isinstance(node, ast.BinOp):
        operation = _BINARY_OPERATORS.get(type(node.op))
        if operation is None:
            raise ValueError("Esse operador não é permitido.")

        left = _evaluate(node.left, depth + 1)
        right = _evaluate(node.right, depth + 1)
        if isinstance(node.op, ast.Div) and right == 0:
            raise ZeroDivisionError("Divisão por zero.")

        return _validate_number(operation(left, right))

    raise ValueError("A expressão contém conteúdo não permitido.")


def _validate_number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Use apenas números e operações aritméticas básicas.")
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("O resultado precisa ser um número finito.")
    if abs(value) > MAX_ABSOLUTE_VALUE:
        raise ValueError("O resultado excede o limite aceito.")
    return value
