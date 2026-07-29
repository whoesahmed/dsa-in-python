def dfs(adjacency_matrix, start):
    """Return all nodes reachable from start using depth-first search."""
    if not adjacency_matrix or not (0 <= start < len(adjacency_matrix)):
        return []

    visited = []
    visited_set = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited_set:
            continue

        visited_set.add(node)
        visited.append(node)

        for neighbor in range(len(adjacency_matrix[node])):
            if adjacency_matrix[node][neighbor] and neighbor not in visited_set:
                stack.append(neighbor)

    return visited
print(dfs([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 0]], 0))