import json

class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        combinations = []
        self.backtrack(candidates, target, [], combinations)
        return json.dumps(combinations)

    def backtrack(self, candidates, target, current, combinations):
        if target == 0:
            combinations.append(current)
            return
        for i in range(len(candidates)):
            if candidates[i] > target:
                break
            self.backtrack(candidates[i:], target - candidates[i], current + [candidates[i]], combinations)
