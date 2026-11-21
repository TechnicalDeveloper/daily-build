import unittest
from solution import merge_intervals

class TestMergeIntervals(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(merge_intervals([]), [])

    def test_non_overlapping(self):
        intervals = [(1,3), (4,6), (7,9)]
        self.assertEqual(merge_intervals(intervals), [(1,3), (4,6), (7,9)])

    def test_overlapping(self):
        intervals = [(1,3), (2,6), (8,10), (15,18)]
        self.assertEqual(merge_intervals(intervals), [(1,6), (8,10), (15,18)])

    def test_adjacent(self):
        intervals = [(1,2), (2,3)]
        self.assertEqual(merge_intervals(intervals), [(1,3)])

    def test_unsorted_input(self):
        intervals = [(5,8), (1,3), (2,4)]
        self.assertEqual(merge_intervals(intervals), [(1,4), (5,8)])

if __name__ == '__main__':
    unittest.main()
