import unittest
from solution import glob_match

class TestGlobMatch(unittest.TestCase):

    def test_empty_pattern_empty_path(self):
        self.assertTrue(glob_match('', ''))

    def test_star_matches_entire_non_slash_path(self):
        self.assertTrue(glob_match('*', 'hello'))

    def test_star_does_not_cross_slash(self):
        self.assertFalse(glob_match('*', 'a/b'))

    def test_question_mark_single_character(self):
        self.assertTrue(glob_match('a?c', 'abc'))

    def test_question_mark_rejects_slash(self):
        self.assertFalse(glob_match('a?b', 'a/b'))

    def test_literal_exact_match(self):
        self.assertTrue(glob_match('foo/bar', 'foo/bar'))

    def test_literal_no_match(self):
        self.assertFalse(glob_match('foo/bar', 'foo/baz'))

    def test_multiple_stars_and_question_marks(self):
        self.assertTrue(glob_match('a?c/*/e?g', 'abc/x/efg'))

    def test_pattern_with_trailing_star(self):
        self.assertTrue(glob_match('abc/*', 'abc/def'))

    def test_star_matches_empty_in_middle(self):
        self.assertTrue(glob_match('a*b', 'ab'))

if __name__ == '__main__':
    unittest.main()
