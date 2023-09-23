class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(nums):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left

        def binary_search(nums, target, left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        pivot = find_pivot(nums)
        if nums[pivot] == target:
            return pivot
        if pivot == 0:
            return binary_search(nums, target, 0, len(nums) - 1)
        if target < nums[0]:
            return binary_search(nums, target, pivot, len(nums) - 1)
        return binary_search(nums, target, 0, pivot - 1)