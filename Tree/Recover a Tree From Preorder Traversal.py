from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n=len(traversal)
        s = traversal
        stack=[]
        i=0
        while i<n:
            level = 0
            while i<n  and s[i] == '-':
                level+=1
                i+=1

            val=0
            while i<n and s[i].isdigit():
                val = val*10 + int(s[i])
                i+=1

            node = TreeNode(val)

            if level == 0:
                stack.append(node)
            else:
                while len(stack)!=level:
                    stack.pop()
                if stack:
                    parent = stack[-1]
                    if not parent.left:
                        parent.left = node
                    else:
                        parent.right = node

            stack.append(node)

        return stack[0]
    
# Approach-1 (BFS)
# T.C : O(n)
# S.C : O(n)

sol= Solution()

traversal = "1-401--398---90--88"