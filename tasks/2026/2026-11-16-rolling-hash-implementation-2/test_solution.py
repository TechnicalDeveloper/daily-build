import unittest
from solution import RollingHash

class TestRollingHash(unittest.TestCase):
    def test_initial_hash_matches_naive(self):
        text = "hello world"
        w = 5
        rh = RollingHash(text, w)
        expected = 0
        for i, ch in enumerate(text[:w]):
            expected = (expected * 256 + ord(ch)) % (10**9 + 7)
        self.assertEqual(rh.get_hash(), expected)

    def test_roll_sequence(self):
        text = "abcdefgh"
        w = 3
        rh = RollingHash(text, w)
        naive_hashes = []
        mod = 10**9 + 7
        for i in range(len(text) - w + 1):
            h = 0
            for ch in text[i:i+w]:
                h = (h * 256 + ord(ch)) % mod
            naive_hashes.append(h)
        self.assertEqual(rh.get_hash(), naive_hashes[0])
        for expected in naive_hashes[1:]:
            self.assertTrue(rh.roll())
            self.assertEqual(rh.get_hash(), expected)
        self.assertFalse(rh.roll())

    def test_window_size_one(self):
        text = "abcde"
        w = 1
        rh = RollingHash(text, w)
        self.assertEqual(rh.get_hash(), ord('a'))
        self.assertTrue(rh.roll())
        self.assertEqual(rh.get_hash(), ord('b'))
        self.assertTrue(rh.roll())
        self.assertTrue(rh.roll())
        self.assertTrue(rh.roll())
        self.assertFalse(rh.roll())

    def test_invalid_initialization(self):
        with self.assertRaises(ValueError):
            RollingHash("abc", 0)
        with self.assertRaises(ValueError):
            RollingHash("abc", 4)
        with self.assertRaises(ValueError):
            RollingHash("", 0)

    def test_roll_at_end_no_change(self):
        text = "abc"
        w = 3
        rh = RollingHash(text, w)
        h0 = rh.get_hash()
        self.assertFalse(rh.roll())
        self.assertEqual(rh.get_hash(), h0)
        self.assertEqual(rh.start, 0)  # start should not move

if __name__ == '__main__':
    unittest.main()
