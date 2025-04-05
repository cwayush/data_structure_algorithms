from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self,root):
        if not root:
            return (0,None)

        l_depth, l_node = self.solve(root.left)
        r_depth, r_node = self.solve(root.right)

        if l_depth == r_depth:
            return (l_depth + 1,root)
        elif l_depth>r_depth:
            return (l_depth + 1,l_node)
        else:
            return (r_depth + 1,r_node)

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.solve(root)[1]

# Approach-1 (One Pass)
# T.C : O(n)
# S.C : O(n)  

sol=Solution()

root = [3,5,1,6,2,0,8,None,None,7,4]