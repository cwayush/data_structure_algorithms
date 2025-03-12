from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count_neg=0
        count_pos=0

        for num in nums:
            if num<0:
                count_neg+=1
            elif num>0:
                count_pos+=1

        return max(count_neg,count_pos)
    
# Approach-1 (Traversal)
# T.C : O(n)
# S.C : O(1)  

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def first_positive():
            left =0
            right =len(nums)-1
            index = len(nums)
            while left<=right:
                mid=(left+right)//2
                if nums[mid]>0:
                    index = mid
                    right = mid-1
                else:
                    left = mid+1
            return index

        def first_non_negative():
            left =0
            right =len(nums)-1
            index = len(nums)
            while left<=right:
                mid=(left+right)//2
                if nums[mid]>=0:
                    index = mid
                    right = mid-1
                else:
                    left = mid+1
            return index

        count_negative = first_non_negative()
        count_positive = len(nums) - first_positive()

        return max(count_negative,count_positive)
    
# Approach-2 (Binary Search)
# T.C : O(log n)
# S.C : O(1)  

sol=Solution()

nums = [-3,-2,-1,0,0,1,2]
print(sol.maximumCount(nums))