from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num))%2==0:
                count+=1
        return count
    
# Approach-1 (Math)
# T.C : O(n)
# S.C : O(1)
    
sol=Solution()

nums = [12,345,2,6,7896,673989]
print(sol.findNumbers(nums))
