import unittest
import threading
import time
import queue
from solution import BackpressureQueue

class TestBackpressureQueue(unittest.TestCase):
    def test_put_get_order(self):
        q = BackpressureQueue(maxsize=3)
        for i in range(3):
            q.put(i)
        self.assertTrue(q.full())
        for i in range(3):
            self.assertEqual(q.get(), i)
        self.assertTrue(q.empty())

    def test_get_when_empty_blocks_with_timeout(self):
        q = BackpressureQueue(maxsize=2)
        start = time.time()
        with self.assertRaises(queue.Empty):
            q.get(block=True, timeout=0.1)
        elapsed = time.time() - start
        self.assertGreaterEqual(elapsed, 0.1)
        self.assertLess(elapsed, 0.5)

    def test_put_when_full_blocks_with_timeout(self):
        q = BackpressureQueue(maxsize=2)
        q.put(1)
        q.put(2)
        start = time.time()
        with self.assertRaises(queue.Full):
            q.put(3, block=True, timeout=0.1)
        elapsed = time.time() - start
        self.assertGreaterEqual(elapsed, 0.1)

    def test_non_blocking_operations(self):
        q = BackpressureQueue(maxsize=2)
        q.put_nowait(1)
        q.put_nowait(2)
        with self.assertRaises(queue.Full):
            q.put_nowait(3)
        self.assertEqual(q.get_nowait(), 1)
        self.assertEqual(q.get_nowait(), 2)
        with self.assertRaises(queue.Empty):
            q.get_nowait()

    def test_concurrent_put_get(self):
        q = BackpressureQueue(maxsize=2)
        results = []
        def producer():
            for i in range(4):
                q.put(i)
        def consumer():
            for _ in range(4):
                results.append(q.get())
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start(); t2.start()
        t1.join(); t2.join()
        self.assertEqual(results, [0,1,2,3])

if __name__ == '__main__':
    unittest.main()
