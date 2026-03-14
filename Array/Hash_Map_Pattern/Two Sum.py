from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = defaultdict(int)
        for i,num in enumerate(nums):
            rem = target - num
            if rem in mapp:
                return [mapp[rem],i]
            mapp[num] = i

        return -1
    
# Approach-1 (Hashmapp)
# T.C : O(n)        
# S.C : O(n)

sol=Solution()

nums = [2,7,11,15]
target = 9
print(sol.twoSum(nums,target))
