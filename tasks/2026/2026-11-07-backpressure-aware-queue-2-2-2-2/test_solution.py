from solution import BackpressureQueue
import unittest

class TestBackpressureQueue(unittest.TestCase):

    def test_push_and_pop(self):
        q = BackpressureQueue(3)
        self.assertTrue(q.push(1))
        self.assertTrue(q.push(2))
        self.assertTrue(q.push(3))
        self.assertEqual(q.pop(), 1)
        self.assertEqual(q.pop(), 2)
        self.assertEqual(q.pop(), 3)
        self.assertTrue(q.empty())

    def test_backpressure_on_full(self):
        q = BackpressureQueue(2)
        self.assertTrue(q.push('a'))
        self.assertTrue(q.push('b'))
        self.assertFalse(q.push('c'))  # backpressure
        self.assertTrue(q.full())
        self.assertEqual(q.size(), 2)

    def test_pop_from_empty_raises(self):
        q = BackpressureQueue(5)
        with self.assertRaises(IndexError):
            q.pop()

    def test_maxsize_zero_always_full(self):
        q = BackpressureQueue(0)
        self.assertTrue(q.full())
        self.assertFalse(q.push(1))
        self.assertEqual(q.size(), 0)

    def test_unlimited_maxsize(self):
        q = BackpressureQueue(None)
        self.assertFalse(q.full())
        for i in range(100):
            self.assertTrue(q.push(i))
        self.assertEqual(q.size(), 100)
        self.assertFalse(q.full())

    def test_negative_maxsize_unlimited(self):
        q = BackpressureQueue(-1)
        self.assertFalse(q.full())
        q.push(1)
        q.push(2)
        self.assertEqual(q.size(), 2)

if __name__ == '__main__':
    unittest.main()
