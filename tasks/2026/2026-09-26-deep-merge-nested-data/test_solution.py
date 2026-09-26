import unittest
from solution import deep_merge

class TestDeepMerge(unittest.TestCase):
    def test_simple_overwrite(self):
        base = {'a': 1, 'b': 2}
        update = {'b': 3, 'c': 4}
        result = deep_merge(base, update)
        self.assertEqual(result, {'a': 1, 'b': 3, 'c': 4})
        # ensure original not mutated
        self.assertEqual(base, {'a': 1, 'b': 2})

    def test_nested_merge(self):
        base = {'a': {'x': 1, 'y': 2}}
        update = {'a': {'y': 3, 'z': 4}}
        result = deep_merge(base, update)
        self.assertEqual(result, {'a': {'x': 1, 'y': 3, 'z': 4}})

    def test_non_dict_overwrite(self):
        base = {'a': {'x': 1}}
        update = {'a': 'string'}
        result = deep_merge(base, update)
        self.assertEqual(result, {'a': 'string'})

    def test_none_value(self):
        base = {'a': {'x': 1}, 'b': 2}
        update = {'a': None, 'b': 3}
        result = deep_merge(base, update)
        self.assertEqual(result, {'a': None, 'b': 3})

    def test_empty_dicts(self):
        base = {}
        update = {'a': 1}
        result = deep_merge(base, update)
        self.assertEqual(result, {'a': 1})
        result2 = deep_merge(update, {})
        self.assertEqual(result2, {'a': 1})

if __name__ == '__main__':
    unittest.main()
