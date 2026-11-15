import unittest
from solution import chunk

class TestChunk(unittest.TestCase):
    def test_normal_chunking(self):
        self.assertEqual(chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_empty_sequence(self):
        self.assertEqual(chunk([], 3), [])

    def test_size_larger_than_sequence(self):
        self.assertEqual(chunk([1, 2], 5), [[1, 2]])

    def test_size_one(self):
        self.assertEqual(chunk([1, 2, 3], 1), [[1], [2], [3]])

    def test_invalid_size_raises(self):
        with self.assertRaises(ValueError):
            chunk([1, 2], 0)
        with self.assertRaises(ValueError):
            chunk([1, 2], -3)

if __name__ == '__main__':
    unittest.main()
