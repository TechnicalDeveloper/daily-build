import unittest
from solution import window_hashes


class WindowHashesTests(unittest.TestCase):
    def test_empty_and_too_large_window(self):
        self.assertEqual(window_hashes('', 1), [])
        self.assertEqual(window_hashes('abc', 4), [])

    def test_single_full_window(self):
        text = 'abc'
        expected = [(ord(text[0]) * 257 * 257 + ord(text[1]) * 257 + ord(text[2])) % 1_000_000_007]
        self.assertEqual(window_hashes(text, 3), expected)

    def test_rolling_matches_naive_default_parameters(self):
        text = 'abracadabra'
        size = 3
        base = 257
        modulus = 1_000_000_007

        def naive(chunk):
            h = 0
            for ch in chunk:
                h = (h * base + ord(ch)) % modulus
            return h

        expected = [naive(text[i:i + size]) for i in range(len(text) - size + 1)]
        self.assertEqual(window_hashes(text, size), expected)

    def test_custom_base_and_modulus(self):
        text = 'banana'
        size = 4
        base = 31
        modulus = 10_000_000_007

        def naive(chunk):
            h = 0
            for ch in chunk:
                h = (h * base + ord(ch)) % modulus
            return h

        expected = [naive(text[i:i + size]) for i in range(len(text) - size + 1)]
        self.assertEqual(window_hashes(text, size, base, modulus), expected)

    def test_invalid_arguments(self):
        with self.assertRaises(ValueError):
            window_hashes('abc', 0)
        with self.assertRaises(ValueError):
            window_hashes('abc', -1)
        with self.assertRaises(ValueError):
            window_hashes('abc', 2, modulus=0)


if __name__ == '__main__':
    unittest.main()
