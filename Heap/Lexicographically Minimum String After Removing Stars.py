import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        s = list(s)
        for i,char in enumerate(s):
            if heap and char == '*':
                char,idx = heapq.heappop(heap)
                s[-idx] = '#'
                s[i] = '#'
            else:
                heapq.heappush(heap,(char,-(i)))
        result = ''.join(c for c in s if c!='#')

        return result

# Approach-1 (min-heap)
# T.C : O(n)
# S.C : O(n) 

sol = Solution()

s = "aaba*"
print(sol.clearStars(s))