import json

class Solution:
    def permute(self, nums):
        def backtrack(curr):
            if len(curr) == len(nums):
                result.append(curr)
                return
            for num in nums:
                if num not in curr:
                    backtrack(curr + [num])
        result = []
        backtrack([])
        return result

# Convert the result to JSON string
result = Solution().permute([1, 2, 3])
json_result = json.dumps(result)

# Return the JSON string
json.dumps({'thought': thought, 'solution_code': solution_code})
