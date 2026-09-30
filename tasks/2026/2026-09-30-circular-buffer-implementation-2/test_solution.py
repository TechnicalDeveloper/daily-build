import unittest
from solution import CircularBuffer

class TestCircularBuffer(unittest.TestCase):
    def test_enqueue_dequeue(self):
        buf = CircularBuffer(3)
        buf.enqueue(1)
        buf.enqueue(2)
        buf.enqueue(3)
        self.assertEqual(buf.dequeue(), 1)
        self.assertEqual(buf.dequeue(), 2)
        self.assertEqual(buf.dequeue(), 3)
        self.assertTrue(buf.is_empty())

    def test_overwrite_on_full(self):
        buf = CircularBuffer(2)
        buf.enqueue('a')
        buf.enqueue('b')
        buf.enqueue('c')  # overwrites 'a'
        self.assertEqual(buf.dequeue(), 'b')
        self.assertEqual(buf.dequeue(), 'c')
        self.assertTrue(buf.is_empty())

    def test_dequeue_empty_raises(self):
        buf = CircularBuffer(3)
        with self.assertRaises(IndexError):
            buf.dequeue()

    def test_peek_empty_raises(self):
        buf = CircularBuffer(3)
        with self.assertRaises(IndexError):
            buf.peek()

    def test_peek_returns_oldest(self):
        buf = CircularBuffer(3)
        buf.enqueue(10)
        buf.enqueue(20)
        self.assertEqual(buf.peek(), 10)
        buf.dequeue()
        self.assertEqual(buf.peek(), 20)

    def test_size_and_full(self):
        buf = CircularBuffer(3)
        self.assertEqual(buf.size(), 0)
        self.assertFalse(buf.is_full())
        buf.enqueue(1)
        buf.enqueue(2)
        buf.enqueue(3)
        self.assertEqual(buf.size(), 3)
        self.assertTrue(buf.is_full())
        buf.dequeue()
        self.assertEqual(buf.size(), 2)
        self.assertFalse(buf.is_full())

if __name__ == '__main__':
    unittest.main()
