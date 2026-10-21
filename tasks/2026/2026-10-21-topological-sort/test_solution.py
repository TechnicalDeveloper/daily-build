import unittest
from solution import topological_sort

class TestTopologicalSort(unittest.TestCase):

    def test_empty_graph(self):
        self.assertEqual(topological_sort({}), [])

    def test_single_node(self):
        graph = {0: []}
        self.assertEqual(topological_sort(graph), [0])

    def test_simple_dag(self):
        graph = {0: [1], 1: [2], 2: []}
        result = topological_sort(graph)
        # Must be a valid topological order: 0 before 1 before 2
        self.assertEqual(result, [0, 1, 2])

    def test_cycle_raises(self):
        graph = {0: [1], 1: [0]}
        with self.assertRaises(ValueError) as context:
            topological_sort(graph)
        self.assertEqual(str(context.exception), "Graph contains a cycle")

    def test_disconnected_components(self):
        graph = {0: [], 1: [2], 2: [], 3: [4], 4: []}
        result = topological_sort(graph)
        # Check that ordering respects edges: 1 before 2, 3 before 4
        self.assertLess(result.index(1), result.index(2))
        self.assertLess(result.index(3), result.index(4))
        # Check all nodes are present
        self.assertEqual(set(result), {0, 1, 2, 3, 4})

if __name__ == '__main__':
    unittest.main()
