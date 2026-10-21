from collections import deque

def topological_sort(graph):
    """
    Perform topological sort on a DAG represented as adjacency list.
    Raises ValueError if graph contains a cycle.
    """
    # Count indegree for each node
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] = indegree.get(neighbor, 0) + 1

    # Initialize queue with nodes that have indegree 0
    queue = deque([node for node in indegree if indegree[node] == 0])

    sorted_nodes = []
    while queue:
        node = queue.popleft()
        sorted_nodes.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # If not all nodes were processed, there is a cycle
    if len(sorted_nodes) != len(graph):
        raise ValueError("Graph contains a cycle")

    return sorted_nodes
