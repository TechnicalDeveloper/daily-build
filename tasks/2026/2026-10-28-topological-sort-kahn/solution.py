from collections import defaultdict, deque

def topological_sort(vertices: list, edges: list[tuple]) -> list:
    # Build adjacency list and in-degree count
    adjacency = defaultdict(list)
    in_degree = {v: 0 for v in vertices}

    for u, v in edges:
        adjacency[u].append(v)
        in_degree[v] = in_degree.get(v, 0) + 1
        # Ensure u is tracked even if not in vertices? We'll assume u is in vertices.
        # If not, we add it to in_degree with zero in-degree but that could be unexpected.
        # For safety, we assume edges only involve vertices from the list.

    # Initialize queue with vertices having in-degree 0
    queue = deque([v for v in vertices if in_degree.get(v, 0) == 0])
    result = []

    while queue:
        u = queue.popleft()
        result.append(u)
        for v in adjacency[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # If result does not contain all vertices, there is a cycle
    if len(result) != len(vertices):
        raise ValueError("Graph contains a cycle")

    return result
