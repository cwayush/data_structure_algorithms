from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        summ=float('-inf')
        i=0
        j=len(height)-1
        while i<j:
            new_summ=min(height[i],height[j])*(j-i)
            summ=max(summ,new_summ)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return summ
    
# Approach-1 (Two Pointer)
# T.C : O(n)
# S.C : O(1)

sol=Solution()

height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))
        