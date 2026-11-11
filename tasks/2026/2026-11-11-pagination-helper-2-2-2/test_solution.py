import unittest
from solution import paginate, page_count

class TestPaginationHelper(unittest.TestCase):

    def test_basic_page(self):
        items = list(range(10))
        self.assertEqual(paginate(items, 1, 3), [0, 1, 2])
        self.assertEqual(paginate(items, 2, 3), [3, 4, 5])
        self.assertEqual(paginate(items, 4, 3), [9])

    def test_page_out_of_range(self):
        items = list(range(10))
        self.assertEqual(paginate(items, 5, 3), [])
        self.assertEqual(paginate(items, 99, 10), [])

    def test_invalid_arguments(self):
        items = list(range(10))
        with self.assertRaises(ValueError):
            paginate(items, 0, 3)
        with self.assertRaises(ValueError):
            paginate(items, 1, 0)
        with self.assertRaises(ValueError):
            paginate(items, -1, 3)
        with self.assertRaises(ValueError):
            paginate(items, 1, -5)

    def test_page_count(self):
        self.assertEqual(page_count(10, 3), 4)
        self.assertEqual(page_count(9, 3), 3)
        self.assertEqual(page_count(0, 3), 0)

    def test_page_count_invalid(self):
        with self.assertRaises(ValueError):
            page_count(10, 0)

if __name__ == '__main__':
    unittest.main()
