# Topological Sort

Implement a function `topological_sort(graph)` that returns a topological ordering of a directed acyclic graph (DAG). The graph is represented as an adjacency list: a dictionary where keys are nodes and values are lists of successor nodes. The function should return a list of nodes in a valid topological order. If the graph contains a cycle, raise a `ValueError` with the message "Graph contains a cycle".

**Signature:**
```python
def topological_sort(graph: dict) -> list:
    pass
```

**Edge cases to consider:**
1. Empty graph `{}` should return an empty list `[]`.
2. Graph with a single node `{0: []}` should return `[0]`.
3. Graph with a cycle (e.g., `{0: [1], 1: [0]}`) must raise `ValueError`.
