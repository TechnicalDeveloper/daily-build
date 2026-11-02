import unittest
from solution import chunk

class TestChunk(unittest.TestCase):
    def test_chunk_basic(self):
        self.assertEqual(list(chunk([1,2,3,4,5,6], 2)), [[1,2],[3,4],[5,6]])

    def test_chunk_remainder(self):
        self.assertEqual(list(chunk([1,2,3,4,5], 2)), [[1,2],[3,4],[5]])

    def test_chunk_empty(self):
        self.assertEqual(list(chunk([], 3)), [])

    def test_chunk_single_large_size(self):
        self.assertEqual(list(chunk([1,2], 10)), [[1,2]])

    def test_chunk_generator(self):
        gen = (i for i in range(5))
        self.assertEqual(list(chunk(gen, 2)), [[0,1],[2,3],[4]])

    def test_chunk_invalid_size_zero(self):
        with self.assertRaises(ValueError):
            list(chunk([1], 0))

    def test_chunk_invalid_size_negative(self):
        with self.assertRaises(ValueError):
            list(chunk([1], -1))

if __name__ == '__main__':
    unittest.main()
