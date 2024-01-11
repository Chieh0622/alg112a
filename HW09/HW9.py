# 使用ChatGPT，並理解

def is_safe(board, row, col, n):
    # 檢查同一列是否有皇后
    for i in range(row):
        if board[i][col] == 1:
            return False

    # 檢查左上到右下的對角線是否有皇后
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # 檢查左下到右上的對角線是否有皇后
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, n, count):
    if row == n:
        # 找到一個解
        count[0] += 1
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            # 放置皇后
            board[row][col] = 1

            # 遞歸放置下一行的皇后
            solve_n_queens_util(board, row + 1, n, count)

            # 回溯，撤銷當前的放置，試下一個位置
            board[row][col] = 0

def print_solution(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    count = [0]  # 用列表包裝計數器，以便在遞歸中修改
    solve_n_queens_util(board, 0, n, count)
    print(f"共有 {count[0]} 種解法。")

# 解决八皇后问题
solve_n_queens(8)