from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        totalSum = sum(stones)
        target = totalSum//2

        dp = [[0]*(target+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(target+1):
                dp[i][j] = dp[i-1][j]
                if j >= stones[i-1]:
                    val = stones[i-1] + dp[i-1][j-stones[i-1]]
                    dp[i][j] = max(val,dp[i][j])

        return totalSum - 2*(dp[n][target])