class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        dp = [0]*(n+1)
        isPal = [[False]*n for _ in range(n)]

        for i in range(n):
            isPal[i][i] = True

        for i in range(n-1):
            isPal[i][i+1] = (s[i] == s[i+1])

        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                isPal[i][j] = (s[i] == s[j] and isPal[i+1][j-1])

        for i in range(n-1,-1,-1):
            minCost = float('inf')

            for j in range(i,n):
                if isPal[i][j]:
                    cost = 1 + dp[j+1]

                    minCost = min(minCost,cost)

            dp[i] = minCost

        return dp[0] - 1
    
# Approach-1 (Bottom Up)
# T.C : O(m*n)
# S.C : O(m*n)
    
sol=Solution()
s = "abcbadeabcba"

print(sol.minCut(s))

# abcba | d | e | abcba
