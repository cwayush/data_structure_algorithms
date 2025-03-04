from typing import List

class SOlution:
    def rangeAddition(self,length: int, updates: List[List[int]]) -> List[int]:
        result=[0]*length
        n=len(updates)
        for start,end,inc in updates:
            for i in range(start,end+1):
                result[i]+= inc
                
        return result

# Approach-1 (Loop)
# T.C : O(n*length)
# S.C : O(length)
  
sol=SOlution()

length = 5
updates = [ [1,  3,  2],
            [2,  4,  3],
            [0,  2, -2] ]
        
print(sol.rangeAddition(length,updates))