from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        curr = count = 0 
        for num in nums:
            if num==0:
                curr+=1
                count+=curr
            else:
                curr=0

        return count
    
# Approach-1 (Iterate)
# T.C : O(n)
# S.C : O(1) 
    
sol = Solution()
nums = [1,3,0,0,2,0,0,4]
print(sol.zeroFilledSubarray(nums))  