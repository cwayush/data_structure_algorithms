from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_El = max(nums)
        n = len(nums)
        indices = []
        result = 0
        for i,num in enumerate(nums):
            if num==max_El:
                indices.append(i)

            if len(indices)>=k:
                last_idx= indices[len(indices) - k]
                result+=(last_idx+1)

        return result
    
# Approach-1 (Array)
# T.C : O(n)
# S.C : O(n)
    
sol=Solution()

nums=[1,3,2,3,3]
k = 2
print(sol.countSubarrays(nums,k))