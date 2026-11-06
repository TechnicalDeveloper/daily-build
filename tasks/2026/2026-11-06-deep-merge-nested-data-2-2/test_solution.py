import unittest
from solution import deep_merge

class TestDeepMerge(unittest.TestCase):

    def test_simple_overwrite(self):
        a = {'x': 1, 'y': 2}
        b = {'y': 3, 'z': 4}
        result = deep_merge(a, b)
        self.assertEqual(result, {'x': 1, 'y': 3, 'z': 4})
        # Ensure originals are unchanged
        self.assertEqual(a, {'x': 1, 'y': 2})
        self.assertEqual(b, {'y': 3, 'z': 4})

    def test_nested_merge(self):
        a = {'a': {'b': 1, 'c': 2}}
        b = {'a': {'c': 3, 'd': 4}}
        result = deep_merge(a, b)
        self.assertEqual(result, {'a': {'b': 1, 'c': 3, 'd': 4}})

    def test_empty_dict(self):
        a = {'x': 1}
        b = {}
        result = deep_merge(a, b)
        self.assertEqual(result, {'x': 1})
        result = deep_merge({}, a)
        self.assertEqual(result, {'x': 1})

    def test_non_dict_overwrite(self):
        a = {'a': {'b': 1}}
        b = {'a': 2}
        result = deep_merge(a, b)
        self.assertEqual(result, {'a': 2})

    def test_missing_keys(self):
        a = {'x': 1}
        b = {'y': 2}
        result = deep_merge(a, b)
        self.assertEqual(result, {'x': 1, 'y': 2})

    def test_deep_nested(self):
        a = {'a': {'b': {'c': 1}}}
        b = {'a': {'b': {'d': 2}, 'e': 3}}
        result = deep_merge(a, b)
        self.assertEqual(result, {'a': {'b': {'c': 1, 'd': 2}, 'e': 3}})

if __name__ == '__main__':
    unittest.main()
