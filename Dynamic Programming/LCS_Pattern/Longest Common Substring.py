class Solution:
    def longestCommonSubstr(self, s1, s2):
        n=len(s1)
        m=len(s2)
        dp=[[-1]*(m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0]=0
        for j in range(m+1):
            dp[0][j]=0

        ans = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    ans = max(ans,dp[i][j])
                
                else:
                    dp[i][j] = 0

        return ans
    
# Approach-1 (Bottom Up)
# T.C : O(m*n)
# S.C : O(m*n)
    
sol=Solution()
input1 = "ABCDGH"
input2 = "ACDGHR"

print(sol.longestCommonSubstr(input1,input2))