from typing import List

class Solution:
    def solve(self,i,n,questions):
        if i>=n:
            return 0

        skip = self.solve(i+1,n,questions)
        non_skip = questions[i][0] + self.solve(i+questions[i][1]+1,n,questions)

        return max(skip,non_skip)

    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        return self.solve(0,n,questions)
    
# Approach-1 (Recursion)
# T.C : Exponential
# S.C : O(n) 

##############################################################################################################################################

class Solution:
    def solve(self,i,n,questions,memo):
        if i>=n:
            return 0

        if memo[i]!=-1:
            return memo[i]

        skip = self.solve(i+1,n,questions,memo)
        non_skip = questions[i][0] + self.solve(i+questions[i][1]+1,n,questions,memo)

        memo[i] = max(skip,non_skip)
        return memo[i]

    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        memo = [-1]*(n+1)
        return self.solve(0,n,questions,memo)
    
# Approach-2 (Memoization)
# T.C : O(n)
# S.C : O(n)

##############################################################################################################################################

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        if n == 1:
            return questions[0][0]
        dp = [0]*(200001)
        
        for i in range(n-1,-1,-1):
            dp[i] = max(questions[i][0] + dp[i+questions[i][1]+1], dp[i+1])

        return dp[0]
    
# Approach-3 (Bottom Up)
# T.C : O(n)
# S.C : O(n)

sol=Solution()

questions = [[3,2],[4,3],[4,4],[2,5]]
print(sol.mostPoints(questions))