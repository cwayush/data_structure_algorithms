from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        def reverse(i,j):
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
            return nums

        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        
        return nums
    
# Approach-1 (Array_)
# T.C : O(n)
# S.C : O(1) 

sol=Solution()

nums = [1,2,3,4,5,6,7]
k = 3
print(sol.rotate(nums,k))