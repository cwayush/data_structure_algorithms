from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        n = len(nums)
        i=j=0
        summ = 0
        while j<n:
            summ+=nums[j]
            while i<=j and summ*(j-i+1)>=k:
                summ-=nums[i]
                i+=1

            result+=(j-i+1)
            j+=1
        return result

# Approach-1 (Sliding Window)
# T.C : O(n)
# S.C : O(1)
    
sol=Solution()

nums=[2,1,4,3,5]
k = 10
print(sol.countSubarrays(nums,k))