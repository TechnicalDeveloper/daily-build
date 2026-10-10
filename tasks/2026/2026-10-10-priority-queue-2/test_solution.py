import unittest
from solution import PriorityQueue

class TestPriorityQueue(unittest.TestCase):

    def test_basic_order(self):
        pq = PriorityQueue()
        pq.push(2, 'second')
        pq.push(1, 'first')
        self.assertEqual(pq.pop(), 'first')
        self.assertEqual(pq.pop(), 'second')

    def test_same_priority_fifo(self):
        pq = PriorityQueue()
        pq.push(1, 'a')
        pq.push(1, 'b')
        pq.push(1, 'c')
        self.assertEqual(pq.pop(), 'a')
        self.assertEqual(pq.pop(), 'b')
        self.assertEqual(pq.pop(), 'c')

    def test_empty_raises(self):
        pq = PriorityQueue()
        with self.assertRaises(IndexError):
            pq.pop()

    def test_len(self):
        pq = PriorityQueue()
        self.assertEqual(len(pq), 0)
        pq.push(1, 'item')
        self.assertEqual(len(pq), 1)
        pq.pop()
        self.assertEqual(len(pq), 0)

    def test_mixed_priorities(self):
        pq = PriorityQueue()
        pq.push(3, 'low')
        pq.push(1, 'high')
        pq.push(2, 'medium')
        self.assertEqual(pq.pop(), 'high')
        self.assertEqual(pq.pop(), 'medium')
        self.assertEqual(pq.pop(), 'low')

if __name__ == '__main__':
    unittest.main()
