from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, left):
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target or (left and nums[mid] == target):
                    high = mid - 1
                else:
                    low = mid + 1
            return low
        left_index = binary_search(nums, target, True)
        if left_index >= len(nums) or nums[left_index] != target:
            return [-1, -1]
        right_index = binary_search(nums, target, False) - 1
        return [left_index, right_index]