class Solution:
    def grayCode(self, n: int) -> List[int]:
        def backtrack(curr, used):
            if len(curr) == 2**n:
                return curr
            for i in range(n):
                next_num = curr[-1] ^ (1 << i)
                if next_num not in used:
                    used.add(next_num)
                    result = backtrack(curr + [next_num], used)
                    if result:
                        return result
                    used.remove(next_num)
        return backtrack([0], {0})