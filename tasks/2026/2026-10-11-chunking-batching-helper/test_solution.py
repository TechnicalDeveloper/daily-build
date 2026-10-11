import unittest
from solution import chunked

class TestChunked(unittest.TestCase):

    def test_basic_chunking(self):
        self.assertEqual(
            list(chunked([1, 2, 3, 4, 5], 2)),
            [[1, 2], [3, 4], [5]]
        )

    def test_exact_multiple(self):
        self.assertEqual(
            list(chunked([1, 2, 3, 4], 2)),
            [[1, 2], [3, 4]]
        )

    def test_size_greater_than_length(self):
        self.assertEqual(
            list(chunked([1, 2], 5)),
            [[1, 2]]
        )

    def test_empty_iterable(self):
        self.assertEqual(list(chunked([], 3)), [])

    def test_invalid_size_raises(self):
        with self.assertRaises(ValueError):
            list(chunked([1, 2], 0))
        with self.assertRaises(ValueError):
            list(chunked([1, 2], -1))

    def test_generator_input(self):
        gen = (x for x in range(5))
        self.assertEqual(
            list(chunked(gen, 2)),
            [[0, 1], [2, 3], [4]]
        )

if __name__ == "__main__":
    unittest.main()
