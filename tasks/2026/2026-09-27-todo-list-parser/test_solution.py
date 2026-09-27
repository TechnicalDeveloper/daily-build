from solution import parse_todo
import unittest

class TestParseTodo(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(parse_todo(""), [])

    def test_incomplete_task(self):
        result = parse_todo("- [ ] Buy milk")
        self.assertEqual(len(result), 1)
        self.assertFalse(result[0]["completed"])
        self.assertEqual(result[0]["description"], "Buy milk")

    def test_completed_task(self):
        result = parse_todo("- [x] Finish homework")
        self.assertEqual(len(result), 1)
        self.assertTrue(result[0]["completed"])
        self.assertEqual(result[0]["description"], "Finish homework")

    def test_mixed_tasks(self):
        text = """- [ ] Task 1
- [x] Task 2
- [ ] Task 3"""
        result = parse_todo(text)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0]["description"], "Task 1")
        self.assertFalse(result[0]["completed"])
        self.assertTrue(result[1]["completed"])
        self.assertFalse(result[2]["completed"])

    def test_ignore_non_tasks(self):
        text = """This is a header
- [ ] Valid task
Some comment
- [x] Another task
# maybe a comment line
- [ ] Last task"""
        result = parse_todo(text)
        self.assertEqual(len(result), 3)

    def test_whitespace_handling(self):
        text = """   - [ ]   Buy eggs   
- [x]   Wash dishes   """
        result = parse_todo(text)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["description"], "Buy eggs")
        self.assertFalse(result[0]["completed"])
        self.assertEqual(result[1]["description"], "Wash dishes")
        self.assertTrue(result[1]["completed"])

if __name__ == "__main__":
    unittest.main()
