from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = defaultdict(int)

        n = len(s)
        i = j = 0

        maxLen = 0

        while i<=j and j<n:
            char = s[j]
            while char in store:
                store[s[i]]-=1
                if store[s[i]] == 0:
                    del store[s[i]]
                
                i+=1

            store[char]+=1

            maxLen = max(maxLen,j-i+1)

            j+=1


        return maxLen