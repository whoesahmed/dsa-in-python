INF = float('inf')
# Example adjacency matrix for a weighted undirected graph.
# Use INF to represent no direct edge between two nodes.
adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]

def shortest_path(matrix, start_node, target_node=None):
    """Compute shortest paths from start_node to all nodes (or a target) using Dijkstra's algorithm.

    Parameters:
    - matrix: adjacency matrix where matrix[i][j] is the weight from i to j or INF.
    - start_node: source vertex index.
    - target_node: optional single destination index; if provided, printing is limited to this node.

    Returns a tuple (distances, paths):
    - distances: list of shortest distances from start_node to every node.
    - paths: list of node lists representing the discovered shortest path to each node.
    """
    n = len(matrix)
    # Initialize distances to infinity and 0 for the start node
    distances = [INF] * n
    distances[start_node] = 0
    # Initialize paths: each node's path starts as itself (will be updated)
    paths = [[node_no] for node_no in range(n)]
    # Visited keeps track of nodes for which shortest distance is finalized
    visited = [False] * n
    
    for _ in range(n):
        min_distance = INF
        current = -1
        for node_no in range(n):
            if not visited[node_no] and distances[node_no] < min_distance:
                min_distance = distances[node_no]
                current = node_no
        
        # If no reachable unvisited node remains, stop
        if current == -1:
            break
        visited[current] = True
        
        # Relaxation step: update distances to neighbors of current
        for node_no in range(n):
            distance = matrix[current][node_no]
            if distance != INF and not visited[node_no]:
                new_distance = distances[current] + distance
                if new_distance < distances[node_no]:
                    distances[node_no] = new_distance
                    # Record the path by extending current's path with the neighbor
                    paths[node_no] = paths[current] + [node_no]
    
    # Prepare list of nodes to print (either a single target or all nodes)
    targets = [target_node] if target_node is not None else range(n)
    for node_no in targets:
        # Skip the start node itself and unreachable nodes
        if node_no == start_node or distances[node_no] == INF:
            continue
        # Format the path for display
        string_path = (str(n) for n in paths[node_no])
        path = ' -> '.join(string_path)
        print(f'\n{start_node}-{node_no} distance: {distances[node_no]}\nPath: {path}')
    
    return distances, paths

if __name__ == '__main__':
    # Example usage: compute shortest path from node 0 to node 5
    shortest_path(adj_matrix, 0, 5)