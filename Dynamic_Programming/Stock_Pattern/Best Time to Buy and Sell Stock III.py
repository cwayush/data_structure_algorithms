from typing import List

class Solution:
    def buy_sell(self,idx,buy,cap,prices,n):
        if idx == n or cap == 0:
            return 0

        if buy:
            return max(-prices[idx] + self.buy_sell(idx+1,0,cap,prices,n),
                                0 + self.buy_sell(idx+1,1,cap,prices,n))

        return max(prices[idx] + self.buy_sell(idx+1,1,cap-1,prices,n),
                                0 + self.buy_sell(idx+1,0,cap,prices,n))

    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        return self.buy_sell(0,1,2,prices,n)
      
# Approach-1 (Recursion) 
# T.C : EXPONENTIAL
# S.C : AUXILLARY STACK SPACE
    
    
##############################################################################################################################################

class Solution:
    def buy_sell(self,idx,buy,cap,prices,n,memo):
        if idx == n or cap == 0:
            return 0

        if memo[idx][buy][cap]!=-1:
            return memo[idx][buy][cap]

        if buy:
            memo[idx][buy][cap] = max(-prices[idx] + self.buy_sell(idx+1,0,cap,prices,n,memo),
                                0 + self.buy_sell(idx+1,1,cap,prices,n,memo))

        else:
            memo[idx][buy][cap] = max(prices[idx] + self.buy_sell(idx+1,1,cap-1,prices,n,memo),
                                    0 + self.buy_sell(idx+1,0,cap,prices,n,memo))

        return memo[idx][buy][cap]

    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        memo = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]  

        return self.buy_sell(0,1,2,prices,n,memo)
       
# Approach-2 (Memoization)
# T.C : O(n*2*3)    
# S.C : O(n*2*3) + Auxillary Stack space
    
##############################################################################################################################################

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]  

        for i in range(n+1):
            for j in range(2):
                dp[i][j][0] = 0

        for i in range(2):
            for j in range(3):
                dp[n][i][j] = 0

        for idx in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,3):
                    if buy:
                        dp[idx][buy][cap] = max(-prices[idx] + dp[idx+1][0][cap],0 + dp[idx+1][1][cap])

                    else:
                        dp[idx][buy][cap] = max(prices[idx] + dp[idx+1][1][cap-1], 0 + dp[idx+1][0][cap])
            
        return dp[0][1][2]
       
# Approach-3 (Tabulation)
# T.C : O(n*2*3)
# S.C : O(n*2*3)
            
##############################################################################################################################################
            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*5 for _ in range(n+1)]

        for idx in range(n-1,-1,-1):
            for trans in range(4,-1,-1):
                if trans % 2 == 0:  # Buy
                    if trans < 4:
                        dp[idx][trans] = max(-prices[idx] + dp[idx+1][trans+1], dp[idx+1][trans])
                    else:
                        dp[idx][trans] = dp[idx+1][trans] 
                else:  # Sell
                    if trans < 4:
                        dp[idx][trans] = max(prices[idx] + dp[idx+1][trans+1], dp[idx+1][trans])
                    else:
                        dp[idx][trans] = dp[idx+1][trans]


        return dp[0][0]
    
# Approach-4 (Optimal Tabulation) : Use (idx,trans) insted of (idx,buy,cap) : trans: buy(0) sell(1) buy(2) sell(3)
# T.C : O(n*2*3)
# S.C : O(n*2*3)
            
sol=Solution()

prices = [3,3,5,0,0,3,1,4]
print(sol.maxProfit(prices))