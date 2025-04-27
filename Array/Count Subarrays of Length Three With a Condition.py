from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        number = 0
        n = len(nums)
        if n<3:
            return number
        i = 0
        j = 2
        while j<n:
            if (nums[i]+nums[j])==nums[i+1]/2:
                number+=1
            i+=1
            j+=1
        return number
    
# Approach-1 (Two Pointer)
# T.C : O(n)
# S.C : O(1) 
    
sol=Solution()

nums = [1,2,1,4,1]
print(sol.countSubarrays(nums))