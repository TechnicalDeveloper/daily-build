import unittest

from solution import BackpressureQueue, QueueEmpty, QueueFull


class BackpressureQueueTests(unittest.TestCase):
    def test_put_get_fifo_order(self):
        q = BackpressureQueue(3)
        for item in [1, 2, 3]:
            q.put(item)
        self.assertEqual(q.get(), 1)
        self.assertEqual(q.get(), 2)
        self.assertEqual(q.get(), 3)

    def test_get_from_empty_queue_raises_queue_empty(self):
        q = BackpressureQueue(2)
        with self.assertRaises(QueueEmpty):
            q.get()

    def test_put_to_full_queue_raises_queue_full(self):
        q = BackpressureQueue(1)
        q.put('only')
        with self.assertRaises(QueueFull):
            q.put('too much')
        self.assertEqual(q.qsize(), 1)
        self.assertEqual(q.get(), 'only')
        q.put('again')
        self.assertEqual(q.get(), 'again')

    def test_qsize_full_and_empty_flags(self):
        q = BackpressureQueue(2)
        self.assertTrue(q.empty())
        self.assertFalse(q.full())
        self.assertEqual(q.qsize(), 0)

        q.put('a')
        self.assertFalse(q.empty())
        self.assertFalse(q.full())
        self.assertEqual(q.qsize(), 1)

        q.put('b')
        self.assertFalse(q.empty())
        self.assertTrue(q.full())
        self.assertEqual(q.qsize(), 2)

        q.get()
        self.assertFalse(q.full())
        self.assertEqual(q.qsize(), 1)

    def test_invalid_maxsize_rejected(self):
        for bad in (0, -1, 1.5, '3'):
            with self.assertRaises(ValueError):
                BackpressureQueue(bad)
