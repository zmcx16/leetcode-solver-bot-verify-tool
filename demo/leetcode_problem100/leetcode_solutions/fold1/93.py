class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(s, position, current, result):
            if position == 3:
                if s and int(s) <= 255 and (len(s) == 1 or s[0] != '0'):
                    result.append(current + s)
                return
            for i in range(1, min(len(s), 4)):
                if int(s[:i]) <= 255 and (i == 1 or s[0] != '0'):
                    backtrack(s[i:], position + 1, current + s[:i] + '.', result)
        result = []
        backtrack(s, 0, '', result)
        return result