# Topological Sort using Kahn's Algorithm

Implement a function `topological_sort(vertices, edges)` that performs a topological sort on a directed acyclic graph (DAG).

**Signature:**
```python
def topological_sort(vertices: list, edges: list[tuple]) -> list:
    pass
```

**Input:**
- `vertices`: a list of unique node identifiers (can be strings or integers).
- `edges`: a list of tuples `(u, v)` representing a directed edge from node `u` to node `v`.

**Output:**
- Return a list of all nodes in a valid topological order (i.e., for every edge `(u, v)`, `u` appears before `v` in the list).

**Edge cases to handle:**
1. If the graph contains a cycle, raise a `ValueError` with the message "Graph has a cycle".
2. If `vertices` is empty, return an empty list `[]`.
3. If there is a single node with no edges, return a list containing that node.
