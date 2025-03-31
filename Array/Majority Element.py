from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # number = None
        count = 0
        for num in nums:
            if count == 0:
                majEl = num
                count+=1
            elif num == majEl:
                count+=1
            else:
                count -=1
        
        return majEl
    
# Approach-1 (Array_)
# T.C : O(n)
# S.C : O(1) 

sol=Solution()

nums = [3,2,3]
print(sol.majorityElement(nums))
    
