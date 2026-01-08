from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        n = len(words)

        def compare(word1:str,word2:str) -> bool:
            freq = [0]*26

            for ch in word1:
                freq[ord(ch)-ord('a')] +=1

            for ch in word2:
                freq[ord(ch)-ord('a')] -=1

            return all(x==0 for x in freq)

        for i in range(1,n):
            if compare(words[i-1],words[i]):
                continue

            res.append(words[i])

        return res
        
# Approach-1 (HashMap)
# T.C : O(n*m)  
# S.C : O(1)

sol = Solution()

words = ["abba","baba","bbaa","cd","cd"]
print(sol.removeAnagrams(words))  