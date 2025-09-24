from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiagonalSq = 0   
        maxArea = 0

        for i in range(len(dimensions)):
            l, w = dimensions[i]
            diagSq = l*l + w*w
            area = l * w

            if diagSq > maxDiagonalSq:
                maxDiagonalSq = diagSq
                maxArea = area
            elif diagSq == maxDiagonalSq and area > maxArea:
                maxArea = area

        return maxArea

# Approach-1 (Math)
# T.C : O(n)
# S.C : O(1) 

sol = Solution()
dimensions = [[5,4],[3,4],[2,3]]    
print(sol.areaOfMaxDiagonal(dimensions))