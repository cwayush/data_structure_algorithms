from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum2 = 0
        zero1 = zero2 = 0
        for num in nums1:
            sum1+=num
            if num == 0:
                sum1+=1
                zero1+=1

        for num in nums2:
            sum2+=num
            if num == 0:
                sum2+=1
                zero2+=1

        if (zero1 == 0 and sum2>sum1) or (zero2 == 0 and sum1>sum2):
            return -1

        return max(sum1,sum2)
    
# Approach-1 (Greedy)
# T.C : O(n)        
# S.C : O(1) 
    
sol=Solution()

nums1 = [3,2,0,1,0]
nums2 = [6,5,0]
print(sol.minSum(nums1,nums2))