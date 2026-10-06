import unittest
from solution import get_page_info

class TestPaginationHelper(unittest.TestCase):
    def test_normal_case(self):
        result = get_page_info(25, 10, 2)
        self.assertEqual(result['page'], 2)
        self.assertEqual(result['total_pages'], 3)
        self.assertEqual(result['start_index'], 10)
        self.assertEqual(result['end_index'], 19)
        self.assertTrue(result['has_previous'])
        self.assertTrue(result['has_next'])

    def test_zero_items(self):
        result = get_page_info(0, 10, 1)
        self.assertEqual(result['page'], 1)
        self.assertEqual(result['total_pages'], 1)
        self.assertEqual(result['start_index'], 0)
        self.assertEqual(result['end_index'], 0)
        self.assertFalse(result['has_previous'])
        self.assertFalse(result['has_next'])

    def test_current_page_too_high(self):
        result = get_page_info(5, 10, 100)
        self.assertEqual(result['page'], 1)  # only one page
        self.assertEqual(result['start_index'], 0)
        self.assertEqual(result['end_index'], 4)
        self.assertFalse(result['has_next'])

    def test_current_page_too_low(self):
        result = get_page_info(20, 10, -5)
        self.assertEqual(result['page'], 1)
        self.assertEqual(result['start_index'], 0)
        self.assertEqual(result['end_index'], 9)
        self.assertTrue(result['has_next'])

    def test_page_size_zero_raises(self):
        with self.assertRaises(ValueError):
            get_page_info(10, 0, 1)

if __name__ == '__main__':
    unittest.main()
