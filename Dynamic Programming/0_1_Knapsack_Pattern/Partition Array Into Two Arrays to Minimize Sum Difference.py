class Solution:                            
    def minimumDifference(self, nums):

        n = len(nums)

        if n == 0:
            return 0

        totalSum = sum(nums)

        dp = [[False]*(totalSum+1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True

        if nums[0] <= totalSum:
            dp[0][nums[0]] = True

        for i in range(1,n):
            for j in range(1,totalSum+1):

                exclude = dp[i-1][j]

                include = False
                if nums[i] <= j:
                    include = dp[i-1][j-nums[i]]

                dp[i][j] = exclude or include

        mini = float('inf')

        for num in range(totalSum//2 + 1):
            if dp[n-1][num]:
                mini = min(mini, abs(totalSum - 2*num))

        return mini