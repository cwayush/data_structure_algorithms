from collections import defaultdict
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = defaultdict(int)
        for i,char in enumerate(s):
            last_occurence[char] = i

        result=[]
        start = 0
        end = 0

        for i,char in enumerate(s):
            end = max(end,last_occurence[char])

            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result

# Approach-1 (String_hashmap)
# T.C : O(n)
# S.C : O(k) 

sol=Solution()

s = "ababcbacadefegdehijhklij"
print(sol.partitionLabels(s))