class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, index):
            # Check if we have found the word
            if index == len(word):
                return True
            # Check if current cell is out of bounds or has already been visited
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index]:
                return False
            # Mark current cell as visited
            temp = board[row][col]
            board[row][col] = '#'
            # Recursively search in all four directions
            found = backtrack(row + 1, col, index + 1) or backtrack(row - 1, col, index + 1) or 
                    backtrack(row, col + 1, index + 1) or backtrack(row, col - 1, index + 1)
            # Restore the original value of the cell
            board[row][col] = temp
            return found
        # Iterate through each cell in the grid
        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(row, col, 0):
                    return True
        return False