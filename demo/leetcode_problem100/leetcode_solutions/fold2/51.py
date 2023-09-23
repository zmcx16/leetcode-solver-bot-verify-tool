class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
                j = row - i
                if col - j >= 0 and board[i][col - j] == 'Q':
                    return False
                if col + j < n and board[i][col + j] == 'Q':
                    return False
            return True

        def backtrack(board, row):
            nonlocal solutions
            if row == n:
                solutions.append(list(board))
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row + 1)
                    board[row][col] = '.'

        solutions = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(board, 0)
        return solutions