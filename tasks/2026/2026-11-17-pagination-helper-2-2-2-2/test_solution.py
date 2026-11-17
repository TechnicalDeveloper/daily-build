import unittest
from solution import Pagination

class TestPagination(unittest.TestCase):
    def test_empty_items(self):
        p = Pagination([])
        self.assertEqual(p.total_pages(), 0)
        self.assertEqual(p.get_page(1), [])
        self.assertFalse(p.has_next(1))
        self.assertFalse(p.has_previous(1))

    def test_basic_pagination(self):
        items = list(range(1, 11))
        p = Pagination(items, page_size=3)
        self.assertEqual(p.total_pages(), 4)
        self.assertEqual(p.get_page(1), [1, 2, 3])
        self.assertEqual(p.get_page(2), [4, 5, 6])
        self.assertEqual(p.get_page(3), [7, 8, 9])
        self.assertEqual(p.get_page(4), [10])
        self.assertTrue(p.has_next(1))
        self.assertFalse(p.has_next(4))
        self.assertFalse(p.has_previous(1))
        self.assertTrue(p.has_previous(2))

    def test_page_out_of_range(self):
        items = [1, 2, 3, 4, 5]
        p = Pagination(items, page_size=2)
        with self.assertRaises(ValueError):
            p.get_page(0)
        with self.assertRaises(ValueError):
            p.get_page(-1)
        self.assertEqual(p.get_page(100), [])

    def test_invalid_page_size(self):
        with self.assertRaises(ValueError):
            Pagination([1, 2, 3], page_size=0)
        with self.assertRaises(ValueError):
            Pagination([1, 2, 3], page_size=-5)

    def test_large_items(self):
        items = list(range(100))
        p = Pagination(items, page_size=10)
        self.assertEqual(p.total_pages(), 10)
        self.assertEqual(p.get_page(1)[0], 0)
        self.assertEqual(p.get_page(2)[0], 10)
        self.assertEqual(len(p.get_page(10)), 10)

if __name__ == '__main__':
    unittest.main()
