class Solution:
    def plusOne(self, digits):
        n = len(digits)

        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits
    
# Approach-1 (Greedy)
# T.C : O(n)
# S.C : O(1)

sol = Solution()

digits = [1,2,3]
print(sol.plusOne(digits))