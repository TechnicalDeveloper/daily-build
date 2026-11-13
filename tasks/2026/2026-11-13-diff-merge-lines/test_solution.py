import unittest
from solution import diff_lines, apply_patch

class TestDiffLines(unittest.TestCase):

    def test_simple_insertion(self):
        old = ["a", "c"]
        new = ["a", "b", "c"]
        ops = diff_lines(old, new)
        self.assertEqual(ops, [
            ('equal', 'a'),
            ('insert', 'b'),
            ('equal', 'c'),
        ])

    def test_simple_deletion(self):
        old = ["a", "b", "c"]
        new = ["a", "c"]
        ops = diff_lines(old, new)
        self.assertEqual(ops, [
            ('equal', 'a'),
            ('delete', 'b'),
            ('equal', 'c'),
        ])

    def test_replace(self):
        old = ["x", "y"]
        new = ["x", "z"]
        ops = diff_lines(old, new)
        self.assertEqual(ops, [
            ('equal', 'x'),
            ('delete', 'y'),
            ('insert', 'z'),
        ])

    def test_empty_old(self):
        old = []
        new = ["a", "b"]
        ops = diff_lines(old, new)
        self.assertEqual(ops, [
            ('insert', 'a'),
            ('insert', 'b'),
        ])

    def test_empty_new(self):
        old = ["a", "b"]
        new = []
        ops = diff_lines(old, new)
        self.assertEqual(ops, [
            ('delete', 'a'),
            ('delete', 'b'),
        ])

    def test_apply_patch_simple(self):
        old = ["a", "c"]
        new = ["a", "b", "c"]
        patch = diff_lines(old, new)
        result = apply_patch(old, patch)
        self.assertEqual(result, new)

    def test_apply_patch_replace(self):
        old = ["1", "2", "3"]
        new = ["1", "4", "3"]
        patch = diff_lines(old, new)
        result = apply_patch(old, patch)
        self.assertEqual(result, new)

    def test_apply_patch_empty_base(self):
        base = []
        new = ["a", "b"]
        patch = diff_lines(base, new)
        result = apply_patch(base, patch)
        self.assertEqual(result, new)

    def test_apply_patch_empty_new(self):
        base = ["a", "b"]
        new = []
        patch = diff_lines(base, new)
        result = apply_patch(base, patch)
        self.assertEqual(result, new)

if __name__ == '__main__':
    unittest.main()
