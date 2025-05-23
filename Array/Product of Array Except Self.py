from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = [1]*n

        for i in range(1,n):
            product[i] = product[i-1]*nums[i-1]

        right = nums[-1]
        for i in range(n-2,-1,-1):
            product[i] = product[i]*right
            right = right*nums[i]

        return product
    
# Approach-1 (Hashmap)
# T.C : O(n)
# S.C : O(1) 

sol=Solution()

nums = [1,2,3,4]
print(sol.productExceptSelf(nums))