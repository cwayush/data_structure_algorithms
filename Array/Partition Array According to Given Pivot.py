from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        result=[0]*n
        
        i = i_ = 0
        j = j_ = n-1

        while i<n and j>=0:
            if nums[i]<pivot:
                result[i_] = nums[i]
                i_+=1
            
            if nums[j]>pivot:
                result[j_] = nums[j]
                j_-=1

            i+=1
            j-=1

        while i_ <= j_:
            result[i_] = pivot
            i_+=1
            
        return result

# Approach-1 (Two Pointer)
# T.C : O(n)
# S.C : O(n)
  
sol=Solution()

nums = [9,12,5,10,14,3,10]
pivot = 10
print(sol.pivotArray(nums,pivot))