import unittest
from solution import evaluate

class TestExpressionEvaluator(unittest.TestCase):

    def test_basic_arithmetic(self):
        self.assertAlmostEqual(evaluate("1+2"), 3.0)
        self.assertAlmostEqual(evaluate("3*4"), 12.0)
        self.assertAlmostEqual(evaluate("10/2"), 5.0)
        self.assertAlmostEqual(evaluate("5-3"), 2.0)

    def test_precedence_and_parentheses(self):
        self.assertAlmostEqual(evaluate("1+2*3"), 7.0)
        self.assertAlmostEqual(evaluate("(1+2)*3"), 9.0)
        self.assertAlmostEqual(evaluate("2*(3+4)"), 14.0)
        self.assertAlmostEqual(evaluate("10-2*3+4"), 8.0)

    def test_unary_minus(self):
        self.assertAlmostEqual(evaluate("-3+4"), 1.0)
        self.assertAlmostEqual(evaluate("-(5+2)"), -7.0)
        self.assertAlmostEqual(evaluate("--5"), 5.0)
        self.assertAlmostEqual(evaluate("-(-8)"), 8.0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate("1/0")
        with self.assertRaises(ZeroDivisionError):
            evaluate("(2+3)/(5-5)")

    def test_invalid_expressions(self):
        with self.assertRaises(ValueError):
            evaluate("1++2")
        with self.assertRaises(ValueError):
            evaluate("1+2)")
        with self.assertRaises(ValueError):
            evaluate("()")
        with self.assertRaises(ValueError):
            evaluate("   ")

if __name__ == "__main__":
    unittest.main()
