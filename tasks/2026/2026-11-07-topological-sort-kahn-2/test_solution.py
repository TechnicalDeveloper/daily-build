import unittest
from solution import topological_sort

def is_topological_order(vertices, edges, order):
    # Check that order contains all vertices exactly once
    if sorted(order) != sorted(vertices):
        return False
    # Check every edge: u must appear before v
    pos = {node: idx for idx, node in enumerate(order)}
    for u, v in edges:
        if pos[u] >= pos[v]:
            return False
    return True

class TestTopologicalSort(unittest.TestCase):

    def test_simple_dag(self):
        vertices = ['a', 'b', 'c', 'd']
        edges = [('a', 'b'), ('b', 'c'), ('a', 'd')]
        result = topological_sort(vertices, edges)
        self.assertTrue(is_topological_order(vertices, edges, result))

    def test_cycle_raises_error(self):
        vertices = ['x', 'y', 'z']
        edges = [('x', 'y'), ('y', 'z'), ('z', 'x')]
        with self.assertRaises(ValueError):
            topological_sort(vertices, edges)

    def test_empty_graph(self):
        vertices = []
        edges = []
        result = topological_sort(vertices, edges)
        self.assertEqual(result, [])

    def test_single_node(self):
        vertices = ['a']
        edges = []
        result = topological_sort(vertices, edges)
        self.assertEqual(result, ['a'])

    def test_disconnected_graph(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (3, 4)]
        result = topological_sort(vertices, edges)
        self.assertTrue(is_topological_order(vertices, edges, result))

if __name__ == '__main__':
    unittest.main()
