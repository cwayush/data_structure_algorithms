from typing import List

class Solution:
    def recursion(self,idx,prev_idx,nums,n):
        if idx==n:
            return 0

        lenn = 0 + self.recursion(idx+1,prev_idx,nums,n)
        if prev_idx==-1 or nums[idx]>nums[prev_idx]:
            lenn = max(lenn,1 + self.recursion(idx+1,idx,nums,n))

        return lenn
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        return self.recursion(0,-1,nums,n)

# Approach-1 (Recursion)
# T.C : Exponential
# S.C : O(n) 

##############################################################################################################################################

class Solution:
    def recursion(self,idx,prev_idx,nums,n,memo):
        if idx==n:
            return 0
        if memo[idx][prev_idx+1]!=-1:
            return memo[idx][prev_idx+1]

        lenn = 0 + self.recursion(idx+1,prev_idx,nums,n,memo)
        if prev_idx==-1 or nums[idx]>nums[prev_idx]:
            lenn = max(lenn,1 + self.recursion(idx+1,idx,nums,n,memo))
        memo[idx][prev_idx+1] = lenn
        
        return memo[idx][prev_idx+1]
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        memo = [[-1]*(n+1) for _ in range(n)]
        return self.recursion(0,-1,nums,n,memo)

# Approach-2 (Memoization)
# T.C : O(n^2)
# S.C : O(n^2)

##############################################################################################################################################

sol=Solution()

nums = [10,9,2,5,3,7,101,18]
print(sol.lengthOfLIS(nums))