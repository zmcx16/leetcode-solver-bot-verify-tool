import json

class Solution:
    def permuteUnique(self, nums: List[int]) -> str:
        def backtrack(path, used):
            if len(path) == len(nums):
                permutations.append(path.copy())
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and i-1 not in used:
                    continue
                if i in used:
                    continue
                path.append(nums[i])
                used.add(i)
                backtrack(path, used)
                path.pop()
                used.remove(i)
        nums.sort()
        permutations = []
        backtrack([], set())
        return json.dumps(permutations)