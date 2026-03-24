from typing import List

class Solution:
    def solve90(self,mat):
        n = len(mat)
        res = [[0]*n for _ in range(n)] 

        for i in range(n):
            for j in range(n):
                res[j][n-i-1] = mat[i][j]

        for i in range(n):
            for j in range(n):
                mat[i][j] = res[i][j]

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:        

        for _ in range(4):  
            if mat == target:
                return True
            self.solve90(mat)

        return False