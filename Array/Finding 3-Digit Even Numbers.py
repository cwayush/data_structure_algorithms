from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        arr = []
        for i in range(100,999):
            flag = True
            mapp = Counter(digits)

            for s in str(i):
                if int(s) not in mapp:
                    flag = False
                    break
                else:
                    mapp[int(s)]-=1
                    if mapp[int(s)] == 0:
                        del mapp[int(s)]
            
            if flag and i%2==0:
                arr.append(i)

        return arr

# Approach-1 (Hashmap)
# T.C : O(n)
# S.C : O(n)

sol=Solution()

digits = [2,1,3,0]
print(sol.findEvenNumbers(digits))