import unittest
from solution import stable_multi_sort

class TestStableMultiSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(stable_multi_sort([], ['a']), [])

    def test_single_item(self):
        data = [{'a': 1}]
        self.assertEqual(stable_multi_sort(data, ['a']), data)

    def test_one_key_sort(self):
        data = [{'a': 3}, {'a': 1}, {'a': 2}]
        expected = [{'a': 1}, {'a': 2}, {'a': 3}]
        self.assertEqual(stable_multi_sort(data, ['a']), expected)

    def test_two_keys_and_stability(self):
        data = [
            {'last': 'Smith', 'first': 'John'},
            {'last': 'Doe', 'first': 'Jane'},
            {'last': 'Smith', 'first': 'Adam'},
            {'last': 'Doe', 'first': 'Alice'},
            {'last': 'Smith', 'first': 'Zoe'}
        ]
        # Sort by last name, then first name (both ascending)
        expected = [
            {'last': 'Doe', 'first': 'Alice'},
            {'last': 'Doe', 'first': 'Jane'},
            {'last': 'Smith', 'first': 'Adam'},
            {'last': 'Smith', 'first': 'John'},
            {'last': 'Smith', 'first': 'Zoe'}
        ]
        self.assertEqual(stable_multi_sort(data, ['last', 'first']), expected)

    def test_original_list_not_modified(self):
        data = [{'a': 2}, {'a': 1}]
        stable_multi_sort(data, ['a'])
        self.assertEqual(data, [{'a': 2}, {'a': 1}])

    def test_all_keys_equal_preserves_order(self):
        data = [
            {'x': 1, 'y': 2},
            {'x': 1, 'y': 2},
            {'x': 1, 'y': 2}
        ]
        self.assertEqual(stable_multi_sort(data, ['x', 'y']), data)

if __name__ == '__main__':
    unittest.main()
