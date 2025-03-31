from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxi = float('-inf')
        summ = 0
        for num in nums:
            summ+=num
            maxi = max(maxi,summ)

            if summ<0:
                summ = 0
        return maxi
    
# Approach-1 (Kadane's Algorithm)
# T.C : O(n)
# S.C : O(1) 

sol=Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray(nums))