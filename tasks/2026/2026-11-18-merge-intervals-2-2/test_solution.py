import unittest
from solution import merge_intervals

class TestMergeIntervals(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(merge_intervals([]), [])

    def test_unsorted_and_overlap(self):
        self.assertEqual(merge_intervals([(5,7), (1,3), (2,6)]), [[1,7]])

    def test_nested(self):
        self.assertEqual(merge_intervals([(1,10), (2,5), (3,7)]), [[1,10]])

    def test_no_overlap(self):
        self.assertEqual(merge_intervals([(1,2), (3,4), (5,6)]), [[1,2], [3,4], [5,6]])

    def test_touch_merge(self):
        self.assertEqual(merge_intervals([(1,2), (2,3), (3,4)]), [[1,4]])

    def test_single_interval(self):
        self.assertEqual(merge_intervals([(3,5)]), [[3,5]])

    def test_negative_and_zero(self):
        self.assertEqual(merge_intervals([(-5,-1), (0,2), (-1,0)]), [[-5,2]])

if __name__ == '__main__':
    unittest.main()
