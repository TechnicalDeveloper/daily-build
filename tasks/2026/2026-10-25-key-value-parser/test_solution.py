import unittest
from solution import parse

class TestParse(unittest.TestCase):
    def test_simple_pairs(self):
        text = "name=Alice\nage=30\ncity=New York"
        expected = {"name": "Alice", "age": "30", "city": "New York"}
        self.assertEqual(parse(text), expected)

    def test_comments_and_blanks(self):
        text = "# this is a comment\n\nkey1=val1\n  \nkey2=val2\n# another comment"
        expected = {"key1": "val1", "key2": "val2"}
        self.assertEqual(parse(text), expected)

    def test_edge_cases(self):
        text = "empty=\nmultiple===signs\n  spaced= value with spaces  \ninvalid_no_equal\n\t"
        # empty= gives value ""
        # multiple===signs gives value "==signs" (first = splits)
        # spaced= gives "value with spaces" after strip
        # invalid_no_equal ignored (no =)
        expected = {"empty": "", "multiple": "==signs", "spaced": "value with spaces"}
        self.assertEqual(parse(text), expected)

    def test_empty_string(self):
        self.assertEqual(parse(""), {})

if __name__ == '__main__':
    unittest.main()
