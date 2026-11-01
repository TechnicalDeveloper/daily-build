import unittest
from solution import IntervalTree

class TestIntervalTree(unittest.TestCase):
    def test_add_and_query(self):
        it = IntervalTree()
        it.add((1, 5))
        it.add((10, 15))
        self.assertEqual(it.query(0), 0)
        self.assertEqual(it.query(3), 1)
        self.assertEqual(it.query(10), 1)
        self.assertEqual(it.query(5), 0)

    def test_remove_splits_interval(self):
        it = IntervalTree()
        it.add((0, 10))
        it.remove((3, 7))
        self.assertEqual(it.query(2), 1)
        self.assertEqual(it.query(5), 0)
        self.assertEqual(it.query(8), 1)

    def test_merge_overlap(self):
        it = IntervalTree()
        it.add((1, 4))
        it.add((3, 6))
        it.add((8, 10))
        merged = it.merge()
        self.assertEqual(merged, [[1, 6], [8, 10]])

    def test_empty_after_removal(self):
        it = IntervalTree()
        it.add((2, 8))
        it.remove((2, 8))
        self.assertEqual(it.merge(), [])
        self.assertEqual(it.query(5), 0)

if __name__ == '__main__':
    unittest.main()
