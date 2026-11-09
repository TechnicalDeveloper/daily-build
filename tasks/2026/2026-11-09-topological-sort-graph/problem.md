# Topological Sort of a Directed Acyclic Graph

Implement a function `topological_sort(vertices: int, edges: list[tuple[int, int]]) -> list[int]` that returns a topological ordering of vertices (0-indexed) in a directed acyclic graph (DAG).

The function receives:
- `vertices`: number of vertices (0 to vertices-1)
- `edges`: list of directed edges (u, v) meaning u -> v

Return a list of vertex labels in topological order. If the graph contains a cycle, return an empty list.

**Edge cases to respect:**
- Single vertex with no edges.
- Graph that is already topologically sorted as a chain.
- Graph with a cycle (must return empty list).
