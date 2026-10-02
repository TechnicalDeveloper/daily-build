import unittest
from solution import evaluate

class TestEvaluator(unittest.TestCase):
    def test_simple_addition(self):
        self.assertEqual(evaluate("2+3"), 5)

    def test_precedence(self):
        self.assertEqual(evaluate("2+3*4"), 14)

    def test_division(self):
        self.assertEqual(evaluate("10/2-3"), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            evaluate("5/0")

    def test_single_number(self):
        self.assertEqual(evaluate("42"), 42)

    def test_spaces(self):
        self.assertEqual(evaluate(" 3 + 4 "), 7)

if __name__ == '__main__':
    unittest.main()
