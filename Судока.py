def solve_sudoku(matrix):
    row, col, values = min(
        [[row, col, [i for i in range(1, 5) if i not in set(matrix[row])
                     | {matrix[i][col] for i in range(4)} | {matrix[i][j]
                                                             for i in range(row // 2 * 2, row // 2 * 2 + 2)
                                                             for j in range(col // 2 * 2, col // 2 * 2 + 2)}]]
         for row in range(4) for col in range(4) if not matrix[row][col]], key=lambda x: len(x[2]))
    matrix[row][col] = values[0]
    if any(0 in i for i in matrix):
        solve_sudoku(matrix)
    return matrix


print(*[''.join(str(j) for j in i) for i in solve_sudoku([[int(i) for i in input().strip()] for _ in range(4)])],
      sep='\n')
