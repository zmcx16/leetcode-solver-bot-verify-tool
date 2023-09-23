class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row):
            nonlocal count
            if row == n:
                count += 1
                return
            for col in range(n):
                if col in columns or row+col in diagonal1 or row-col in diagonal2:
                    continue
                columns.add(col)
                diagonal1.add(row+col)
                diagonal2.add(row-col)
                backtrack(row+1)
                columns.remove(col)
                diagonal1.remove(row+col)
                diagonal2.remove(row-col)
        count = 0
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        backtrack(0)
        return count