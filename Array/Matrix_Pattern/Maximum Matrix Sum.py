from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_abs_val = float("inf")
        negative_count = 0

        for row in matrix:
            for val in row:
                total_sum += abs(val)
                if val < 0:
                    negative_count += 1
                min_abs_val = min(min_abs_val, abs(val))

        if negative_count % 2 != 0:
            total_sum -= 2 * min_abs_val

        return total_sum
    
# Approach-1 (Greedy)
# T.C : O(n*m)
# S.C : O(1)

sol = Solution()

matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
print(sol.maxMatrixSum(matrix))