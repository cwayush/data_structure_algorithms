from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        pre = 0
        suff = 0
        maxpro = float('-inf')

        for i in range(n):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1

            pre = pre*nums[i]
            suff = suff*nums[n-i-1]
            maxpro = max(maxpro,pre,suff)

        return maxpro
    
# Approach-1 (Array)
# T.C : O(n)
# S.C : O(1) 

sol=Solution()

nums = [2,3,-2,4]
print(sol.maxProduct(nums))