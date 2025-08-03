from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)
        chunk=0
        prefix=[None]*n
        prefix[0]=arr[0]
        for i in range(1,n):
            if arr[i]>prefix[i-1]:
                prefix[i]=arr[i]
            else:
                prefix[i]=prefix[i-1]
                
        suffix=[None]*n
        suffix[n-1]=arr[n-1]
        for i in range(n-2,-1,-1):
            if arr[i]<suffix[i+1]:
                suffix[i]=arr[i]
            else:
                suffix[i]=suffix[i+1]

        for i in range(n):
            premax=prefix[i-1] if i>0 else -1
            sufmin=suffix[i]
            if premax<sufmin:
                chunk+=1
    
        return chunk

# Approach-1 (Hashtable)
# T.C : O(n)
# S.C : O(n)

##############################################################################################################################################

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)
        chunk=0

        max_sum = 0
        for index in range(n):
            max_sum = max(max_sum,arr[index])
            if max_sum==index:
                chunk+=1

        return chunk

# Approach-2 (Space Optimal)
# T.C : O(n)
# S.C : O(1)

sol=Solution()

arr = [1,0,2,3,4,5]
print(sol.maxChunksToSorted(arr))