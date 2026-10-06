import unittest
from solution import parse_config

class TestParseConfig(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(parse_config(''), {})

    def test_simple_key_value(self):
        text = "name: Alice\nage: 30"
        expected = {'name': 'Alice', 'age': '30'}
        self.assertEqual(parse_config(text), expected)

    def test_whitespace_handling(self):
        text = "  key1  :  value1  \n  key2:value2"
        expected = {'key1': 'value1', 'key2': 'value2'}
        self.assertEqual(parse_config(text), expected)

    def test_comments_and_blanks(self):
        text = "# comment\n\nkey: val\n# another comment"
        expected = {'key': 'val'}
        self.assertEqual(parse_config(text), expected)

    def test_extra_colons(self):
        text = "a:b:c:d"
        expected = {'a': 'b:c:d'}
        self.assertEqual(parse_config(text), expected)

    def test_empty_value(self):
        text = "key:"
        expected = {'key': ''}
        self.assertEqual(parse_config(text), expected)

    def test_duplicate_key_overwrites(self):
        text = "x: first\nx: second"
        expected = {'x': 'second'}
        self.assertEqual(parse_config(text), expected)

    def test_ignore_lines_with_empty_key(self):
        text = ": value\n:val2\nkey: real"
        expected = {'key': 'real'}
        self.assertEqual(parse_config(text), expected)

if __name__ == '__main__':
    unittest.main()
