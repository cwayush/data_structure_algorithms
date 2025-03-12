from typing import List
from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n=len(arr)
        dp=[[2]*n for _ in range(n)]
        mpp=defaultdict(int)

        for i in range(n):
            mpp[arr[i]] = i

        maxlength = 0
        for j in range(1,n):
            for k in range(j+1,n):
                target = arr[k] - arr[j]
                if target in mpp and mpp[target]<j:
                    i = mpp[target]
                    dp[j][k] = 1 + dp[i][j]

                maxlength = max(maxlength,dp[j][k])

        return maxlength if maxlength>=3 else 0
    
# Approach-1 (Tabulation)
# T.C : O(n^2)
# S.C : O(n)

sol=Solution()

arr= [1,2,3,4,5,6,7,8]
print(sol.lenLongestFibSubseq(arr))
