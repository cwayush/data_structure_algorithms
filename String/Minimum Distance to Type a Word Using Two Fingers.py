class Solution:
    def minimumDistance(self, word: str) -> int:
        coordinate = []

        for s in word:
            pos = ord(s) - ord('A')
            coordinate.append((pos//6,pos%6))

        def cal_dist(a,b):
            if a == -1:
                return 0
            x1,y1 = a
            x2,y2 = b

            return abs(x2-x1) + abs(y2-y1)

        dp = {}

        def solve(idx,f1,f2):
            if idx == len(coordinate):
                return 0

            key = (idx,f1,f2)

            if key in dp:
                return dp[key]
            
            curr_cord = coordinate[idx]

            cost_hand1 = cal_dist(f1,curr_cord) + solve(idx+1,curr_cord,f2)

            cost_hand2 = cal_dist(f2,curr_cord) + solve(idx+1,f1,curr_cord)

            dp[key] = min(cost_hand1,cost_hand2)
            return dp[key]
        
        return solve(0,-1,-1)