import unittest
from solution import stable_sort_by_keys

class TestStableSortByKeys(unittest.TestCase):
    
    def test_multiple_keys_ascending(self):
        data = [
            {"name": "Alice", "age": 30, "score": 90},
            {"name": "Bob", "age": 25, "score": 95},
            {"name": "Charlie", "age": 30, "score": 85},
            {"name": "Diana", "age": 25, "score": 90},
        ]
        # Sort by age ascending, then score ascending.
        key_age = lambda d: d["age"]
        key_score = lambda d: d["score"]
        result = stable_sort_by_keys(data, [key_age, key_score])
        expected = [
            {"name": "Diana", "age": 25, "score": 90},
            {"name": "Bob", "age": 25, "score": 95},
            {"name": "Charlie", "age": 30, "score": 85},
            {"name": "Alice", "age": 30, "score": 90},
        ]
        self.assertEqual(result, expected)

    def test_stability(self):
        # Items with same keys should keep original order.
        data = [
            {"id": 1, "group": "b", "val": 10},
            {"id": 2, "group": "a", "val": 20},
            {"id": 3, "group": "b", "val": 30},
            {"id": 4, "group": "a", "val": 20},
            {"id": 5, "group": "b", "val": 10},
        ]
        # Sort by group.
        result = stable_sort_by_keys(data, [lambda d: d["group"]])
        groups = [d["group"] for d in result]
        self.assertEqual(groups, ["a", "a", "b", "b", "b"])
        # For equal groups, preserve original order relative to each other.
        a_items = [d["id"] for d in result if d["group"] == "a"]
        b_items = [d["id"] for d in result if d["group"] == "b"]
        self.assertEqual(a_items, [2, 4])  # original order: 2 then 4
        self.assertEqual(b_items, [1, 3, 5])  # original order: 1 then 3 then 5

    def test_none_keys_sort_first(self):
        data = [
            {"name": "A", "value": None},
            {"name": "B", "value": 3},
            {"name": "C", "value": 1},
            {"name": "D", "value": None},
        ]
        key_value = lambda d: d["value"]
        result = stable_sort_by_keys(data, [key_value])
        names = [d["name"] for d in result]
        self.assertEqual(names, ["A", "D", "C", "B"])  # None then 1 then 3

    def test_empty_iterable(self):
        self.assertEqual(stable_sort_by_keys([], [lambda x: x]), [])

    def test_no_key_funcs_preserves_order(self):
        data = [3, 1, 2]
        self.assertEqual(stable_sort_by_keys(data, []), data)

if __name__ == "__main__":
    unittest.main()
