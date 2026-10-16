import unittest
from solution import PriorityScheduler

class TestPriorityScheduler(unittest.TestCase):

    def test_basic_add_and_get(self):
        scheduler = PriorityScheduler()
        scheduler.add_task("task1", priority=1)
        scheduler.add_task("task2", priority=2)
        self.assertEqual(scheduler.get_next_task(), "task2")  # higher priority first
        self.assertEqual(scheduler.get_next_task(), "task1")
        self.assertTrue(scheduler.is_empty())

    def test_priority_order(self):
        scheduler = PriorityScheduler()
        scheduler.add_task("low", priority=1)
        scheduler.add_task("high", priority=10)
        scheduler.add_task("medium", priority=5)
        self.assertEqual(scheduler.get_next_task(), "high")
        self.assertEqual(scheduler.get_next_task(), "medium")
        self.assertEqual(scheduler.get_next_task(), "low")

    def test_equal_priority_fifo(self):
        scheduler = PriorityScheduler()
        scheduler.add_task("first", priority=5)
        scheduler.add_task("second", priority=5)
        scheduler.add_task("third", priority=5)
        self.assertEqual(scheduler.get_next_task(), "first")
        self.assertEqual(scheduler.get_next_task(), "second")
        self.assertEqual(scheduler.get_next_task(), "third")

    def test_peek(self):
        scheduler = PriorityScheduler()
        scheduler.add_task("top", priority=100)
        scheduler.add_task("bottom", priority=1)
        self.assertEqual(scheduler.peek(), "top")
        self.assertEqual(scheduler.size(), 2)  # peek does not remove
        self.assertEqual(scheduler.get_next_task(), "top")
        self.assertEqual(scheduler.peek(), "bottom")

    def test_empty_queue_raises(self):
        scheduler = PriorityScheduler()
        with self.assertRaises(IndexError):
            scheduler.get_next_task()
        with self.assertRaises(IndexError):
            scheduler.peek()
        self.assertTrue(scheduler.is_empty())
        self.assertEqual(scheduler.size(), 0)

    def test_negative_and_zero_priority(self):
        scheduler = PriorityScheduler()
        scheduler.add_task("neg", priority=-5)
        scheduler.add_task("zero", priority=0)
        scheduler.add_task("pos", priority=3)
        # Order: pos (3) > zero (0) > neg (-5)
        self.assertEqual(scheduler.get_next_task(), "pos")
        self.assertEqual(scheduler.get_next_task(), "zero")
        self.assertEqual(scheduler.get_next_task(), "neg")

    def test_size_and_is_empty(self):
        scheduler = PriorityScheduler()
        self.assertTrue(scheduler.is_empty())
        self.assertEqual(scheduler.size(), 0)
        scheduler.add_task("a", priority=1)
        self.assertFalse(scheduler.is_empty())
        self.assertEqual(scheduler.size(), 1)
        scheduler.add_task("b", priority=2)
        self.assertEqual(scheduler.size(), 2)
        scheduler.get_next_task()
        self.assertEqual(scheduler.size(), 1)
        scheduler.get_next_task()
        self.assertTrue(scheduler.is_empty())

if __name__ == "__main__":
    unittest.main()
