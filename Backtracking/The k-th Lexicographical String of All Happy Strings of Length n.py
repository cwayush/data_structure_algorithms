class Solution:
    def solve(self,n,result,curr):
        if len(curr)==n:
            result.append(''.join(curr))
            return 

        for i in range(3):
            ch=chr(ord('a') + i)
            if curr and curr[-1]==ch:
                continue
            curr.append(str(ch))
            self.solve(n,result,curr)
            curr.pop()

    def getHappyString(self, n: int, k: int) -> str:
        result=[]
        curr = []
        self.solve(n,result,curr)
        if len(result)<k:
            return ""
        return result[k-1]
        
# Approach-1 (Backtracking)
# T.C : Exponential
# S.C : Exponential

##############################################################################################################################################
     
class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        result=""
        count=0

        def solve(curr):
            nonlocal count,result
            if len(curr)==n:
                count+=1
                if count==k:
                    result=''.join(curr)
                return 

            for ch in 'abc':
                if curr and curr[-1]==ch:
                    continue
                curr.append(ch)
                solve(curr)
                curr.pop()
                if result:
                    return 

        solve([])
        return result if result else ""
        
# Approach-2 (Space optimal)
# T.C : Exponential
# S.C : O(n) 

sol=Solution()

n=3
k=9
print(sol.getHappyString(n,k))
