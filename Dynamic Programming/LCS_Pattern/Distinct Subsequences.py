class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        dp=[[-1]*(m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1
        for j in range(1,m+1):
            dp[0][j] = 0

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][m]
    
# Approach-1 (Bottom Up)
# T.C : O(m*n)
# S.C : O(m*n)

##############################################################################################################################################

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        prev = [0]*(n+1)
        curr = [0]*(m+1)

        prev[0]=curr[0]=1

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==t[j-1]:
                    curr[j] = prev[j-1] + prev[j]

                else:
                    curr[j] = prev[j]
                    
            prev = curr

        return prev[m]
    
# Approach-2 (Space Optimal)
# T.C : O(m*n)
# S.C : O(max(n,m))

##############################################################################################################################################

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        prev = [0]*(n+1)

        prev[0]=1

        for i in range(1,n+1):
            for j in range(m,-1,-1):
                if s[i-1]==t[j-1]:
                    prev[j] = prev[j-1] + prev[j]
                    

        return prev[m]
    
# Approach-3 (Space Optimal)
# T.C : O(m*n)
# S.C : O(n)

sol=Solution()

s = "babgbag"
t = "bag"
print(sol.numDistinct(s,t))   
        