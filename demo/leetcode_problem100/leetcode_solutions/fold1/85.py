class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols + 1)
        max_area = 0
        for i in range(rows):
            stack = []
            for j in range(cols + 1):
                if j < cols:
                    if matrix[i][j] == '1':
                        heights[j] += 1
                    else:
                        heights[j] = 0
                while stack and heights[stack[-1]] > heights[j]:
                    height = heights[stack.pop()]
                    width = j if not stack else j - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(j)
        return max_area