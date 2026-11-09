def topological_sort(vertices: int, edges: list[tuple[int, int]]) -> list[int]:
    # Build adjacency list and in-degree array
    graph = [[] for _ in range(vertices)]
    in_degree = [0] * vertices
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Collect vertices with in-degree 0
    queue = [i for i in range(vertices) if in_degree[i] == 0]
    result = []

    while queue:
        node = queue.pop(0)
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If we visited all vertices, it's a valid topological order
    if len(result) == vertices:
        return result
    else:
        return []
