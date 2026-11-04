from solution import stable_multi_sort
import unittest

class TestStableMultiSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(stable_multi_sort([], [lambda x: x]), [])

    def test_single_key(self):
        items = [3, 1, 2]
        self.assertEqual(stable_multi_sort(items, [lambda x: x]), [1, 2, 3])

    def test_multiple_keys_ties(self):
        # Items: (primary=1, secondary varies).
        # Stability: items with same primary retain original order.
        items = [(1, 'a'), (1, 'b'), (2, 'c'), (1, 'c')]
        # primary key = first element, secondary = second element (string)
        keys = [lambda x: x[0], lambda x: x[1]]
        # Expected: primary 1 items keep order: (1,'a'), (1,'b'), (1,'c'), then (2,'c')
        expected = [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'c')]
        self.assertEqual(stable_multi_sort(items, keys), expected)

    def test_stability_all_keys_equal(self):
        items = [{'a': 5}, {'a': 5}, {'a': 5}]
        keys = [lambda x: x['a']]
        # All keys equal; must preserve original order (and they are distinct objects)
        result = stable_multi_sort(items, keys)
        self.assertIs(result[0], items[0])
        self.assertIs(result[1], items[1])
        self.assertIs(result[2], items[2])

    def test_priority_of_keys(self):
        # Primary key overrides secondary
        items = [(1, 3), (2, 1), (1, 2)]
        keys = [lambda x: x[0], lambda x: x[1]]
        expected = [(1, 2), (1, 3), (2, 1)]
        self.assertEqual(stable_multi_sort(items, keys), expected)

if __name__ == '__main__':
    unittest.main()
