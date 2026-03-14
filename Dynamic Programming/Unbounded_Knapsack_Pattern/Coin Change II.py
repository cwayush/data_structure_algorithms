from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[0]*(amount+1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1
        
        for j in range(amount+1):
            dp[0][j] = 1 if j%coins[0] == 0 else 0
        
        for i in range(1,n):
            for j in range(amount+1):
                exclude = dp[i-1][j]
                include = 0
                if coins[i] <= j:
                    include = dp[i][j-coins[i]]
                
                dp[i][j] = exclude + include

        return dp[n-1][amount]
        