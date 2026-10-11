import unittest

from safe_calculator import evaluate_expression


class SafeCalculatorTests(unittest.TestCase):
    def test_basic_arithmetic_and_precedence(self):
        self.assertEqual(evaluate_expression("-2 + 3 * (4 - 1)"), 7)

    def test_decimal_comma(self):
        self.assertEqual(evaluate_expression("2,5 / 0,5"), 5)

    def test_division_by_zero_is_reported(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate_expression("10 / (3 - 3)")

    def test_rejects_python_expressions_and_unsupported_operators(self):
        for expression in ("__import__('os')", "2 ** 8", "1 // 2", "True"):
            with self.subTest(expression=expression):
                with self.assertRaises(ValueError):
                    evaluate_expression(expression)

    def test_rejects_long_expressions(self):
        with self.assertRaises(ValueError):
            evaluate_expression("1" * 201)

    def test_rejects_excessive_ast_nodes_and_depth(self):
        too_many_nodes = "*".join(["1"] * 35)
        too_deep = "+".join(["1"] * 22)

        with self.assertRaises(ValueError):
            evaluate_expression(too_many_nodes)
        with self.assertRaises(ValueError):
            evaluate_expression(too_deep)

    def test_rejects_non_finite_and_oversized_results(self):
        with self.assertRaises(ValueError):
            evaluate_expression("1e999")
        with self.assertRaises(ValueError):
            evaluate_expression(str(10**100) + " * 2")


if __name__ == "__main__":
    unittest.main()
