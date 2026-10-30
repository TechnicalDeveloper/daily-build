import unittest
from solution import match_path


class TestMatchPath(unittest.TestCase):
    def test_simple_star(self):
        self.assertTrue(match_path('foo/*.txt', 'foo/bar.txt'))
        self.assertFalse(match_path('foo/*.txt', 'foo/bar/baz.txt'))
        self.assertTrue(match_path('foo/*', 'foo/'))

    def test_question_mark(self):
        self.assertTrue(match_path('a?c', 'abc'))
        self.assertFalse(match_path('a?c', 'ac'))
        self.assertFalse(match_path('a?c', 'a/c'))

    def test_double_star(self):
        self.assertTrue(match_path('a/**/b', 'a/b'))
        self.assertTrue(match_path('a/**/b', 'a/x/y/b'))
        self.assertFalse(match_path('a/**/b', 'a/x/y/c'))
        self.assertTrue(match_path('**/foo', 'bar/baz/foo'))
        self.assertTrue(match_path('**/foo', 'foo'))
        self.assertTrue(match_path('foo/**', 'foo/bar/baz'))

    def test_invalid_double_star(self):
        with self.assertRaises(ValueError):
            match_path('a**b', 'ab')
        with self.assertRaises(ValueError):
            match_path('a/**b', 'a/b')
        with self.assertRaises(ValueError):
            match_path('a**/b', 'a/b')

    def test_edge_cases(self):
        self.assertTrue(match_path('', ''))
        self.assertFalse(match_path('', 'a'))
        self.assertTrue(match_path('*', ''))
        self.assertFalse(match_path('*', 'a/b'))
        self.assertTrue(match_path('**', 'a/b/c'))
        self.assertTrue(match_path('**', ''))
        self.assertTrue(match_path('a/**/b/**/c', 'a/b/c'))
        self.assertTrue(match_path('a/**/b/**/c', 'a/x/b/y/c'))


if __name__ == '__main__':
    unittest.main()
