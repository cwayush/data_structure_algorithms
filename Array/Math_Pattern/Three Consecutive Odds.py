from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        maxx_count = 0
        for num in arr:
            if num%2!=0:
                count+=1
                maxx_count = max(maxx_count,count)
            else:
                count = 0

        return True if maxx_count>=3 else False

# Approach-1 (Counting)
# T.C : O(n)        
# S.C : O(1)

sol=Solution()

arr = [1,2,34,3,4,5,7,23,12]
print(sol.threeConsecutiveOdds(arr))