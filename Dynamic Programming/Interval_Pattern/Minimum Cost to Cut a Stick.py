from typing import List

class Solution:
    def solve(self,i,j,cuts,dp):
        if i>j:
            return 0

        if dp[i][j]!=-1:
            return dp[i][j]

        mini = float('inf')
        for idx in range(i,j+1):
            cost = cuts[j+1] - cuts[i-1] + self.solve(i,idx-1,cuts,dp) + self.solve(idx+1,j,cuts,dp)

            mini= min(mini,cost)
        dp[i][j] = mini
        return dp[i][j]

    def minCost(self, n: int, cuts: List[int]) -> int: 
        c= len(cuts)
        cuts.insert(0,0)
        cuts.append(n)
        dp =[[-1]*(c+1) for _ in range(c+1)]
        cuts.sort()
        return self.solve(1,c,cuts,dp)
    
# Approach-1 (Memoization)
# T.C : O(c^2)
# S.C : O(c^2) + Auxillary Stack Space

##############################################################################################################################################

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int: 
        c= len(cuts)
        cuts.insert(0,0)
        cuts.append(n)
        dp =[[0]*(c+2) for _ in range(c+2)]
        cuts.sort()
        for i in range(c,0,-1):
            for j in range(1,c+1):
                if i>j:
                    continue
                mini = float('inf')
                for idx in range(i,j+1):
                    cost = cuts[j+1] - cuts[i-1] + dp[i][idx-1] + dp[idx+1][j]
                    mini= min(mini,cost)

                dp[i][j] = mini

        return dp[1][c]
    
# Approach-2 (Tabulation)
# T.C : O(c^2)
# S.C : O(c^2) 

##############################################################################################################################################

sol=Solution()

n = 9
cuts = [5,6,1,4,2]
print(sol.minCost(n,cuts))