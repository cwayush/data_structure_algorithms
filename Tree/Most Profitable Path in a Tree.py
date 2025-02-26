from typing import List
from collections import defaultdict

class Solution:
    def __init__(self):
        self.alicemax_income = float('-inf')

    def bob_dfs(self,curr,t,visit):
        visit[curr] = True
        self.mapp[curr] = t

        if curr == 0:
            return True

        for ngb in self.adj[curr]:
            if not visit[ngb]:
                if self.bob_dfs(ngb,t+1,visit):
                    return True
        
        del self.mapp[curr]
        return False    
    
    def alice_dfs(self,curr,t,visit,income,amount):
        visit[curr] = True

        if curr not in self.mapp or t<self.mapp[curr]:
            income+=amount[curr]

        elif t == self.mapp[curr]:
            income+= (amount[curr])//2

        if len(self.adj[curr]) == 1 and curr!=0:
            self.alicemax_income = max(self.alicemax_income,income)

        for ngb in self.adj[curr]:
            if not visit[ngb]:
                self.alice_dfs(ngb,t+1,visit,income,amount)



    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n=len(amount)
        self.adj = defaultdict(list)
        self.mapp = defaultdict(int)
        for u,v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)

        visit = [False]*n
        self.bob_dfs(bob,0,visit)


        visit = [False]*n
        self.alice_dfs(0,0,visit,0,amount)

        return self.alicemax_income
    
# Approach-1 (DFS)
# T.C : O(n)
# S.C : O(n)

sol=Solution()

edges = [[0,1],[1,2],[1,3],[3,4]]
bob = 3 
amount = [-2,4,2,-4,6]
print(sol.mostProfitablePath(edges,bob,amount))