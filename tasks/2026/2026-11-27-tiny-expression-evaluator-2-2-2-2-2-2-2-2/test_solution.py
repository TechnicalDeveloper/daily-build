import unittest
from solution import evaluate

class TestExpressionEvaluator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(evaluate("1+2"), 3.0)

    def test_precedence(self):
        self.assertEqual(evaluate("2+3*4"), 14.0)
        self.assertEqual(evaluate("10/2+3"), 8.0)

    def test_parentheses(self):
        self.assertEqual(evaluate("(2+3)*4"), 20.0)
        self.assertEqual(evaluate("((1+2)*(3-1))"), 6.0)

    def test_unary_minus(self):
        self.assertEqual(evaluate("-5"), -5.0)
        self.assertEqual(evaluate("-(3+2)"), -5.0)

    def test_division(self):
        self.assertEqual(evaluate("10/4"), 2.5)

    def test_whitespace(self):
        self.assertEqual(evaluate("  1 + 2  * 3 "), 7.0)
        self.assertEqual(evaluate("1\n+\t2"), 3.0)

    def test_invalid_syntax(self):
        with self.assertRaises(SyntaxError):
            evaluate("1+")
        with self.assertRaises(SyntaxError):
            evaluate("(1+2")
        with self.assertRaises(ValueError):
            evaluate("")
        with self.assertRaises(ValueError):
            evaluate("1#2")

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate("1/0")

if __name__ == '__main__':
    unittest.main()
