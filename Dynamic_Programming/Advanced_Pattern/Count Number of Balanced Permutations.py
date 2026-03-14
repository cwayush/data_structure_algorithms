class Solution:
    def __init__(self):
        self.M = 10**9 + 7

    def findPower(self,a,b):
        if b==0:
            return 1
        
        half = self.findPower(a,b//2)
        result = (half*half) % self.M
        if b % 2 == 1:
            result = (result*a) % self.M

        return result
    def solve(self,digit,evenIdxDigitCount,currSum,freq,fermatFact,n,totalDigitSum,totalPermPossible,dp):
        if digit == 10:
            if currSum == totalDigitSum//2 and evenIdxDigitCount == (n+1)//2:
                return totalPermPossible

            return 0
        
        if dp[digit][evenIdxDigitCount][currSum]!=-1:
            return dp[digit][evenIdxDigitCount][currSum]

        ways = 0
        for count in range(min(freq[digit],(n+1)//2 - evenIdxDigitCount)+1):
            evenpossCount = count
            oddpossCount = freq[digit] - count

            div = (fermatFact[evenpossCount] * fermatFact[oddpossCount]) % self.M 

            val = self.solve(digit + 1,evenIdxDigitCount + evenpossCount,currSum + digit * count,freq,fermatFact,n,totalDigitSum,totalPermPossible,dp)

            ways = (ways + (val * div) % self.M) % self.M

        dp[digit][evenIdxDigitCount][currSum] = ways

        return dp[digit][evenIdxDigitCount][currSum]



    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)
        totalDigitSum = 0
        freq = [0] * 10

        for i in range(n):
            totalDigitSum+=int(num[i])
            freq[int(num[i])]+=1

        if (totalDigitSum%2!=0):
            return 0

        fact=[1]*(n+1)
        fact[0] = 1
        fact[1] = 1
        for i in range(2,n+1):
            fact[i] = (fact[i-1]*i) % self.M

        fermatFact = [1]*(n+1)
        for i in range(n+1):
            fermatFact[i] = self.findPower(fact[i],self.M-2) % self.M

        totalPermPossible = (fact[(n + 1) // 2] * fact[n // 2]) % self.M
        
        digit = 0
        currSum = 0
        evenIdxDigitCount = 0

        dp = [[[-1 for _ in range(totalDigitSum + 1)] for _ in range((n + 1) // 2 + 1)] for _ in range(11)]

        return self.solve(0,evenIdxDigitCount,currSum,freq,fermatFact,n,totalDigitSum,totalPermPossible,dp)
    
# Approach-1 (Dynamic Programming)
# T.C : O(n**3)        
# S.C : O(n**2)

sol = Solution()

num = "123"
print(sol.countBalancedPermutations(num))