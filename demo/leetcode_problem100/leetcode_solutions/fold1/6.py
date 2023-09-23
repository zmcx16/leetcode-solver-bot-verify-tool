class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = ['' for _ in range(min(numRows, len(s)))]
        current_row = 0
        direction = 1
        for char in s:
            rows[current_row] += char
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1
            current_row += direction
        return ''.join(rows)