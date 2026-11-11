import unittest
from solution import all_of, any_of, none_of, negate

def is_positive(value):
    return value > 0

def is_even(value):
    return value % 2 == 0

def is_string(value):
    return isinstance(value, str)

def ends_with_bang(value):
    return isinstance(value, str) and value.endswith('!')

class ValidationCombinatorsTest(unittest.TestCase):

    def test_all_of_returns_true_when_all_validators_pass(self):
        validator = all_of(is_positive, is_even)
        self.assertTrue(validator(4))
        self.assertFalse(validator(3))
        self.assertFalse(validator(-2))

    def test_any_of_returns_true_when_any_validator_passes(self):
        validator = any_of(is_string, ends_with_bang)
        self.assertTrue(validator('hello'))
        self.assertTrue(validator('wow!'))
        self.assertFalse(validator(42))

    def test_none_of_returns_true_when_all_validators_fail(self):
        validator = none_of(is_positive, is_even)
        self.assertTrue(validator(-3))
        self.assertFalse(validator(-2))
        self.assertFalse(validator(3))

    def test_negate_inverts_validator_result(self):
        not_positive = negate(is_positive)
        self.assertTrue(not_positive(-1))
        self.assertFalse(not_positive(1))

    def test_empty_combinators_use_identity_behaviour(self):
        always_true = all_of()
        always_false = any_of()
        always_true_none = none_of()
        self.assertTrue(always_true(0))
        self.assertFalse(always_false(0))
        self.assertTrue(always_true_none(0))

    def test_combinators_short_circuit(self):
        def boom(value):
            raise AssertionError('short-circuit violation')

        always_false = lambda value: False
        always_true = lambda value: True

        self.assertFalse(all_of(always_false, boom)(1))
        self.assertTrue(any_of(always_true, boom)(1))
        self.assertFalse(none_of(always_true, boom)(1))

if __name__ == '__main__':
    unittest.main()
