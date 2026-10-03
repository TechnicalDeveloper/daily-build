import unittest
from solution import evaluate

class TestExpressionEvaluator(unittest.TestCase):
    def test_basic_addition(self):
        self.assertEqual(evaluate("2+3"), 5)

    def test_multiplication_precedence(self):
        self.assertEqual(evaluate("2+3*4"), 14)

    def test_parentheses(self):
        self.assertEqual(evaluate("(2+3)*4"), 20)

    def test_division(self):
        self.assertEqual(evaluate("10/2"), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            evaluate("10/0")

    def test_invalid_character(self):
        with self.assertRaises(ValueError):
            evaluate("2+3a")

    def test_mismatched_parentheses(self):
        with self.assertRaises(ValueError):
            evaluate("(2+3")

    def test_empty_expression(self):
        with self.assertRaises(ValueError):
            evaluate("")

if __name__ == '__main__':
    unittest.main()
