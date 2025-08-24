from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        minRow = n
        maxRow = -1
        minCol = m
        maxCol = -1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    minRow = min(minRow,i)
                    maxRow = max(maxRow,i)

                    minCol = min(minCol,j)
                    maxCol = max(maxCol,j)

        return (maxRow - minRow + 1)*(maxCol - minCol + 1)
    
# Approach-1 (Matrix Traversal)
# T.C : O(n*m)
# S.C : O(1)

sol = Solution()

grid = [[1,1,0,0,1],
        [0,0,1,0,0],
        [1,0,0,1,0],
        [0,1,0,0,1],
        [1,0,1,0,1]]
print(sol.minimumArea(grid))