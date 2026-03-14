from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = []
        for i in range(len(groups)):
            if i==0 or groups[i]!=groups[i-1]:
                result.append(words[i])

        return result

# Approach-1 (Greedy)
# T.C : O(n)
# S.C : O(n) 

sol=Solution()

words = ["e","a","b"]
groups = [0,0,1]
print(sol.getLongestSubsequence(words,groups))