from collections import deque

class Solution(object):
    def find_cord(self,num,n):
        row_top = (num-1)//n
        row_botm = n-1-row_top
        
        col = (num-1)%n
        if row_top % 2 == 1:
            col = n - 1 - col

        return row_botm,col

    def snakesAndLadders(self, board):
        n = len(board)
        que = deque()
        visit = [[False]*n for _ in range(n)]
        que.append(1)
        visit[n-1][0] = True
        steps = 0

        while que:
            for _ in range(len(que)):
                u = que.popleft()
                for i in range(1,7):
                    t = u + i

                    if t>n*n:
                        break

                    row,col = self.find_cord(t,n)
                    if visit[row][col]:
                        continue
                    
                    visit[row][col] = True
                    next_pos = board[row][col] if board[row][col] != -1 else t
                    
                    if next_pos == n*n:
                        return steps + 1

                    que.append(next_pos)
                    
            steps+=1

        return -1
    
# Approach-1 (BFS Algorithm)
# T.C : O(n**2)
# S.C : O(n**2) 

sol = Solution()

board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
print(sol.snakesAndLadders(board))