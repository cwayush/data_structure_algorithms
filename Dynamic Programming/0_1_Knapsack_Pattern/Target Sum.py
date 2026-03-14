from typing import List

class Solution:
    def dfs(self,i,nums,currentsum,target,memo):
        if i == len(nums):
            return 1 if currentsum==target else 0
        
        if currentsum > target:  
            return 0  

        if memo[i][currentsum]!=-1:
            return memo[i][currentsum]

        exclude = self.dfs(i+1,nums,currentsum,target,memo)
        include = 0
        if currentsum + nums[i] <= target:
            include= self.dfs(i+1,nums,currentsum + nums[i],target,memo)

        memo[i][currentsum]= include + exclude

        return memo[i][currentsum]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        totalsum = sum(nums)
        if (target + totalsum)%2!=0 or target>totalsum:
            return 0
        s1 = (target + totalsum)//2
        memo=[[-1]*(s1+1) for _ in range(n)]

        return self.dfs(0,nums,0,s1,memo)
        