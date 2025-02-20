class Solution:
    def solve(self,idx,j,arr,dp):
        if idx==j:
            return 0
            
        if dp[idx][j]!=-1:
            return dp[idx][j]
        
        mini=float('inf')
        for k in range(idx,j):
            operation = arr[idx-1]*arr[k]*arr[j] + self.solve(idx,k,arr,dp) + self.solve(k+1,j,arr,dp)
            
            mini= min(mini,operation)
            
        dp[idx][j] = mini
        
        return dp[idx][j]
        
    def matrixMultiplication(self, arr):
        n=len(arr)
        dp=[[-1]*n for _ in range(n)]
        return self.solve(1,n-1,arr,dp)

# Approach-1 (Memoization)
# T.C : O(n^2)
# S.C : O(n^2) + Auxillary Stack Space

##############################################################################################################################################

class Solution:
    def matrixMultiplication(self, arr):
        n=len(arr)
        dp=[[-1]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i]=0
            
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                mini=float('inf')
                for k in range(i,j):
                    operation = arr[i-1]*arr[k]*arr[j] + dp[i][k] +  dp[k+1][j]
                    
                    mini= min(mini,operation)
                    
                dp[i][j] = mini
                
        return dp[1][n-1]

# Approach-2 (Tabulation)
# T.C : O(n^2)
# S.C : O(n^2)

##############################################################################################################################################

sol=Solution()

arr=[1, 2, 3, 4, 3]
print(sol.matrixMultiplication(arr))

