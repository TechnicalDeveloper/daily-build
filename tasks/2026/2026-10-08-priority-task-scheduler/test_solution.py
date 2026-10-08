import unittest
from solution import TaskScheduler

class TestTaskScheduler(unittest.TestCase):
    def test_basic_priority(self):
        s = TaskScheduler()
        s.add_task('low', 5, 10)
        s.add_task('high', 1, 10)
        self.assertEqual(s.get_next_task(10), 'high')
        self.assertEqual(s.get_next_task(10), 'low')

    def test_time_order_with_same_priority(self):
        s = TaskScheduler()
        s.add_task('a', 2, 5)
        s.add_task('b', 2, 3)
        # At time 5, both are due; b has earlier due_time
        self.assertEqual(s.get_next_task(5), 'b')
        self.assertEqual(s.get_next_task(5), 'a')

    def test_same_priority_same_time_fifo(self):
        s = TaskScheduler()
        s.add_task('first', 3, 7)
        s.add_task('second', 3, 7)
        self.assertEqual(s.get_next_task(7), 'first')
        self.assertEqual(s.get_next_task(7), 'second')

    def test_no_ready_task(self):
        s = TaskScheduler()
        s.add_task('future', 1, 100)
        self.assertIsNone(s.get_next_task(50))

    def test_past_due_time(self):
        s = TaskScheduler()
        s.add_task('old', 2, 10)
        # current_time is 20, past due_time
        self.assertEqual(s.get_next_task(20), 'old')
        self.assertIsNone(s.get_next_task(20))

    def test_multiple_pending_mixed(self):
        s = TaskScheduler()
        s.add_task('a', 3, 5)
        s.add_task('b', 1, 10)
        s.add_task('c', 2, 8)
        # At time 7: a is due (priority 3), b and c not yet.
        self.assertEqual(s.get_next_task(7), 'a')
        # At time 11: b and c are due; b has priority 1, c has 2
        self.assertEqual(s.get_next_task(11), 'b')
        self.assertEqual(s.get_next_task(11), 'c')
        self.assertIsNone(s.get_next_task(11))

if __name__ == '__main__':
    unittest.main()
