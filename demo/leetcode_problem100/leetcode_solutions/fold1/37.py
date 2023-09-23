class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(board, row, col, num):
            # Check if the number is already used in the row
            for i in range(9):
                if board[row][i] == num:
                    return False
            # Check if the number is already used in the column
            for j in range(9):
                if board[j][col] == num:
                    return False
            # Check if the number is already used in the 3x3 sub-grid
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False
            return True

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            if is_valid(board, i, j, num):
                                board[i][j] = num
                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = '.'
                        return False
            return True

        solve(board)