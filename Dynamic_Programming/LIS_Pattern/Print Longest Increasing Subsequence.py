class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        dp=[1]*N
        
        idx_arr=[i for i in range(N)]
        maxi=0
        last_idx=0
        for idx in range(N):
            for prev in range(idx):
                if arr[idx]>arr[prev] and 1 + dp[prev]>dp[idx]:
                    dp[idx]=1+dp[prev]
                    idx_arr[idx]=prev
            
            if dp[idx]>maxi:
                maxi=dp[idx]
                last_idx=idx
                
        result=[]
        result.append(arr[last_idx])
        while idx_arr[last_idx]!=last_idx:
            last_idx=idx_arr[last_idx]
            result.append(arr[last_idx])
            
        return list(reversed(result))
            
# Approach-1 (Space Optimal)
# T.C : O(n^2)
# S.C : O(n)

sol=Solution()

n = 16
arr = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
print(sol.longestIncreasingSubsequence(n,arr))