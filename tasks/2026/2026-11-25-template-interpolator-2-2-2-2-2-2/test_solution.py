import unittest
from solution import interpolate

class TestInterpolate(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(interpolate("Hello {name}", {"name": "Alice"}), "Hello Alice")

    def test_multiple_and_non_string(self):
        self.assertEqual(interpolate("{a}-{b}-{a}", {"a": 1, "b": 2.5}), "1-2.5-1")

    def test_missing_key_raises(self):
        with self.assertRaises(KeyError):
            interpolate("{name}", {"age": 30})

    def test_escaped_braces(self):
        self.assertEqual(interpolate("{{literal}} and {key}", {"key": "value"}), "{literal} and value")

    def test_empty_template(self):
        self.assertEqual(interpolate("", {}), "")

    def test_unescaped_brace_error(self):
        with self.assertRaises(ValueError):
            interpolate("}", {})

if __name__ == '__main__':
    unittest.main()
