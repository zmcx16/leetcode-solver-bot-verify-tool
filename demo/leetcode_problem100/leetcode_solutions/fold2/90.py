import json


class Solution:
    def subsetsWithDup(self, nums):
        def backtrack(start, subset):
            unique_subsets.add(tuple(subset))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                backtrack(i+1, subset)
                subset.pop()

        unique_subsets = set()
        nums.sort()
        backtrack(0, [])
        return list(unique_subsets)


# Convert the output to JSON string
solution = Solution()
output = solution.subsetsWithDup([1, 2, 2])
json_output = json.dumps(output)

# Return the JSON string
json_output