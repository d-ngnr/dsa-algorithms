def isValidSudoku(sudoku):
    seen = set()
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != '.':
                if (sudoku[i][j], i, j) in seen or (sudoku[i][j], j, i) in seen or (sudoku[i][j], (i // 3, j // 3)) in seen:
                    return False
                seen.add((sudoku[i][j], i, j))
    return True

# Example usage
sudoku = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print(isValidSudoku(sudoku)) # Output: True