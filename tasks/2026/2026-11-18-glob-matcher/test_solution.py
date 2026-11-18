import unittest
from solution import is_match

class TestGlobMatcher(unittest.TestCase):

    def test_basic_equality(self):
        self.assertTrue(is_match("abc", "abc"))
        self.assertFalse(is_match("abc", "abd"))

    def test_star_matches_any(self):
        self.assertTrue(is_match("", "*"))
        self.assertTrue(is_match("anything", "*"))
        self.assertTrue(is_match("a/b/c", "a/*/c"))
        self.assertTrue(is_match("abc", "a*c"))
        self.assertFalse(is_match("ab", "a*c"))

    def test_question_mark_matches_one(self):
        self.assertTrue(is_match("abc", "a?c"))
        self.assertFalse(is_match("ac", "a?c"))
        self.assertTrue(is_match("", ""))

    def test_edge_cases(self):
        self.assertTrue(is_match("", ""))
        self.assertFalse(is_match("a", ""))
        self.assertFalse(is_match("", "?"))
        self.assertTrue(is_match("foo", "**foo"))
        self.assertTrue(is_match("foo", "foo**"))
        self.assertTrue(is_match("abc", "*a*b*c*"))
        self.assertFalse(is_match("abc", "*a*d*"))

if __name__ == '__main__':
    unittest.main()
