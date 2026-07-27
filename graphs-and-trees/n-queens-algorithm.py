def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []
    cols = set()
    diag1 = set()  # row + col
    diag2 = set()  # row - col
    current = []

    def backtrack(row):
        if row == n:
            solutions.append(current.copy())
            return

        for col in range(n):
            d1 = row + col
            d2 = row - col
            if col in cols or d1 in diag1 or d2 in diag2:
                continue

            cols.add(col)
            diag1.add(d1)
            diag2.add(d2)
            current.append(col)

            backtrack(row + 1)

            current.pop()
            cols.remove(col)
            diag1.remove(d1)
            diag2.remove(d2)

    backtrack(0)
    return solutions


if __name__ == '__main__':
    n = 4
    solutions = dfs_n_queens(n)
    print(f'Total solutions for {n}-queens: {len(solutions)}')
    for solution in solutions:
        print(solution)
