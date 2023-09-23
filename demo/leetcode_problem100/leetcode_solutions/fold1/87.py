class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n != len(s2):
            return False
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = (s1[i] == s2[j])
        for k in range(2, n + 1):
            for i in range(n - k + 1):
                for j in range(n - k + 1):
                    for p in range(1, k):
                        if (dp[i][j][p] and dp[i + p][j + p][k - p]) or (dp[i][j + k - p][p] and dp[i + p][j][k - p]):
                            dp[i][j][k] = True
                            break
        return dp[0][0][n]