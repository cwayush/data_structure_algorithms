from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*(2*k+1) for _ in range(n+1)]

        for idx in range(n-1,-1,-1):
            for trans in range(2*k,-1,-1):
                if trans % 2 == 0:  # Buy
                    if trans < 2*k:
                        dp[idx][trans] = max(-prices[idx] + dp[idx+1][trans+1], dp[idx+1][trans])
                    else:
                        dp[idx][trans] = dp[idx+1][trans] 
                else:  # Sell
                    if trans < 2*k:
                        dp[idx][trans] = max(prices[idx] + dp[idx+1][trans+1], dp[idx+1][trans])
                    else:
                        dp[idx][trans] = dp[idx+1][trans]


        return dp[0][0]

# Approach-1 (Tabulation)
# T.C : O(n*k)
# S.C : O(n*k)

sol=Solution()
k = 2
prices = [3,2,6,5,0,3]
print(sol.maxProfit(k,prices))