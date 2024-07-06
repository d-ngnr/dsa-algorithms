def gameOfLife(board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    rows = len(board)
    cols = len(board[0])
    for r in range(rows):
        for c in range(cols):
            live_neighbors = 0
            if r > 0 and board[r - 1][c] == 1:
                live_neighbors += 1
            if r > 0 and c < cols - 1 and board[r - 1][c + 1] == 1:
                live_neighbors += 1
            if r > 0 and c > 0 and board[r - 1][c - 1] == 1:
                live_neighbors += 1
            if c < cols - 1 and board[r][c + 1] == 1:
                live_neighbors += 1
            if c > 0 and board[r][c - 1] == 1:
                live_neighbors += 1
            if c > 0 and r < rows - 1 and board[r + 1][c - 1] == 1:
                live_neighbors += 1
            if r < rows - 1 and board[r + 1][c] == 1:
                live_neighbors += 1
            if r < rows - 1 and c < cols - 1 and board[r + 1][c + 1] == 1:
                live_neighbors += 1

            if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[r][c] = -1
            if board[r][c] == 0 and live_neighbors == 3:
                board[r][c] = 2

    for r in range(rows):
        for c in range(cols):
            if board[r][c] > 0:
                board[r][c] = 1
            else:
                board[r][c] = 0

    return board

# Example usage
board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
print(gameOfLife(board))  # Output: [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]