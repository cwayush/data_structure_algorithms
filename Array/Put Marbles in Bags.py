from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n=len(weights)
        pair_sum=[0]*(n-1)
        for i in range(n-1):
            pair_sum[i] = weights[i] + weights[i+1]

        pair_sum.sort()

        min_sum = sum(pair_sum[:k-1])
        max_sum = sum(pair_sum[n-1-k+1:])

        return max_sum - min_sum
    
# Approach-1 (Greedy Algorithm)
# T.C : O(n*log(n))
# S.C : O(n) 

sol=Solution()

weights = [1,3,5,1]
k = 2
print(sol.putMarbles(weights,k))