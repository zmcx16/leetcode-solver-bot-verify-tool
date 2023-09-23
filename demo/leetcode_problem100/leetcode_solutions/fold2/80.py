class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        count = 1
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                count += 1
                if count <= 2:
                    i += 1
                    nums[i] = nums[j]
            else:
                i += 1
                nums[i] = nums[j]
                count = 1
        return i + 1