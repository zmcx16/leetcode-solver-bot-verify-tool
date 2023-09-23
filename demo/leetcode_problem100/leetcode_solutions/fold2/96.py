class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for root in range(1, i+1):
                dp[i] += dp[root-1] * dp[i-root]
        return dp[n]