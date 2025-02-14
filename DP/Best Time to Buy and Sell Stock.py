class Solution(object):
    def maxProfit(self, prices):
        mini=prices[0]
        maxi_profit=0
        for i in range(1,len(prices)):
            cost =(prices[i]-mini)
            maxi_profit=max(maxi_profit,cost)
            mini =min(mini,prices[i])
        return maxi_profit
            
# Approach-1 (Greedy Algo)
# T.C : O(n)
# S.C : O(1) 
            
sol=Solution()

prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))