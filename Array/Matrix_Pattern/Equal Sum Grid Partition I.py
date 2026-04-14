from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])

        total = sum(sum(row) for row in grid)

        if total % 2:
            return False

        target = total // 2

        summ = 0

        for i in range(n-1):
            summ += sum(grid[i])

            if summ == target:
                return True

        summ = 0

        for j in range(m-1):
            for i in range(n):
                summ += grid[i][j]

            if summ == target:
                return True

        return False