from typing import List

class Solution:
    def solve(self,idx,n,used,result):
        if idx>=len(result):
            return True

        if result[idx]!=-1:
            return self.solve(idx+1,n,used,result)

        for num in range(n,0,-1):
            if used[num]:
                continue

            used[num] =True
            result[idx] =num

            if num ==1:
                if (self.solve(idx+1,n,used,result)):
                    return True

            else:
                j=result[idx] + idx
                if j<len(result) and result[j]==-1:
                    result[j]=num
                    if (self.solve(idx+1,n,used,result)):
                        return True

                    result[j]=-1

            used[num]=False
            result[idx]=-1

        return False


    def constructDistancedSequence(self, n: int) -> List[int]:
        result=[-1]*(2*n-1)
        used=[False]*(n+1)

        self.solve(0,n,used,result)
        return result
    
# Approach-1 (Backtracking)
# T.C : O(n!)
# S.C : O(n)

sol=Solution()

n=5
print(sol.constructDistancedSequence(n))