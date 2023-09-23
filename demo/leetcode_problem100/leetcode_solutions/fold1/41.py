class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # Mark positive numbers within [1, n] as negative
        for i in range(n):
            if 1 <= nums[i] <= n:
                nums[nums[i] - 1] = -abs(nums[nums[i] - 1])
        # Find the first positive number
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        # If all numbers within [1, n] are present, return n + 1
        return n + 1