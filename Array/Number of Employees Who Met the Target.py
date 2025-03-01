from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        nums = hours
        return sum(num>=target for num in nums)
        
# Approach-1 (Traversal)
# T.C : O(n)
# S.C : O(1)

sol=Solution()

hours = [0,1,2,3,4]
target = 2
print(sol.numberOfEmployeesWhoMetTarget(hours,target))