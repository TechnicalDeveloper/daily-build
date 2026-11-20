import unittest
from solution import is_string, is_integer, min_length, regex, all_of, any_of, optional

class TestValidationCombinators(unittest.TestCase):
    def test_is_integer_accepts_int(self):
        self.assertEqual(is_integer(5), 5)
        self.assertEqual(is_integer(-3), -3)

    def test_is_integer_rejects_bool(self):
        with self.assertRaises(ValueError):
            is_integer(True)
        with self.assertRaises(ValueError):
            is_integer(False)

    def test_all_of_validates_success(self):
        validator = all_of(is_string, min_length(5), regex(r'[a-z]+'))
        self.assertEqual(validator('abcde'), 'abcde')
        self.assertEqual(validator('hello'), 'hello')

    def test_all_of_raises_on_first_error(self):
        validator = all_of(is_string, min_length(5))
        with self.assertRaises(ValueError):
            validator(123)
        with self.assertRaises(ValueError):
            validator('abc')

    def test_any_of_accepts_if_one_matches(self):
        validator = any_of(is_integer, is_string)
        self.assertEqual(validator('hello'), 'hello')
        self.assertEqual(validator(123), 123)

    def test_any_of_rejects_if_none_match(self):
        validator = any_of(is_integer, is_string)
        with self.assertRaises(ValueError):
            validator(3.14)

    def test_optional_allows_none(self):
        validator = optional(is_integer)
        self.assertIsNone(validator(None))
        self.assertEqual(validator(10), 10)
        with self.assertRaises(ValueError):
            validator('not an int')

    def test_regex_requires_full_match(self):
        validator = regex(r'\d{3}')
        self.assertEqual(validator('123'), '123')
        with self.assertRaises(ValueError):
            validator('1234')
        with self.assertRaises(ValueError):
            validator('abc')

if __name__ == '__main__':
    unittest.main()
