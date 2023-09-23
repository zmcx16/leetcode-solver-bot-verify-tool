import json

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(combination, index, target):
            if target == 0:
                result.append(combination)
                return
            if target < 0 or index >= len(candidates):
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                backtrack(combination + [candidates[i]], i + 1, target - candidates[i])
        backtrack([], 0, target)
        return json.dumps(result)