from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        fornt1=[0]*2
        fornt2=[0]*2

        for i in range(n-1,-1,-1):
            curr=[0]*2
            curr[1] = max(-prices[i] + fornt1[0], 0 + fornt1[1])

            curr[0] = max(prices[i] + fornt2[1], 0 + fornt1[0])

            fornt2 = fornt1
            fornt1 = curr

        return curr[1]
    
# Approach-1 (Space Optimal)
# T.C : O(n)
# S.C : O(1)

sol=Solution()

prices = [1,2,3,0,2]
print(sol.maxProfit(prices))