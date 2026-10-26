import unittest
from solution import ok, fail, all_of, one_of, transform, satisfies

class TestValidationCombinators(unittest.TestCase):

    def test_ok_always_succeeds(self):
        v = ok()
        self.assertEqual(v(42), (True, 42))
        self.assertEqual(v("hello"), (True, "hello"))

    def test_fail_always_fails(self):
        v = fail("error")
        self.assertEqual(v(100), (False, "error"))
        self.assertEqual(v(None), (False, "error"))

    def test_all_of_with_no_validators(self):
        v = all_of()
        self.assertEqual(v("anything"), (True, "anything"))

    def test_all_of_with_all_success(self):
        v = all_of(ok(), ok())
        self.assertEqual(v(1), (True, 1))

    def test_all_of_with_one_failure(self):
        v = all_of(ok(), fail("second failed"))
        self.assertEqual(v(1), (False, "second failed"))

    def test_one_of_with_success_first(self):
        v = one_of(ok(), fail("second"))
        self.assertEqual(v(1), (True, 1))

    def test_one_of_with_no_validators(self):
        v = one_of()
        self.assertEqual(v(1), (False, []))

    def test_one_of_all_fail(self):
        v = one_of(fail("a"), fail("b"))
        success, errors = v(1)
        self.assertFalse(success)
        self.assertEqual(errors, ["a", "b"])

    def test_transform_success(self):
        v = transform(ok(), lambda x: x * 2)
        self.assertEqual(v(5), (True, 10))

    def test_transform_failure_preserves_error(self):
        v = transform(fail("nope"), lambda x: x * 2)
        self.assertEqual(v(5), (False, "nope"))

    def test_satisfies_pass(self):
        v = satisfies(lambda x: x > 0, "must be positive")
        self.assertEqual(v(5), (True, 5))

    def test_satisfies_fail(self):
        v = satisfies(lambda x: x > 0, "must be positive")
        self.assertEqual(v(-1), (False, "must be positive"))

if __name__ == '__main__':
    unittest.main()
