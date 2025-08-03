from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        n=len(players)
        m=len(trainers)
        match_count= 0
        
        i = j = 0
        while i<n and j<m:
            while j<m and players[i]>trainers[j]:
                j+=1
            if j<m:
                match_count+=1
            i+=1
            j+=1

        return match_count
    
sol = Solution()

players,trainers = [4,7,9],[8,2,5,8]
print(sol.matchPlayersAndTrainers(players,trainers))