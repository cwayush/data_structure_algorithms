class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n=len(p)
        m=len(s)
        dp=[[False]*(m+1) for _ in range(n+1)]

        dp[0][0] = True

        for j in range(1,m+1):
            dp[0][j]=False

        for i in range(1,n+1):
            if p[i-1] =='*':
                dp[i][0] = dp[i-1][0]


        for i in range(1,n+1):
            for j in range(1,m+1):
                if p[i-1]==s[j-1] or p[i-1]=='?':
                    dp[i][j] = dp[i-1][j-1]
                
                elif p[i-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]

                else:
                    dp[i][j] = False


        return dp[n][m]
    
# Approach-1 (Bottom Up)
# T.C : O(n*m)
# S.C : O(n*m)

sol=Solution()

s = "cb"
p = "?a"
print(sol.isMatch(s,p))
        