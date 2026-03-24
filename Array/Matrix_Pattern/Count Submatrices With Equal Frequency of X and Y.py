from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        cummSumX = [[0]*m for _ in range(n)]
        cummSumY = [[0]*m for _ in range(n)]

        count = 0

        for i in range(n):
            for j in range(m):

                cummSumX[i][j] = (grid[i][j] == 'X')
                cummSumY[i][j] = (grid[i][j] == 'Y')
                
                if j > 0:
                    cummSumX[i][j] += cummSumX[i][j-1] 
                    cummSumY[i][j] += cummSumY[i][j-1]

                if i > 0:
                    cummSumX[i][j] += cummSumX[i-1][j] 
                    cummSumY[i][j] += cummSumY[i-1][j]
                    
                if i > 0 and j > 0:
                    cummSumX[i][j] -= cummSumX[i-1][j-1]
                    cummSumY[i][j] -= cummSumY[i-1][j-1]

                if cummSumX[i][j] == cummSumY[i][j] and cummSumX[i][j] > 0:
                    count += 1

        return count
