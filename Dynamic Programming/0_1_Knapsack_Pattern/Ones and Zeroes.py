from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        dp = [[[0]*(n+1) for _ in range(m+1)] for _ in range(len(strs)+1)]

        for i in range(1,len(strs)+1):
            count0 = strs[i-1].count('0')
            count1 = strs[i-1].count('1')

            for zero in range(m+1):
                for one in range(n+1):
                    exclude = dp[i-1][zero][one]
                    include = 0
                    if zero >= count0 and one >= count1:
                        include = 1 + dp[i-1][zero - count0][one - count1]

                    dp[i][zero][one] = max(include,exclude)

        return dp[len(strs)][m][n]