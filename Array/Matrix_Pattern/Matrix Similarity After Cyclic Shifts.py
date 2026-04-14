from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        n = len(mat)
        m = len(mat[0])

        new_mat = [row[:] for row in mat]

        for _ in range(k):
            temp = []

            for i in range(n):
                row = new_mat[i][:]

                if i%2 == 0:
                    row = row[1:] + [row[0]]

                else:
                    row = [row[-1]] + row[:-1]

                temp.append(row)

            new_mat = temp
    
        return mat == new_mat