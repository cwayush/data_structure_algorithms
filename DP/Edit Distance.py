class Solution:
    def find_distance(self,i,j,s,t):
        if i<0:
            return j+1
        if j<0:
            return i+1

        if s[i]==t[j]:
            return 0 + self.find_distance(i-1,j-1,s,t)

        return 1 + min(
            (self.find_distance(i,j-1,s,t)), # Insertion
            (self.find_distance(i-1,j,s,t)), # Deletion
            (self.find_distance(i-1,j-1,s,t)) # Replace
        )


    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        return self.find_distance(n-1,m-1,word1,word2)

# Approach-1 (Recursion)
# T.C : Exponential
# S.C : O(n+m) 

##############################################################################################################################################

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        dp = [[-1]*(m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = i
        
        for j in range(m+1):
            dp[0][j] = j

        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

            
        return dp[n][m]
    
# Approach-2 (Bottom Up)
# T.C : O(n*m)
# S.C : O(n*m) 
    
##############################################################################################################################################

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        prev = [0]*(m+1)

        for j in range(m+1):
            prev[j] = j

        for i in range(1,n+1):
            curr = [0] * (m + 1)  
            curr[0]=i
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1 + min(prev[j], curr[j-1], prev[j-1])

            prev = curr

        return prev[m]
    
# Approach-3 (Space Optimal)
# T.C : O(n*m)
# S.C : O(m) 

sol=Solution()

word1 = "intention"
word2 = "execution"
print(sol.minDistance(word1,word2))