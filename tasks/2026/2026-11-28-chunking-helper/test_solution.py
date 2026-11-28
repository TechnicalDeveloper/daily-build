import unittest
from solution import chunk

class TestChunk(unittest.TestCase):
    def test_chunk_basic(self):
        result = list(chunk([1,2,3,4,5,6,7,8,9,10], 3))
        self.assertEqual(result, [[1,2,3],[4,5,6],[7,8,9],[10]])

    def test_chunk_empty(self):
        result = list(chunk([], 3))
        self.assertEqual(result, [])

    def test_chunk_size_larger_than_length(self):
        result = list(chunk([1,2], 5))
        self.assertEqual(result, [[1,2]])

    def test_chunk_invalid_size(self):
        with self.assertRaises(ValueError):
            list(chunk([1,2], 0))
        with self.assertRaises(ValueError):
            list(chunk([1,2], -1))

    def test_chunk_with_generator(self):
        gen = (x for x in range(5))
        result = list(chunk(gen, 2))
        self.assertEqual(result, [[0,1],[2,3],[4]])

if __name__ == '__main__':
    unittest.main()
