from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num=[0]*100
        count = 0
        for x,y in dominoes:
            val = x*10 + y if x<=y else y*10 + x
            count+=num[val]
            num[val]+=1
        return count

# Approach-1 (Hashmap)
# T.C : O(n)
# S.C : O(1)
  
sol=Solution()

dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
print(sol.numEquivDominoPairs(dominoes))