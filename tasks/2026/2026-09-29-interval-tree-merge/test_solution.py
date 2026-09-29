import unittest
from solution import IntervalTree

class TestIntervalTree(unittest.TestCase):
    def setUp(self):
        self.tree = IntervalTree()

    def test_add_and_merge_overlapping(self):
        self.tree.add(1, 3)
        self.tree.add(2, 5)
        self.assertEqual(self.tree.get_intervals(), [(1, 5)])

    def test_add_adjacent(self):
        self.tree.add(1, 2)
        self.tree.add(3, 4)
        self.assertEqual(self.tree.get_intervals(), [(1, 4)])

    def test_remove_partial(self):
        self.tree.add(1, 10)
        self.tree.remove(3, 5)
        self.assertEqual(self.tree.get_intervals(), [(1, 2), (6, 10)])

    def test_remove_multiple_intervals(self):
        self.tree.add(1, 3)
        self.tree.add(5, 7)
        self.tree.add(10, 12)
        self.tree.remove(2, 11)
        self.assertEqual(self.tree.get_intervals(), [(1, 1), (12, 12)])

    def test_remove_outside_range(self):
        self.tree.add(5, 10)
        self.tree.remove(1, 3)
        self.assertEqual(self.tree.get_intervals(), [(5, 10)])

if __name__ == '__main__':
    unittest.main()
