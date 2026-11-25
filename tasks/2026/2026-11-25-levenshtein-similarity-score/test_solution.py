import unittest
from solution import similarity

class LevenshteinSimilarityTest(unittest.TestCase):
    def test_identical_strings_return_one(self):
        self.assertEqual(similarity('same', 'same'), 1.0)
        self.assertEqual(similarity('', ''), 1.0)

    def test_empty_and_nonempty_returns_zero(self):
        self.assertEqual(similarity('', 'hello'), 0.0)
        self.assertEqual(similarity('hello', ''), 0.0)

    def test_completely_different_equal_length_strings(self):
        self.assertEqual(similarity('abc', 'xyz'), 0.0)

    def test_single_substitution(self):
        self.assertAlmostEqual(similarity('kitten', 'sitten'), 1.0 - 1.0 / 6.0)

    def test_insertion_and_deletion(self):
        self.assertAlmostEqual(similarity('cat', 'catch'), 1.0 - 2.0 / 5.0)

    def test_transposition_is_two_edits(self):
        self.assertEqual(similarity('ab', 'ba'), 0.0)

    def test_case_sensitive(self):
        self.assertLess(similarity('Cat', 'cat'), 1.0)

if __name__ == '__main__':
    unittest.main()
