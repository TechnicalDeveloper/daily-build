import unittest
from solution import diff, apply_patch


class TestDiffPatch(unittest.TestCase):

    def test_empty_to_nonempty(self):
        patch = diff([], [1, 2, 3])
        self.assertEqual(patch, [('insert', 1), ('insert', 2), ('insert', 3)])
        self.assertEqual(apply_patch([], patch), [1, 2, 3])

    def test_nonempty_to_empty(self):
        patch = diff([1, 2, 3], [])
        self.assertEqual(patch, [('delete', 1), ('delete', 2), ('delete', 3)])
        self.assertEqual(apply_patch([1, 2, 3], patch), [])

    def test_identical_sequences(self):
        seq = ['a', 'b', 'c']
        patch = diff(seq, seq)
        self.assertEqual(patch, [('equal', x) for x in seq])
        self.assertEqual(apply_patch(seq, patch), seq)

    def test_insertion_and_deletion_roundtrip(self):
        a = [1, 2, 5]
        b = [1, 3, 4, 5]
        patch = diff(a, b)
        self.assertEqual(apply_patch(a, patch), b)

    def test_duplicate_items_roundtrip(self):
        a = [1, 1, 2, 3]
        b = [1, 2, 2, 3, 3]
        patch = diff(a, b)
        self.assertEqual(apply_patch(a, patch), b)

    def test_invalid_patch_raises(self):
        with self.assertRaises(ValueError):
            apply_patch([1, 2], [('delete', 9)])


if __name__ == '__main__':
    unittest.main()
