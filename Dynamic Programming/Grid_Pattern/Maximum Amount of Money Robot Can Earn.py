from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n = len(coins)
        m = len(coins[0])

        def solve(i,j,k):
            if i >= n or j >= m:
                return float('-inf')

            if i == n-1 and j == m-1:
                if coins[i][j] < 0 and k > 0:
                    return 0
                return coins[i][j]

            val = coins[i][j]

            if val >= 0:
                return val + max(solve(i+1,j,k),solve(i,j+1,k))

            else:
                skip = val + max(solve(i+1,j,k),solve(i,j+1,k))

                use = float('-inf')
                if k>0:
                    use = max(solve(i+1,j,k-1),solve(i,j+1,k-1))

                return max(use,skip)

        return solve(0,0,2)

# Approach-1 (Recursive)
# T.C : O(2^(n*m))
# S.C : Auxillary Stack Space

##############################################################################################################################################

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n = len(coins)
        m = len(coins[0])

        dp = [[[None]*3 for _ in range(m)] for _ in range(n)]

        def solve(i,j,k):
            nonlocal dp
            if i >= n or j >= m:
                return float('-inf')

            if i == n-1 and j == m-1:
                if coins[i][j] < 0 and k > 0:
                    return 0
                return coins[i][j]

            if dp[i][j][k] is not None:
                return dp[i][j][k]

            val = coins[i][j]

            if val >= 0:
                dp[i][j][k] = val + max(solve(i+1,j,k),solve(i,j+1,k))

            else:
                skip = val + max(solve(i+1,j,k),solve(i,j+1,k))

                use = float('-inf')
                if k>0:
                    use = max(solve(i+1,j,k-1),solve(i,j+1,k-1))

                dp[i][j][k] = max(use,skip)
                
            return dp[i][j][k]

        return solve(0,0,2)
    
# Approach-2 (Memoization/Top Down)
# T.C : O(n*m)
# S.C : O(n*m) + Auxillary Stack Space

sol=Solution()

coins = [[0,1,-1],[1,-2,3],[2,-3,4]]
print(sol.maximumAmount(coins))