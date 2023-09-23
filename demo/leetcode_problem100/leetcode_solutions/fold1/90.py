class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        self.generate_subsets(nums, 0, [], subsets)
        return subsets

    def generate_subsets(self, nums, index, current, subsets):
        subsets.append(current[:])
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            current.append(nums[i])
            self.generate_subsets(nums, i + 1, current, subsets)
            current.pop()
