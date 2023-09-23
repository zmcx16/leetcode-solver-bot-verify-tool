from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path, res):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]], res)
        res = []
        backtrack(nums, [], res)
        return res


# create an object of the Solution class
solution = Solution()
# example inputs
nums = [1, 2, 3]
# call the permute method and print the result
print(solution.permute(nums))
