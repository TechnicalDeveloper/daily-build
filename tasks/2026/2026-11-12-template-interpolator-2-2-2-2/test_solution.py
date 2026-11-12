import unittest
from solution import interpolate

class TestInterpolate(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(interpolate("Hello, {name}!", {"name": "Alice"}), "Hello, Alice!")

    def test_multiple(self):
        tmpl = "{greeting}, {name}! You have {count} new messages."
        vars = {"greeting": "Hi", "name": "Bob", "count": 3}
        self.assertEqual(interpolate(tmpl, vars), "Hi, Bob! You have 3 new messages.")

    def test_missing_key_raises(self):
        with self.assertRaises(KeyError):
            interpolate("Hello {name}!", {})

    def test_no_placeholders(self):
        self.assertEqual(interpolate("No placeholders", {"a": 1}), "No placeholders")

    def test_empty_template(self):
        self.assertEqual(interpolate("", {"a": 1}), "")

if __name__ == '__main__':
    unittest.main()
