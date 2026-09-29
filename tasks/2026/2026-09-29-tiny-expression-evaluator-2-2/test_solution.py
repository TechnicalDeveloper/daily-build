import unittest
from solution import evaluate


class TestExpressionEvaluator(unittest.TestCase):
    def test_addition_and_subtraction(self):
        self.assertEqual(evaluate("1 + 2 - 3"), 0.0)
        self.assertEqual(evaluate("10 - 2 + 8"), 16.0)

    def test_multiplication_and_division(self):
        self.assertEqual(evaluate("2 * 3 + 4"), 10.0)
        self.assertEqual(evaluate("10 / 2 / 5"), 1.0)
        self.assertEqual(evaluate("7 - 2 * 3"), 1.0)

    def test_parentheses_and_unary_minus(self):
        self.assertEqual(evaluate("(2 + 3) * 4"), 20.0)
        self.assertEqual(evaluate("-(2 + 3)"), -5.0)
        self.assertEqual(evaluate("1--2"), 3.0)
        self.assertEqual(evaluate("-( -5 )"), 5.0)

    def test_errors(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate("1 / 0")
        with self.assertRaises(ValueError):
            evaluate("")
        with self.assertRaises(ValueError):
            evaluate("1 + $")
        with self.assertRaises(ValueError):
            evaluate("(1 + 2")
        with self.assertRaises(ValueError):
            evaluate("1 2")


if __name__ == "__main__":
    unittest.main()
