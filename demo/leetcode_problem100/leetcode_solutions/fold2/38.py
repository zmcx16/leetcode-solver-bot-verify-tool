class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        prev = self.countAndSay(n-1)
        result = ''
        count = 1
        for i in range(1, len(prev)):
            if prev[i] == prev[i-1]:
                count += 1
            else:
                result += str(count) + prev[i-1]
                count = 1
        result += str(count) + prev[-1]
        return result