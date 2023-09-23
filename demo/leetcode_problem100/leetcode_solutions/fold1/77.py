import json

class Solution:
    def combine(self, n: int, k: int) -> str:
        def backtrack(combination, start, remaining):
            if remaining == 0:
                result.append(combination[:])
                return
            for i in range(start, n + 1):
                combination.append(i)
                backtrack(combination, i + 1, remaining - 1)
                combination.pop()
        result = []
        backtrack([], 1, k)
        return json.dumps(result)