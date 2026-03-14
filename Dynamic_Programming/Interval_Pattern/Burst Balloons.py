from typing import List

class Solution:
    def solve(self,i,j,nums):
        if i>j:
            return 0

        maxi = float('-inf')
        for idx in range(i,j+1):
            cost = nums[i-1]*nums[idx]*nums[j+1] + self.solve(i,idx-1,nums) + self.solve(idx+1,j,nums)

            maxi=max(cost,maxi)

        return maxi 

    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        nums.insert(0,1)
        nums.append(1)
        return self.solve(1,n,nums)
    
# Approach-1 (Recursion)
# T.C : Exponential
# S.C : Exponential

##############################################################################################################################################

class Solution:
    def solve(self,i,j,nums,dp):
        if i>j:
            return 0

        if dp[i][j]!=-1:
            return dp[i][j]
        maxi = float('-inf')
        for idx in range(i,j+1):
            cost = nums[i-1]*nums[idx]*nums[j+1] + self.solve(i,idx-1,nums,dp) + self.solve(idx+1,j,nums,dp)

            maxi=max(cost,maxi)

        dp[i][j] = maxi
        return dp[i][j] 

    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        nums.insert(0,1)
        nums.append(1)
        dp=[[-1]*(n+1) for _ in range(n+1)]
        return self.solve(1,n,nums,dp)
    
# Approach-2 (Memoization)
# T.C : O(n^3)
# S.C : O(n^2) + Auxillary Stack Space

##############################################################################################################################################

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        nums.insert(0,1)
        nums.append(1)
        dp=[[0]*(n+2) for _ in range(n+2)]
        for i in range(n,0,-1):
            for j in range(1,n+1):
                if i>j:
                    continue
                maxi = float('-inf')
                for idx in range(i,j+1):
                    cost = nums[i-1]*nums[idx]*nums[j+1] + dp[i][idx-1] + dp[idx+1][j]
                    maxi=max(cost,maxi)

                dp[i][j] = maxi

        return dp[1][n]
    
# Approach-3 (Tabulation)
# T.C : O(n^3)
# S.C : O(n^2)


sol=Solution()

nums = [3,1,5,8]
print(sol.maxCoins(nums))
