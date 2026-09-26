import unittest
from solution import CircularBuffer

class TestCircularBuffer(unittest.TestCase):
    def test_put_and_get(self):
        buf = CircularBuffer(3)
        buf.put(1)
        buf.put(2)
        buf.put(3)
        self.assertEqual(buf.get(), 1)
        self.assertEqual(buf.get(), 2)
        self.assertEqual(buf.get(), 3)
        self.assertTrue(buf.is_empty())

    def test_overwrite(self):
        buf = CircularBuffer(3)
        buf.put(1)
        buf.put(2)
        buf.put(3)
        buf.put(4)  # overwrites 1
        self.assertEqual(buf.get(), 2)  # oldest now is 2
        buf.put(5)  # overwrites 2?
        self.assertEqual(buf.get(), 3)
        self.assertEqual(buf.get(), 4)
        self.assertEqual(buf.get(), 5)
        self.assertTrue(buf.is_empty())

    def test_empty_buffer_raises(self):
        buf = CircularBuffer(2)
        with self.assertRaises(IndexError):
            buf.get()

    def test_empty_and_full_states(self):
        buf = CircularBuffer(2)
        self.assertTrue(buf.is_empty())
        self.assertFalse(buf.is_full())
        buf.put('a')
        self.assertFalse(buf.is_empty())
        self.assertFalse(buf.is_full())
        buf.put('b')
        self.assertFalse(buf.is_empty())
        self.assertTrue(buf.is_full())
        buf.get()
        self.assertFalse(buf.is_empty())
        self.assertFalse(buf.is_full())
        buf.get()
        self.assertTrue(buf.is_empty())
        self.assertFalse(buf.is_full())

    def test_capacity_one(self):
        buf = CircularBuffer(1)
        self.assertTrue(buf.is_empty())
        buf.put('x')
        self.assertTrue(buf.is_full())
        self.assertEqual(buf.get(), 'x')
        self.assertTrue(buf.is_empty())
        buf.put('y')
        self.assertEqual(buf.get(), 'y')
        # overwrite
        buf.put('a')
        buf.put('b')  # overwrites 'a'
        self.assertEqual(buf.get(), 'b')
        self.assertTrue(buf.is_empty())

if __name__ == '__main__':
    unittest.main()
