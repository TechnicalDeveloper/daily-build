import unittest
from solution import evaluate

class TestEvaluate(unittest.TestCase):

    def test_simple_addition(self):
        self.assertEqual(evaluate("3+5"), 8)

    def test_multiplication_precedence(self):
        self.assertEqual(evaluate("2+3*4"), 14)

    def test_left_to_right_same_precedence(self):
        self.assertEqual(evaluate("8-3+2"), 7)

    def test_whitespace_handling(self):
        self.assertEqual(evaluate(" 10 * 2 + 5 "), 25)

    def test_single_number(self):
        self.assertEqual(evaluate("42"), 42)

    def test_another_expression(self):
        self.assertEqual(evaluate("1+2*3+4"), 11)

if __name__ == '__main__':
    unittest.main()
