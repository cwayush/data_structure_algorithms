class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n=len(grid)
        hash_map = [0]*(n*n+1)
        for i in range(n):
            for j in range(n):
                hash_map[grid[i][j]] +=1
        rep = miss =0
        for i in range(1,n*n+1):
            if hash_map[i]>1:
                rep = i
            
            if hash_map[i] == 0:
                miss =i

        return [rep,miss]

# Approach-1 (Math)
# T.C : O(n^2)
# S.C : O(n^2)   

sol=Solution()

grid = [[9,1,7],[8,9,2],[3,4,6]]
print(sol.findMissingAndRepeatedValues(grid))