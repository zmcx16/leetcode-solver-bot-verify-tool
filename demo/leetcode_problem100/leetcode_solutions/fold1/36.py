class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_valid(nums):
            seen = set()
            for num in nums:
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)
            return True
        for i in range(9):
            # check rows
            if not check_valid(board[i]):
                return False
            # check columns
            if not check_valid([board[j][i] for j in range(9)]):
                return False
            # check sub-boxes
            if not check_valid([board[i//3*3 + j//3][i%3*3 + j%3] for j in range(9)]):
                return False
        return True