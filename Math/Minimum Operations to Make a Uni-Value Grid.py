from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m=len(grid)
        n=len(grid[0])

        vec=[]
        for i in range(m):
            for j in range(n):
                vec.append(grid[i][j])

        length = len(vec)

        vec.sort()
        target = vec[length//2]
        result = 0
        for num in vec:
            if num%x != target%x:
                return -1

            result+=abs(target-num)//x

        return result
    
# Approach-1 (Sorting)
# T.C : O(n*m(*log(n*m)))
# S.C : O(n*m) 

sol=Solution()

grid = [[2,4],[6,8]]
x = 2
print(sol.minOperations(grid,x))