import unittest
from solution import chunk

class TestChunk(unittest.TestCase):

    def test_empty_iterable(self):
        self.assertEqual(list(chunk([], 3)), [])

    def test_chunk_size_one(self):
        self.assertEqual(list(chunk([1, 2, 3], 1)), [[1], [2], [3]])

    def test_chunk_size_larger_than_iterable(self):
        self.assertEqual(list(chunk([1, 2], 10)), [[1, 2]])

    def test_exact_multiple(self):
        self.assertEqual(list(chunk([1, 2, 3, 4], 2)), [[1, 2], [3, 4]])

    def test_last_chunk_smaller(self):
        self.assertEqual(list(chunk([1, 2, 3, 4, 5], 2)), [[1, 2], [3, 4], [5]])

    def test_generator_input(self):
        gen = (x for x in range(5))
        self.assertEqual(list(chunk(gen, 3)), [[0, 1, 2], [3, 4]])

    def test_negative_size_raises_value_error(self):
        with self.assertRaises(ValueError):
            list(chunk([1, 2, 3], -1))

    def test_zero_size_raises_value_error(self):
        with self.assertRaises(ValueError):
            list(chunk([1, 2, 3], 0))

    def test_non_int_size_raises_type_error(self):
        with self.assertRaises(TypeError):
            list(chunk([1, 2, 3], 2.5))

if __name__ == '__main__':
    unittest.main()
