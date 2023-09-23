class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def backtrack(used: List[bool], result: List[str]) -> str:
            nonlocal count
            if len(result) == n:
                count += 1
                if count == k:
                    return ''.join(result)
                return
            for i in range(1, n + 1):
                if not used[i]:
                    used[i] = True
                    result.append(str(i))
                    res = backtrack(used, result)
                    if res:
                        return res
                    used[i] = False
                    result.pop()
        count = 0
        used = [False] * (n + 1)
        result = []
        return backtrack(used, result)