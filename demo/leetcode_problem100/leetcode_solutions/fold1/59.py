from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        num = 1
        top, bottom, left, right = 0, n-1, 0, n-1
        direction = 'right'
        while num <= n*n:
            if direction == 'right':
                for i in range(left, right+1):
                    matrix[top][i] = num
                    num += 1
                top += 1
                direction = 'down'
            elif direction == 'down':
                for i in range(top, bottom+1):
                    matrix[i][right] = num
                    num += 1
                right -= 1
                direction = 'left'
            elif direction == 'left':
                for i in range(right, left-1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1
                direction = 'up'
            elif direction == 'up':
                for i in range(bottom, top-1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
                direction = 'right'
        return matrix
