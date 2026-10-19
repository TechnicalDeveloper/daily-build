import unittest
from solution import RollingHash

class TestRollingHash(unittest.TestCase):

    def test_empty_string(self):
        rh = RollingHash(256, 1000000007)
        self.assertEqual(rh.hash(""), 0)

    def test_single_character(self):
        rh = RollingHash(256, 1000000007)
        self.assertEqual(rh.hash("a"), ord('a') % 1000000007)

    def known_hashes(self):
        base = 256
        mod = 1000000007
        rh = RollingHash(base, mod)
        s = "abc"
        expected = (ord('a') * base**2 + ord('b') * base + ord('c')) % mod
        self.assertEqual(rh.hash(s), expected)

    def test_update_consistency(self):
        base = 256
        mod = 1000000007
        rh = RollingHash(base, mod)
        s = "hello"
        # hash of first 3 chars
        h1 = rh.hash(s[:3])
        # slide window by one: remove 'h', add 'l'
        h2 = rh.update(h1, 'h', 'l', 3)
        # direct hash of resulting substring "ell"
        h2_direct = rh.hash(s[1:4])
        self.assertEqual(h2, h2_direct)

    def test_update_window_length_one(self):
        base = 10
        mod = 97
        rh = RollingHash(base, mod)
        # hash of single char 'a'
        h1 = rh.hash("a")
        # slide window of length 1: remove 'a', add 'b'
        h2 = rh.update(h1, 'a', 'b', 1)
        # should equal hash of 'b'
        self.assertEqual(h2, rh.hash("b"))

    def test_mod_one(self):
        rh = RollingHash(256, 1)
        self.assertEqual(rh.hash("anything"), 0)
        self.assertEqual(rh.update(0, 'a', 'b', 3), 0)

    def test_same_char_update(self):
        base = 31
        mod = 1000003
        rh = RollingHash(base, mod)
        window = "abc"
        h_win = rh.hash(window)
        # slide window with same left and right char
        h_new = rh.update(h_win, 'a', 'a', 3)
        # hash should be unchanged because we removed 'a' and added same 'a'
        # However note: the window length is 3, after removing 'a' and adding 'a'
        # the resulting string is "bca", not "abc". So hash changes.
        # For hash to be unchanged, the whole window must become identical.
        # That is only possible if the removed char equals the new char
        # AND the rest of the window shifts appropriately. Let's test
        # a case where window chars are all same: "aaa"
        rh2 = RollingHash(base, mod)
        h2 = rh2.hash("aaa")
        h2_new = rh2.update(h2, 'a', 'a', 3)
        self.assertEqual(h2_new, rh2.hash("aaa"))

if __name__ == '__main__':
    unittest.main()
