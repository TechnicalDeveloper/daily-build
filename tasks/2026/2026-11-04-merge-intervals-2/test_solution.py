import unittest
from solution import merge_intervals

class TestMergeIntervals(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(merge_intervals([]), [])

    def test_no_overlap(self):
        intervals = [(1,2), (3,4), (5,6)]
        expected = [(1,2), (3,4), (5,6)]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_full_overlap(self):
        intervals = [(1,5), (2,3), (4,6)]
        expected = [(1,6)]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_touching_intervals(self):
        intervals = [(1,2), (2,3), (3,4)]
        expected = [(1,4)]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_single_interval(self):
        intervals = [(5,10)]
        expected = [(5,10)]
        self.assertEqual(merge_intervals(intervals), expected)

if __name__ == '__main__':
    unittest.main()
