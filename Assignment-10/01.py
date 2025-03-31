def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    for i in range(row):
        if board[i][col] == 'Q':
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_queens(board, row, n, ans):
    if row == n:
        ans.append(["".join(r) for r in board])
        return

    for i in range(n):
        if is_safe(board, row, i, n):
            board[row][i] = 'Q'
            solve_queens(board, row + 1, n, ans)
            board[row][i] = '.'

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    ans = []

    solve_queens(board, 0, n, ans)

    return ans

n = 4
solutions = solve_n_queens(n)
for sol in solutions:
    for row in sol:
        print(row)
    print()