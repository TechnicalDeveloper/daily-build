import unittest
from solution import stable_sort_by_keys


class TestStableSortByKeys(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(stable_sort_by_keys([], [lambda x: x]), [])

    def test_no_keys_returns_copy(self):
        items = [3, 1, 2]
        result = stable_sort_by_keys(items, [])
        self.assertEqual(result, items)
        self.assertIsNot(result, items)

    def test_single_key_stable(self):
        items = [('a', 1), ('b', 1), ('c', 0)]
        result = stable_sort_by_keys(items, [lambda x: x[1]])
        self.assertEqual(result, [('c', 0), ('a', 1), ('b', 1)])

    def test_multiple_keys_priority(self):
        items = [(1, 2, 'a'), (1, 1, 'b'), (0, 2, 'c'), (0, 1, 'd')]
        result = stable_sort_by_keys(items, [lambda x: x[0], lambda x: x[1]])
        self.assertEqual(result, [(0, 1, 'd'), (0, 2, 'c'), (1, 1, 'b'), (1, 2, 'a')])

    def test_all_keys_equal_keeps_order(self):
        items = [('x', 1, 2), ('y', 1, 2), ('z', 1, 2)]
        key_funcs = [lambda t: t[1], lambda t: t[2]]
        self.assertEqual(stable_sort_by_keys(items, key_funcs), items)

    def test_input_not_mutated(self):
        items = [(1, 2), (1, 1), (0, 0)]
        original = list(items)
        stable_sort_by_keys(items, [lambda x: x[0], lambda x: x[1]])
        self.assertEqual(items, original)


if __name__ == '__main__':
    unittest.main()
