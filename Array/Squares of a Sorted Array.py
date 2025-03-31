from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n

        left = 0
        right = n-1
        for i in range(n-1,-1,-1):
            if abs(nums[left])>abs(nums[right]):
                result[i] = nums[left]**2
                left+=1
            else:
                result[i] = nums[right]**2
                right-=1

        return result
    
# Approach-1 (Array_)
# T.C : O(n)
# S.C : O(n) 

sol=Solution()

nums = [-4,-1,0,3,10]
print(sol.sortedSquares(nums))