from collections import deque

def topological_sort(graph: dict) -> list:
    nodes = list(graph.keys())
    seen = set(nodes)
    for successors in graph.values():
        for successor in successors:
            if successor not in seen:
                seen.add(successor)
                nodes.append(successor)

    indegree = {node: 0 for node in nodes}
    for successors in graph.values():
        for successor in successors:
            indegree[successor] += 1

    adjacency = {node: list(graph.get(node, [])) for node in nodes}
    queue = deque([node for node in nodes if indegree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for successor in adjacency[node]:
            indegree[successor] -= 1
            if indegree[successor] == 0:
                queue.append(successor)

    if len(result) != len(nodes):
        raise ValueError('Graph contains a cycle')
    return result
