class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        for num in nums[2:]:
            if num != nums[i-2]:
                nums[i] = num
                i += 1
        return i