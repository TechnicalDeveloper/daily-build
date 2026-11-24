# Topological Sort

Build a function `topological_sort(graph: dict) -> list` that returns a list of nodes in topological order for the given directed graph. The graph is represented as an adjacency dictionary: each key is a node, and its value is an iterable of successor nodes. Nodes that appear only as successors are included in the output. If the graph contains a cycle, raise `ValueError`.

Signature: `def topological_sort(graph: dict) -> list:`

Edge cases to respect:
- Empty graph: returns `[]`.
- Nodes that are not present as keys but appear as successors must be included.
- Any cycle (including a self-loop) must raise `ValueError`.
