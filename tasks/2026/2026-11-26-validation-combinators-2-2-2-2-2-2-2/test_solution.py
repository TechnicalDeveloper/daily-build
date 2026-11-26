import unittest
from solution import all_of, any_of, none_of, not_validator

def is_even(x):
    return x % 2 == 0

def is_positive(x):
    return x > 0

def is_less_than_ten(x):
    return x < 10

class TestAllOf(unittest.TestCase):
    def test_all_of_empty(self):
        v = all_of()
        self.assertTrue(v(42))
        self.assertTrue(v("anything"))

    def test_all_of_multiple(self):
        v = all_of(is_even, is_positive, is_less_than_ten)
        self.assertTrue(v(4))
        self.assertFalse(v(-2))  # not positive
        self.assertFalse(v(12))  # not <10
        self.assertFalse(v(3))   # not even

class TestAnyOf(unittest.TestCase):
    def test_any_of_empty(self):
        v = any_of()
        self.assertFalse(v(42))
        self.assertFalse(v("anything"))

    def test_any_of_multiple(self):
        v = any_of(is_even, is_positive)
        self.assertTrue(v(4))
        self.assertTrue(v(-2))  # even, not positive
        self.assertTrue(v(3))   # positive, not even
        self.assertFalse(v(-3)) # neither

class TestNoneOf(unittest.TestCase):
    def test_none_of_empty(self):
        v = none_of()
        self.assertTrue(v(42))
        self.assertTrue(v("anything"))

    def test_none_of_multiple(self):
        v = none_of(is_even, is_positive)
        self.assertTrue(v(-3))   # neither even nor positive
        self.assertFalse(v(-2))  # even
        self.assertFalse(v(3))   # positive

class TestNotValidator(unittest.TestCase):
    def test_not_validator(self):
        v = not_validator(is_even)
        self.assertTrue(v(3))
        self.assertFalse(v(4))

if __name__ == '__main__':
    unittest.main()
