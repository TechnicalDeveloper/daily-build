from solution import stable_multi_sort
import unittest


class TestStableMultiSort(unittest.TestCase):

    def test_sort_by_two_keys(self):
        data = [
            {'name': 'alice', 'age': 25},
            {'name': 'bob', 'age': 20},
            {'name': 'charlie', 'age': 25},
            {'name': 'diana', 'age': 20}
        ]
        result = stable_multi_sort(data, ['age', 'name'])
        expected = [
            {'name': 'bob', 'age': 20},
            {'name': 'diana', 'age': 20},
            {'name': 'alice', 'age': 25},
            {'name': 'charlie', 'age': 25}
        ]
        self.assertEqual(result, expected)

    def test_stability(self):
        data = [
            {'id': 1, 'val': 10},
            {'id': 2, 'val': 10},
            {'id': 3, 'val': 5},
            {'id': 4, 'val': 10}
        ]
        result = stable_multi_sort(data, ['val'])
        ids = [d['id'] for d in result]
        self.assertEqual(ids, [3, 1, 2, 4])

    def test_empty_list(self):
        self.assertEqual(stable_multi_sort([], ['key']), [])

    def test_missing_keys(self):
        data = [
            {'a': 2},
            {'a': 1, 'b': 3},
            {'b': 2}
        ]
        result = stable_multi_sort(data, ['a', 'b'])
        expected = [
            {'b': 2},
            {'a': 1, 'b': 3},
            {'a': 2}
        ]
        self.assertEqual(result, expected)

    def test_callable_key(self):
        data = [
            {'name': 'car', 'price': 20000},
            {'name': 'bus', 'price': 50000},
            {'name': 'bike', 'price': 500}
        ]
        result = stable_multi_sort(data, [lambda d: len(d['name'])])
        expected = [
            {'name': 'car', 'price': 20000},
            {'name': 'bus', 'price': 50000},
            {'name': 'bike', 'price': 500}
        ]
        self.assertEqual(result, expected)

    def test_reverse_sort(self):
        data = [
            {'x': 2, 'y': 1},
            {'x': 1, 'y': 2},
            {'x': 2, 'y': 0}
        ]
        result = stable_multi_sort(data, ['x', 'y'], reverse=True)
        expected = [
            {'x': 2, 'y': 1},
            {'x': 2, 'y': 0},
            {'x': 1, 'y': 2}
        ]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
