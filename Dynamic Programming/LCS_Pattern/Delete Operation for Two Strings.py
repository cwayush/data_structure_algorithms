class Solution:
    def longestCommonSubseq(self,text1,text2,n,m):
        dp=[[-1]*(m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0]=0
        for j in range(m+1):
            dp[0][j]=0

        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        return dp[n][m]

    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        return n + m - 2*(self.longestCommonSubseq(word1,word2,n,m)) 
    
    
sol=Solution()

word1 = "leetcode"
word2 = "etco"
print(sol.minDistance(word1,word2))