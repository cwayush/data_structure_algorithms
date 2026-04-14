from typing import List

class Solution:
    def __init__(self):
        self.totalSum = 0

    def checkHorizontal(self, grid):
        n = len(grid)
        m = len(grid[0])

        seen = set()
        top = 0

        for i in range(n-1):
            for j in range(m):
                seen.add(grid[i][j])
                top += grid[i][j]

            bottom = self.totalSum - top
            diff = top - bottom  

            if diff == 0:
                return True

            if diff == grid[0][0]: return True
            if diff == grid[0][m-1]: return True
            if diff == grid[i][0]: return True

            if i > 0 and m > 1 and diff in seen:
                return True

        return False


    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        n = len(grid)
        m = len(grid[0])

        self.totalSum = 0
        for i in range(n):
            for j in range(m):
                self.totalSum += grid[i][j]

        if (self.checkHorizontal(grid)):
            return True

        grid_rev = grid[::-1]

        if (self.checkHorizontal(grid_rev)):
            return True

        transpose = [[grid[i][j] for i in range(n)] for j in range(m)]

        if self.checkHorizontal(transpose):
            return True
        
        transpose_rev = transpose[::-1]

        if self.checkHorizontal(transpose_rev):
            return True

        return False