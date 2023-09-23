class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n != len(s2):
            return False
        dp = [[[False] * (n+1) for _ in range(n)] for _ in range(n)]
        for length in range(1, n+1):
            for i in range(n - length + 1):
                for j in range(n - length + 1):
                    if length == 1:
                        dp[i][j][length] = s1[i] == s2[j]
                    else:
                        for k in range(1, length):
                            if (dp[i][j][k] and dp[i + k][j + k][length - k]) or (dp[i][j + length - k][k] and dp[i + k][j][length - k]):
                                dp[i][j][length] = True
                                break
        return dp[0][0][n]