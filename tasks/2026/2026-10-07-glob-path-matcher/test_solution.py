import unittest
from solution import matches

class TestGlobMatcher(unittest.TestCase):
    def test_exact_match(self):
        self.assertTrue(matches('abc', 'abc'))
        self.assertFalse(matches('abc', 'abd'))

    def test_star_wildcard(self):
        self.assertTrue(matches('a*c', 'abc'))
        self.assertTrue(matches('a*c', 'ac'))
        self.assertTrue(matches('a*c', 'abdc'))
        self.assertTrue(matches('*', ''))
        self.assertFalse(matches('a*c', 'abx'))

    def test_question_mark(self):
        self.assertTrue(matches('a?c', 'abc'))
        self.assertFalse(matches('a?c', 'ac'))
        self.assertFalse(matches('a?c', 'abbc'))

    def test_multiple_stars(self):
        self.assertTrue(matches('*a*b*', 'xayb'))
        self.assertTrue(matches('*a*b*', 'ab'))
        self.assertFalse(matches('*a*b*', 'xayz'))

    def test_no_match(self):
        self.assertFalse(matches('abc', 'ab'))
        self.assertFalse(matches('a*b', 'ac'))

    def test_case_sensitive(self):
        self.assertFalse(matches('A', 'a'))
        self.assertTrue(matches('A', 'A'))

    def test_empty_pattern(self):
        self.assertTrue(matches('', ''))
        self.assertFalse(matches('', 'a'))

if __name__ == '__main__':
    unittest.main()
