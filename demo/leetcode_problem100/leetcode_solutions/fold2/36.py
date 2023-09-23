class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in seen:
                    return False
                seen.add(board[i][j])
            seen.clear()
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in seen:
                    return False
                seen.add(board[j][i])
            seen.clear()
            row_start = (i // 3) * 3
            col_start = (i % 3) * 3
            for row in range(row_start, row_start + 3):
                for col in range(col_start, col_start + 3):
                    if board[row][col] != '.' and board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
            seen.clear()
        return True