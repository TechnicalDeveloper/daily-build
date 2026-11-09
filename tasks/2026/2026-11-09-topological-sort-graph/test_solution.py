import unittest
from solution import topological_sort

class TestTopologicalSort(unittest.TestCase):
    def test_single_vertex(self):
        self.assertEqual(topological_sort(1, []), [0])

    def test_chain(self):
        edges = [(0, 1), (1, 2), (2, 3)]
        result = topological_sort(4, edges)
        # Only possible order is [0,1,2,3]
        self.assertEqual(result, [0, 1, 2, 3])

    def test_graph_with_cycle(self):
        edges = [(0, 1), (1, 2), (2, 0)]
        self.assertEqual(topological_sort(3, edges), [])

    def test_disconnected_dag(self):
        edges = [(0, 2), (1, 2)]
        result = topological_sort(3, edges)
        # 0 and 1 have no incoming, 2 has incoming from both
        # Possible orders: [0,1,2] or [1,0,2]
        self.assertIn(result, [[0, 1, 2], [1, 0, 2]])

    def test_complex_dag(self):
        edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
        result = topological_sort(6, edges)
        # Verify no vertex appears before its prerequisites
        for u, v in edges:
            self.assertLess(result.index(u), result.index(v))

if __name__ == '__main__':
    unittest.main()
