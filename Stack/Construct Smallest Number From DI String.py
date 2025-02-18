class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n=len(pattern)
        stack=[]
        res=""
        counter=1
        for i in range(n+1):
            stack.append(counter)
            counter+=1

            if i==n or pattern[i]=='I':
                while stack:
                    res+=str(stack.pop())

        return res
    
# Approach-1 
# T.C : O(n+1)
# S.C : O(n+1) 

sol=Solution()

pattern = "IIIDIDDD"
print(sol.smallestNumber(pattern))