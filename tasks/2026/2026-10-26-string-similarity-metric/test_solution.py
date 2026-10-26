import unittest
from solution import string_similarity


class TestStringSimilarity(unittest.TestCase):

    def test_identical_strings(self):
        self.assertAlmostEqual(string_similarity("hello", "hello"), 1.0)
        self.assertAlmostEqual(string_similarity("abc", "abc", n=2), 1.0)

    def test_different_strings(self):
        self.assertAlmostEqual(string_similarity("abc", "xyz"), 0.0)
        self.assertAlmostEqual(string_similarity("", "a"), 0.0)
        self.assertAlmostEqual(string_similarity("a", "b", n=2), 0.0)

    def test_partial_similarity(self):
        # "abcdef" vs "abcefg" with n=3 -> Jaccard = 1/7
        self.assertAlmostEqual(string_similarity("abcdef", "abcefg", n=3), 1/7, places=5)
        # with n=2 -> Jaccard = 3/7
        self.assertAlmostEqual(string_similarity("abcdef", "abcefg", n=2), 3/7, places=5)

    def test_edge_cases_empty_strings(self):
        self.assertAlmostEqual(string_similarity("", ""), 1.0)
        self.assertAlmostEqual(string_similarity("", "abc"), 0.0)
        self.assertAlmostEqual(string_similarity("abc", ""), 0.0)

    def test_large_n_gram(self):
        # n larger than both strings
        self.assertAlmostEqual(string_similarity("ab", "cd", n=10), 0.0)
        self.assertAlmostEqual(string_similarity("a", "a", n=2), 1.0)
        self.assertAlmostEqual(string_similarity("a", "b", n=2), 0.0)


if __name__ == '__main__':
    unittest.main()
