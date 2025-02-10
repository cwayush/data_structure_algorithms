class Solution:
    def lcs(self,text1,text2,n):
        dp=[[-1]*(n+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0]=0
        for j in range(n+1):
            dp[0][j]=0

        for i in range(1,n+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        return dp[n][n]

    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        t = "".join(reversed(s))
        return self.lcs(s,t,n)
    
    
sol = Solution()

input = "bbbab"
print(sol.longestPalindromeSubseq(input))