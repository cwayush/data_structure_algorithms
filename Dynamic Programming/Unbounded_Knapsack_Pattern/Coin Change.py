from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [[0]*(amount+1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 0

        for j in range(amount+1):
            dp[0][j] = dp[0][j] = j // coins[0] if j % coins[0] == 0 else float('inf')
    

        for i in range(1,n):
            for j in range(1,amount+1):
                exclude = dp[i-1][j]

                include = float('inf')
                if coins[i] <= j:
                    include = 1 + dp[i][j-coins[i]]

                dp[i][j] = min(include,exclude)

        ans = dp[n-1][amount] 

        if ans == float('inf'):
            return -1
        return ans
        