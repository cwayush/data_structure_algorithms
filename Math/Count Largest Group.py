import collections

class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashmap = collections.Counter()
        for i in range(1,n+1):
            key = sum(int(x) for x in str(i))
            hashmap[key]+=1

        maxValue = max(hashmap.values())
        count = sum(1 for v in hashmap.values() if v==maxValue)
        return count
        
# Approach-1 (Hashmap)
# T.C : O(nlogn)
# S.C : O(logn)    

sol=Solution()

n=28
print(sol.countLargestGroup(n))