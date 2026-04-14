from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        n, m = len(grid), len(grid[0])

        arr = []
        for i in range(n):
            for j in range(m):
                arr.append(grid[i][j] % mod)

        size = len(arr)

        prefix = [1] * size
        suffix = [1] * size

        for i in range(1, size):
            prefix[i] = (prefix[i-1] * arr[i-1]) % mod

        for i in range(size-2, -1, -1):
            suffix[i] = (suffix[i+1] * arr[i+1]) % mod

        res = []
        k = 0
        for i in range(n):
            row = []
            for j in range(m):
                row.append((prefix[k] * suffix[k]) % mod)
                k += 1
            res.append(row)

        return res
    
# Approach-1 (Prefix Sum)
# T.C : O(n*m)
# S.C : O(n*m)

sol = Solution()

grid = [[1,2],[3,4]]
print(sol.constructProductMatrix(grid))