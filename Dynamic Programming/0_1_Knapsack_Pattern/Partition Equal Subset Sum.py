from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        summ = 0
        for num in nums:
            summ+=num

        if summ%2!=0:
            return False

        target = summ//2

        dp = [[None]*(target+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = True

        for j in range(1,target+1):
            dp[0][j] = False

        for i in range(1,n+1):
            for j in range(1,target+1):
                if nums[i-1]<=j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]

                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][target]

# Approach-1 (Bottom up)
# T.C : O(n*m)
# S.C : O(n*m)      

sol=Solution()

nums = [1,5,11,5]
print(sol.canPartition(nums))