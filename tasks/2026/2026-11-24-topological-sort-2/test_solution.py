import unittest
from solution import topological_sort


class TestTopologicalSort(unittest.TestCase):

    def test_empty_graph(self):
        self.assertEqual(topological_sort({}), [])

    def test_single_node(self):
        self.assertEqual(topological_sort({'a': []}), ['a'])

    def test_successor_only_node(self):
        result = topological_sort({'a': ['b']})
        self.assertIn('a', result)
        self.assertIn('b', result)
        self.assertLess(result.index('a'), result.index('b'))

    def test_linear_dependencies(self):
        graph = {
            'a': ['b'],
            'b': ['c'],
            'c': [],
        }
        self.assertEqual(topological_sort(graph), ['a', 'b', 'c'])

    def test_diamond_dependencies(self):
        graph = {
            'a': ['b', 'c'],
            'b': ['d'],
            'c': ['d'],
            'd': [],
        }
        result = topological_sort(graph)
        self.assertEqual(set(result), {'a', 'b', 'c', 'd'})
        self.assertLess(result.index('a'), result.index('b'))
        self.assertLess(result.index('a'), result.index('c'))
        self.assertLess(result.index('b'), result.index('d'))
        self.assertLess(result.index('c'), result.index('d'))

    def test_disconnected_components(self):
        graph = {
            'a': [],
            'b': ['c'],
            'c': [],
        }
        result = topological_sort(graph)
        self.assertEqual(set(result), {'a', 'b', 'c'})
        self.assertLess(result.index('b'), result.index('c'))

    def test_cycle_raises_value_error(self):
        graph = {
            'a': ['b'],
            'b': ['a'],
        }
        with self.assertRaises(ValueError):
            topological_sort(graph)

    def test_self_loop_raises_value_error(self):
        graph = {'a': ['a']}
        with self.assertRaises(ValueError):
            topological_sort(graph)


if __name__ == '__main__':
    unittest.main()
