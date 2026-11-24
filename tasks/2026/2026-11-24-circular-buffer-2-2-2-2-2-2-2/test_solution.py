import unittest
from solution import CircularBuffer

class TestCircularBuffer(unittest.TestCase):
    def test_fifo_order_within_capacity(self):
        buf = CircularBuffer(3)
        for value in (1, 2, 3):
            buf.append(value)
        self.assertEqual(len(buf), 3)
        self.assertEqual(buf.pop(), 1)
        self.assertEqual(buf.pop(), 2)
        self.assertEqual(buf.pop(), 3)
        self.assertTrue(buf.is_empty())

    def test_overwrite_oldest_when_full(self):
        buf = CircularBuffer(3)
        for value in (1, 2, 3):
            buf.append(value)
        buf.append(4)
        buf.append(5)
        self.assertEqual(len(buf), 3)
        self.assertEqual(buf.pop(), 3)
        self.assertEqual(buf.pop(), 4)
        self.assertEqual(buf.pop(), 5)
        self.assertTrue(buf.is_empty())

    def test_wraparound_after_partial_reads(self):
        buf = CircularBuffer(3)
        buf.append(1)
        buf.append(2)
        self.assertEqual(buf.pop(), 1)
        buf.append(3)
        buf.append(4)
        self.assertEqual(buf.pop(), 2)
        self.assertEqual(buf.pop(), 3)
        self.assertEqual(buf.pop(), 4)
        buf.append(5)
        self.assertEqual(buf.pop(), 5)

    def test_capacity_one_buffer_overwrites_every_time(self):
        buf = CircularBuffer(1)
        self.assertTrue(buf.is_empty())
        self.assertFalse(buf.is_full())
        buf.append('a')
        self.assertFalse(buf.is_empty())
        self.assertTrue(buf.is_full())
        self.assertEqual(buf.peek(), 'a')
        buf.append('b')
        self.assertEqual(len(buf), 1)
        self.assertEqual(buf.pop(), 'b')
        self.assertTrue(buf.is_empty())

    def test_empty_pop_and_peek_raise_index_error(self):
        buf = CircularBuffer(2)
        with self.assertRaises(IndexError):
            buf.pop()
        with self.assertRaises(IndexError):
            buf.peek()

    def test_invalid_capacity_raises_value_error(self):
        with self.assertRaises(ValueError):
            CircularBuffer(0)
        with self.assertRaises(ValueError):
            CircularBuffer(-1)

if __name__ == '__main__':
    unittest.main()
