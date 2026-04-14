class Solution:
    def isPalindrome(self,strr):
        n=len(strr)
        i,j=0,n-1
        while i<j:
            if strr[i]!=strr[j]:
                return False
            i+=1
            j-=1
        return True

    def solve(self,i,n,s):
        if i==n:
            return 0

        temp=""
        mini_part = float('inf')
        for j in range(i,n):
            temp+=s[j]
            if self.isPalindrome(temp):
                part = 1 + self.solve(j+1,n,s)
                mini_part = min(mini_part,part)

        return mini_part

    def minCut(self, s: str) -> int:
        n=len(s)
        return self.solve(0,n,s)-1

# Approach-1 (Recursive)
# T.C : O(2^n)
# S.C : Auxillary Stack Space

##############################################################################################################################################

class Solution:
    def isPalindrome(self,strr):
        n=len(strr)
        i,j=0,n-1
        while i<j:
            if strr[i]!=strr[j]:
                return False
            i+=1
            j-=1
        return True

    def minCut(self, s: str) -> int:
        n=len(s)
        dp=[0]*(n+1)
        
        dp[n]=0
        for i in range(n-1,-1,-1):
            temp=""
            mini_part = float('inf')
            for j in range(i,n):
                temp+=s[j]
                if self.isPalindrome(temp):
                    part = 1 + dp[j+1]
                    mini_part = min(mini_part,part)

            dp[i] = mini_part

        return dp[0] - 1

# Approach-2 (Memoization)
# T.C : O(n^3)
# S.C : O(n)

##############################################################################################################################################

class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        dp=[0]*(n+1)
        isPal = [[False] * n for _ in range(n)]
        
        # Precompute palindrome table
        for i in range(n):
            for j in range(i, n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    isPal[i][j] = True
        
        dp[n]=0
        for i in range(n-1,-1,-1):
            temp=""
            mini_part = float('inf')
            for j in range(i,n):
                temp+=s[j]
                if isPal[i][j]:
                    part = 1 + dp[j+1]
                    mini_part = min(mini_part,part)

            dp[i] = mini_part

        return dp[0] - 1

# Approach-3 (Tabulation)
# T.C : O(n^2)
# S.C : O(n^2) 

sol=Solution()

s = "aab"
print(sol.minCut(s))