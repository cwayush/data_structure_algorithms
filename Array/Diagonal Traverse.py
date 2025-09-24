from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n,m = len(mat), len(mat[0])

        res = []
        intermediate = []

        for d in range(n+m-1):
            intermediate.clear()

            r,c = 0 if d<m else d-m+1, d if d<m else m-1

            while r<n and c>-1:
                intermediate.append(mat[r][c])
                r+=1
                c-=1

            if d%2==0:
                res.extend(intermediate[::-1])
            else:
                res.extend(intermediate)

        return res
    
sol = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.findDiagonalOrder(mat))