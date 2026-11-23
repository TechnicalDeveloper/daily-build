import unittest
from solution import interpolate

class TestInterpolate(unittest.TestCase):

    def test_basic_replacement(self):
        self.assertEqual(
            interpolate("Hello {name}!", {"name": "World"}),
            "Hello World!"
        )

    def test_missing_key_raises(self):
        with self.assertRaises(KeyError):
            interpolate("Hello {unknown}!", {})

    def test_escaped_braces(self):
        self.assertEqual(interpolate("{{name}}", {}), "{name}")
        self.assertEqual(interpolate("a {{b}} c", {}), "a {b} c")

    def test_multiple_placeholders(self):
        template = "{a}-{b}-{a}"
        mapping = {"a": "x", "b": "y"}
        self.assertEqual(interpolate(template, mapping), "x-y-x")

    def test_non_string_values(self):
        self.assertEqual(
            interpolate("num: {n}", {"n": 42}),
            "num: 42"
        )

if __name__ == '__main__':
    unittest.main()
