import unittest
from solution import diff

class TestDiff(unittest.TestCase):
    def test_empty_strings(self):
        self.assertEqual(diff("", ""), "")

    def test_identical_strings(self):
        self.assertEqual(diff("abc", "abc"), " a\n b\n c")

    def test_one_string_empty(self):
        self.assertEqual(diff("ab", ""), "-a\n-b")
        self.assertEqual(diff("", "ab"), "+a\n+b")

    def test_no_common_characters(self):
        self.assertEqual(diff("abc", "xyz"), "-a\n-b\n-c\n+x\n+y\n+z")

    def test_replacement(self):
        self.assertEqual(diff("abc", "abd"), " a\n b\n-c\n+d")

    def test_deletion_and_insertion(self):
        self.assertEqual(diff("abcdef", "abdf"), " a\n b\n-c\n d\n-e\n f")
