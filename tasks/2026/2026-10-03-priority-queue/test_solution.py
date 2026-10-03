from solution import PriorityQueue
import unittest

class TestPriorityQueue(unittest.TestCase):

    def test_insert_and_extract(self):
        pq = PriorityQueue()
        pq.insert('task1', 3)
        pq.insert('task2', 1)
        pq.insert('task3', 2)
        self.assertEqual(pq.extract_min(), 'task2')
        self.assertEqual(pq.extract_min(), 'task3')
        self.assertEqual(pq.extract_min(), 'task1')

    def test_empty_queue_raises(self):
        pq = PriorityQueue()
        with self.assertRaises(IndexError):
            pq.extract_min()

    def test_duplicate_priorities_fifo(self):
        pq = PriorityQueue()
        pq.insert('A', 1)
        pq.insert('B', 1)
        pq.insert('C', 1)
        self.assertEqual(pq.extract_min(), 'A')
        self.assertEqual(pq.extract_min(), 'B')
        self.assertEqual(pq.extract_min(), 'C')

    def test_size_and_empty(self):
        pq = PriorityQueue()
        self.assertTrue(pq.is_empty())
        self.assertEqual(pq.size(), 0)
        pq.insert('X', 10)
        self.assertFalse(pq.is_empty())
        self.assertEqual(pq.size(), 1)
        pq.extract_min()
        self.assertTrue(pq.is_empty())
        self.assertEqual(pq.size(), 0)

    def test_mixed_priorities(self):
        pq = PriorityQueue()
        pq.insert('a', 5)
        pq.insert('b', 3)
        pq.insert('c', 4)
        pq.insert('d', 3)
        self.assertEqual(pq.extract_min(), 'b')  # priority 3, first among 3's
        self.assertEqual(pq.extract_min(), 'd')  # priority 3, second
        self.assertEqual(pq.extract_min(), 'c')  # priority 4
        self.assertEqual(pq.extract_min(), 'a')  # priority 5

if __name__ == '__main__':
    unittest.main()
