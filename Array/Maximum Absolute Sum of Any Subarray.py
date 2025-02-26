from typing import List

class Solution:

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_end_here = max_so_far = 0
        min_end_here = min_so_far = 0

        for num in nums:
            max_end_here+=num
            min_end_here+=num

            max_end_here = max(max_end_here,0)
            min_end_here = min(min_end_here,0)

            max_so_far = max(max_end_here,max_so_far)
            min_so_far = min(min_end_here,min_so_far)

        return max(max_so_far,abs(min_so_far))
    
# Approach-1 (Space_Optimal)
# T.C : O(n)
# S.C : O(1)
    
sol=Solution()

nums = [2,-5,1,-4,3,-2]
print(sol.maxAbsoluteSum(nums))