import unittest
from solution import parse_records

class TestParseRecords(unittest.TestCase):
    def test_simple_records(self):
        text = 'name: Alice\nage: 30\n\nname: Bob\nage: 25'
        self.assertEqual(parse_records(text), [
            {'name': 'Alice', 'age': '30'},
            {'name': 'Bob', 'age': '25'},
        ])

    def test_comments_and_blank_lines(self):
        text = '# comment\nname: Alice\n\n  # indented comment\nname: Bob\n\n\n'
        self.assertEqual(parse_records(text), [
            {'name': 'Alice'},
            {'name': 'Bob'},
        ])

    def test_value_contains_colon(self):
        text = 'url: http://example.com:8080/path\n'
        self.assertEqual(parse_records(text), [
            {'url': 'http://example.com:8080/path'}
        ])

    def test_duplicate_key_last_wins(self):
        text = 'k: v1\nk: v2\n'
        self.assertEqual(parse_records(text), [{'k': 'v2'}])

    def test_missing_colon_raises(self):
        with self.assertRaises(ValueError):
            parse_records('this line has no colon\n')

    def test_empty_key_raises(self):
        with self.assertRaises(ValueError):
            parse_records(': value\n')
