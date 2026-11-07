from collections import deque

def topological_sort(vertices, edges):
    # Build adjacency list and in-degree count
    adj = {v: [] for v in vertices}
    in_degree = {v: 0 for v in vertices}
    
    for u, v in edges:
        if u not in adj or v not in adj:
            raise ValueError("Edge references unknown vertex")
        adj[u].append(v)
        in_degree[v] += 1
    
    # Initialize queue with nodes of in-degree 0
    queue = deque([v for v in vertices if in_degree[v] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(result) != len(vertices):
        raise ValueError("Graph has a cycle")
    
    return result
