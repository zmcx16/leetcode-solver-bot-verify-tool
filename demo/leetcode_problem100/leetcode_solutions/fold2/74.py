class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                row = mid // len(matrix[0])
                col = mid % len(matrix[0])
                if nums[row][col] == target:
                    return True
                elif nums[row][col] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        return binarySearch([num for row in matrix for num in row], target)