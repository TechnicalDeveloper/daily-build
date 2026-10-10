import unittest
from solution import diff

class TestDiff(unittest.TestCase):
    def test_both_empty(self):
        """Both sequences empty -> empty list"""
        self.assertEqual(diff([], []), [])

    def test_first_empty(self):
        """seq1 empty, seq2 non-empty -> all inserts"""
        self.assertEqual(diff([], ['a', 'b']),
                         [('insert', 'a'), ('insert', 'b')])

    def test_second_empty(self):
        """seq1 non-empty, seq2 empty -> all deletes"""
        self.assertEqual(diff(['a', 'b'], []),
                         [('delete', 'a'), ('delete', 'b')])

    def test_identical(self):
        """Identical sequences -> all keeps"""
        self.assertEqual(diff(['a', 'b', 'c'], ['a', 'b', 'c']),
                         [('keep', 'a'), ('keep', 'b'), ('keep', 'c')])

    def test_completely_different(self):
        """No common elements -> all deletes then all inserts"""
        self.assertEqual(diff(['x', 'y'], ['a', 'b']),
                         [('delete', 'x'), ('delete', 'y'),
                          ('insert', 'a'), ('insert', 'b')])

    def test_mixed_changes(self):
        """Mixed insert, delete, keep operations"""
        # seq1: [1, 2, 3, 4]   seq2: [2, 5, 3]
        # LCS = [2,3], edit script: del 1, keep 2, ins 5, keep 3, del 4
        self.assertEqual(diff([1, 2, 3, 4], [2, 5, 3]),
                         [('delete', 1), ('keep', 2),
                          ('insert', 5), ('keep', 3),
                          ('delete', 4)])

if __name__ == '__main__':
    unittest.main()
