from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n

        for i,num in enumerate(nums):
            result[i] = nums[num]
        return result

# Approach-1 (Hashmap)
# T.C : O(n)        
# S.C : O(n) 

##############################################################################################################################################

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[nums[_]] for _ in range(n)]

# Approach-2 (In build Feature)
# T.C : O(n)        
# S.C : O(1) 

##############################################################################################################################################

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i]+= 1000*(nums[nums[i]]%1000)

        for i in range(n):
            nums[i] = nums[i]//1000

        return nums
    
# Approach-3 (Math)
# T.C : O(n)        
# S.C : O(1) 

sol=Solution()

nums = [5,0,1,2,3,4]
print(sol.buildArray(nums))