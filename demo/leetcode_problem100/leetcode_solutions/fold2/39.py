import json

class Solution:
    def combinationSum(self, candidates, target):
        def backtrack(combination, remaining, start):
            if remaining == 0:
                result.append(combination)
                return
            if remaining < 0:
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                backtrack(combination + [candidates[i]], remaining - candidates[i], i)
        candidates.sort()
        result = []
        backtrack([], target, 0)
        return json.dumps(result)