import unittest
from solution import parse_ini

class TestIniParser(unittest.TestCase):
    def test_basic_sections(self):
        text = """
[server]
host = localhost
port = 8080

[database]
dbname = mydb
user = admin
"""
        result = parse_ini(text)
        self.assertEqual(result['server']['host'], 'localhost')
        self.assertEqual(result['server']['port'], '8080')
        self.assertEqual(result['database']['dbname'], 'mydb')
        self.assertEqual(result['database']['user'], 'admin')

    def test_global_section(self):
        text = "key1=value1\n[sec]\nkey2=value2\n"
        result = parse_ini(text)
        self.assertEqual(result['global']['key1'], 'value1')
        self.assertEqual(result['sec']['key2'], 'value2')

    def test_comments_and_blank_lines(self):
        text = "# comment\n; another comment\n\n[section]\n# comment inside\nkey = value\n"
        result = parse_ini(text)
        self.assertEqual(result['section']['key'], 'value')
        self.assertIn('section', result)

    def test_duplicate_keys_overwrite(self):
        text = "[s]\nkey=first\nkey=second\n"
        result = parse_ini(text)
        self.assertEqual(result['s']['key'], 'second')

    def test_empty_input(self):
        self.assertEqual(parse_ini(""), {})

    def test_invalid_line_raises(self):
        with self.assertRaises(ValueError):
            parse_ini("this is not valid\n")

    def test_key_without_value(self):
        with self.assertRaises(ValueError):
            parse_ini("key\n")

if __name__ == '__main__':
    unittest.main()
