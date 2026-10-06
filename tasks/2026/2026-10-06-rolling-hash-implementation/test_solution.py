import unittest
from solution import rolling_hash

class TestRollingHash(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(rolling_hash("", 3), [])

    def test_window_zero(self):
        self.assertEqual(rolling_hash("abc", 0), [])

    def test_window_negative(self):
        self.assertEqual(rolling_hash("abc", -1), [])

    def test_window_larger_than_string(self):
        self.assertEqual(rolling_hash("ab", 3), [])

    def test_single_window_equal_to_string(self):
        # window size equals length -> one hash
        result = rolling_hash("hello", 5)
        self.assertEqual(len(result), 1)
        base, mod = 131, 10**9+7
        h = 0
        for ch in "hello":
            h = (h * base + ord(ch)) % mod
        self.assertEqual(result[0], h)

    def test_normal_rolling(self):
        s = "hello"
        window_size = 2
        base, mod = 131, 10**9+7
        expected = []
        for i in range(len(s) - window_size + 1):
            h = 0
            for ch in s[i:i+window_size]:
                h = (h * base + ord(ch)) % mod
            expected.append(h)
        result = rolling_hash(s, window_size, base, mod)
        self.assertEqual(result, expected)

    def test_rolling_update_correctness(self):
        s = "abcdefghij"
        w = 3
        base, mod = 131, 10**9+7
        direct = []
        for i in range(len(s) - w + 1):
            h = 0
            for ch in s[i:i+w]:
                h = (h * base + ord(ch)) % mod
            direct.append(h)
        result = rolling_hash(s, w, base, mod)
        self.assertEqual(result, direct)

if __name__ == '__main__':
    unittest.main()
