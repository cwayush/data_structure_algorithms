from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        max_count = 0
        n = len(mat)
        m = len(mat[0])

        height=[0]*m

        for i in range(n):
            for j in range(m):
                if mat[i][j]:
                    height[j] +=1
                else:
                    height[j] = 0

            sum_rect = [0]*m
            stack = []

            for j in range(m):
                while stack and height[stack[-1]] >= height[j]:
                    stack.pop()

                if stack:
                    prev = stack[-1]
                    sum_rect[j] = sum_rect[prev] + height[j]*(j-prev)

                else:
                    sum_rect[j] = height[j]*(j+1)

                max_count += sum_rect[j]
                stack.append(j)

        return max_count            

sol = Solution()

mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
print(sol.numSubmat(mat))