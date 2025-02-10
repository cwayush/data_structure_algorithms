class Solution:
    def print_lcs(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[-1]*(m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0]=0
        for j in range(m+1):
            dp[0][j]=0

        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        maxlen = dp[n][m]
        index = maxlen-1
        str_list=['$']*maxlen            
        i,j=n,m
        
        while i>0 and j>0:
            if text1[i-1] == text2[j-1]:
                str_list[index]=text1[i-1]
                index-=1
                i-=1
                j-=1
            elif dp[i-1][j]>dp[i][j-1]:
                i-=1
            else:
                j-=1
    
        return ''.join(str_list)
    
# Approach-1 (Bottom Up)
# T.C : O(m*n)
# S.C : O(m*n) + O(min(n,m)) ≈ O(n*m)
    
sol=Solution()
input1 = "abcde"
input2 = "ace"

print(sol.print_lcs(input1,input2))