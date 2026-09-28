import unittest
from solution import evaluate

class TestEvaluator(unittest.TestCase):
    def test_simple_addition(self):
        self.assertEqual(evaluate("1+2"), 3)

    def test_precedence(self):
        self.assertEqual(evaluate("2+3*4"), 14)

    def test_parentheses(self):
        self.assertEqual(evaluate("(2+3)*4"), 20)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate("1/0")

    def test_empty_expression(self):
        with self.assertRaises(ValueError):
            evaluate("")

    def test_negative_numbers(self):
        self.assertEqual(evaluate("-5+3"), -2)
        self.assertEqual(evaluate("(-5+3)*2"), -4)

    def test_whitespace(self):
        self.assertEqual(evaluate(" 1 + 2 "), 3)

    def test_invalid_characters(self):
        with self.assertRaises(ValueError):
            evaluate("1+a")

if __name__ == '__main__':
    unittest.main()
