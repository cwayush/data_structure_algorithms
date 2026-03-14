from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res,maxDiff,maxEl = 0,0,0

        for k in range(n):
            res = max(res,maxDiff*nums[k])
            maxDiff = max(maxDiff,maxEl - nums[k])
            maxEl = max(maxEl,nums[k])

        return res       
    
# Approach-1 (Greedy Optimise)
# T.C : O(n)
# S.C : O(1) 

sol=Solution()

nums = [12,6,1,2,7]
print(sol.maximumTripletValue(nums))