import unittest
from solution import dice_similarity

class TestDiceSimilarity(unittest.TestCase):

    def test_identical_strings(self):
        self.assertAlmostEqual(dice_similarity("night", "night"), 1.0)
        self.assertAlmostEqual(dice_similarity("abc", "abc"), 1.0)

    def test_no_overlap(self):
        self.assertAlmostEqual(dice_similarity("abc", "def"), 0.0)
        self.assertAlmostEqual(dice_similarity("xyz", "abc"), 0.0)

    def test_partial_overlap(self):
        # "ab" and "bc" share bigram "b"? Wait: "ab" has bigrams {"ab"}, "bc" has {"bc"} -> no overlap.
        # Better case: "abc" -> {"ab","bc"}; "bcd" -> {"bc","cd"} -> intersect {"bc"} -> size_s1=2, size_s2=2 -> 2*1/(2+2)=0.5
        self.assertAlmostEqual(dice_similarity("abc", "bcd"), 0.5)
        # "night" and "nacht": bigrams: "ni","ig","gh","ht" vs "na","ac","ch","ht" -> only "ht" -> 2*1/(4+4)=0.25
        self.assertAlmostEqual(dice_similarity("night", "nacht"), 0.25)

    def test_empty_strings(self):
        self.assertEqual(dice_similarity("", ""), 1.0)
        self.assertEqual(dice_similarity("", "abc"), 0.0)
        self.assertEqual(dice_similarity("abc", ""), 0.0)

    def test_single_character_strings(self):
        # Strings with length 1 produce no bigrams, hence 0.0 (unless both empty, already tested)
        self.assertEqual(dice_similarity("a", "b"), 0.0)
        self.assertEqual(dice_similarity("a", "a"), 0.0)
        self.assertEqual(dice_similarity("ab", "a"), 0.0)

if __name__ == '__main__':
    unittest.main()
