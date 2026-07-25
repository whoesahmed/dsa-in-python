def adjacency_list_to_matrix(adj_list):
    """Convert an adjacency list (dict) to an adjacency matrix (list of lists).

    The function prints each row of the resulting matrix and returns it.
    """
    if not adj_list:
        print([])
        return []

    # determine number of nodes (assume nodes are numbered with integers)
    try:
        n = max(adj_list.keys()) + 1
    except Exception:
        n = len(adj_list)

    # initialize n x n matrix of zeros
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    # set edges
    for node, neighbors in adj_list.items():
        for nei in neighbors:
            if 0 <= node < n and 0 <= nei < n:
                matrix[node][nei] = 1

    # print each row
    for row in matrix:
        print(row)

    return matrix


if __name__ == "__main__":
    # quick sanity check (not used by tests)
    sample = {0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}
    adjacency_list_to_matrix(sample)
