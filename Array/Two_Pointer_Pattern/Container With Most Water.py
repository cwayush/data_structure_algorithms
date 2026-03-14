from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water=0
        i=0
        j=len(height)-1
        while i<j:
            store_water=min(height[i],height[j])*(j-i)
            max_water=max(max_water,store_water)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_water
    
# Approach-1 (Two Pointer)
# T.C : O(n)
# S.C : O(1)

sol=Solution()

height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))
        