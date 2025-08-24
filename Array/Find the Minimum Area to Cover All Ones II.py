from typing import List

class Solution:

    def rotatedClock(self, grid):
        n = len(grid)
        m = len(grid[0])
        rotated = [[0]*n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                rotated[j][n-i-1] = grid[i][j]

        return rotated

    def minimumArea(self, rowStart, rowEnd, colStart, colEnd, grid):
        n = len(grid)
        m = len(grid[0])
        
        minRow, maxRow = n, -1
        minCol, maxCol = m, -1

        for i in range(rowStart, rowEnd):
            for j in range(colStart, colEnd):
                if grid[i][j] == 1:
                    minRow = min(minRow, i)
                    maxRow = max(maxRow, i)
                    minCol = min(minCol, j)
                    maxCol = max(maxCol, j)

        if maxRow == -1:   # no 1s
            return (0, False)

        area = (maxRow - minRow + 1) * (maxCol - minCol + 1)
        return (area, True)

    def utility_fun(self, grid):
        n = len(grid)
        m = len(grid[0])
        result = float('inf')

        # Case 1: split into top + bottom-left + bottom-right
        for i in range(1, n):
            for j in range(1, m):
                top, ok1 = self.minimumArea(0, i, 0, m, grid)
                bottomleft, ok2 = self.minimumArea(i, n, 0, j, grid)
                bottomright, ok3 = self.minimumArea(i, n, j, m, grid)

                if ok1 and ok2 and ok3:
                    result = min(result, top + bottomleft + bottomright)

                topleft, ok1 = self.minimumArea(0, i, 0, j, grid)
                topright, ok2 = self.minimumArea(0, i, j, m, grid)
                bottom, ok3 = self.minimumArea(i, n, 0, m, grid)

                if ok1 and ok2 and ok3:
                    result = min(result, topleft + topright + bottom)

        # Case 2: split into top + middle + bottom
        for i in range(1, n):
            for j in range(i+1, n):
                top, ok1 = self.minimumArea(0, i, 0, m, grid)
                middle, ok2 = self.minimumArea(i, j, 0, m, grid)
                bottom, ok3 = self.minimumArea(j, n, 0, m, grid)

                if ok1 and ok2 and ok3:
                    result = min(result, top + middle + bottom)

        return result

    def minimumSum(self, grid: List[List[int]]) -> int:
        result = self.utility_fun(grid)
        rotateGrid = self.rotatedClock(grid)
        result = min(result, self.utility_fun(rotateGrid))
        return result

# Approach-1 (Brute Force)
# T.C : O((n**2)*m)
# S.C : O(n*m) 


sol = Solution()

grid = [[1,0,1,0],[0,1,0,1]]
print(sol.minimumSum(grid))