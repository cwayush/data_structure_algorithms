class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)

        if numFriends == 1:
            return word

        longest_possible = n - (numFriends -1)
        result = ''
        for i in range(n):
            can_take_length = min(longest_possible,n-i)
            result = max(result,word[i:i + can_take_length])

        return result
    
# Approach-1 (Normal looping)
# T.C : O(n**2)
# S.C : O(1) 

sol = Solution()
word = "dbca"
numFriends = 2
print(sol.answerString(word,numFriends))