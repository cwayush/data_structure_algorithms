from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        
        count=0
        majEl =-1
        for num in nums:
            if count==0:
                majEl =num
                count=1

            elif majEl == num:
                count+=1
            else:
                count-=1

        majElCount = 0
        for num in nums:
            if num == majEl:
                majElCount+=1
        
        count=0
        for i,num in enumerate(nums):
            if num == majEl:
                count+=1

            remaing_count = majElCount - count
            n1= i+1
            n2 = len(nums)-i-1
            if count*2>n1  and remaing_count*2>n2:
                return i 

        return -1
    
# Approach-1 (Boyre Moore Algorithm)
# T.C : O(n)
# S.C : O(1) 

sol=Solution()

nums = [2,1,3,1,1,1,7,1,2,1]
print(sol.minimumIndex(nums))