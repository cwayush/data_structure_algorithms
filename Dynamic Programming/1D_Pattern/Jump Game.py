from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0

        for i in range(len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])

        return True
    
# Approach-1 (Bottom Up)
# T.C : O(n)        
# S.C : O(1)
    
sol=Solution()

nums = [2,3,1,1,4]
print(sol.canJump(nums))