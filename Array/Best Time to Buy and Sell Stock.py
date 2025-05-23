from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for price in prices[1:]:
            if buy_price>price:
                buy_price = price
            profit = max(profit, price - buy_price)

        return profit

# Approach-1 (Greedy)
# T.C : O(n)        
# S.C : O(1)

sol=Solution()

prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))