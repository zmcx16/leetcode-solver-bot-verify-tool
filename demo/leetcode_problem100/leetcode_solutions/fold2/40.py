import json

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.backtrack(candidates, target, [], result, 0)
        return json.dumps(result)

    def backtrack(self, candidates, target, combination, result, start):
        if target == 0:
            result.append(combination.copy())
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break
            combination.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], combination, result, i + 1)
            combination.pop()