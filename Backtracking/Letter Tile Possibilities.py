class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        vec=[0]*26
        count=0

        for tile in tiles:
            vec[ord(tile)-ord('A')]+=1

        def solve(vec):
            nonlocal count
            count+=1

            for i in range(26):
                if vec[i]==0:
                    continue

                vec[i]-=1
                solve(vec)
                vec[i]+=1

        solve(vec)

        return count-1
    
sol=Solution()

tiles = 'AAABBC'
print(int(sol.numTilePossibilities(tiles)))