# Topological Sort using Kahn's Algorithm

Implement a function that performs a topological sort on a directed acyclic graph (DAG) using Kahn's algorithm.

**Signature**: `def topological_sort(vertices: list, edges: list[tuple]) -> list`

- `vertices`: a list of unique hashable objects representing all nodes in the graph.
- `edges`: a list of tuples `(u, v)` meaning there is a directed edge from `u` to `v` (i.e., `u` must come before `v` in the ordering).

**Returns**: a list of all vertices in a topological order. If multiple valid orders exist, any one is acceptable.

**Raises**: `ValueError` if the graph contains a cycle.

**Edge cases to handle**:
1. **Cycle detection**: If the graph has a cycle, raise `ValueError`.
2. **Disconnected graph**: Vertices that are not connected by any edge must still appear in the result (they may be placed anywhere).
3. **Single vertex**: A graph with only one vertex and no edges should return that vertex.
