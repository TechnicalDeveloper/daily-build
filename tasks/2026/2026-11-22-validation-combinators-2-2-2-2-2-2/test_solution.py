import unittest
from solution import all_of, any_of, none_of, not_validator


def is_even(x):
    return x % 2 == 0


def is_positive(x):
    return x > 0


class TestAllOf(unittest.TestCase):
    def test_all_of_pass(self):
        validator = all_of(is_even, is_positive)
        self.assertTrue(validator(4))
        self.assertTrue(validator(10))

    def test_all_of_fail(self):
        validator = all_of(is_even, is_positive)
        self.assertFalse(validator(3))
        self.assertFalse(validator(-2))

    def test_all_of_empty(self):
        validator = all_of()
        self.assertTrue(validator(123))  # vacuous truth


class TestAnyOf(unittest.TestCase):
    def test_any_of_pass(self):
        validator = any_of(is_even, is_positive)
        self.assertTrue(validator(2))
        self.assertTrue(validator(3))
        self.assertTrue(validator(-2))

    def test_any_of_fail(self):
        validator = any_of(is_even, is_positive)
        self.assertFalse(validator(-3))

    def test_any_of_empty(self):
        validator = any_of()
        self.assertFalse(validator(0))


class TestNoneOf(unittest.TestCase):
    def test_none_of_pass(self):
        validator = none_of(is_even, is_positive)
        self.assertTrue(validator(-3))
        self.assertTrue(validator(-5))

    def test_none_of_fail(self):
        validator = none_of(is_even, is_positive)
        self.assertFalse(validator(2))
        self.assertFalse(validator(3))

    def test_none_of_empty(self):
        validator = none_of()
        self.assertTrue(validator(42))  # no validators, so none pass


class TestNotValidator(unittest.TestCase):
    def test_not_validator_negates(self):
        is_odd = not_validator(is_even)
        self.assertTrue(is_odd(3))
        self.assertFalse(is_odd(2))

    def test_not_validator_with_positive(self):
        is_non_positive = not_validator(is_positive)
        self.assertTrue(is_non_positive(-1))
        self.assertFalse(is_non_positive(1))


if __name__ == '__main__':
    unittest.main()
