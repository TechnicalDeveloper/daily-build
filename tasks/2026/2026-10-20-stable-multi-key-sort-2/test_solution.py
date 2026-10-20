import unittest
from solution import stable_sort_by_keys

class TestStableSortByKeys(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(stable_sort_by_keys([], [lambda x: x]), [])

    def test_single_key(self):
        items = [3, 1, 4, 1, 5, 9, 2, 6]
        result = stable_sort_by_keys(items, [lambda x: x])
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 6, 9])

    def test_multiple_keys_stable(self):
        # Items where primary key equal, secondary key differs; stable sort must preserve original order
        items = [(1, 'b'), (2, 'a'), (1, 'a')]
        result = stable_sort_by_keys(items, [lambda x: x[0], lambda x: x[1]])
        self.assertEqual(result, [(1, 'a'), (1, 'b'), (2, 'a')])

    def test_multiple_keys_with_ties(self):
        # All keys equal: stable sort must keep original order
        items = ['c', 'a', 'b']
        result = stable_sort_by_keys(items, [lambda x: 0])
        self.assertEqual(result, ['c', 'a', 'b'])

    def test_empty_keys(self):
        items = [2, 0, 1]
        result = stable_sort_by_keys(items, [])
        self.assertEqual(result, [2, 0, 1])

if __name__ == '__main__':
    unittest.main()
