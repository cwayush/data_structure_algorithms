from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        l_x = x + k - 1
        l_y = y + k - 1

        top = x
        bottom = l_x

        while top < bottom:
            for j in range(y, l_y + 1):
                grid[top][j], grid[bottom][j] = grid[bottom][j], grid[top][j]

            top += 1
            bottom -= 1

        return grid
    
# Approach-1 (Brute Force)
# T.C : O(n**2)
# S.C : O(1)