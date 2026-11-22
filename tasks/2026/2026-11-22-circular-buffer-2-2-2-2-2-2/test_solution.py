import unittest
from solution import CircularBuffer

class TestCircularBuffer(unittest.TestCase):
    def test_basic_append_pop(self):
        cb = CircularBuffer(3)
        cb.append(1)
        cb.append(2)
        cb.append(3)
        self.assertEqual(len(cb), 3)
        self.assertTrue(cb.is_full())
        self.assertEqual(cb.pop(), 1)
        self.assertEqual(cb.pop(), 2)
        self.assertEqual(cb.pop(), 3)
        self.assertTrue(cb.is_empty())

    def test_overwrite_when_full(self):
        cb = CircularBuffer(2)
        cb.append('a')
        cb.append('b')
        cb.append('c')  # overwrites 'a'
        self.assertEqual(cb.peek(), 'b')
        self.assertEqual(cb.pop(), 'b')
        self.assertEqual(cb.pop(), 'c')
        self.assertTrue(cb.is_empty())

    def test_pop_empty_raises(self):
        cb = CircularBuffer(2)
        with self.assertRaises(IndexError):
            cb.pop()
        cb.append(1)
        cb.pop()
        with self.assertRaises(IndexError):
            cb.pop()

    def test_peek_empty_raises(self):
        cb = CircularBuffer(1)
        with self.assertRaises(IndexError):
            cb.peek()

    def test_capacity_validation(self):
        with self.assertRaises(ValueError):
            CircularBuffer(0)
        with self.assertRaises(ValueError):
            CircularBuffer(-1)

    def test_len_and_is_empty(self):
        cb = CircularBuffer(1)
        self.assertTrue(cb.is_empty())
        self.assertEqual(len(cb), 0)
        cb.append('x')
        self.assertFalse(cb.is_empty())
        self.assertEqual(len(cb), 1)
        self.assertTrue(cb.is_full())

if __name__ == '__main__':
    unittest.main()
