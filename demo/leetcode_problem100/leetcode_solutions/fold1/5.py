class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        table = [[False] * n for _ in range(n)]
        start, max_len = 0, 1
        for i in range(n):
            table[i][i] = True
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j] and (j - i <= 2 or table[i+1][j-1]):
                    table[i][j] = True
                    if j - i + 1 > max_len:
                        start = i
                        max_len = j - i + 1
        return s[start:start+max_len]
