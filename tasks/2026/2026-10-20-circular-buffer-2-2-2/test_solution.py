import unittest
from solution import CircularBuffer

class TestCircularBuffer(unittest.TestCase):
    def test_enqueue_dequeue_basic(self):
        buf = CircularBuffer(3)
        buf.enqueue(1)
        buf.enqueue(2)
        buf.enqueue(3)
        self.assertEqual(buf.dequeue(), 1)
        self.assertEqual(buf.dequeue(), 2)
        self.assertEqual(buf.dequeue(), 3)
        self.assertTrue(buf.is_empty())

    def test_overwrite_when_full(self):
        buf = CircularBuffer(3)
        buf.enqueue(1)
        buf.enqueue(2)
        buf.enqueue(3)
        buf.enqueue(4)  # overwrites 1
        self.assertEqual(buf.dequeue(), 2)
        self.assertEqual(buf.dequeue(), 3)
        self.assertEqual(buf.dequeue(), 4)
        self.assertTrue(buf.is_empty())

    def test_peek(self):
        buf = CircularBuffer(2)
        buf.enqueue('a')
        buf.enqueue('b')
        self.assertEqual(buf.peek(), 'a')
        buf.dequeue()
        self.assertEqual(buf.peek(), 'b')

    def test_empty_buffer_raises(self):
        buf = CircularBuffer(5)
        with self.assertRaises(IndexError):
            buf.dequeue()
        with self.assertRaises(IndexError):
            buf.peek()

    def test_length_and_full(self):
        buf = CircularBuffer(2)
        self.assertEqual(len(buf), 0)
        self.assertTrue(buf.is_empty())
        self.assertFalse(buf.is_full())
        buf.enqueue(10)
        self.assertEqual(len(buf), 1)
        buf.enqueue(20)
        self.assertEqual(len(buf), 2)
        self.assertTrue(buf.is_full())
        buf.dequeue()
        self.assertEqual(len(buf), 1)
        self.assertFalse(buf.is_full())

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError):
            CircularBuffer(0)
        with self.assertRaises(ValueError):
            CircularBuffer(-1)

if __name__ == '__main__':
    unittest.main()
