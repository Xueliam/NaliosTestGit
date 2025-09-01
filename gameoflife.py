def GameOfLife(board):
    def count_live_neighbors(x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                count += board[nx][ny]
        return count

    def update_cell(x, y):
        live_neighbors = count_live_neighbors(x, y)
        if board[x][y] == 1:
            return 1 if live_neighbors in [2, 3] else 0
        else:
            return 1 if live_neighbors == 3 else 0

    new_board = []
    for x in range(len(board)):
        row = []
        for y in range(len(board[0])):
            row.append(update_cell(x, y))
        new_board.append(row)
    return new_board

def PlayGameOfLife(board):
    for _ in range(5):
        board = GameOfLife(board)
    return board
