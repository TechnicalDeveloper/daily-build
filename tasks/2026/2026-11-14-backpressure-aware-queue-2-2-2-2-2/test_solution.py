import unittest
import threading
import time
import queue as queue_module
from solution import BackpressureQueue

class TestBackpressureQueue(unittest.TestCase):
    def test_put_get(self):
        q = BackpressureQueue(maxsize=2)
        q.put(1)
        q.put(2)
        self.assertEqual(q.qsize(), 2)
        self.assertEqual(q.get(), 1)
        self.assertEqual(q.get(), 2)
        self.assertEqual(q.qsize(), 0)

    def test_put_blocking_when_full(self):
        q = BackpressureQueue(maxsize=1)
        q.put('a')
        result = []
        def producer():
            try:
                q.put('b', timeout=0.1)
            except queue_module.Full:
                result.append('full')
        t = threading.Thread(target=producer)
        t.start()
        t.join()
        self.assertEqual(result, ['full'])

        # Test that get unblocks a blocked put
        q = BackpressureQueue(maxsize=1)
        q.put('x')
        result = []
        def producer():
            q.put('y')
            result.append('put done')
        t = threading.Thread(target=producer)
        t.start()
        time.sleep(0.05)
        self.assertEqual(q.get(), 'x')
        t.join(timeout=1)
        self.assertFalse(t.is_alive())
        self.assertEqual(result, ['put done'])

    def test_get_blocking_when_empty(self):
        q = BackpressureQueue(maxsize=2)
        result = []
        def consumer():
            try:
                q.get(timeout=0.1)
            except queue_module.Empty:
                result.append('empty')
        t = threading.Thread(target=consumer)
        t.start()
        t.join()
        self.assertEqual(result, ['empty'])

        # Test that put unblocks a blocked get
        q = BackpressureQueue(maxsize=2)
        result = []
        def consumer():
            result.append(q.get())
        t = threading.Thread(target=consumer)
        t.start()
        time.sleep(0.05)
        q.put('data')
        t.join(timeout=1)
        self.assertFalse(t.is_alive())
        self.assertEqual(result, ['data'])

    def test_timeout_zero(self):
        q = BackpressureQueue(maxsize=1)
        q.put('a')
        with self.assertRaises(queue_module.Full):
            q.put('b', timeout=0)
        q.get()
        with self.assertRaises(queue_module.Empty):
            q.get(timeout=0)

    def test_non_blocking(self):
        q = BackpressureQueue(maxsize=1)
        with self.assertRaises(queue_module.Empty):
            q.get(block=False)
        q.put('a')
        with self.assertRaises(queue_module.Full):
            q.put('b', block=False)
        self.assertEqual(q.get(block=False), 'a')

if __name__ == '__main__':
    unittest.main()
