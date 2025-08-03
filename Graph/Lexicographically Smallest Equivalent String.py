from collections import defaultdict

class Solution:
    def dfsFind_minChar(self,adj,curr_ch,visited):
        visited[ord(curr_ch) - ord('a')] = 1

        minChar = curr_ch
        for new_ch in adj[curr_ch]:
            if not visited[ord(new_ch) - ord('a')]:
                minChar = min(minChar, self.dfsFind_minChar(adj,new_ch,visited))

        return minChar

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        adj = defaultdict(list)

        for i in range(n):
            u = s1[i]
            v = s2[i]
            adj[u].append(v)
            adj[v].append(u)

        result = ''
        
        m = len(baseStr)
        for i in range(m):
            ch = baseStr[i]
            visited = [0]*26
            minChar = self.dfsFind_minChar(adj,ch,visited)

            result+=minChar
        return result
    
sol = Solution()

s1 = "leetcode"
s2 = "programs"
baseStr = "sourcecode"
print(sol.smallestEquivalentString(s1,s2,baseStr))