class Solution:
    def check_num(self,i,curr_sum,str_s,num):
        if i==len(str_s):
            return curr_sum == num

        if curr_sum>num:
            return False
        possible = False
        for j in range(i,len(str_s)):
            n_str = str_s[i:j+1]
            val = int(n_str)
            possible= possible or self.check_num(j+1,curr_sum+val,str_s,num)

            if possible:
                return True

    def punishmentNumber(self, n: int) -> int:
        result=0
        for num in range(1,n+1):
            sq = num*num
            str_sq = str(sq)
            if self.check_num(0,0,str_sq,num):
                result+=sq

        return result
    
# Approach-1 (Recursion)
# T.C : Exponential
# S.C : Auxillary
            
##############################################################################################################################################
            
class Solution:
    def check_num(self,i,curr_sum,str_s,num,memo):
        if i==len(str_s):
            return curr_sum == num

        if curr_sum>num:
            return False

        if memo[i][curr_sum]!=-1:
            return memo[i][curr_sum]

        possible = False
        for j in range(i,len(str_s)):
            n_str = str_s[i:j+1]
            val = int(n_str)
            possible= possible or self.check_num(j+1,curr_sum+val,str_s,num,memo)

            if possible:
                return True

        memo[i][curr_sum] = possible
        return memo[i][curr_sum]

    def punishmentNumber(self, n: int) -> int:
        result=0
        for num in range(1,n+1):
            sq = num*num
            str_sq = str(sq)
            memo = [[-1]*(num+1) for _ in range(len(str_sq)+1)]
            if self.check_num(0,0,str_sq,num,memo):
                result+=sq

        return result
    
# Approach-2 (Memoization)
# T.C : O(n*2^(log(n^2)))
# S.C : O(n*2^(log(n^2)) + log(n^2))
            
##############################################################################################################################################
            
sol=Solution()

n = 37
print(sol.punishmentNumber(n))