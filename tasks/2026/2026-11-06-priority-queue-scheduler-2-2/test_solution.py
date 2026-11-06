from solution import PriorityQueue
import unittest

class TestPriorityQueue(unittest.TestCase):
    def test_add_and_get(self):
        pq = PriorityQueue()
        pq.add_task('task1', 2)
        pq.add_task('task2', 1)
        self.assertEqual(pq.get_next_task(), 'task2')
        self.assertEqual(pq.get_next_task(), 'task1')

    def test_priority_order(self):
        pq = PriorityQueue()
        pq.add_task('low', 5)
        pq.add_task('medium', 3)
        pq.add_task('high', 1)
        self.assertEqual(pq.get_next_task(), 'high')
        self.assertEqual(pq.get_next_task(), 'medium')
        self.assertEqual(pq.get_next_task(), 'low')

    def test_priority_tie_fifo(self):
        pq = PriorityQueue()
        pq.add_task('first', 1)
        pq.add_task('second', 1)
        pq.add_task('third', 2)
        self.assertEqual(pq.get_next_task(), 'first')
        self.assertEqual(pq.get_next_task(), 'second')
        self.assertEqual(pq.get_next_task(), 'third')

    def test_empty_exception(self):
        pq = PriorityQueue()
        with self.assertRaises(IndexError):
            pq.get_next_task()

if __name__ == '__main__':
    unittest.main()
