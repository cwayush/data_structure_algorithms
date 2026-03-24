class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n + m != len(s3):
            return False

        dp = [[False]*(m+1) for _ in range(n+1)]

        dp[0][0] = True

        for i in range(n+1):
            for j in range(m+1):
                if i>0 and s1[i-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i-1][j]

                if j>0 and s2[j-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i][j-1]

        return dp[n][m]
    
# Approach-1 (Bottom Up)
# T.C : O(m*n)
# S.C : O(m*n)

sol=Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

print(sol.isInterleave(s1,s2,s3))