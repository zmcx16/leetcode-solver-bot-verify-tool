from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            # Check if there is a queen in the same column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # Check if there is a queen in the upper left diagonal
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # Check if there is a queen in the upper right diagonal
            i = row - 1
            j = col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(board, row):
            # Base case: all queens are placed
            if row == n:
                solution = []
                for i in range(n):
                    solution.append(''.join(board[i]))
                solutions.append(solution)
                return

            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row + 1)
                    board[row][col] = '.'

        board = [['.' for _ in range(n)] for _ in range(n)]
        solutions = []
        backtrack(board, 0)
        return solutions
