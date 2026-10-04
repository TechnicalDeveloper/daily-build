import unittest
from solution import paginate

class TestPagination(unittest.TestCase):

    def test_normal_page(self):
        result = paginate(100, 3, 10)
        self.assertEqual(result['page'], 3)
        self.assertEqual(result['start'], 20)
        self.assertEqual(result['end'], 30)
        self.assertEqual(result['total_pages'], 10)
        self.assertTrue(result['has_prev'])
        self.assertTrue(result['has_next'])

    def test_first_page(self):
        result = paginate(100, 1, 10)
        self.assertEqual(result['page'], 1)
        self.assertEqual(result['start'], 0)
        self.assertEqual(result['end'], 10)
        self.assertFalse(result['has_prev'])
        self.assertTrue(result['has_next'])

    def test_last_page(self):
        result = paginate(100, 10, 10)
        self.assertEqual(result['page'], 10)
        self.assertEqual(result['start'], 90)
        self.assertEqual(result['end'], 100)
        self.assertTrue(result['has_prev'])
        self.assertFalse(result['has_next'])

    def test_total_zero(self):
        result = paginate(0, 1, 10)
        self.assertEqual(result['page'], 1)
        self.assertEqual(result['total_pages'], 0)
        self.assertEqual(result['start'], 0)
        self.assertEqual(result['end'], 0)
        self.assertFalse(result['has_prev'])
        self.assertFalse(result['has_next'])

    def test_page_clamped_down(self):
        result = paginate(50, 0, 10)
        self.assertEqual(result['page'], 1)
        self.assertEqual(result['start'], 0)

    def test_page_clamped_up(self):
        result = paginate(25, 5, 10)
        self.assertEqual(result['page'], 3)  # last valid page = 3
        self.assertEqual(result['start'], 20)
        self.assertEqual(result['end'], 25)

    def test_invalid_per_page_raises(self):
        with self.assertRaises(ValueError):
            paginate(10, 1, 0)
        with self.assertRaises(ValueError):
            paginate(10, 1, -5)

if __name__ == '__main__':
    unittest.main()
