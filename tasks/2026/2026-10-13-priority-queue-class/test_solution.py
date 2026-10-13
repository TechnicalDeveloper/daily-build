import unittest
from solution import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def test_push_pop(self):
        pq = PriorityQueue()
        pq.push(1, "low")
        pq.push(0, "high")
        self.assertEqual(pq.pop(), "high")
        self.assertEqual(pq.pop(), "low")

    def test_empty_exception(self):
        pq = PriorityQueue()
        with self.assertRaises(IndexError):
            pq.pop()
        with self.assertRaises(IndexError):
            pq.peek()

    def test_peek(self):
        pq = PriorityQueue()
        pq.push(2, "second")
        pq.push(1, "first")
        self.assertEqual(pq.peek(), "first")
        self.assertEqual(pq.peek(), "first")
        pq.pop()
        self.assertEqual(pq.peek(), "second")

    def test_order(self):
        pq = PriorityQueue()
        pq.push(3, "c")
        pq.push(1, "a")
        pq.push(2, "b")
        self.assertEqual(pq.pop(), "a")
        self.assertEqual(pq.pop(), "b")
        self.assertEqual(pq.pop(), "c")

    def test_is_empty(self):
        pq = PriorityQueue()
        self.assertTrue(pq.is_empty())
        pq.push(0, "x")
        self.assertFalse(pq.is_empty())
        pq.pop()
        self.assertTrue(pq.is_empty())

if __name__ == "__main__":
    unittest.main()
