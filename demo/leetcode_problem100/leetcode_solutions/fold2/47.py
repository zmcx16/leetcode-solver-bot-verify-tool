import json

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(permutation, remaining, result):
            if not remaining:
                result.append(permutation[:])
            else:
                for i in range(len(remaining)):
                    if i > 0 and remaining[i] == remaining[i - 1]:
                        continue
                    permutation.append(remaining[i])
                    backtrack(permutation, remaining[:i] + remaining[i + 1:], result)
                    permutation.pop()
        result = []
        nums.sort()
        backtrack([], nums, result)
        return json.dumps(result)