from solution import deep_merge
import unittest

class TestDeepMerge(unittest.TestCase):
    def test_basic_merge(self):
        base = {'a': 1, 'b': 2}
        override = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(deep_merge(base, override), expected)

    def test_nested_dicts(self):
        base = {'a': {'x': 1, 'y': 2}, 'b': 3}
        override = {'a': {'y': 99, 'z': 100}}
        expected = {'a': {'x': 1, 'y': 99, 'z': 100}, 'b': 3}
        self.assertEqual(deep_merge(base, override), expected)

    def test_conflicting_types(self):
        base = {'a': {'inner': 'dict'}}
        override = {'a': 'string'}
        expected = {'a': 'string'}
        self.assertEqual(deep_merge(base, override), expected)

    def test_lists_are_replaced(self):
        base = {'items': [1, 2, 3]}
        override = {'items': [4, 5]}
        expected = {'items': [4, 5]}
        self.assertEqual(deep_merge(base, override), expected)

    def test_empty_and_missing_keys(self):
        base = {}
        override = {'a': 1}
        self.assertEqual(deep_merge(base, override), {'a': 1})
        base2 = {'a': 1}
        override2 = {}
        self.assertEqual(deep_merge(base2, override2), {'a': 1})

if __name__ == '__main__':
    unittest.main()
