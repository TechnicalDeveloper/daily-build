import unittest
from solution import predicate, all_of, any_of, optional, not_validator

class TestValidationCombinators(unittest.TestCase):

    def test_predicate_pass(self):
        is_positive = predicate(lambda x: x > 0, "Must be positive")
        success, err = is_positive(5)
        self.assertTrue(success)
        self.assertIsNone(err)

    def test_predicate_fail(self):
        is_positive = predicate(lambda x: x > 0, "Must be positive")
        success, err = is_positive(-1)
        self.assertFalse(success)
        self.assertEqual(err, "Must be positive")

    def test_all_of_pass(self):
        is_positive = predicate(lambda x: x > 0, "Must be positive")
        is_int = predicate(lambda x: isinstance(x, int), "Must be int")
        combined = all_of(is_positive, is_int)
        success, err = combined(42)
        self.assertTrue(success)
        self.assertIsNone(err)

    def test_all_of_fail(self):
        is_positive = predicate(lambda x: x > 0, "Must be positive")
        is_even = predicate(lambda x: x % 2 == 0, "Must be even")
        combined = all_of(is_positive, is_even)
        success, err = combined(3)
        self.assertFalse(success)
        self.assertEqual(err, "Must be even")

    def test_any_of_pass(self):
        is_positive = predicate(lambda x: x > 0, "Must be positive")
        is_negative = predicate(lambda x: x < 0, "Must be negative")
        combined = any_of(is_positive, is_negative)
        success, err = combined(-5)
        self.assertTrue(success)
        self.assertIsNone(err)

    def test_any_of_fail(self):
        is_positive = predicate(lambda x: x > 0, "Must be positive")
        is_negative = predicate(lambda x: x < 0, "Must be negative")
        combined = any_of(is_positive, is_negative)
        success, err = combined(0)
        self.assertFalse(success)
        self.assertIn("Must be positive", err)
        self.assertIn("Must be negative", err)

    def test_optional_with_none(self):
        is_positive = predicate(lambda x: x > 0, "Must be positive")
        optional_is_positive = optional(is_positive)
        success, err = optional_is_positive(None)
        self.assertTrue(success)
        self.assertIsNone(err)

    def test_optional_with_value(self):
        is_positive = predicate(lambda x: x > 0, "Must be positive")
        optional_is_positive = optional(is_positive)
        success, err = optional_is_positive(10)
        self.assertTrue(success)
        self.assertIsNone(err)

    def test_not_validator_pass(self):
        is_positive = predicate(lambda x: x > 0, "Must be positive")
        not_positive = not_validator(is_positive)
        success, err = not_positive(-1)
        self.assertTrue(success)
        self.assertIsNone(err)

    def test_not_validator_fail(self):
        is_positive = predicate(lambda x: x > 0, "Must be positive")
        not_positive = not_validator(is_positive)
        success, err = not_positive(5)
        self.assertFalse(success)
        self.assertEqual(err, "Value not expected")

    def test_empty_all_of(self):
        always_pass = all_of()
        success, err = always_pass("anything")
        self.assertTrue(success)
        self.assertIsNone(err)

    def test_empty_any_of(self):
        always_fail = any_of()
        success, err = always_fail("anything")
        self.assertFalse(success)
        self.assertEqual(err, "No validators provided")

if __name__ == '__main__':
    unittest.main()
