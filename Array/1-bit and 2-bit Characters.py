class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1

# Approach-1 (Greedy)
# T.C : O(n)
# S.C : O(1)

sol = Solution()

bits = [1,1,1,0]
print(sol.isOneBitCharacter(bits))