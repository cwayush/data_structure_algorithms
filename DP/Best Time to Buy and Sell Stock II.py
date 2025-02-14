from typing import List
class Solution:
    def buy_sell(self,i,buy,prices,n):
        if i==n:
            return 0

        profit = 0
        if buy:
            profit = max(-prices[i] + self.buy_sell(i+1,0,prices,n), 0 + self.buy_sell(i+1,1,prices,n) )

        else:
            profit = max(prices[i] + self.buy_sell(i+1,1,prices,n), 0 + self.buy_sell(i+1,0,prices,n) )

        return profit

    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        return self.buy_sell(0,1,prices,n)

# Approach-1 (Recursion)
# T.C : Exponential
# S.C : O(n) 

##############################################################################################################################################


    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp = [[-1]*(2) for _ in range(n+1)]

        dp[n][0] = dp[n][1] = 0

        for i in range(n-1,-1,-1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(-prices[i] + dp[i+1][0], 0 + dp[i+1][1])

                else:
                    profit = max(prices[i] + dp[i+1][1], 0 + dp[i+1][0])

                dp[i][buy] = profit

        return dp[0][1]
    
# Approach-2 (Bottom Up)
# T.C : O(2n)
# S.C : O(2n) 

##############################################################################################################################################

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        ahead =[0]*2
        curr =[0]*2

        ahead[0] = ahead[1] = 0

        for i in range(n-1,-1,-1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(-prices[i] + ahead[0], 0 + ahead[1])

                else:
                    profit = max(prices[i] + ahead[1], 0 + ahead[0])

                curr[buy] = profit
            ahead = curr

        return ahead[1]
    
# Approach-3 (Space Optimal)
# T.C : O(2n)
# S.C : O(1) 

sol=Solution()

prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))