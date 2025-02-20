class Solution:
#     def solve(self,idx,j,arr,dp):
#         if idx==j:
#             return 0
            
#         if dp[idx][j]!=-1:
#             return dp[idx][j]
        
#         mini=float('inf')
#         for k in range(idx,j):
#             operation = arr[idx-1]*arr[k]*arr[j] + self.solve(idx,k,arr,dp) + self.solve(k+1,j,arr,dp)
            
#             mini= min(mini,operation)
            
#         dp[idx][j] = mini
        
#         return dp[idx][j]
        
#     def matrixMultiplication(self, arr):
#         n=len(arr)
#         dp=[[-1]*n for _ in range(n)]
#         return self.solve(1,n-1,arr,dp)