from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
    
        answer = [[0] * (cols - k + 1) for _ in range(rows - k + 1)]
        
        for start_row in range(rows - k + 1):
            for start_col in range(cols - k + 1):
                
                elements = []
                
                for r in range(start_row, start_row + k):
                    for c in range(start_col, start_col + k):
                        elements.append(grid[r][c])
                
                elements.sort()
                
                min_diff = float("inf")
                
                for idx in range(1, len(elements)):
                    if elements[idx] == elements[idx - 1]:
                        continue
                    min_diff = min(min_diff, elements[idx] - elements[idx - 1])
                
                if min_diff != float("inf"):
                    answer[start_row][start_col] = min_diff
        
        return answer