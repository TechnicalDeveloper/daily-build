import unittest
from solution import topological_sort

class TestTopologicalSort(unittest.TestCase):

    def test_simple_linear(self):
        vertices = [0, 1, 2, 3]
        edges = [(0, 1), (1, 2), (2, 3)]
        result = topological_sort(vertices, edges)
        # Must respect order: 0 before 1, 1 before 2, 2 before 3
        positions = {v: i for i, v in enumerate(result)}
        self.assertTrue(positions[0] < positions[1])
        self.assertTrue(positions[1] < positions[2])
        self.assertTrue(positions[2] < positions[3])
        self.assertCountEqual(result, vertices)  # same set

    def test_disconnected_graph(self):
        vertices = ['a', 'b', 'c']
        edges = [('a', 'b')]  # 'c' is isolated
        result = topological_sort(vertices, edges)
        # 'a' must be before 'b', 'c' can be anywhere
        positions = {v: i for i, v in enumerate(result)}
        self.assertTrue(positions['a'] < positions['b'])
        self.assertEqual(len(result), 3)
        self.assertCountEqual(result, vertices)

    def test_cycle_raises_error(self):
        vertices = [1, 2, 3]
        edges = [(1, 2), (2, 3), (3, 1)]
        with self.assertRaises(ValueError):
            topological_sort(vertices, edges)

    def test_single_vertex(self):
        vertices = [42]
        edges = []
        result = topological_sort(vertices, edges)
        self.assertEqual(result, [42])

    def test_empty_vertices(self):
        vertices = []
        edges = []
        result = topological_sort(vertices, edges)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
