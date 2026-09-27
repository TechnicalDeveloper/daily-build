import unittest
from solution import interpolate

class TestInterpolate(unittest.TestCase):
    def test_basic(self):
        result = interpolate("Hello, {name}!", {"name": "Alice"})
        self.assertEqual(result, "Hello, Alice!")
    
    def test_missing_key(self):
        with self.assertRaises(KeyError):
            interpolate("Hello, {name}!", {"age": 30})
    
    def test_multiple(self):
        result = interpolate("{a} {b} {a}", {"a": "x", "b": "y"})
        self.assertEqual(result, "x y x")
    
    def test_non_string(self):
        result = interpolate("Value: {val}", {"val": 42})
        self.assertEqual(result, "Value: 42")
    
    def test_empty_template(self):
        result = interpolate("", {"a": 1})
        self.assertEqual(result, "")
