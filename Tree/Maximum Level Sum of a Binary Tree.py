from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, ans, level = float('-inf'), 0, 0

        q = deque()
        q.append(root)

        while q:
            level += 1
            sum_at_current_level = 0
            for _ in range(len(q)):
                node = q.popleft()
                sum_at_current_level += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if max_sum < sum_at_current_level:
                max_sum, ans = sum_at_current_level, level
           
        return ans
    
# Approach-1 (BFS)
# T.C : O(n)
# S.C : O(n)

sol= Solution()

root = [989,None,10250,98693,-89388,None,None,None,-32127]
        