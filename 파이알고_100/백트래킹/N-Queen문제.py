# https://100.pyalgo.co.kr/?page=98#


def solution(n):
    def isSafe(board, row, col, n):
        # 같은 열에 퀸이 있는지 확인
        for i in range(row):
            if board[i][col] == 1:
                return False

        # 대각선에 퀸이 있는지 확인
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def solve(board, row, n, count):
        if row == n:
            return count + 1

        for col in range(n):
            if isSafe(board, row, col, n):
                board[row][col] = 1
                count = solve(board, row + 1, n, count)
                board[row][col] = 0

        return count

    board = [[0 for j in range(n)] for i in range(n)]
    return solve(board, 0, n, 0)


solution(8)
