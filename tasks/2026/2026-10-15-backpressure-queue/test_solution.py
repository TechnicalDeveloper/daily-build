import unittest
import threading
import time
from solution import BackpressureQueue, Full, Empty

class TestBackpressureQueue(unittest.TestCase):
    def test_basic_put_get(self):
        q = BackpressureQueue(maxsize=5)
        q.put(1)
        q.put(2)
        self.assertEqual(q.get(), 1)
        self.assertEqual(q.get(), 2)

    def test_blocking_on_full(self):
        q = BackpressureQueue(maxsize=1)
        q.put('a')
        def delayed_get():
            time.sleep(0.2)
            q.get()
        t = threading.Thread(target=delayed_get)
        t.start()
        start = time.monotonic()
        q.put('b')
        elapsed = time.monotonic() - start
        self.assertGreaterEqual(elapsed, 0.15)
        self.assertEqual(q.get(), 'b')
        t.join()

    def test_timeout_put(self):
        q = BackpressureQueue(maxsize=1)
        q.put('a')
        with self.assertRaises(Full):
            q.put('b', timeout=0.1)

    def test_timeout_get(self):
        q = BackpressureQueue(maxsize=1)
        with self.assertRaises(Empty):
            q.get(timeout=0.1)

    def test_blocking_on_empty(self):
        q = BackpressureQueue(maxsize=2)
        def delayed_put():
            time.sleep(0.2)
            q.put('x')
        t = threading.Thread(target=delayed_put)
        t.start()
        start = time.monotonic()
        result = q.get()
        elapsed = time.monotonic() - start
        self.assertGreaterEqual(elapsed, 0.15)
        self.assertEqual(result, 'x')
        t.join()

    def test_multiple_threads(self):
        q = BackpressureQueue(maxsize=3)
        produced = []
        consumed = []
        def producer():
            for i in range(10):
                q.put(i)
        def consumer():
            for _ in range(10):
                consumed.append(q.get())
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        self.assertEqual(sorted(consumed), list(range(10)))

if __name__ == '__main__':
    unittest.main()
