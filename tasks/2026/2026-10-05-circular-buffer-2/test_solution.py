import unittest
from solution import CircularBuffer

class TestCircularBuffer(unittest.TestCase):

    def test_append_and_get_fifo(self):
        buf = CircularBuffer(3)
        buf.append(1)
        buf.append(2)
        buf.append(3)
        self.assertEqual(buf.get(), 1)
        self.assertEqual(buf.get(), 2)
        self.assertEqual(buf.get(), 3)
        self.assertTrue(buf.is_empty())

    def test_overwrite_when_full(self):
        buf = CircularBuffer(2)
        buf.append(1)
        buf.append(2)
        self.assertTrue(buf.is_full())
        buf.append(3)  # overwrites 1
        self.assertEqual(buf.get(), 2)
        self.assertEqual(buf.get(), 3)
        self.assertTrue(buf.is_empty())

    def test_empty_peek_get_raise(self):
        buf = CircularBuffer(2)
        with self.assertRaises(IndexError):
            buf.peek()
        with self.assertRaises(IndexError):
            buf.get()

    def test_is_empty_and_full_state(self):
        buf = CircularBuffer(1)
        self.assertTrue(buf.is_empty())
        buf.append('a')
        self.assertTrue(buf.is_full())
        buf.append('b')
        self.assertTrue(buf.is_full())
        self.assertEqual(buf.get(), 'b')
        self.assertTrue(buf.is_empty())

    def test_len_reflects_current_items(self):
        buf = CircularBuffer(4)
        self.assertEqual(len(buf), 0)
        buf.append(10)
        buf.append(20)
        self.assertEqual(len(buf), 2)
        buf.get()
        self.assertEqual(len(buf), 1)

if __name__ == '__main__':
    unittest.main()
