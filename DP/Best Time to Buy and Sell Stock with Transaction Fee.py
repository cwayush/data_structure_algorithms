from typing import List

class Solution:     
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        dp = [[-1]*(2) for _ in range(n+1)]

        dp[n][0] = dp[n][1] = 0

        for i in range(n-1,-1,-1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(-prices[i] + dp[i+1][0], 0 + dp[i+1][1])

                else:
                    profit = max(prices[i] - fee + dp[i+1][1], 0 + dp[i+1][0])

                dp[i][buy] = profit

        return dp[0][1]
    
# Approach-1 (Tabulation)
# T.C : O(n*2)
# S.C : O(n*2)

sol=Solution()

prices = [1,3,2,8,4,9]
fee = 2
print(sol.maxProfit(prices,fee))