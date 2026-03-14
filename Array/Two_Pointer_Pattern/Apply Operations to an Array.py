from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1] and nums[i]!=0:
                nums[i] = 2*nums[i]
                nums[i+1] = 0
        
        idx=0
        for i in range(n):
            if nums[i]!=0:
                nums[idx] = nums[i]
                idx+=1

        while idx<n:
            nums[idx] = 0
            idx+=1

        return nums 
    
# Approach-1 (Space_Optimal)
# T.C : O(n)
# S.C : O(1)

sol=Solution()

arr =[1,2,2,1,1,0]
print(sol.applyOperations(arr))
