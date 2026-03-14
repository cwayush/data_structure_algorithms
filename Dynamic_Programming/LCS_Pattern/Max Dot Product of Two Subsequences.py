from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        memo = [[float('-inf')]*501 for _ in range(501)]

        def solve(i,j):
            if (i==n or j==m):
                return float('-inf')

            if memo[i][j] != float('-inf'):
                return memo[i][j]

            product = nums1[i]*nums2[j]

            take_i_j = product + solve(i+1,j+1)
            take_i = solve(i,j+1)
            take_j = solve(i+1,j)

            memo[i][j] = max(product, take_i_j, take_i, take_j)

            return memo[i][j]

        return solve(0,0)
    
# Approach-1 (Memoization)
# T.C : O(n*m)
# S.C : O(n*m)

sol=Solution()

nums1 = [2,1,-2,5]
nums2 = [3,0,-6]
print(sol.maxDotProduct(nums1,nums2))