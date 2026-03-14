from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        res = self.get_rotation(tops,bottoms,tops[0])
        if bottoms[0]!=tops[0]:
            res = min(res,self.get_rotation(tops,bottoms,bottoms[0]))
        return -1 if res == float('inf') else res

    def get_rotation(self,tops,bottoms,target):
        toprotate = 0
        bottomrotate = 0
        for i in range(len(tops)):
            if tops[i]!=target and bottoms[i]!=target:
                return float('inf')
            if tops[i]!=target:
                toprotate +=1
            if bottoms[i]!=target:
                bottomrotate +=1
        return min(toprotate,bottomrotate)
    
sol=Solution()

tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]
print(sol.minDominoRotations(tops,bottoms))