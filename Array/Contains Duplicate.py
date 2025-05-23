from typing import List
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapp = defaultdict(int)

        for i,num in enumerate(nums):
            if num in mapp:
                return True
            mapp[num]+=1
        return False
    
# Approach-1 (Hashmap)
# T.C : O(n)        
# S.C : O(n)

##############################################################################################################################################

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            seen.add(num)

        return len(nums)!=len(seen)

# Approach-2 (Set)
# T.C : O(n)        
# S.C : O(1)

sol=Solution()

nums = [1,2,3,1]
print(sol.containsDuplicate(nums))