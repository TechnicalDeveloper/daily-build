import unittest
from solution import (
    is_integer, is_positive, is_non_empty_string, is_email,
    and_, or_, not_, all_, any_, maybe
)


class TestValidators(unittest.TestCase):

    def test_and_combinator(self):
        v = and_(is_integer(), is_positive())
        self.assertIsNone(v(5))
        self.assertIsNotNone(v(-1))
        self.assertIsNotNone(v(0))
        self.assertIsNotNone(v("abc"))

    def test_or_combinator(self):
        v = or_(is_integer(), is_non_empty_string())
        self.assertIsNone(v(123))
        self.assertIsNone(v("hello"))
        self.assertIsNotNone(v(""))  # both fail: not integer, empty string
        self.assertIsNotNone(v(3.14))  # neither integer nor string

    def test_not_combinator(self):
        v = not_(is_integer())
        self.assertIsNone(v("abc"))   # integer validator fails -> not_ passes
        self.assertIsNotNone(v(42))    # integer validator passes -> not_ fails

    def test_maybe_combinator(self):
        v = maybe(is_integer())
        self.assertIsNone(v(None))
        self.assertIsNone(v(10))
        self.assertIsNotNone(v("x"))

    def test_all_any_combinators(self):
        # all_ with no validators -> always pass
        v_all_empty = all_()
        self.assertIsNone(v_all_empty("anything"))

        v_all = all_(is_integer(), is_positive())
        self.assertIsNone(v_all(5))
        self.assertIsNotNone(v_all("5"))
        self.assertIsNotNone(v_all(-1))

        # any_ with no validators -> always fail
        v_any_empty = any_()
        self.assertIsNotNone(v_any_empty("anything"))

        v_any = any_(is_integer(), is_positive())
        self.assertIsNone(v_any(5))
        self.assertIsNone(v_any(-5))  # is_integer passes, so any_ passes
        self.assertIsNotNone(v_any("x"))  # both fail
        self.assertIsNone(v_any(0))  # is_integer passes, so any_ passes

    def test_email_validator(self):
        v = is_email()
        self.assertIsNone(v("user@example.com"))
        self.assertIsNotNone(v("notanemail"))
        self.assertIsNotNone(v("@domain.com"))
        self.assertIsNotNone(v("user@.com"))


if __name__ == '__main__':
    unittest.main()
